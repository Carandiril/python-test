from Nauka.zadanie_sklep.package import zamowienie


def start():
    continue_shopping = None

    while continue_shopping != 'X':
        product = input('Podaj nazwe produktu: ')
        quantity = int(input('Podaj ilość: '))

        ordered_product = zamowienie.is_product_in_shop(product)
        if ordered_product:
            zamowienie.create_order(ordered_product, quantity)

        continue_shopping = input('Jeżeli chcesz kontunuować zakupy wpisz dowolny znak, aby przerwać wpisz "X": ')


if __name__ == '__main__':
    start()
