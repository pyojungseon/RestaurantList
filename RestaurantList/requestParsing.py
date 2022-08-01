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

        try:
            param1 = params['contexts'][tagPoint]['params']['param1']['value']
        except Exception as ex:
            param1 = ""
        try:
            param2 = params['contexts'][tagPoint]['params']['param2']['value']
        except Exception as ex:
            param2 = ""
        try:
            param3 = params['contexts'][tagPoint]['params']['param3']['value']
        except Exception as ex:
            param3 = ""

        param4=""
        param5=""

        if content=="사용법" or content=="추가" or content=="추천" or content=="삭제":
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
