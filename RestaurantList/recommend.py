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
            if requestDto.lifeSpan == 5 or requestDto.lifeSpan == 0:
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
            elif requestDto.lifeSpan == 4:
                if requestDto.content == str(1):
                    requestDto.content = "한식"
                elif requestDto.content == str(2):
                    requestDto.content = "일식"
                elif requestDto.content == str(3):
                    requestDto.content = "중식"
                elif requestDto.content == str(4):
                    requestDto.content = "양식"
                elif requestDto.content == str(5):
                    requestDto.content = "아시안"
                elif requestDto.content == str(6):
                    requestDto.content = "랜덤"

                if requestDto.content == "한식" or requestDto.content == "일식" or requestDto.content == "중식" or requestDto.content == "양식" or requestDto.content == "아시안" or requestDto.content == "랜덤":
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