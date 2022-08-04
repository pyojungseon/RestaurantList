import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO
from MariaDB.DBCon import DBConnection

class modRestaurant:

    def delRes(self, requestDto, dbCon):

        if requestDto.tag == "수정":
            print("수정 content in")
            if requestDto.lifeSpan == 5 or requestDto.lifeSpan == 0:
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "수정을 원하는 음식점 명을 입력해주세요."
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "수정",
                                "lifeSpan": 5
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
                                    "text": requestDto.content+" 음식점 정보 출력하기\n수정내용(0:금액대 1:음식구분 2:목적성 3:삭제)\n삭제의 경우 2명 이상의 신고가 필요합니다."
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "수정",
                                "lifeSpan": 3,
                                "params": {
                                    "param1": requestDto.content
                                }
                            }
                        ]
                    }
                }
            elif requestDto.lifeSpan == 3:
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": requestDto.content + ": 수정할 내용을 입력해주세요"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "수정",
                                "lifeSpan": 2,
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
                                    "text": requestDto.param1+", "+requestDto.param2+", "+requestDto.content+ " 수정기능 구현 중"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "수정",
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
                                    "text": "입력 오류입니다 다시 입력해주세요"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "수정",
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
                            "name": "수정",
                            "lifeSpan": 0
                        }
                    ]
                }
            }
        return dataSend