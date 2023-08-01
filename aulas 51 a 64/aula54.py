import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i' or opcao == 'I':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        print('i')
    elif opcao == 'a' or opcao == 'A':
        indice_str = input('Qual indice deseja apagar?')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite números inteiros')
        except IndexError:
            print('Indice inválido')
        except Exception:
            print('Erro desconhecido')
        print(f'Indice "{valor}" apagado')

    elif opcao == 'l' or opcao == 'L':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Inválido!')
