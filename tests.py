# -*- coding: utf-8 -*-
'''
Created by Jotagê Sales on 18/08/15.
'''

import unittest
from vogais import conta_vogais_consoantes

class TestVogais(unittest.TestCase):

    def test_conta_vogais(self):
        qtde_vogais, qtde_consoantes = conta_vogais_consoantes('Python')

        self.assertEqual(qtde_vogais, 1)
        self.assertEqual(qtde_consoantes, 5)

    def test_conta_vogais_espaco(self):
        qtde_vogais, qtde_consoantes = conta_vogais_consoantes('Jotage Sales')

        self.assertEqual(qtde_vogais, 5)
        self.assertEqual(qtde_consoantes, 6)

unittest.main()