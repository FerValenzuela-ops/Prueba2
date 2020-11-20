import requests
#traer a todos los usuarios
r = requests.get("http://127.0.0.1:8000/users", auth=('admin', 'contraseña'))
#traer a todas las personas
s = requests.get("http://127.0.0.1:8000/personas", auth=('admin', 'contraseña'))
#usuario especifico
z = requests.get("http://127.0.0.1:8000/users/6", auth=('admin', 'contraseña'))
#persona especifico
p = requests.get("http://127.0.0.1:8000/personas/10", auth=('admin', 'contraseña'))

print(r.text)
print(s.text)
print(z.text)
print(p.text)
