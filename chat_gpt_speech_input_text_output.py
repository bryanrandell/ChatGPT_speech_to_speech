# Description: This script uses the OpenAI API to create a chatbot that takes speech input and outputs text.
# Bryan Randell 2023

from speech_to_text_whisper import main_audio_to_text
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


def main_speech_input_text_output():
    model_engine = "gpt-3.5-turbo"  # Replace with "gpt-4" once available
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    while True:
        role = "user"
        input_message = main_audio_to_text()
        print(f"User: {input_message}")
        if not input_message:
            break
        messages.append({"role": role, "content": input_message})
        role, response = gpt_chat_response(messages, model_engine)
        print(f"Bot {role}: {response}")
        messages.append({"role": role, "content": response})


if __name__ == "__main__":
    main_speech_input_text_output()
