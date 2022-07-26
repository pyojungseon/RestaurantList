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
            print(ex)
            lifeSpan = 0

        print(content)
        print(userId)
        print("tag : " + tag)
        print("lifepan : " + str(lifeSpan))
        dto = RequestDTO(userId, content, header, tag, lifeSpan)
        return dto
