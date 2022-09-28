import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO
from MariaDB.DBCon import DBConnection

class evalRestaurant:

    def evalRes(self, requestDto, dbCon):

        if requestDto.tag == "평가":
            print("평가 content in")
            lifespan=4
            if requestDto.lifeSpan == 5 or requestDto.lifeSpan == 0:
                contents = requestDto.content.split(" ")
                if len(contents)>1:
                    name = contents[1]
                    restaurnt = dbCon.getRestaurant(name)
                    if len(restaurnt)>1:
                        dataSend = {
                            "version": "2.0",
                            "template": {
                                "outputs": [
                                    {
                                        "simpleText": {
                                            "text": "가계명 : "+name+" 에 대한 평가멘트를 적어주세요."
                                        }
                                    }
                                ]
                            },
                            "context": {
                                "values": [
                                    {
                                        "name": "평가",
                                        "lifeSpan": lifespan-1,
                                        "params": {
                                            "param1": name,
                                            "param2": ""
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
                                            "text": "가계명 : "+name+ "이 등록되어있지 않습니다. 평가할 가계명을 다시 입력해주세요"
                                        }
                                    }
                                ]
                            },
                            "context": {
                                "values": [
                                    {
                                        "name": "평가",
                                        "lifeSpan": lifespan,
                                        "params": {
                                            "param1": "",
                                            "param2": ""
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
                                        "text": "평가할 가계명을 입력해주세요"
                                    }
                                }
                            ]
                        },
                        "context": {
                            "values": [
                                {
                                    "name": "평가",
                                    "lifeSpan": lifespan,
                                    "params": {
                                        "param1": "",
                                        "param2": ""
                                    }
                                }
                            ]
                        }
                    }
            elif requestDto.lifeSpan == 4:
                name = requestDto.content
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "가계명 : "+name+" 의 평가 문구를 입력해주세요"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "평가",
                                "lifeSpan": 3,
                                "params": {
                                    "param1": name,
                                    "param2": ""
                                }
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 3:
                name = requestDto.param1
                content = requestDto.content
                dbCon.updateRestEval(name, content)
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "입력 완료되었습니다"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "평가",
                                "lifeSpan": 5,
                                "params": {
                                    "param1": "",
                                    "param2": ""
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
                            "name": "평가",
                            "lifeSpan": 0
                        }
                    ]
                }
            }
        return dataSend