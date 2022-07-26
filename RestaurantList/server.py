from flask import Flask, json, request, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.LogDTO import LogDTO
from DTO.ContextDTO import ContextDTO
from MariaDB.DBCon import DBConnection

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask"

@app.route('/restaurant', methods=['POST'])
def restaurant():
    params = request.get_json()
    print(params)
    userId = params['userRequest']['user']['id']
    userId = userId.replace("\n", "")
    content = params['userRequest']['utterance']
    content = content.replace("\n", "")
    header = content.split(" ")[0]
    try:
        tag = params['contexts'][0]['name']
    except Exception as ex:
        print(ex)
        tag=header
    try:
        lifeSpan = params['contexts'][0]['lifespan']
    except Exception as ex:
        print(ex)
        lifeSpan=0

    print(content)
    print(userId)
    print("tag : "+tag)
    print("lifepan : "+str(lifeSpan))

    logData = LogDTO(userId, content, tag)
    dbCon.insertLogData(logData)

    if header == "아이디":
        print("if문아이디 content in")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": userId
                        }
                    }
                ]
            }
        }

    elif header == "사용법":
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
    elif tag == "추천":
        print("추천 content in")
        if lifeSpan==5 or lifeSpan==0:
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
        elif lifeSpan==4 :
            if content==1 :
                content="한식"
            elif content==2:
                content="일식"
            elif content==3:
                content="중식"
            elif content==4:
                content="양식"
            elif content==5:
                content="아시안"
            elif content==6:
                content="랜덤"

            if content=="한식" or content=="일식" or content=="중식" or content=="양식" or content=="아시안" or content=="랜덤":
                conData = ContextDTO(userId, tag, lifeSpan, content, 'N')
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
            else :
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
                    }
                }
        elif lifeSpan == 3:
            conData = ContextDTO(userId, tag, lifeSpan, content, 'N')
            contextData = dbCon.getContextData(conData)
            print(contextData)

    elif header == "김소영":
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
    return jsonify(dataSend)


@app.route('/restaurantTest', methods=['POST'])
def test():
    params = request.get_json()
    userId = params['userRequest']['user']['id']
    userId = userId.replace("\n", "")
    content = params['userRequest']['utterance']
    content = content.replace("\n", "")
    print(content)
    print(userId)

    if content == "아이디":
        print("if문아이디 content in")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": userId
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == '__main__':
    dbCon = DBConnection('P')
    dbCon.dbConnection()
    app.run(host='0.0.0.0', port=10002, debug=True)
