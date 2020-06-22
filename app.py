def validaPassword(password:str)->(bool, str):
    if (len(password)<10):
        return False, "Password incorrecte, ha de tenir 8 caràcters..."
    
    nLletresMaj=0
    nLletresMin=0
    nDigitsNumerics=0
    nSymbols=0
    pos =0
    for lletra in password:
        cod = ord(lletra)
        if lletra in '0123456789':
            nDigitsNumerics+=1
        elif cod >= 65 and cod <= 90:
            nLletresMin+=1
        elif cod >= 97 and cod <= 122:
            nLletresMaj+=1
        else:
            if pos>0 and pos<len(password):
                nSymbols+=1
        pos+=1

    if nDigitsNumerics<2:
        return False, "Ens calen 2 dígits numèrics almenys."
    
    if nLletresMaj==0 or nLletresMin==0:
        return False, "Cal una lletra majúscula i una minúscula"

    if nSymbols==0:
        return False, "Cal un símbol que no pot estar ni al principi ni al final."

    return True, ""

passwordCorrecte=False
while(not passwordCorrecte):
    passwordCorrecte, msg = validaPassword(input("Entra un password:"))
    if not passwordCorrecte:
        print (msg)
    