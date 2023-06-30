# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dbs8mvKWvZil06gCk-MzJDcAFBXwxWC5
"""



import random

def chat():
    print("Hello, I am ChatBot. How can I assist you today?")
    print("Feel free to end this conversation at any time by typing 'bye'")
    print("Please enter your question or statement below:")

    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            break
        else:
            response = generate_response()
            print(response)

    print("Thank you for chatting with me. Goodbye!")

def generate_response():
    random_responses = ["I understand. Please tell me more.",
                        "That's an interesting point. Can you elaborate?",
                        "Why do you think that is the case?",
                        "Oh, really? Tell me more about it.",
                        "Let's switch gears. What else would you like to discuss?",
                        "By the way, have you watched any good movies lately?"]
    return random.choice(random_responses)

if __name__ == "__main__":
    chat()