import math
import matplotlib.pyplot as plt
import decimal

decimal.getcontext().prec = 20

# отрезок
a = 0
b = 150
# шаг
h = 5
#начальные независимые условия
k = 0.000589507

#начальные зависимые условия
v0 = 1000
alpha = (45)*math.pi/180
g_const = 9.81

# целевая функция для x
def fx(t, vx, vy):
    print(-k*math.sqrt(vx**2 + vy**2)*vx)
    return (-k*math.sqrt(vx**2 + vy**2)*vx)

def gx(t, vx, vy):
    return vx

# целевая функция для y
def fy(t, vx, vy):
    return (-k*math.sqrt(vx**2 + vy**2)*vy - g_const)

def gy(t, vx, vy):
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
def RungeKutta():
    for i in range(int((b - a) // h) + 1):
        K1x = h * fx(t[i], vx[i], vy[i])
        L1x = h * gx(t[i], vx[i], vy[i])
        K1y = h * fy(t[i], vx[i], vy[i])
        L1y = h * gy(t[i], vx[i], vy[i])

        K2x = h * fx(t[i] + h / 2, vx[i] + K1x / 2, vy[i] + L1x / 2)
        L2x = h * gx(t[i] + h / 2, vx[i] + K1x / 2, vy[i] + L1x / 2)
        K2y = h * fy(t[i] + h / 2, vx[i] + K1y / 2, vy[i] + L1y / 2)
        L2y = h * gy(t[i] + h / 2, vx[i] + K1y / 2, vy[i] + L1y / 2)

        K3x = h * fx(t[i] + h / 2, vx[i] + K2x / 2, vy[i] + L2x / 2)
        L3x = h * gx(t[i] + h / 2, vx[i] + K2x / 2, vy[i] + L2x / 2)
        K3y = h * fy(t[i] + h / 2, vx[i] + K2y / 2, vy[i] + L2y / 2)
        L3y = h * gy(t[i] + h / 2, vx[i] + K2y / 2, vy[i] + L2y / 2)

        K4x = h * fx(t[i] + h, vx[i] + K3x, vy[i] + L3x)
        L4x = h * gx(t[i] + h, vx[i] + K3x, vy[i] + L3x)
        K4y = h * fy(t[i] + h, vx[i] + K3y, vy[i] + L3y)
        L4y = h * gy(t[i] + h, vx[i] + K3y, vy[i] + L3y)

        x.append(x[i] + (L1x + 2 * L2x + 2 * L3x + L4x) / 6)
        y.append(y[i] + (L1y + 2 * L2y + 2 * L3y + L4y) / 6)
        vx.append(vx[i] + (K1x + 2 * K2x + 2 * K3x + K4x) / 6)
        vy.append(vy[i] + (K1y + 2 * K2y + 2 * K3y + K4y) / 6)


for i in range(1, int((b - a) // h) + 1):
    t.append(i * h)

RungeKutta()

x.pop()
y.pop()
vx.pop()
vy.pop()

#print
print(t)
print(vy)

# Вывод графика
plt.figure("Mathematical modeling")
plt.title("Modelling by Runge-Kutta method")
plt.grid(True)
#plt.plot(t, vx, 'g', label='vx', linewidth=2)
#plt.plot(t, x, 'b', label='x', linewidth=2)
#plt.plot(t, vy, 'y', label='vy', linewidth=2)
#plt.plot(t, y, 'r', label='y', linewidth=2)

plt.plot(x, y, 'b', label='trajectory', linewidth=2)
plt.legend(loc = 'lower right')

plt.show()
