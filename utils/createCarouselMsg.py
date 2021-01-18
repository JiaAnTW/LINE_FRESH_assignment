from linebot.models import MessageTemplateAction, URITemplateAction, TemplateSendMessage, CarouselTemplate, CarouselColumn


def createCarouselMsg(infoArr):
    outputMsg = []
    for title, info in infoArr.items():
        outputMsg.append(
            CarouselColumn(
                thumbnail_image_url=info['imageUrl'],
                title=title,
                text=info['subtitle'],
                actions=[
                    MessageTemplateAction(
                        label='說明/description',
                        text=title
                    ),
                    URITemplateAction(
                        label='連結/link',
                        uri=info['link']
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
