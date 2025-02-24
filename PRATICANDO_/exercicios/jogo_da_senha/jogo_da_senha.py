from exercicios.utils import message, pause_clear
from exercicios.jogo_da_senha.funcs_principais_js import *

#Inicializa o jogo:
if __name__ == "__main__" :
    message("JOGO DA SENHA: ADIVINHE A SENHA", ["Tam. da senha: 4 a 8 dígitos", "Adivinhe os dígitos da senha"])
    pause_clear()
    jogo_da_senha()