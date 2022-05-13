from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))


import re
from calendar import week


print('Desafio do hotel mais barato - Syngenta - 13/05/2022')
print('Desafiada: Fernanda Wigner')
print('*****************************************************')

# Lista de dicionários dos três hotéis
l = {'name': 'Lakewood', 'classification': 3, 'weekPrice': 110,
     'weekendPrice': 90, 'weekPriceRew': 80, 'weekendPriceRew': 80}

b = {'name': 'Bridgewood', 'classification': 4, 'weekPrice': 160,
     'weekendPrice': 60, 'weekPriceRew': 110, 'weekendPriceRew': 50}

r = {'name': 'Ridgewood', 'classification': 5, 'weekPrice': 220,
     'weekendPrice': 150, 'weekPriceRew': 100, 'weekendPriceRew': 40}


# Método(função) que retorna o hotel mais barato se empate com maior classificação.
def get_cheapest_hotel(x, y, z, nL, nB, nR):

    if z > x < y:
        print('O melhor hotel é o ' + str(nL))
    elif y < z:
        print('O Melhor hotel é o ' + str(nB))
    else:
        print('O melhor hotel é o ' + str(nR))


# loop de confirmação básica das entradas do usuário.
while True:

    try:
        print('Insira o tipo do cliente; se "Regular ou Reward" e tres datas no formato ddMMMyyyy(ddd) separadas por vírgula.')
        print('(Exemplo: Regular:16Mar2009(mon),17Mar2009(tues),18Mar2009(wed))')
        user_input = input('Insira aqui:')
        user_input = user_input.split(':')
        user_type = user_input[0]
        print('Tipo de Cliente:', user_type)
        chosen_dates = user_input[1].split(',')
        print('Datas escolhidas:', chosen_dates)

        if (re.search(r'sat', str(chosen_dates))) or (re.search(r'sun', str(chosen_dates))):

            if 'Regular' in str(user_type):
                x = l.get('weekendPrice')  # 90
                y = b.get('weekendPrice')  # 60
                z = r.get('weekendPrice')  # 150
                nL = l.get('name')
                nB = b.get('name')
                nR = r.get('name')

                get_cheapest_hotel(x, y, z, nL, nB, nR)

            if 'Rewards' in str(user_type):
                x = l.get('weekendPriceRew')  # 80
                y = b.get('weekendPriceRew')  # 50
                z = r.get('weekendPriceRew')  # 40
                nL = l.get('name')
                nB = b.get('name')
                nR = r.get('name')

                get_cheapest_hotel(x, y, z, nL, nB, nR)
        else:

            if 'Regular' in str(user_type):
                x = l.get('weekPrice')  # 110
                y = b.get('weekPrice')  # 160
                z = r.get('weekPrice')  # 220
                nL = l.get('name')
                nB = b.get('name')
                nR = r.get('name')

                get_cheapest_hotel(x, y, z, nL, nB, nR)

            if 'Rewards' in str(user_type):
                x = l.get('weekPriceRew')  # 80
                y = b.get('weekPriceRew')  # 110
                z = r.get('weekPriceRew')  # 100
                nL = l.get('name')
                nB = b.get('name')
                nR = r.get('name')

                get_cheapest_hotel(x, y, z, nL, nB, nR)
    except:
        print('FORMATO INVÁLIDO! Insira os dados como no exemplo: Regular:16Mar2009(Mon),17Mar2009(Tues),27Mar2022(Sun).')
        print('Por favor, execute o programa novamente.')

    break





