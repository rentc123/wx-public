import requests
import werobot

robot = werobot.WeRoBot(token='abc')

bot_url = "http://dialogue_agent:5008/dialogue_agent/response"


@robot.text
def hello(message):
    user_input_text = message.content
    message_id = message.message_id
    user_id = message.source
    tenant_id = "1000"
    qaParams = {
        "toAnswer": 3,
        "lang": "zh"
    }
    post_json = {
        "tenantId": tenant_id,
        "userId": str(user_id),
        "messageId": message_id,
        "text": user_input_text,
        "qaParams": qaParams
    }
    #
    r=requests.post(bot_url, json=post_json, timeout=3)

    return "{} {} {}".format(user_id, user_input_text, message_id)


@robot.image
def img(message):
    return message.img


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
