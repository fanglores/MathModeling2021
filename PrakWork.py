import math
import matplotlib.pyplot as plt

# отрезок
a = 0
b = 150
# шаг
h = 5
#начальные независимые условия
k = 0
#начальные зависимые условия
v0 = 1000
alpha = (45)*math.pi/180
g_const = 9.81

# целевая функция для x
def fx(t, vx, vy):
    return (-k*math.sqrt(vx**2 + vy**2)*vx)

def gx(t, vx, vy):
    return vx

# целевая функция для y
def fy(t, vy, vx):
    return (-k*math.sqrt(vx**2 + vy**2)*vy - g_const)

def gy(t, vy, vx):
    return (vy - g_const)

t = []
x = []
y = []
vx = []
vy = []

# инициализируем значения в точке 0
t.append(float(0))
x.append(float(0))
y.append(float(0))
vx.append(float(v0*math.cos(alpha)))
vy.append(float(v0*math.sin(alpha)))

# Метод Рунге-Кутта
def RungeKutt_x():
    for i in range(int((b - a) // h) + 1):
        K1 = h * fx(t[i], vx[i], x[i])
        L1 = h * gx(t[i], vx[i], x[i])

        K2 = h * fx(t[i] + h / 2, vx[i] + K1 / 2, x[i] + L1 / 2)
        L2 = h * gx(t[i] + h / 2, vx[i] + K1 / 2, x[i] + L1 / 2)

        K3 = h * fx(t[i] + h / 2, vx[i] + K2 / 2, x[i] + L2 / 2)
        L3 = h * gx(t[i] + h / 2, vx[i] + K2 / 2, x[i] + L2 / 2)

        K4 = h * fx(t[i] + h, vx[i] + K3, x[i] + L3)
        L4 = h * gx(t[i] + h, vx[i] + K3, x[i] + L3)

        vx.append(vx[i] + (K1 + 2 * K2 + 2 * K3 + K4) / 6)
        x.append(x[i] + (L1 + 2 * L2 + 2 * L3 + L4) / 6)

def RungeKutt_y():
    for i in range(int((b - a) // h) + 1):
        K1 = h * fy(t[i], vy[i], y[i])
        L1 = h * gy(t[i], vy[i], y[i])

        K2 = h * fy(t[i] + h / 2, vy[i] + K1 / 2, y[i] + L1 / 2)
        L2 = h * gy(t[i] + h / 2, vy[i] + K1 / 2, y[i] + L1 / 2)

        K3 = h * fy(t[i] + h / 2, vy[i] + K2 / 2, y[i] + L2 / 2)
        L3 = h * gy(t[i] + h / 2, vy[i] + K2 / 2, y[i] + L2 / 2)

        K4 = h * fy(t[i] + h, vy[i] + K3, y[i] + L3)
        L4 = h * gy(t[i] + h, vy[i] + K3, y[i] + L3)

        vy.append(vy[i] + (K1 + 2 * K2 + 2 * K3 + K4) / 6)
        y.append(y[i] + (L1 + 2 * L2 + 2 * L3 + L4) / 6)


for i in range(1, int((b - a) // h) + 1):
    t.append(i * h)

RungeKutt_x()
RungeKutt_y()

x.pop()
y.pop()
vx.pop()
vy.pop()

#print
#print(t)
#print(vy)

# Вывод графика
plt.figure("Mathematical modeling")
plt.title("Modelling by Runge-Kutta method")
plt.grid(True)
plt.plot(t, vx, 'g', label='vx', linewidth=2)
#plt.plot(t, x, 'b', label='x', linewidth=2)
plt.plot(t, vy, 'y', label='vy', linewidth=2)
#plt.plot(t, y, 'r', label='y', linewidth=2)
plt.legend(loc = 'lower right')

plt.show()
