import requests
#crear a un usuario


r = requests.delete("http://127.0.0.1:8000/users/42/", auth=('admin', 'contraseña'))
print(r)
print(r.text)