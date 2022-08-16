import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO
from MariaDB.DBCon import DBConnection

class recRestaurant:

    def rec(self, requestDto, dbCon):

        if requestDto.tag == "추천":
            print("추천 content in")
            if requestDto.lifeSpan == 5 or requestDto.lifeSpan == 0:
                print("추천 content in lifespan = "+str(requestDto.lifeSpan))
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
                                "lifeSpan": 4,
                                "params": {
                                    "param1": requestDto.param1,
                                    "param2": requestDto.param2,
                                    "param3": requestDto.param3
                                }
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 4:
                print("추천 content in lifespan = "+str(requestDto.lifeSpan))
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
                                    "param1": requestDto.param1,
                                    "param2": requestDto.param2,
                                    "param3": requestDto.param3
                                }
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 3:
                print("추천 content in lifespan = "+str(requestDto.lifeSpan))
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "요청내용 : "+requestDto.param1+" , "+requestDto.param2+", "+requestDto.content+"\nDB 구성중. 구성되고 나면 추천레스토랑 보여줄 것"
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
                                    "param1": requestDto.param1,
                                    "param2": requestDto.param2,
                                    "param3": requestDto.param3
                                }
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 2:
                print("추천 content in lifespan = "+str(requestDto.lifeSpan))
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "2요청내용 : "+requestDto.param1+" , "+requestDto.param2+", "+requestDto.content+"\nDB 구성중. 구성되고 나면 추천레스토랑 보여줄 것"
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
                                    "param3": ""
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