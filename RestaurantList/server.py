from flask import Flask, json, request, jsonify
from requestParsing import requestParsing
from recRestaurant import recRestaurant
from basement import basement
from addRestaurant import addRestaurant
from modRestaurant import modRestaurant
from evalRestaurant import evalRestaurant
from suggestion import suggestion
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.logDTO import logDTO
from DTO.requestDTO import RequestDTO
from MariaDB.DBCon import DBConnection

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask"


@app.route('/restaurant/recommend', methods=['POST'])
def recommend():
    params = request.get_json()
    parser = requestParsing()
    requestDto = parser.parsing(params)
    requestDto.tag="추천"

    logData = logDTO(requestDto.userId, requestDto.content, requestDto.tag)
    dbCon.insertLogData(logData)

    rec_menu = recRestaurant()
    dataSend = rec_menu.rec(requestDto, dbCon)

    return jsonify(dataSend)


@app.route('/restaurant', methods=['POST'])
def restaurant():
    params = request.get_json()
    parser = requestParsing()
    requestDto = parser.parsing(params)

    logData = logDTO(requestDto.userId, requestDto.content, requestDto.tag)
    dbCon.insertLogData(logData)

    if requestDto.tag=='추천':
        rec_menu = recRestaurant()
        dataSend = rec_menu.rec(requestDto, dbCon)
    elif requestDto.tag=='추가':
        add_res = addRestaurant()
        dataSend = add_res.add(requestDto, dbCon)
    elif requestDto.tag=='수정':
        mod_res = modRestaurant()
        dataSend = mod_res.delRes(requestDto, dbCon)
    elif requestDto.tag=='평가':
        eval_res = evalRestaurant()
        dataSend = eval_res.evalRes(requestDto, dbCon)
    elif requestDto.tag=='건의':
        sug_res = suggestion()
        dataSend = sug_res.sug(requestDto, dbCon)
    else:
        base_ment = basement()
        dataSend = base_ment.ment(requestDto)

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
