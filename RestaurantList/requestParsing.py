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
        tag=""
        if contextSize>0:
            for i in range(0,contextSize):
                if int(params['contexts'][i]['lifespan'])<5:
                    lifeSpan = params['contexts'][i]['lifespan']
                    tag = params['contexts'][i]['name']
                    tagPoint=i
                    break

        try:
            param1 = params['action']['clientExtra']['param1']
        except Exception as ex:
            try :
                param1 = params['contexts'][tagPoint]['params']['param1']['value']
            except Exception as ex:
                param1 = ""

        try:
            param2 = params['action']['clientExtra']['param2']
        except Exception as ex:
            try:
                param2 = params['contexts'][tagPoint]['params']['param2']['value']
            except Exception as ex:
                param2 = ""
        try:
            param3 = params['action']['clientExtra']['param3']
        except Exception as ex:
            try:
                param3 = params['contexts'][tagPoint]['params']['param3']['value']
            except Exception as ex:
                param3 = ""
        try:
            param4 = params['action']['clientExtra']['param4']
        except Exception as ex:
            try:
                param4 = params['contexts'][tagPoint]['params']['param4']['value']
            except Exception as ex:
                param4 = ""

        param5=""

        if header=="사용법" or header=="추가" or header=="추천" or header=="수정" or header=="평가" or header=="건의":
            tag = content

        print(content)
        print(userId)
        print("tag : " + tag)
        print("lifepan : " + str(lifeSpan))
        print("param1 : " + str(param1))
        print("param2 : " + str(param2))
        print("param3 : " + str(param3))
        dto = RequestDTO(userId, content, tag, tag, lifeSpan, param1, param2, param3, param4, param5)
        return dto
