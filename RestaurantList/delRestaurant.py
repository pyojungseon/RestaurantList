import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import RequestDTO
from DTO.ContextDTO import ContextDTO
from MariaDB.DBCon import DBConnection

class delRestaurant:

    def delRes(self, requestDto, dbCon):

        if requestDto.tag == "삭제":
            print("삭제 content in")
            if requestDto.lifeSpan == 5 or requestDto.lifeSpan == 0:
                dataSend = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "simpleText": {
                                    "text": "삭제기능 구현 중"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "삭제",
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
                                    "text": "삭제기능 구현 중"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "삭제",
                                "lifeSpan": 5,
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
                                    "text": "입력 오류입니다 다시 입력해주세요"
                                }
                            }
                        ]
                    },
                    "context": {
                        "values": [
                            {
                                "name": "삭제",
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
                            "name": "삭제",
                            "lifeSpan": 0
                        }
                    ]
                }
            }
        return dataSend