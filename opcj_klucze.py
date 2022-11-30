def reminder(number, divisor):
    return number % divisor


assert reminder(20, 7) == 6

my_kwargs = {
    'number': 20,

}

other_kwarg = {
    'divisor': 7,
}

assert reminder(**my_kwargs, **other_kwarg) == 6


def print_param(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}={v}')



print_param(alpha=1, beta=0.8, gamma=2.6)
