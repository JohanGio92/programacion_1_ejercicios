

def rebotar(height, times):
    for time in range(1, times + 1):
        new_height = height * (3/5) ** time
        print(round(new_height, 2))


def main(parameters):
    height = float(parameters[1])
    times = int(parameters[2])
    if len(parameters) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' ' necesitas pasar los argumentos height y times')
    rebotar(height, times)


if __name__ == '__main__':
    import sys
    main(sys.argv)
