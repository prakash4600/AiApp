import os
from flask import Flask, render_template, request, jsonify, session
from openai import AzureOpenAI
from dotenv import load_dotenv
import secrets

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Azure OpenAI Configuration

endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
subscription_key = os.environ.get("AZURE_OPENAI_KEY")
deployment = os.environ.get("DEPLOYMENT_NAME", "gpt-4o-mini")
api_version = os.environ.get("API_VERSION", "2024-12-01-preview")

if not subscription_key or not endpoint:
    raise ValueError("Missing required environment variables: AZURE_OPENAI_KEY or AZURE_OPENAI_ENDPOINT")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

@app.route('/')
def home():
    """Render chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        # Get conversation history from session
        if 'conversation' not in session:
            session['conversation'] = []
        
        # Add user message
        session['conversation'].append({
            "role": "user",
            "content": user_message
        })
        
        # Prepare messages (system prompt + history)
        messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ] + session['conversation']
        
        # Call Azure OpenAI
        response = client.chat.completions.create(
            messages=messages,
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model=deployment
        )
        
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to history
        session['conversation'].append({
            "role": "assistant",
            "content": assistant_message
        })
        
        # Keep last 20 messages to avoid token limits
        if len(session['conversation']) > 20:
            session['conversation'] = session['conversation'][-20:]
        
        session.modified = True
        
        return jsonify({
            'success': True,
            'response': assistant_message
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/clear', methods=['POST'])
def clear_conversation():
    """Clear chat history"""
    session['conversation'] = []
    session.modified = True
    return jsonify({'success': True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)