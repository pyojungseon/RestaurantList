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
            lifeSpan = params['contexts'][0]['lifespan']
            param1 = params['contexts'][0]['param1']
            param2= params['contexts'][0]['param2']
            param3 = params['contexts'][0]['param3']
            param4 = params['contexts'][0]['param4']
            param5 = params['contexts'][0]['param5']
        except Exception as ex:
            print(ex)
            tag = header
            lifeSpan = 0
            param1 = ""
            param2 = ""
            param3 = ""
            param4 = ""
            param5 = ""


        print(content)
        print(userId)
        print("tag : " + tag)
        print("lifepan : " + str(lifeSpan))
        dto = RequestDTO(userId, content, header, tag, lifeSpan, param1, param2, param3, param4, param5)
        return dto
