from users import User, Privileges , Admin


#istanza classe User
persona:User=User("Valentina","Bologna","valeboloasr","vale@gmail.com")

#istanza 2 classe User per fare altra prova
persona2:User=User("Stefano","Martelloni","stevenhammer10","stefano@hotmail.it")

#istanza classe Privileges con lista Privilegi
lista_privilegi:Privileges=Privileges (["accesso diretto","visualizza file", "copia hard disk","Login by impronta digitale"])

#creazione di due istanze Admin
admin10=Admin(persona,lista_privilegi)

admin11=Admin(persona2,lista_privilegi)
#descrizione persona1
print(admin10.user.describe_user())
print("------------------------------------------")
print(admin10.user.greet_users())
print("------------------------------------------")
print(admin10.privileges.show_privileges())
print("------------------------------------------")

#descrizione persona2
print(admin11.user.describe_user())
print("------------------------------------------")
print(admin11.user.greet_users())
print("------------------------------------------")
print(admin11.privileges.show_privileges())
print("------------------------------------------")


