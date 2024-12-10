import json
from openai import OpenAI


client = OpenAI()

class AIans:
    def __init__(self):
        pass

    def gpt_response(self, text1, text2):
        system_prompt = text1
        user_prompt = text2
        completion = client.chat.completions.create(
            model = "gpt-4o",
            top_p = 0,
            messages = [
                {"role": "system","content": system_prompt},
                {
                    "role": "user", 
                    "content": user_prompt

                }
            ]
        )
        return (completion.choices[0].message.content)