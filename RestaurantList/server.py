from flask import Flask, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask"

@app.route('/innerteam', methods=['POST'])
def innerteam():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10002, debug=True)
