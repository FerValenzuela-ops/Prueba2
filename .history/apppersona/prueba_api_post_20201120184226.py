import requests
#crear a un usuario
"""
posttest = {'username': 'posttest','first_name' : 'posttest', 'last_name' : 'posttest', 'email' : 'posttest@gmail.com'}

r = requests.post("http://127.0.0.1:8000/users/", auth=('admin', 'contraseña'), data= posttest)
print(r)
print(r.text)
"""

#crear a una persona
personitanueva = {  
    "username": "posttest",
    "nombre": "personitanueva",
    "apellido": "personitanueva",
    "email": "personitanueva@gmail.com",
    "celular": 233123123,
    "rut": "32.231.231-2",
    "region": "quinta",
    "edad": 24}

z = requests.post("http://127.0.0.1:8000/users/", auth=('admin', 'contraseña'), data= personitanueva)



print(z)
print(z.text)
