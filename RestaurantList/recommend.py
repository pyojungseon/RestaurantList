import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO
from DTO.ContextDTO import ContextDTO
from MariaDB.DBCon import DBConnection

class recommend:

    def rec(self, requestDto, dbCon):

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
                                        "text": "금액대(만원)을 입력하세요(제한없음은 0, 최대값은 12)"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추천",
                                    "lifeSpan": 3,
                                    "params": {
                                        "param1": requestDto.content
                                    }
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
                if int(requestDto.content)<0 or int(requestDto.content)>13:
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "입력 금액 오류입니다 다시 입력해주세요"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추천",
                                    "lifeSpan": 2,
                                    "params": {
                                        "param1": requestDto.param1
                                    }
                                }
                            ]
                        }
                    }
                else:
                    conData = ContextDTO(requestDto.userId, requestDto.tag, requestDto.lifeSpan, requestDto.content, 'N')
                    contextData = dbCon.getContextData(conData)
                    print(contextData)
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "용도는?\n(0:없음 1:팀장급이상 회식 2:차과장급 회식 3:조사역급 회식 4:목성 5:노조간담회비)"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추천",
                                    "lifeSpan": 1,
                                    "params": {
                                        "param1": requestDto.param1,
                                        "param2": requestDto.content
                                    }
                                }
                            ]
                        }
                    }
            elif requestDto.lifeSpan == 2:
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "요청내용 : "+requestDto.param1+" , "+requestDto.param2+", "+requestDto.param3
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "추천",
                                "lifeSpan": 0,
                                "params": {
                                    "param1": requestDto.param1,
                                    "param2": requestDto.param2,
                                    "param3": requestDto.param3
                                }
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
                                    "text": "입력 오류입니다 다시 입력해주세요"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "추천",
                                "lifeSpan": 0,
                                "params": {
                                    "param1": "",
                                    "param2": "",
                                    "param3": "",
                                    "param4": "",
                                    "param5": ""
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