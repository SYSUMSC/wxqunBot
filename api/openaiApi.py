import base64
import os
import traceback

from openai import OpenAI
from config import *

class openaiApi:
    def __init__(self):
        self.sf_client = OpenAI(
            base_url=sf_url,
            api_key=sf_key,
        )
        self.zp_client = OpenAI(
            base_url=zp_url,
            api_key=zp_key,
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

    def chat_img(self, user_prompt, img_path:str) -> tuple:
        try:
            #读取文件转为base64
            with open(img_path, "rb") as f:
                base64_image = base64.b64encode(f.read()).decode("utf-8")
            response = self.zp_client.chat.completions.create(
                model="glm-4v-flash",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                }
                            },
                            {
                                "type": "text",
                                "text": user_prompt
                            }
                        ]
                    }
                ],
            )
            return response.choices[0].message.content, ""
        except Exception as e:
            errmsg = f"{str(e)}\n{traceback.format_exc()}"
            print(errmsg)
            return None, errmsg
if __name__ == "__main__":
    #python -m api.openaiApi
    oai = openaiApi()
    img_path = r"C:\Code\wxqunBot\tmp\c9860c522388cf2470d5b80986487070.jpg"
    prompt = "中文描述图片"
    res,errmsg = oai.chat_img(prompt,img_path)
    print(res)