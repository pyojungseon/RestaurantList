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
        try:
            tag = params['contexts'][0]['name']
        except Exception as ex:
            print(ex)
            tag = header
        try:
            lifeSpan = params['contexts'][0]['lifespan']
        except Exception as ex:
            lifeSpan = 0
        try:
            param1 = params['contexts'][0]['params']['param1']['value']
        except Exception as ex:
            param1 = ""
        try:
            param2 = params['contexts'][0]['params']['param2']['value']
        except Exception as ex:
            param2 = ""
        try:
            param3 = params['contexts'][0]['params']['param3']['value']
        except Exception as ex:
            param3 = ""

        param4=""
        param5=""
        print(content)
        print(userId)
        print("tag : " + tag)
        print("lifepan : " + str(lifeSpan))
        print("param1 : " + str(param1))
        print("param2 : " + str(param2))
        print("param3 : " + str(param3))
        dto = RequestDTO(userId, content, header, tag, lifeSpan, param1, param2, param3, param4, param5)
        return dto
