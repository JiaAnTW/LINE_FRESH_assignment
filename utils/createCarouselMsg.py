from linebot.models import MessageTemplateAction, URITemplateAction, TemplateSendMessage, CarouselTemplate, CarouselColumn


def createCarouselMsg(msgArr):
    outputMsg = []
    for msg in msgArr:
        outputMsg.append(
            CarouselColumn(
                thumbnail_image_url=msg['imageUrl'],
                title=msg['title'],
                text=msg['subtitle'],
                actions=[
                    MessageTemplateAction(
                        label='說明/description',
                        text=msg['title']+'的說明'
                    ),
                    URITemplateAction(
                        label='連結/link',
                        uri=msg['link']
                    ),
                    MessageTemplateAction(
                        label='返回/back',
                        text='返回/back'
                    ),
                ]
            )
        )
    return TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(columns=outputMsg)
    )
