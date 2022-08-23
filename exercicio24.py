class Data:
    def __init__(self, d, m, a):
        self.d = d
        self.m = m
        self.a = a

mesDias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countAnoBissexto(d):

    anos = d.a

    if (d.m <= 2):
        anos -= 1
        
    return int(anos / 4) - int(anos / 100) + int(anos / 400)

def getDiferenca(dt1, dt2):
    n1 = dt1.a * 365 + dt1.d

    for i in range(0, dt1.m - 1):
        n1 += mesDias[i]

    n1 += countAnoBissexto(dt1)

    n2 = dt2.a * 365 + dt2.d

    for i in range(0, dt2.m - 1):
        n2 += mesDias[i]
        n2 += countAnoBissexto(dt2)
            
        return (n2 - n1)

dt1 = Data(1, 2, 2022)
dt2 = Data(22, 8, 2022)
print(getDiferenca(dt1, dt2), "dias")