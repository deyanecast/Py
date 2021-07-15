# -*- coding:utf-8 -*-

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.replace('á', 'a')
    palabra = palabra.replace('é', 'e')
    palabra = palabra.replace('í', 'i')
    palabra = palabra.replace('ó', 'o')
    palabra = palabra.replace('ú', 'u')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else: 
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else: 
        print('no es palindromo')


if __name__ == '__main__':
    run()