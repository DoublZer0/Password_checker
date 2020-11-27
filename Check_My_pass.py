import requests
import hashlib


def get_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/'+query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError('something went wrong')
    return response


def check_api_data(pas):
    hashed_pass = sha1_hash(pas)
    init, tail = hashed_pass[:5], hashed_pass[5:]
    response = get_api_data(init)
    database = (lines.split(':')for lines in response.text.splitlines())
    for i, count in database:
        if i == tail:
            return count
    return 0


def sha1_hash(passwrod):
    hashed_password = hashlib.sha1(
        passwrod.encode('utf-8')).hexdigest().upper()
    return hashed_password


def main(array):
    for i in array:
        result = check_api_data(i)
        if result == 0:
            print(f'{result} breaches your password is safe and secure :)')
        else:
            print(
                f'{result} breaches your password is unsafe ... you might wanna change it :(')
    print('all done')


if __name__ == "__main__":
    pass_to_Check = []
    with open('E:\\Python\\Passsword_checker\\Write_password_you_want_to_check_here.txt', 'r') as file:
        pass_to_Check = file.read().splitlines()

    main(pass_to_Check)
