import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO
from DTO.restaurantDTO import restaurantDTO
from MariaDB.DBCon import DBConnection
from getThumbnail import getThumbnail

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
                                "carousel": {
                                    "type": "basicCard",
                                    "items": [
                                        {
                                            "title": "맛집추천 챗봇입니다",
                                            "description": "본관 주변 맛집을 찾아봅시다",
                                            "thumbnail": {
                                                "imageUrl": ""
                                            },
                                            "buttons": [
                                                {
                                                    "action": "message",
                                                    "label": "1.한식",
                                                    "messageText": "한식"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "2.일식",
                                                    "messageText": "일식"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "3.중식",
                                                    "messageText": "중식"
                                                }
                                            ]
                                        },
                                        {
                                            "title": "개인서버로 서비스 되고있습니다",
                                            "description": "개선 아이디어는 언제나 환영합니다",
                                            "thumbnail": {
                                                "imageUrl": ""
                                            },
                                            "buttons": [
                                                {
                                                    "action": "message",
                                                    "label": "4.양식",
                                                    "messageText": "양식"
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
                                    "param1": requestDto.content,
                                    "param2": requestDto.param2,
                                    "param3": requestDto.param3,
                                    "param4": requestDto.param4
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
                                "carousel": {
                                    "type": "basicCard",
                                    "items": [
                                        {
                                            "title": "금액대를 입력해주세요",
                                            "description": "적당한 가격대?",
                                            "thumbnail": {
                                                "imageUrl": ""
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
                                                    "label": "3만원",
                                                    "messageText": "3"
                                                }
                                            ]
                                        },
                                        {
                                            "title": "금액대를 입력해주세요",
                                            "description": "아니면 비싼걸로?",
                                            "thumbnail": {
                                                "imageUrl": ""
                                            },
                                            "buttons": [
                                                {
                                                    "action": "message",
                                                    "label": "4~6만원",
                                                    "messageText": "4"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "그 이상",
                                                    "messageText": "5"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "랜덤",
                                                    "messageText": "6"
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
                                "name": "추천",
                                "lifeSpan": 3,
                                "params": {
                                    "param1": requestDto.param1,
                                    "param2": requestDto.content,
                                    "param3": requestDto.param3,
                                    "param4": requestDto.param4
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
                                "carousel": {
                                    "type": "basicCard",
                                    "items": [
                                        {
                                            "title": "맛집추천",
                                            "description": "무슨 목적이실까요?",
                                            "thumbnail": {
                                                "imageUrl": ""
                                            },
                                            "buttons": [
                                                {
                                                    "action": "message",
                                                    "label": "0.없음",
                                                    "messageText": "0"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "1.목성",
                                                    "messageText": "1"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "2.야식(PAYCO)",
                                                    "messageText": "2"
                                                }
                                            ]
                                        },
                                        {
                                            "title": "맛집추천",
                                            "description": "회식용도?",
                                            "thumbnail": {
                                                "imageUrl": ""
                                            },
                                            "buttons": [
                                                {
                                                    "action": "message",
                                                    "label": "3.팀장회식",
                                                    "messageText": "3"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "4.과차장회식",
                                                    "messageText": "4"
                                                },
                                                {
                                                    "action": "message",
                                                    "label": "5.조사역회식",
                                                    "messageText": "5"
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
                                "name": "추천",
                                "lifeSpan": 2,
                                "params": {
                                    "param1": requestDto.param1,
                                    "param2": requestDto.param2,
                                    "param3": requestDto.content,
                                    "param4": requestDto.param4
                                }
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 2:
                print("추천 content in lifespan = "+str(requestDto.lifeSpan))
                restDto = restaurantDTO()
                restDto.tag=requestDto.param2
                restDto.hprice=requestDto.param3
                restDto.lprice = requestDto.param3
                if requestDto.param4 == 2:
                    restDto.moksung="Y"
                elif requestDto.param4 == 3:
                    restDto.payco="Y"
                elif requestDto.param4 == 4:
                    restDto.mn5="Y"
                elif requestDto.param4 == 5:
                    restDto.mn4="Y"
                elif requestDto.param4 == 6:
                    restDto.mn2="Y"

                restList = dbCon.getRecRestaurants(restDto)
                print("갯수 : "+str(len(restList)))
                if len(restList)==0:
                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "simpleText": {
                                        "text": "아쉽게도 요청하신 내용의 식당이 없습니다 ㅠ.ㅠ 많은 등록 부탁드려요!"
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
                                        "param4": ""
                                    }
                                }
                            ]
                        }
                    }
                else:
                    thumbnail = getThumbnail()
                    length=len(restList)
                    rdnumber=[]
                    if len(restList)>3:
                        rdnumber=random.randint(0,length-1)
                        length=3
                        while rnd_num in rdnumber:
                            rnd_num = random.randint(1, 45)
                        rdnumber.append(rnd_num)
                    else:
                        for i in range(0,length):
                            rdnumber.append(i)
                    items=[]
                    for i in range(0, length):
                        pointer=rnd_num[i]
                        print("items 추가 : "+str(i)+restList[pointer][1])
                        eval = ""
                        if (restList[pointer][11] is None) :
                            eval = "아직 평가내용이 없습니다. 내용을 등록해주세요!"
                        else :
                            eval = "평가 : "+restList[pointer][11]
                        items.append({
                            "title": restList[pointer][1],
                            "description": eval,
                            "thumbnail": {
                                "imageUrl": thumbnail.getThumbnail(restList[pointer][1])
                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "위치",
                                    "webLinkUrl": restList[pointer][5]
                                },
                                {
                                    "action": "message",
                                    "label": "평가하기",
                                    "messageText": "평가 " + restList[pointer][1]
                                }
                            ]
                        })
                    print(str(items))

                    dataSend = {
                        "version": "2.0",
                        "template": {
                            "outputs": [
                                {
                                    "carousel": {
                                        "type": "basicCard",
                                        "items": items
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
                                        "param4": ""
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