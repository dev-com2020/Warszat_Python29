import argparse
import configparser


def main(number, other_number):
    result = number * other_number
    print(f'Wynik wynosi: {result}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help="Liczba", default=1)
    parser.add_argument('-n2', type=int, help="Inna liczba", default=1)
    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='Plik konfiguracyjny')

    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])

    main(args.n1, args.n2)
