import random
import time
import string



def print_names(alphabet = string.ascii_letters, time_character = 0.003):
    name = input("digite algo: ")
    lista_original = ([*name])
    lista_shuffle = [*alphabet]
    random.shuffle(lista_shuffle)
    feito = ''

    for j in lista_original:

        if j != ' ':
            for i in lista_shuffle:

                print(feito + i)

                if i == j:
                    feito += j
                
                if feito == ''.join(lista_original):
                    break

                time.sleep(time_character)
        
        else:
            feito += ' '

if "__main__" == __name__:
    print_names()

