from requests import get, post, put


# def make_request_get():
#     get('http://localhost:5000/todo1').json()

def make_request_post(data):
    res = post('http://localhost:5000/emails', data=data).json()
    return res

# def make_request_put():
#     put('http://localhost:5000/todo1', data={'data': 'Change my brakepads'}).json()

if __name__ == "__main__":
    data = {'name': 'Alan chen',
            'email;': "541203951@163.com",
            'intro': 'heart of a hero',}
    make_request_post(data)