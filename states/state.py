from abc import ABC, abstractmethod
# 登入類別


class State(ABC):
    @abstractmethod
    def get_msg(self):
        pass

    @abstractmethod
    def get_next_state_by_reply(self):
        pass

    def message_did_send(self, controller, user_id, reply_token):
        pass
