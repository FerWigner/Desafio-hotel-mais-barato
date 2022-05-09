import re
from calendar import week


print('Desafio do hotel mais barato - Syngenta - 09/05/2022')
print('Desafiada: Fernanda Wigner')
print('*****************************************************')

# Lista de dicionários dos três hotéis
hotels = [{'nome': 'Lakewood', 'classification': 3, 'weekPrice': 110,
          'weekendPrice': 90, 'weekPriceRew': 80, 'weekendPriceRew': 80},

          {'nome': 'Bridgewood', 'classification': 4, 'weekPrice': 160,
           'weekendPrice': 60, 'weekPriceRew': 110, 'weekendPriceRew': 50},

          {'nome': 'Ridgewood', 'classification': 5, 'weekPrice': 220,
           'weekendPrice': 150, 'weekPriceRew': 100, 'weekendPriceRew': 40}]


# Método(função) que retorna o hotel mais barato se empate com maior classificação.
def get_cheapest_hotel(hotel_list, index, classification):
    best_hotel = None

    for hotel in hotel_list:
        if not best_hotel:
            best_hotel = hotel

        if hotel[index] < best_hotel[index]:
            best_hotel = hotel

        if hotel[index] == best_hotel[index]:
            if hotel[classification] > best_hotel[classification]:
                best_hotel = hotel
    return best_hotel


# loop de confirmação básica das entradas do usuário.
while True:
    print('Insira o tipo do cliente; se "Regular ou Reward" e tres datas no formato ddMMMyyyy(Dddd) separadas por vírgula.')
    print('(Exemplo: Regular:16Mar2009(Mon),17Mar2009(Tues),18Mar2009(Wed))')
    try:
        user_input = input('Insira aqui:')
        if user_input != 'Regular' or user_input != 'Reward':
            user_input = user_input.split(':')
            user_type = user_input[0]
            print('Tipo de Cliente:', user_type)
            chosen_dates = user_input[1].split(',')
            print('Datas escolhidas:', chosen_dates)

    except:
        print('Formato inválido! Insira o tipo do cliente; se "Regular ou Reward" e tres datas no formato ddMMMyyyy(dddd) separadas por vírgula.')
        print('(Exemplo: Regular:16Mar2009(Mon),17Mar2009(Tues),27Mar2022(Sun))')

    else:
        # Pacote re.

        for day in chosen_dates:
            # if re.search('(Sat)|(Sun)', day):
            result = re.search('(sat)', '(sun)')
            if result == '(sat)' or '(sun)':
                if 'Regular' in user_type:
                    best_hotel = get_cheapest_hotel(
                        hotels, 'weekendPrice', 'classification')
                if 'Rewards' in user_type:
                    best_hotel = get_cheapest_hotel(
                        hotels, 'weekendPriceRew', 'classification')
                    print('O melhor hotel é {}:'.format(best_hotel))
            else:
                result = re.search('(mon)', '(tues)', '(wed)', '(thu)')
                if result != '(sat)' or '(sun)':
                    if 'Regular' in user_type:
                        best_hotel = get_cheapest_hotel(
                            hotels, 'weekPrice', 'classification')
                    if 'Rewards' in user_type:
                        best_hotel = get_cheapest_hotel(
                            hotels, 'weekPriceRew', 'classification')
                    print('O melhor hotel é {}:'.format(best_hotel))

    break
