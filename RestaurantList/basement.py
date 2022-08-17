import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO

class basement:

    def ment(self, requestDto):

        if requestDto.header == "사용법":
            print("사용법 content in")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "basicCard": {
                                "title": "BOK챗봇",
                                "description": "원하시는 기능을 선택해주세요",
                                "thumbnail": {
                                    "imageUrl": ""
                                },
                                "profile": {
                                    "imageUrl": "#",
                                    "nickname": "bok프로필"
                                },
                                "buttons": [
                                    {
                                        "action": "block",
                                        "label": "추천",
                                        "blockId": "62fb28a0fb4d7520b2bbd64b"
                                    },
                                    {
                                        "label": "건의",
                                        "action": "block",
                                        "blockId": "62fb2254f534cf44c78ed656"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "context": {
                    "values": [
                        {
                            "name": "추가",
                            "lifeSpan": 0
                        },{
                            "name": "추천",
                            "lifeSpan": 0
                        },{
                            "name": "수정",
                            "lifeSpan": 0
                        },{
                            "name": "평가",
                            "lifeSpan": 0
                        }
                    ]
                }
            }

        elif requestDto.header == "아이디":
            print("if문 아이디 content in")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "Hash : "+requestDto.userId
                            }
                        }
                    ]
                }
            }
        elif requestDto.header == "김소영":
            print("if문김소영 content in")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "알라뷰~~"
                            }
                        }
                    ]
                }
            }
        elif requestDto.header == "섹스":
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "이런짓은 하는 인간은 고현석뿐 닥쳐라!!"
                            }
                        }
                    ]
                }
            }
        else:
            print("base if문 content out")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "입력값 오류! 사용법이 궁금하시면 사용법이라고 입력해주세요."
                            }
                        }
                    ]
                }
            }
        return dataSend