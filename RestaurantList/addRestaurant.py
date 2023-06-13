import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO
from MariaDB.DBCon import DBConnection

class addRestaurant:

    def add(self, requestDto, dbCon):

        if requestDto.tag == "추가":
            print("추가 content in")
            if requestDto.lifeSpan == 5 or requestDto.lifeSpan == 0:
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "(추가 기능 개발중) 음식점 이름을 입력해주세요(이름 중복등록 불가하므로 프렌차이즈는 지점명까지 부탁드립니다)"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "추가",
                                "lifeSpan": 4
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 4:
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "2.종류를 입력해주세요\n(숫자로 입력. 1.한식 / 2.일식 / 3.중식 / 4.양식 / 5.아시안)"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "추가",
                                "lifeSpan": 3,
                                "params": {
                                    "param1": requestDto.content
                                }
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 3:
                if int(requestDto.content)>0 or int(requestDto.content)<6:
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "3.최소금액대(만원)를 입력해주세요"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 1,
                                    "params": {
                                        "param1": requestDto.param1,
                                        "param2": requestDto.content
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
                                        "text": "입력값 오류. 다시 입력해주세요\n(숫자로 입력. 1.한식 / 2.일식 / 3.중식 / 4.양식 / 5.아시안)"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 3,
                                    "params": {
                                        "param1": requestDto.param1
                                    }
                                }
                            ]
                        }
                    }
            elif requestDto.lifeSpan == 2:
                if int(requestDto.content) > 0 or int(requestDto.content) < 21:
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "4.목적성이 있나요? 숫자로 입력해주세요. "
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 1,
                                    "params": {
                                        "param1": requestDto.param1,
                                        "param2": requestDto.param2,
                                        "param3": requestDto.content
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
                                        "text": "입력값 오류. 다시 입력해주세요"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 3,
                                    "params": {
                                        "param1": requestDto.param1,
                                        "param2": requestDto.param2
                                    }
                                }
                            ]
                        }
                    }
            elif requestDto.lifeSpan == 1:
                if int(requestDto.content) > 0 or int(requestDto.content) < 21:
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "요청내용 : "+requestDto.param1+" , "+requestDto.param2+", "+requestDto.content+"\n 입력하신 자료는 검토 후 등록될 예정입니다. 자료 감사합니다."
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 0,
                                    "params": {
                                        "param1": requestDto.param1,
                                        "param2": requestDto.param2,
                                        "param3": requestDto.content
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
                                        "text": "입력값 오류. 금액을 다시 입력해주세요"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 3,
                                    "params": {
                                        "param1": requestDto.param1
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
                                "name": "추가",
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
        else:
            print("if문 content out")
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "추가 기능 입력오류! 사용법이 궁금하시면 사용법이라고 입력해주세요."
                            }
                        }
                    ]
                },
                "context": {
                    "values": [
                        {
                            "name": "추가",
                            "lifeSpan": 0
                        }
                    ]
                }
            }
        return dataSend