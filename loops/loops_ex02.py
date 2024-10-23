# Escreva um programa que solicite ao usuário que insira uma senha.
# Caso a senha esteja incorreta, exiba uma mensagem de erro e permita que o usuário insira novamente.
# O programa deve ser executado até que a senha correta seja inserida

def senha():
    inserir_senha = int(input('Insira a senha: '))
    senha_correta = 123
    while inserir_senha != senha_correta:
        print('Senha errada! Tente novamente.')
        inserir_senha = int(input('Insira a senha: '))
    else:
        print('Parabéns! Senha correta')


senha()