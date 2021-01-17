from flask import abort


class Controller:

    def __init__(self, app, line_bot_api):
        self.app = app
        self.line_bot_api = line_bot_api
        self.init_state = None

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
            self.line_bot_api.reply_message(
                reply_token, self.state.get_msg()
            )
            self.setState(self.state.get_next_state_by_reply(reply_text))

        except Exception as e:
            self.app.logger.info("[controller.py] " + str(e))
            self.setState(self.init_state)
            abort(400)
