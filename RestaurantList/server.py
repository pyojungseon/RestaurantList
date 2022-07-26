from flask import Flask, json, request, jsonify
from requestParsing import requestParsing
from recommend import recommend
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.LogDTO import LogDTO
from DTO.ContextDTO import ContextDTO
from DTO.requestDTO import RequestDTO
from MariaDB.DBCon import DBConnection

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask"


@app.route('/restaurant', methods=['POST'])
def restaurant():
    params = request.get_json()
    requestDto = requestParsing(params)

    logData = LogDTO(requestDto.userId, requestDto.content, requestDto.tag)
    dbCon.insertLogData(logData)

    rec_menu = recommend(requestDto)
    dataSend=rec_menu.rec()

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
