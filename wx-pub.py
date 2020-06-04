import logging.config
import requests
import werobot
from werobot import WeRoBot

from qa_tool import QaTool

logger = logging.getLogger(__name__)
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

robot = werobot.WeRoBot(token='abc')

# bot_url = "http://dialogue_agent:5008/dialogue_agent/response"
bot_url = "http://0.0.0.0:5008/dialogue_agent/response"
a = WeRoBot()

data_path = 'data/qa_pair_data.txt'
qa_tool = QaTool(data_path)


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
    r = requests.post(bot_url, json=post_json, timeout=3)
    response_texts = []
    if 'responseText' in r:
        for cont in r['responseText']:
            rtype = cont.get('type')
            content = cont.get('content')
            if rtype == 'Text':
                response_texts.append(content)
            elif rtype == 'QA':
                answers = content.get('answers', [])
                if len(answers) == 1:
                    know_id = answers[0].get('answer')
                    answer = qa_tool.get_answer(tenant_id, know_id)
                    response_texts.append(answer)
                elif len(answers) > 1:
                    titles = []
                    for ans in answers:
                        know_id = ans.get('answer')
                        title = qa_tool.get_title(tenant_id, know_id)
                        titles.append(title)
                    response_texts.append("你想咨询以下哪些问题？" + "\n".join(titles))
    response_text = "\n".join(response_texts)

    return response_text


@robot.image
def img(message):
    return message.img


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
