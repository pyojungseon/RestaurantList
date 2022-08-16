import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO


class requestParsing:

    def parsing(self, params):
        print(params)

        userId = params['userRequest']['user']['id']
        userId = userId.replace("\n", "")
        content = params['userRequest']['utterance']
        content = content.replace("\n", "")
        header = content.split(" ")[0]

        contextSize = len(params['contexts'])
        tagPoint = 0
        lifeSpan = 0
        param1=""
        param2=""
        param3=""
        param4=""
        param5=""

        tag = ""
        if contextSize>0:
            for i in range(0,contextSize):
                if int(params['contexts'][i]['lifespan'])<5:
                    tag = params['contexts'][i]['name']
                    lifeSpan = params['contexts'][i]['lifespan']
                    tagPoint=i
                    break
        else:
            tag = header
            lifeSpan = 0

        if not params['action']['clientExtra']['param1']:
            param1 = params['action']['clientExtra']['param1']
        elif not params['contexts'][tagPoint]['params']['param1']['value']:
            param1 = params['contexts'][tagPoint]['params']['param1']['value']

        if not params['action']['clientExtra']['param2']:
            param2 = params['action']['clientExtra']['param2']
        elif not params['contexts'][tagPoint]['params']['param2']['value']:
            param2 = params['contexts'][tagPoint]['params']['param2']['value']

        if not params['action']['clientExtra']['param3']:
            param3 = params['action']['clientExtra']['param3']
        elif not params['contexts'][tagPoint]['params']['param3']['value']:
            param3 = params['contexts'][tagPoint]['params']['param3']['value']

        if content=="사용법" or content=="추가" or content=="추천" or content=="수정" or content=="평가" or content=="건의":
            tag = content

        print(content)
        print(userId)
        print("tag : " + tag)
        print("lifepan : " + str(lifeSpan))
        print("param1 : " + str(param1))
        print("param2 : " + str(param2))
        print("param3 : " + str(param3))
        dto = RequestDTO(userId, content, header, tag, lifeSpan, param1, param2, param3, param4, param5)
        return dto
