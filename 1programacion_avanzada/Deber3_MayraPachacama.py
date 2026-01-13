import re

def validarPwd(password):
    patron='^[a-zA-Z\-\_0-9]{6,}$'
    res=re.search(patron,password)
    return bool(res)


password=input('ingrese la contraseña: ')
pwdValida=validarPwd(password)
print (f'La contraseña: {password} { ' es' if pwdValida else ' no es'} valida')