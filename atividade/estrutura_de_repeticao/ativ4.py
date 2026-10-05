# ==========================================
# Exercício: Estrutura de repetição
# Arquivo: ativ4.py
# Objetivo: validar senha com até três tentativas.
# ==========================================

senha_correta = "admin123"

for tentativa in range(1, 4):
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta! Tente novamente.")

if senha != senha_correta:
    print("Você excedeu o número de tentativas.")
