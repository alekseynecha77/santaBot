

from flask import Flask, request, jsonify
import boto3
import json

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

def invoke_bedrock_model(user_input):
    bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
    
    input_payload = {
        "modelId": "cohere.command-text-v14",
        "contentType": "application/json",
        "accept": "*/*",
        "body": json.dumps({
            "prompt": user_input,
            "max_tokens": 400,
            "temperature": 0.75,
            "p": 0.01,
            "k": 0,
            "stop_sequences": [],
            "return_likelihoods": "NONE"
        })
    }
    
    response = bedrock.invoke_model(**input_payload)
    response_body = json.loads(response['body'].read())
    return response_body

@app.route('/ask-santa', methods=['POST'])
def ask_santa():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    user_query = data.get('query', '').lower()  # Convert to lower case

    # Santa's context for LLM
    santa_context = (
        "You are Santa Claus, a jolly old man who loves Christmas and enjoys spreading joy and cheer. "
        "You're responding to questions and requests from children and adults alike in your warm, friendly, and festive manner. "
        "Remember, you always speak with kindness and a twinkle in your eye. Here's a new message: "
    )
    full_prompt = santa_context + user_query

    # Invoke the Bedrock model with the full prompt
    response_body = invoke_bedrock_model(full_prompt)
    
    # Return the response from the model
    return jsonify(response_body)

if __name__ == '__main__':
    app.run(debug=True)