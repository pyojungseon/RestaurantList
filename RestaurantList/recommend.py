import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO

class recommend:

    def rec(self, requestDto):

        if requestDto.header == "아이디":
            print("if문아이디 content in")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": requestDto.userId
                            }
                        }
                    ]
                }
            }

        elif requestDto.header == "사용법":
            print("사용법 content in")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": '''BOK본관 부근 음식점 추천 챗봇입니다.
                                \n기능 : 추천 / 평가 / 추가'''
                            }
                        }
                    ]
                }
            }
        elif requestDto.tag == "추천":
            print("추천 content in")
            if lifeSpan == 5 or lifeSpan == 0:
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "1.한식 / 2.일식 / 3.중식 / 4.양식 / 5.아시안 / 6.랜덤 중 입력하세요(4 또는 양식)"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "추천",
                                "lifeSpan": 4
                            }
                        ]
                    }
                }
            elif lifeSpan == 4:
                if content == str(1):
                    content = "한식"
                elif content == str(2):
                    content = "일식"
                elif content == str(3):
                    content = "중식"
                elif content == str(4):
                    content = "양식"
                elif content == str(5):
                    content = "아시안"
                elif content == str(6):
                    content = "랜덤"

                if content == "한식" or content == "일식" or content == "중식" or content == "양식" or content == "아시안" or content == "랜덤":
                    conData = ContextDTO(requestDto.userId, requestDto.tag, requestDto.lifeSpan, requestDto.content, 'N')
                    dbCon.insertContextData(conData)
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "금액대(만원)을 입력하세요(제한없음은 0)"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추천",
                                    "lifeSpan": 3
                                }
                            ]
                        }
                    }
                else:
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "입력값 오류! 다시 입력해주세요"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추천",
                                    "lifeSpan": 0
                                }
                            ]
                        }
                    }
            elif requestDto.lifeSpan == 3:
                conData = ContextDTO(requestDto.userId, requestDto.tag, requestDto.lifeSpan, requestDto.content, 'N')
                contextData = dbCon.getContextData(conData)
                print(contextData)

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
        else:
            print("if문 content out")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "입력오류! 사용법이 궁금하시면 사용법이라고 입력해주세요."
                            }
                        }
                    ]
                },
                "context": {
                    "values": [
                        {
                            "name": "추천",
                            "lifeSpan": 0
                        }
                    ]
                }
            }
        return dataSend