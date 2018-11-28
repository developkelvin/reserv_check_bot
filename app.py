from flask import Flask, jsonify, request

from reservation_checker import check_reservation

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/keyboard')
def keyboard():
    ret_data = {
        "type": "buttons",
        "buttons": ["잔여 강의 수 조회", "잔여 강의 상세 조회", "???"]
    }

    return jsonify(ret_data)


@app.route('/message', methods=['POST'])
def message():
    data_receive = request.get_json()
    content = data_receive['content']
    if content == '잔여 강의 수 조회':
        num_of_reservation = check_reservation()

        data_send = {
            "message": {
                'text': '현재 예약 가능 수는 ' + str(num_of_reservation) + '개 입니다.'
            },
            'keyboard': {
                "type": "buttons",
                "buttons": ["잔여 강의 수 조회", "잔여 강의 상세 조회", "???"]
            }
        }

    elif content == "잔여 강의 상세 조회":
        data_send = {
            "message": {
                'text': '준비중입니다.'
            },
            'keyboard': {
                "type": "buttons",
                "buttons": ["잔여 강의 수 조회", "잔여 강의 상세 조회", "???"]
            }
        }
    elif content == "???":
        data_send = {
            "message": {
                'text': 'Made by Yoonsik Jung'
            },
            'keyboard': {
                "type": "buttons",
                "buttons": ["잔여 강의 수 조회", "잔여 강의 상세 조회", "???"]
            }
        }


if __name__ == '__main__':
    app.run()
