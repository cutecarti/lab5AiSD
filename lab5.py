import time
import matplotlib.pyplot as plt
#рекурсия
def recf(n):
    if n < 3:
        return 3
    elif n <= 25:
        return 5*recf(n-1)
    else:
        return 5*recf(n-1)-2*(n-2)

#итерация
def iterf(n):
    if n < 3:
        return 3
    else:
        prev = 3
        for i in range(3, n+1):
            if i <= 25:
                curr = 5*prev
            else:
                curr = 5*prev-2*(i-2)
            prev = curr
        return curr
n = 200
rectimes = []
recval = []
itertimes = []
iterval = []
nval = list(range(2, int(n) + 1))
for n in nval:
    start = time.time()
    recval.append(recf(n))
    end = time.time()
    rectimes.append(end - start)

    start = time.time()
    iterval.append(iterf(n))
    end = time.time()
    itertimes.append(end - start)
table_data = []
for i, n in enumerate(nval):
    table_data.append([n, rectimes[i], itertimes[i], recval[i], iterval[i]])
print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии', 'Значение итерации'))
print('-' * 104)
for data in table_data:
    print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format(data[0], data[1], data[2], data[3], data[4]))
plt.plot(nval, itertimes, label='Итерация')
plt.plot(nval, rectimes, label='Рекурсия')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.title('Сравнение рекурсивного и итерационного подхода')
plt.legend()
plt.show()
