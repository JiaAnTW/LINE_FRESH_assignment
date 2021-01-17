from flask import abort
from states import indexState


class Controller:

    def __init__(self, app, line_bot_api):
        self.app = app
        self.line_bot_api = line_bot_api
        self.init_state = indexState.IndexState()

    def set_init_state(self, state):
        self.setState(state)
        self.initState = state

    def setState(self, nextState):
        try:
            self.state = nextState
        except:
            self.app.logger.info("[controller.py] SetState Error")
            abort(400)

    def send_msg(self, reply_token, reply_text):
        try:
            self.setState(self.state.get_next_state_by_reply(reply_text))
            self.line_bot_api.reply_message(
                reply_token, self.state.get_msg()
            )

        except Exception as e:
            self.app.logger.info("[controller.py] " + str(e))
            self.setState(self.init_state)
            abort(400)
