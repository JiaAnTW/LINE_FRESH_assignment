from flask import abort
from states import indexState


class Controller:

    def __init__(self, app, line_bot_api):
        self.app = app
        self.line_bot_api = line_bot_api
        self.state = None

    def set_state(self, nextState):
        try:
            self.state = nextState
        except:
            self.app.logger.info("[controller.py] SetState Error")
            abort(400)

    # 以state Pattern來控制流程，所有的state都有固定的lifeCycle
    def send_msg(self, user_id, reply_token, reply_text):
        try:
            self.set_state(self.state.get_next_state_by_reply(reply_text))

            self.line_bot_api.reply_message(
                reply_token, self.state.get_msg()
            )

            # life cycle function. similar to componentDidMount in React.js
            self.state.message_did_send(
                controller=self,
                user_id=user_id,
                reply_token=reply_token,
            )

        except Exception as e:
            self.app.logger.info("[controller.py] " + str(e))
            self.set_state(indexState.IndexState())
