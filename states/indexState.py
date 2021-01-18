from states import state, experienceState, textState
from linebot.models import MessageTemplateAction, ButtonsTemplate, TemplateSendMessage


class IndexState(state.State):
    def __init__(self):
        self.intro_msg = "大二從交管系平轉至資工系後開始自學網頁前後端開發，接觸 React.js 兩年。目前主攻web/App 等軟體開發技術，是個 70%前端、30%後端的產品開發者。 偶爾會研究和產品開發相關的知識，如 UI/UX、產品管理、簡報設計等。"
        self._msg = TemplateSendMessage(
            alt_text='張家銨 LINE FRESH',
            template=ButtonsTemplate(
                title='張家銨 Jia An Chang',
                text='根據您的需求點選點選下方功能',
                thumbnail_image_url='https://drive.google.com/uc?id=1N4Hm6EQL1RP8fMuvAWBfFUOueOPZejLp&export=download',
                actions=[
                    MessageTemplateAction(
                        label='個人簡介/Introduction',
                        text='個人簡介/Introduction'
                    ),
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
        if user_reply == '個人簡介/Introduction':
            return textState.TextState(
                text=self.intro_msg,
                before_state=IndexState()
            )
        elif user_reply == '經歷/Experience':
            return experienceState.ExperienceState("./wording/experience.json")
        elif user_reply == '著作/Essay':
            return experienceState.ExperienceState("./wording/essay.json")
        elif user_reply == '作品集/Project':
            return experienceState.ExperienceState("./wording/project.json")
        return IndexState()
