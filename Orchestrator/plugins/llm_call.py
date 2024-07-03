from openai import OpenAI
from dotenv import load_dotenv
import os

from Orchestrator.plugins.format_response import format_string_to_list



load_dotenv()

API_KEY = os.getenv("API_KEY")
LLAMA_BASE_URL = os.getenv("LLAMA_BASE_URL")


def get_client():
    return OpenAI(
        # This is the default and can be omitted
        api_key=API_KEY,
        base_url=LLAMA_BASE_URL
    )


def chat_complete():
    client = get_client()
    with open("prompts/generate_tasks.txt", "r") as file:
        prompt = file.read().strip()  # Read the prompt from the file

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b",
        stream=False,
        temperature=0.7,  # Adjust the temperature value as needed
        top_p=0.9,       # Adjust the top_p value as needed
        max_tokens=150   # Adjust the max_tokens value as needed
    )

    llm_response = chat_completion.choices[0].message.content
    return format_string_to_list(llm_response)
