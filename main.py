import math
import matplotlib.pyplot as plt

# отрезок
a = 0
b = 1
# шаг
h = 0.05


# целевая функция
def f(x, y):
    return (x * math.exp(-(x ** 2)) - 2 * x * y)


E_y = []
RK_y = []
x = []

# инициализируем значения в точке 0
E_y.append(float(1))
RK_y.append(float(1))


# метод Эйлера
def Eiler():
    for i in range(int(1 // h)):
        E_y.append(E_y[i] + h * f(i * h, E_y[i]))


# Метод Рунге-Кутта
def RungeKutt():
    for i in range(int(1 // h)):
        K1 = h * f(x[i], RK_y[i])
        K2 = h * f(x[i] + h / 2, RK_y[i] + K1 / 2)
        K3 = h * f(x[i] + h / 2, RK_y[i] + K2 / 2)
        K4 = h * f(x[i] + h, RK_y[i] + K3)
        RK_y.append(RK_y[i] + (K1 + 2 * K2 + 2 * K3 + K4) / 6)

for i in range(int(1 // h)):
    x.append(i * h)

Eiler()
RungeKutt()

E_y.pop(0)
RK_y.pop(0)
print(x)
print(E_y)
print(RK_y)

# Вывод графика
plt.figure("Mathematical modeling")
plt.title("Eiler and Runge-Kutt methods")
plt.grid(True)
plt.plot(x, E_y, 'b', label = 'Eiler')
plt.plot(x, RK_y, 'r', label = 'Runge-Kutt')
plt.legend(loc = 'lower right')

plt.show()

# print (fig.axes)
# print (len(y))

