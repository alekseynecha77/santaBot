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
    user_query = data.get('query', '').lower()  # Convert to lower case for easier keyword matching

    # Define Santa's responses based on keywords
    santa_responses = {
        'present': 'Ho ho ho! Have you been good this year? What would you like for Christmas?',
    'reindeer': 'My reindeer are resting for the big night! Rudolph says hello.',
    'north pole': "It's chilly up here at the North Pole! But we're warm with the Christmas spirit.",
    'elf': 'The elves are hard at work! They make sure everything is ready for Christmas Eve.',
    'hi': 'Ho, ho, ho! Hello there! Merry Christmas! How can Santa help you today?',
    'santa': 'Yes, it’s me, Santa! Have you written your list for Christmas yet?',
    'christmas': 'Christmas is my favorite time of the year! Joy, gifts, and the spirit of giving!',
    'naughty or nice': 'I’ve got my list, I’m checking it twice! I’ll find out who’s naughty or nice.',
    'cookies': 'Oh, I do love cookies! Make sure to leave some out for me on Christmas Eve.',
    'sleigh': 'The sleigh is all tuned up for delivering presents. We can’t wait to fly around the world!',
    'gift': 'Every gift from a friend is a wish for your happiness. What’s on your wish list?',
    'snow': 'I love a white Christmas, with snowflakes gently falling and covering the world in white.',
    'happy holidays': 'Happy Holidays to you and your family! May your days be merry and bright!',
    'mrs. claus': 'Mrs. Claus is doing wonderfully, thank you. She sends her warmest holiday wishes!',
    'jingle bells': 'Jingle bells, jingle bells, jingle all the way! Oh what fun it is to ride in a one-horse open sleigh, hey!',
    }
    
    # Check if any keyword is in the user query and return the corresponding response
    for keyword, response in santa_responses.items():
        if keyword in user_query:
            return jsonify({'generations': [{'text': response}]})

    # If no keywords are found, invoke the Bedrock model
    response_body = invoke_bedrock_model(user_query)
    return jsonify(response_body)

if __name__ == '__main__':
    app.run(debug=True)
