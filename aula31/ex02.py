"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#------------------MINHA SOLUÇÃO-------------------

hora = input('Que horas são? ')

if hora.isdigit() == True:
    hora_float = float(hora)
    if hora_float <= 12 and hora_float > 4:
        print('Bom dia!')
    elif hora_float <= 18:
        print('Boa tarde!')
    elif hora_float >= 19:
        print('Boa noite!')
    elif hora_float <= 4 and hora_float > 0:
        print('Está de madrugada')
else:
    print('Não é um número')

#---------------CORREÇÃO-------------