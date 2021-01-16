from states.state import State
from linebot.models import TextSendMessage


class IndexState(State):
    def get_msg(self):
        return TextSendMessage(text="hi")

    def get_next_state(self):
        return IndexState()
