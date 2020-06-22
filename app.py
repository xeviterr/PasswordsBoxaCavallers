def hihaLletres(password:str)->bool:
    #Partim de la base que no posaràs mai un accent en un password ;)
    for lletra in password:
        cod = ord(lletra)
        if cod >= 97 and cod <= 122:
            return True
        if cod >= 65 and cod <= 90:
            return True
    return False

def hihaNumero(password:str)->bool:
    for lletra in password:
        if lletra in '0123456789':
            return True
    return False

def validaPassword(password:str)->(bool, str):
    if (len(password)<8):
        return False, "Password incorrecte, ha de tenir 8 caràcters..."
    
    if not hihaLletres(password):
        return False, "No he trobat cap lletra (lletres amb accents no les considero lletres)"

    if not hihaNumero(password):
        return False, "No he trobat cap número"

    return True, ""

passwordCorrecte=False
while(not passwordCorrecte):
    passwordCorrecte, msg = validaPassword(input("Entra un password:"))
    if not passwordCorrecte:
        print (msg)
    