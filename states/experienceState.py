import json
import sys
from pathlib import Path

from states import state, indexState
from utils.createCarouselMsg import createCarouselMsg


class ExperienceState(state.State):
    def __init__(self):
        self.info = self.loadJsonData()['data']
        self._msg = createCarouselMsg(self.info)

    def get_msg(self):
        return self._msg

    def get_next_state_by_reply(self, user_reply):
        if user_reply == '返回/back':
            return indexState.IndexState()
        else:
            return ExperienceState()

    def loadJsonData(self):
        path = Path(__file__).parent / "./wording/experience.json"
        try:
            with open(path, encoding='utf-8') as f:
                data = json.load(f)
                return data
        except Exception as e:
            print("[experienceState.py] " + str(e))
            sys.exit(1)
