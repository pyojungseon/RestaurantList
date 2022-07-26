import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO

class basement:

    def ment(self, requestDto):

        if requestDto.content == "아이디":
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
        elif requestDto.content == "김소영":
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
        elif requestDto.content == "섹스":
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
            print("사용법 content in")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "carousel": {
                                "type": "basicCard",
                                "items": [
                                    {
                                        "title": "맛집추천 챗봇입니다.",
                                        "description": "무엇을 원하시나요?",
                                        "thumbnail": {
                                            "imageUrl": ""
                                        },
                                        "buttons": [
                                            {
                                                "action": "message",
                                                "label": "추천",
                                                "messageText": "추천"
                                            },
                                            {
                                                "action": "message",
                                                "label": "평가",
                                                "messageText": "평가"
                                            },
                                            {
                                                "action": "message",
                                                "label": "건의",
                                                "messageText": "건의"
                                            }
                                        ]
                                    },
                                    {
                                        "title": "맛집추천 챗봇입니다.",
                                        "description": "나만아는 맛집? 등록해주세요! ^^",
                                        "thumbnail": {
                                            "imageUrl": ""
                                        },
                                        "buttons": [
                                            {
                                                "action": "message",
                                                "label": "추가",
                                                "messageText": "추가"
                                            },
                                            {
                                                "action": "message",
                                                "label": "수정",
                                                "messageText": "수정"
                                            },
                                            {
                                                "action": "message",
                                                "label": "삭제",
                                                "messageText": "삭제"
                                            }
                                        ]
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
                        }, {
                            "name": "추천",
                            "lifeSpan": 0
                        }, {
                            "name": "수정",
                            "lifeSpan": 0
                        }, {
                            "name": "평가",
                            "lifeSpan": 0
                        }, {
                            "name": "삭제",
                            "lifeSpan": 0
                        }, {
                            "name": "건의",
                            "lifeSpan": 0
                        }
                    ]
                }
            }
        return dataSend