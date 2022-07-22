from flask import Flask, json, request, jsonify
import sys
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
    print(content)
    print(userId)

    logData = LogDTO(userId, content, tag)
    dbCon.insertLogData(self, logData)

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

    elif content == "김소영":
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
                            "text": "error 입니다"
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
