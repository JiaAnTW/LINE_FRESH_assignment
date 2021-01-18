import json
import sys
from pathlib import Path

from states import state, indexState, textState
from utils.createCarouselMsg import createCarouselMsg


class ExperienceState(state.State):
    def __init__(self, wording_path):
        self.wording_path = wording_path
        self.info = self.loadJsonData()['data']
        self._msg = createCarouselMsg(self.info)

    def get_msg(self):
        return self._msg

    def get_next_state_by_reply(self, user_reply):
        if user_reply == '返回/back':
            return indexState.IndexState()
        for singleInfo in self.info:
            if(user_reply.startswith(singleInfo["title"])):
                return textState.TextState(
                    text="#" +
                    singleInfo["title"]+"\n\n" +
                    singleInfo["description"],
                    before_state=ExperienceState(self.wording_path)
                )
        # Exception handle
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
