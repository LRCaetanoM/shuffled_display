import random
import time
import string



def print_names(name, alphabet = string.ascii_letters, time_character = 0.01):
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



print_names('write the sentence here')