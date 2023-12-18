Overview

SantaBot is a Flask-based web application designed to bring the joy of Christmas to users. Leveraging a natural language processing model, SantaBot responds to user inquiries with cheerful and jolly lines from Christmas carols. This application is integrated with AWS's Bedrock Runtime service for processing chat responses.



Features

Home Page: A user-friendly interface for interacting with SantaBot.
Santa Query: Utilizes a POST endpoint (/santa_query) to process user queries and deliver SantaBot's responses.
AWS Bedrock Runtime Integration: Employs AWS's Bedrock Runtime service to dynamically generate responses based on user input.



Requirements
Python 3.x
Flask
boto3 (AWS SDK for Python)
Internet connection (for AWS services)
