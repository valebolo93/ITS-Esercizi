from users import User
from users import Privileges
from users import Admin

persona:User=User("Valentina","Bologna","vale@gmail.com")
print(persona)

capo:Privileges=Privileges("Login by impronta digitale")
print(capo)

admin10=Admin(persona,capo)
admin10.