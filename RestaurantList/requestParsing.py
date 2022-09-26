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

        contextSize = len(params['contexts'])
        tagPoint = 0
        lifeSpan = 0
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


        param4=""
        param5=""

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
