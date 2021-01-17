from states import state, experienceState
from linebot.models import MessageTemplateAction, ButtonsTemplate, TemplateSendMessage


class IndexState(state.State):
    def __init__(self):
        self._msg = TemplateSendMessage(
            alt_text='張家銨 LINE FRESH',
            template=ButtonsTemplate(
                title='張家銨 Jia An Chang',
                text='根據您的需求點選點選下方功能',
                thumbnail_image_url='https://drive.google.com/uc?id=1N4Hm6EQL1RP8fMuvAWBfFUOueOPZejLp&export=download',
                actions=[
                    MessageTemplateAction(
                        label='經歷/Experience',
                        text='經歷/Experience'
                    ),
                    MessageTemplateAction(
                        label='著作/Essay',
                        text='著作/Essay'
                    ),
                    MessageTemplateAction(
                        label='作品集/Project',
                        text='作品集/Project'
                    )
                ]
            )
        )

    def get_msg(self):
        return self._msg

    def get_next_state_by_reply(self, user_reply):
        if user_reply == '經歷/Experience':
            return experienceState.ExperienceState("./wording/experience.json")
        elif user_reply == '作品集/Project':
            return experienceState.ExperienceState("./wording/project.json")
        return IndexState()
