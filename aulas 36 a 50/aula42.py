# Utilizamos o While quando não sabemos quantas vezes a repetição será executada...

# Qyuando sabemos utilizamos o For


                #Exemplo de cod while

# senha_salva = '12345'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes})x: ')

#     repeticoes += 1

# print(f'Após {repeticoes} tentativas, você acertou a senha, bem-vindo de volta')
# print('Aquele laço acima pode ter repetições infinitas')

texto = 'Python'

for caracteres in texto:
    print(caracteres)