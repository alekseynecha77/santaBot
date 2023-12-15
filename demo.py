from flask import Flask, request, jsonify
import boto3
import json

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

def invoke_bedrock_model(prompt):
    bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
    
    input_payload = {
        "modelId": "cohere.command-text-v14",
        "contentType": "application/json",
        "accept": "*/*",
        "body": json.dumps({
            "prompt": prompt,
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

@app.route('/santa_query', methods=['POST'])
def santa_query():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    user_input = data.get('query', '').lower()

    santa_context = (
        "You are Santa Claus, embodying the spirit of Christmas. "
        "You're cheerful, jolly, and you love spreading Christmas cheer through songs and stories. "
        "Whenever someone asks for a Christmas carol, you happily respond with a line or two from a well-known carol. "
        "Here's a new message from someone: "
    )

    carol_prompt = f"As Santa, sing a line from a Christmas carol. The message is: {user_input}" if 'sing' in user_input or 'carol' in user_input else user_input
    full_prompt = santa_context + carol_prompt

    response_body = invoke_bedrock_model(full_prompt)
    return jsonify(response_body)


if __name__ == '__main__':
    app.run(debug=True)
