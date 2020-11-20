import requests

r = requests.get("http://127.0.0.1:8000/users", auth=('admin', 'contraseña'))

s = requests.get("http://127.0.0.1:8000/personas", auth=('admin', 'contraseña'))

print(r.text)
print(s.text)
