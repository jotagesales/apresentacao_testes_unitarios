# -*- coding: utf-8 -*-
'''
Created by Jotagê Sales on 18/08/15.
'''

VOGAIS = ['a', 'e', 'i', 'o', 'u']

def conta_vogais_consoantes(text=''):
    count_vogal= 0
    count_consoante= 0

    for letra in text:
        # deixando minusculo e removendo os espaços
        letra = letra.lower().strip()

        if letra:
            if letra in VOGAIS:
                count_vogal += 1
            else:
                count_consoante += 1
    return count_vogal, count_consoante