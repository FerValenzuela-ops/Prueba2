import requests
#crear a un usuario

posttest = {'username': 'posttest','first_name' : 'posttest', 'last_name' : 'posttest', 'email' : 'PUTposttest@gmail.com'}

r = requests.put("http://127.0.0.1:8000/users/", auth=('admin', 'contraseña'), data= posttest)
print(r)
print(r.text)