import requests


# check available class in 2018/12
def check_reservation():
    url = 'https://www.digital-blacksmithshop.com:46115/program/calendar/1?y=2018&m=12'
    resp = requests.get(url)

    num_of_available = resp.text.count('모집중')
    try:
        if num_of_available == 0:
            pass
        else:
            num_of_available = num_of_available / 2
    except Exception as e:
        print(e)

    return num_of_available


if __name__ == "__main__":
    available_num = check_reservation()
    print("가능한 예약 수 :", int(available_num))
