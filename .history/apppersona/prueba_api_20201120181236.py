import requests

r = requests.get("http://http://127.0.0.1:8000/users", auth=('admin', 'contraseña'))

print(r.text)
