import requests
#traer a todos los usuarios
posttest = {'username': 'posttest', 'email' : 'posttest@gmail.com'}

r = requests.post("http://127.0.0.1:8000/users", auth=('admin', 'contraseña'), data= posttest)
print(r)
print(r.text)