
import openai
from config import TOKEN_CHAT_GPT

openai.api_key = TOKEN_CHAT_GPT


def request_view(text: str) -> str:

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.0
    )

    completion_text = response.choices[0].text.strip()

    return completion_text
