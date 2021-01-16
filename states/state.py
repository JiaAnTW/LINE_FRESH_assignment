from abc import ABC, abstractmethod
# 登入類別


class State(ABC):
    @abstractmethod
    def get_msg(self):
        pass

    @abstractmethod
    def get_next_state(self):
        pass
