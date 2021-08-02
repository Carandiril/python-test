import Nauka.zadanie_sklep.package.magazyn as store


ORDER_LIST = []


def is_product_in_shop(product_name):
    for product in store.products:
        if product_name == product['name']:
            return product

    print('Nie ma takiego produktu')
    return False


def create_order(product, quantity):
    sum_order = 0
    ORDER_LIST.append({
        'name': product['name'],
        'quantity': quantity,
        'total_price': product["price"] * quantity
    })
    print(ORDER_LIST)

    print('-' * 30)
    print('Oto Twoje zamówienie:')

    for ordered_product in ORDER_LIST:
        print(ordered_product['name'])
        print(f'Liczba sztuk: {ordered_product["quantity"]}')
        print(f'Cena wynosi: {ordered_product["total_price"]} zł')
        print()
        sum_order += ordered_product["total_price"]
    print(f'Cały paragon to {sum_order} zł')
    print('-' * 30)
