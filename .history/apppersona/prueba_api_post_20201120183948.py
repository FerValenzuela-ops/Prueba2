import requests
#crear a un usuario
posttest = {'username': 'posttest','first_name' : 'posttest', 'last_name' : 'posttest', 'email' : 'posttest@gmail.com'}

r = requests.post("http://127.0.0.1:8000/users/", auth=('admin', 'contraseña'), data= posttest)
print(r)
print(r.text)


#crear a una persona
personitanueva = {'username': 'posttest','first_name' : 'posttest', 'last_name' : 'posttest', 'email' : 'posttest@gmail.com'}

r = requests.post("http://127.0.0.1:8000/users/", auth=('admin', 'contraseña'), data= personitanueva)
"http://127.0.0.1:8000/users/42/"


print(r)
print(r.text)
