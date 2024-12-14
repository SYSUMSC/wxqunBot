import os
import traceback

from openai import OpenAI
from config import sf_url, sf_key

class openaiApi:
    def __init__(self):
        self.sf_client = OpenAI(
            base_url=sf_url,
            api_key=sf_key,
        )

    def chat(self, user_prompt, system_prompt="") -> tuple:
        try:
            response = self.sf_client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V2.5",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
            )
            return response.choices[0].message.content, ""
        except Exception as e:
            errmsg = f"{str(e)}\n{traceback.format_exc()}"
            print(errmsg)
            return None, errmsg

if __name__ == "__main__":
    pass