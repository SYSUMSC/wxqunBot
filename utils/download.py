import os
import time
import requests
import os
from urllib3.util.retry import Retry
import xml.etree.ElementTree as ET
import traceback


def download_file(url, file_path, refer_url: str = None, max_retries=3, backoff_factor=1):
    if not url:
        return False, "URL is empty."

    if not file_path:
        return False, "File path is empty."

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Priority': 'u=0, i',
        'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

    if refer_url:
        headers['Referer'] = refer_url

    attempt = 0
    while attempt < max_retries:
        attempt += 1
        try:
            # 尝试下载文件
            response = requests.get(url, headers=headers, stream=False, timeout=300)
            #response.raise_for_status()  # 检查是否返回错误状态码
            #排除404,403,500等错误
            code = response.status_code
            if code in [404,403,500]:
                print(f"Download failed: {url} | {code}")
                continue
            with open(file_path, "wb") as of:
                of.write(response.content)

            # 检查文件大小是否为0
            if os.path.getsize(file_path) == 0:
                raise ValueError("Downloaded file is empty.")

            print(f"Download successful: {file_path}")
            return True, None

        except Exception as e:
            errmsg = f"Attempt {attempt} failed for url `{url}`: {str(e)}\n{traceback.format_exc()}"

            print(errmsg)

            # 如果已达到最大重试次数，则返回错误
            if attempt == max_retries:
                return False, errmsg

            # 退避延迟（指数增长）
            time.sleep(backoff_factor * (2 ** (attempt - 1)))

    return False, "Max retries exceeded."
