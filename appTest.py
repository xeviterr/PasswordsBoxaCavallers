#Test exemple
from app import validaPassword

passwordCorrecte, msg = validaPassword("patata")
assert (passwordCorrecte==False)
passwordCorrecte, msg = validaPassword("patata@N04ad34234")
#aquest hauria de funcionar.
assert (passwordCorrecte==True)

