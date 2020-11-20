import requests
#crear a un usuario


r = requests.put("http://127.0.0.1:8000/users/42/", auth=('admin', 'contraseña'))
print(r)
print(r.text)