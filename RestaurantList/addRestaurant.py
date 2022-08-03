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
                                    "text": "1.음식점 이름을 입력해주세요(중복이름은 등록이 안되므로 필요시 지점명도 입력해주세요)"
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
                                    "text": "2.종류를 입력해주세요(1.한식 / 2.일식 / 3.중식 / 4.양식 / 5.아시안 / 6.랜덤)"
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
                if int(requestDto.content)>0 or int(requestDto.content)<7:
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "3.금액대(만원)를 입력해주세요(모르거나 애매하면 0)"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 2,
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
                                        "text": "입력값 오류. 종류를 다시 입력해주세요"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "추가",
                                    "lifeSpan": 4,
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
                                        "text": "요청내용 : "+requestDto.param1+" , "+requestDto.param2+", "+requestDto.content+"\nDB 구성중. 구성되고 나면 레스토랑 추가 기능 수행"
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