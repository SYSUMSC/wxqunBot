# wxqunBot

环境安装
```shell
conda create -n wxqunBot python=3.12
conda activate wxqunBot
pip install -r requirements.txt
```

机器人框架：https://github.com/lich0821/WeChatFerry?

配套微信：3.9.12.17
https://github.com/lich0821/WeChatFerry/releases/download/v39.4.0/WeChatSetup-3.9.12.17.exe

需要config.py配置key
```python
tmp_dir = "C:/Code/wxqunBot/tmp"
img_dir = "C:/Code/wxqunBot/img"
sf_url = "https://api.siliconflow.cn/v1"
sf_key = "sk-"
zp_url = "https://open.bigmodel.cn/api/paas/v4"
zp_key = ""
```