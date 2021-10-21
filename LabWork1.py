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

#расчитаная функция (решение ур-я)
def true_f(x):
    return 0.5*(math.exp(-(x ** 2))*(x ** 2 + 2))

E_y = []
RK_y = []
x = []
y = []

# инициализируем значения в точке 0
x.append(float(0))
y.append(true_f(x[0]))
E_y.append(float(1))
RK_y.append(float(1))

# метод Эйлера
def Eiler():
    for i in range(int(1 // h) + 1):
        E_y.append(E_y[i] + h * f(i * h, E_y[i]))


# Метод Рунге-Кутта
def RungeKutt():
    for i in range(int(1 // h) + 1):
        K1 = h * f(x[i], RK_y[i])
        K2 = h * f(x[i] + h / 2, RK_y[i] + K1 / 2)
        K3 = h * f(x[i] + h / 2, RK_y[i] + K2 / 2)
        K4 = h * f(x[i] + h, RK_y[i] + K3)
        RK_y.append(RK_y[i] + (K1 + 2 * K2 + 2 * K3 + K4) / 6)

for i in range(1, int(1 // h) + 2):
    x.append(i * h)
    y.append(true_f(x[i]))

Eiler()
RungeKutt()

print(x)
print(E_y)
print(RK_y)

#расчет и вывод погрешностей в точке b (задание б и в)
print("\nEiler error is E = |Yпр - Y| = |", abs(E_y[-1] - true_f(b)))
print("Runge-Kutta error is E = |Yпр - Y| = |", abs(RK_y[-1] - true_f(b)))

# Вывод графика (задание г)
plt.figure("Mathematical modeling")
plt.title("Eiler and Runge-Kutt methods")
plt.grid(True)
plt.plot(x, y, 'g', label='True function', linewidth=3)
plt.plot(x, E_y, 'b', label='Eiler', linewidth=2, linestyle='--')
plt.plot(x, RK_y, 'r', label='Runge-Kutt', linewidth=2, linestyle='--')
plt.legend(loc = 'lower right')

plt.show()
