print('_Умножение и сложение матриц_')
mh1 = int(input('Введите высоту первой матрицы\n'))     #Создание первой матрицы
ml1 = int(input('Введите длину первой матрицы\n'))
a = []
q = mh1
while q > 0:
    a.append([])
    q = q - 1



mh2 = int(input('Введите высоту второй матрицы\n'))     #Создание второй матрицы
ml2 = int(input('Введите длину второй матрицы\n'))
b = []
q = mh2
while q > 0:
    b.append([])
    q = q - 1



w = mh1                                                #Ввод эллементов первой матрицы
h1 = 1
while w > 0:
    n1 = 1
    g = ml1
    while g > 0:
        x1 = int(input('Введите эллемент № %d из строки № %d\n' %(n1, h1)))
        a[h1 - 1].insert(n1 - 1, x1)
        n1 = n1 + 1
        g = g - 1
    w = w - 1
    h1 = h1 + 1
for i in range(mh1):
    print(a[i - 1])



w = mh2                                                #Ввод эллементов второй матрицы
h1 = 1
while w > 0:
    n1 = 1
    g = ml2
    while g > 0:
        x1 = int(input('Введите эллемент № %d из строки № %d\n' %(n1, h1)))
        b[h1 - 1].insert(n1 - 1, x1)
        n1 = n1 + 1
        g = g - 1
    w = w - 1
    h1 = h1 + 1



for i in range(mh2):
    print(b[i - 1])

l = input('Умножить(mult) или сложить(summ)\n')

if l == 'mult':
    if ml1 != mh2:                                         #Выходит из программы, если матрицы нельзя перемножать
        print('Такие матрицы нельзя умножать друг на друга')
        input()
        exit()



    c = []                                                      #Создание матрицы для результатов
    q = mh1
    while q > 0:
        c.append([])
        q = q - 1



    print('Идет подсчет........')                              #Рофл



    h = mh1                                                     #Подсчет и выведение результата умножения
    h1 = 0
    while h > 0:
        g = ml2
        g1 = 0
        while g > 0:
            f = ml1
            f1 = 0
            y1 = 0
            while f > 0:
                y = a[g1][f1] * b[f1][g1]
                y1 += y
                f -= 1
                f1 += 1
            c[h1].insert(g1, y1)
            g -= 1
            g1 += 1
        h -= 1
        h1 += 1
    print('Результат умножения:')
    for i in range(mh1):
        print(c[i - 1])
    input()



if l == 'summ':
    if mh1 != mh2:
        print('Нельзя складывать такие матрицы')               #Прверочка
        input()
        exit()
    if ml1 != ml2:
        print('Нельзя складывать такие матрицы')
        input()
        exit()

    c = []                                                      #Создание матрицы для результатов
    q = mh1
    while q > 0:
        c.append([])
        q = q - 1


    print('Идет подсчет........')                              #Рофл


    h = mh1
    h1 = 0
    while h > 0:
        g = ml1
        g1 = 0
        while g > 0:
            c[h1].insert(g1, a[h1][g1] + b [h1][g1])
            g -= 1
            g1 += 1
        h -= 1
        h1 += 1
    for i in range(mh1):
        print(c[i - 1])
    input()
