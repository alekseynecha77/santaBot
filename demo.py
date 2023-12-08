

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

@app.route('/', methods=['POST'])
def ask_santa():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    user_input = data.get('query', '').lower()  # Convert to lower case

    # Santa's context for LLM
    santa_context = (
        "You are Santa Claus, embodying the spirit of Christmas. "
        "You're cheerful, jolly, and you love spreading Christmas cheer through songs and stories. "
        "Whenever someone asks for a Christmas carol, you happily respond with a line or two from a well-known carol. "
        "Here's a new message from someone: "
    )

    # Check if the user is asking Santa to sing
    if 'sing' in user_input or 'carol' in user_input:
        carol_prompt = "As Santa, sing a line from a Christmas carol. The message is: " + user_input
        full_prompt = santa_context + carol_prompt
    else:
        full_prompt = santa_context + user_input

    # Invoke the Bedrock model with the full prompt
    response_body = invoke_bedrock_model(full_prompt)
    
    # Return the response from the model
    return jsonify(response_body)


if __name__ == '__main__':
    app.run(debug=True)