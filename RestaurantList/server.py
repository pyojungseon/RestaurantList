from flask import Flask, json, request, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.LogDTO import LogDTO
from MariaDB.DBCon import DBConnection

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask"

@app.route('/restaurant', methods=['POST'])
def restaurant():
    params = request.get_json()
    userId = params['userRequest']['user']['id']
    userId = userId.replace("\n", "")
    content = params['userRequest']['utterance']
    content = content.replace("\n", "")
    tag = "/"
    header = content.split(" ")[0]
    if content[0] == '/':
        tag=header

    print(content)
    print(userId)

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
                            "text": '''BOK본관 부근 음식점 추천 챗봇입니다.\n
                            다음의 순서로 입력해주세요\n
                            추천 종류[한식/일식/중식/양식] 금액대(만원)[N]\n 
                            ex)추천 일식 5'''
                        }
                    }
                ]
            }
        }
    elif header == "추천":
        print("추천 content in")
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": '''추천테스트. DB만드느중'''
                        }
                    }
                ]
            }
        }

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
                            "text": "수행할 수 없는 명령문입니다"
                        }
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
