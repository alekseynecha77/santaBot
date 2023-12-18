Overview

Build SantaBot using Flask-based web application designed to interact with users in the spirit of Christmas.
Utilizing a natural language processing model, SantaBot responds to user queries with cheerful and jolly Christmas carol lines.
This application integrates with AWS's Bedrock Runtime service for processing the chat responses.

Features

Home Page: A welcoming interface where users can interact with SantaBot.
Santa Query: A POST endpoint (/santa_query) that processes user queries and returns a response from SantaBot.
AWS Bedrock Runtime Integration: Utilizes AWS's Bedrock Runtime service for generating responses based on user input.


Requirements

Python 3.x
Flask
boto3 (AWS SDK for Python)
Internet connection for AWS services
