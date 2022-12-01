# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None

def divide(a: float, b: float):
    '''dzieli wartośc a przez b
    zgłasza wyjątek jeśli nie można przeprowadzić operacji
    '''

    try:
        wynik = a / b
    except Exception as e:
        print("nieprawidłowe dane:", e.args)
        return 0
    else:
        print('wynik operacji to %.1f' % wynik)
        return wynik


# x, y = 1, 0
# result = divide(x, y)
# if result is None:
#     print('Nieprawidłowe dane')

x, y = 4, 0
divide(x, y)
