# exercicio do imposto de renda ;)

x = float(input())

if x <= 2000.00:
    print('Insento')
if x > 2000.00 and x <= 3000.00:
    print('R$ {:.2f}' .format((x-2000) * 0.08))
if x > 3000.00 and x <=  4500.00:
    s = x - 2000
    s2 = s
    s = 1000 * 0.08
    if s2 > 1000:
        s2 = s2 - 1000
        s2 = s2 * 0.18
        print('R$ {:.2f}' .format(80 + s2))
        # s = 0
        # s2 = 0
    else:
        print('R$ {:.2f}' .format(s))
        s = 0
        s2 = 0
if x > 4500.00:

    # s = 1000 * 0.08
    # s2 = 1500 * 0.18
    s3 = x - 4500.00
    s3 = s3 * 0.28
    print('R$ {:.2f}' .format(80 + 270 + s3))
