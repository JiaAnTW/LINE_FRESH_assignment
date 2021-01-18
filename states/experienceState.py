import json
import sys
from pathlib import Path

from states import state, indexState, textState
from utils.createCarouselMsg import createCarouselMsg


class ExperienceState(state.State):
    def __init__(self, wording_path):
        self.wording_path = wording_path
        self.info = self.loadJsonData()
        self._msg = createCarouselMsg(self.info)

    def get_msg(self):
        return self._msg

    def get_next_state_by_reply(self, user_reply):
        if user_reply == '返回/back':
            return indexState.IndexState()
        try:
            # when users reply unknown msg instead of clicking btn we provide,
            # error will be thrown since there is no match key in self.info
            return textState.TextState(
                text="#" +
                user_reply + "\n\n" +
                self.info[user_reply]["description"],
                before_state=ExperienceState(self.wording_path)
            )
        except:  # unexpected reply
            return ExperienceState(self.wording_path)

    def loadJsonData(self):
        path = Path(__file__).parent / self.wording_path
        try:
            with open(path, encoding='utf-8') as f:
                data = json.load(f)
                return data
        except Exception as e:
            print("[experienceState.py] " + str(e))
            sys.exit(1)
