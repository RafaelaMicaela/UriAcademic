def input_to_minutes(value):
    h, m = (int(v) for v in value.split(":"))
    return h * 60 + m

if (__name__ == '__main__'):
    values = [input_to_minutes(v) for v in input().split()]
    minutes_a_to_b = values[1] - values[0]
    minutes_b_to_a = values[3] - values[2]

    duracao = (minutes_a_to_b + minutes_b_to_a) / 2
    variacao = (minutes_a_to_b - duracao) / 60

    if (duracao < 0):
        minutes_a_to_b += 24 * 60

    duracao = (minutes_a_to_b + minutes_b_to_a) / 2
    variacao = (minutes_a_to_b - duracao) / 60

    if (variacao > 12):
        variacao = (variacao - 12) + (- 12)
    elif (variacao < -12):
        variacao = ((variacao *(-1)) - 12 + (- 12))

    print(int(duracao), int(variacao))