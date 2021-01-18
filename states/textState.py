import time
import re

from states import state, experienceState
from linebot.models import TextSendMessage


class TextState(state.State):
    def __init__(self, text, before_state):
        self._msg = TextSendMessage(text=text)
        self.before_state = before_state

    def get_msg(self):
        return self._msg

    # 理論上因為在lifeCycle就離開這個state, 所以這個不會被執行到
    def get_next_state_by_reply(self, user_reply):
        pass

    def message_did_send(self, controller, user_id, reply_token):
        controller.set_state(self.before_state)
        time.sleep(2)
        controller.line_bot_api.push_message(
            user_id,
            self.before_state.get_msg()
        )
