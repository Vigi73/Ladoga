while True:
    width_f = float(input(':'))
    if width_f < 1000 and width_f == int(width_f):
        pass
    else:
        width_f *= 1000
    print(width_f)