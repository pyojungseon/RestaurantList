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
                                "basicCard": {
                                    "title": "BOK 맛집추천",
                                    "description": "메뉴 종류를 입력해주세요",
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "profile": {
                                        "imageUrl": "",
                                        "nickname": "bok프로필"
                                    },
                                    "buttons": [
                                        {
                                            "action": "message",
                                            "label": "1.한식",
                                            "messageText": "한식"
                                        },
                                        {
                                            "action": "message",
                                            "label": "2.양식",
                                            "messageText": "양식"
                                        },
                                        {
                                            "action": "message",
                                            "label": "3.일식",
                                            "messageText": "일식"
                                        },
                                        {
                                            "action": "message",
                                            "label": "4.중식",
                                            "messageText": "중식"
                                        },
                                        {
                                            "action": "message",
                                            "label": "5.아시안",
                                            "messageText": "아시안"
                                        },
                                        {
                                            "action": "message",
                                            "label": "6.랜덤",
                                            "messageText": "랜덤"
                                        }
                                    ]
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
                                "basicCard": {
                                    "title": "BOK 맛집추천",
                                    "description": "금액대를 입력해주세요",
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "profile": {
                                        "imageUrl": "",
                                        "nickname": "bok프로필"
                                    },
                                    "buttons": [
                                        {
                                            "action": "message",
                                            "label": "1만원",
                                            "messageText": "1"
                                        },
                                        {
                                            "action": "message",
                                            "label": "2만원",
                                            "messageText": "2"
                                        },
                                        {
                                            "action": "message",
                                            "label": "3~6만원",
                                            "messageText": "3"
                                        },
                                        {
                                            "action": "message",
                                            "label": "6만원 이상",
                                            "messageText": "6"
                                        }
                                    ]
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
                                "basicCard": {
                                    "title": "BOK 맛집추천",
                                    "description": "목적을 입력해주세요",
                                    "thumbnail": {
                                        "imageUrl": ""
                                    },
                                    "profile": {
                                        "imageUrl": "",
                                        "nickname": "bok프로필"
                                    },
                                    "buttons": [
                                        {
                                            "action": "message",
                                            "label": "1.없음",
                                            "messageText": "1"
                                        },
                                        {
                                            "action": "message",
                                            "label": "2.팀장회식",
                                            "messageText": "2"
                                        },
                                        {
                                            "action": "message",
                                            "label": "3.과차장회식",
                                            "messageText": "3"
                                        },
                                        {
                                            "action": "message",
                                            "label": "4.조사역회식",
                                            "messageText": "4"
                                        },
                                        {
                                            "action": "message",
                                            "label": "5.목성",
                                            "messageText": "5"
                                        },
                                        {
                                            "action": "message",
                                            "label": "6.야식(PAYCO)",
                                            "messageText": "6"
                                        }
                                    ]
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