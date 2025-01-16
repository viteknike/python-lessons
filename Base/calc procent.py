def percent(kolvomes, summa, stavka):
    i = 0
    endsum = 0
    while i <= kolvomes:
        god = (endsum / 100) * (stavka / 12)
        endsum += god
        if i%12 == 0:
            print(endsum)
            print(i)
        endsum += summa
        i += 1

    print('Через', kolvomes, 'месяцев на счету будет', int(endsum), 'рублей')
    return endsum

percent(240, 2000, 16)