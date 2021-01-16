import os
import sys
from dotenv import load_dotenv
from flask import Flask, jsonify, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from controller import Controller
from states.indexState import IndexState

# 讀取環境變數
load_dotenv()

channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
DEBUG = os.getenv("DEBUG", None) == "TRUE"

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

# 初始化web server
app = Flask(__name__, static_url_path="")
line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

# 初始化Controller
init_state = IndexState()
controller = Controller(app=app, line_bot_api=line_bot_api)
controller.set_init_state(init_state)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        app.logger.info("InvalidSignatureError")
        abort(400)

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        controller.send_msg(event.reply_token)

    return "OK"


if __name__ == "__main__":
    port = os.environ['PORT']
    app.run(host="0.0.0.0", port=port, debug=True)
