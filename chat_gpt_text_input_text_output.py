# Description: This script demonstrates how to use the OpenAI API to create a chatbot using GPT-3.5 Turbo or GPT-4.
# This version of the script uses text input and text output.
# Bryan Randell 2023

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt_chat_response(messages, model_engine="gpt-4"):
    chat = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
    )

    response = chat["choices"][0]["message"]["content"]
    role = chat["choices"][0]["message"]["role"]
    return role, response


def main_text_input_text_output():
    model_engine = "gpt-3.5-turbo"  # Replace with "gpt-4" once available
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    while True:
        role = "user"
        input_message = input("What do you want to say to the bot? ")
        if input_message == "quit":
            break
        messages.append({"role": role, "content": input_message})
        role, response = gpt_chat_response(messages, model_engine)
        print(f"Bot {role}: {response}")
        messages.append({"role": role, "content": response})


if __name__ == "__main__":
    main_text_input_text_output()
