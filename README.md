## ChatGPT API Speech to Speech
An interaction with the ChatGPT API using speech to speech.
Converting speech to text using OpenAI Whisper API and then sending the text to the ChatGPT API. 
The response from the ChatGPT API is then converted to speech using Google Text to Speech API.

## Requirements
- OpenAI API Key with Whisper Access and ChatGPT Access
- Google Text to Speech API Key

## Installation
1. Install the requirements
```bash
pip install -r requirements.txt
```
2. Create the json file for Google Text to Speech API Key

3. Create the .env file for OpenAI API Key
```bash
OPENAI_API_KEY=YOUR-SECRET-KEY
```

## Usage
**Be careful**, the speech to text and text to speech conversion can be **charged** by the API providers.
Read the documentation of the API providers for more information.
