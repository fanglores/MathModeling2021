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
k = 0.0000589507

#начальные зависимые условия
v0 = 1000
alpha = (45)*math.pi/180
g_const = 9.81

# целевые функции
def fx(t, x, y, vx, vy):
    return vx

def fy(t, x, y, vx, vy):
    return vy

def fvx(t, x, y, vx, vy):
    return (-k*math.sqrt(vx**2 + vy**2)*vx)

def fvy(t, x, y, vx, vy):
    return (-k*math.sqrt(vx**2 + vy**2)*vy - g_const)

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
        K1 = h * fx(t[i], x[i], y[i], vx[i], vy[i])
        L1 = h * fy(t[i], x[i], y[i], vx[i], vy[i])
        S1 = h * fvx(t[i], x[i], y[i], vx[i], vy[i])
        Q1 = h * fvy(t[i], x[i], y[i], vx[i], vy[i])

        K2 = h * fx(t[i] + h / 2, x[i] + K1 / 2, y[i] + L1 / 2, vx[i] + S1 / 2, vy[i] + Q1 / 2)
        L2 = h * fy(t[i] + h / 2, x[i] + K1 / 2, y[i] + L1 / 2, vx[i] + S1 / 2, vy[i] + Q1 / 2)
        S2 = h * fvx(t[i] + h / 2, x[i] + K1 / 2, y[i] + L1 / 2, vx[i] + S1 / 2, vy[i] + Q1 / 2)
        Q2 = h * fvy(t[i] + h / 2, x[i] + K1 / 2, y[i] + L1 / 2, vx[i] + S1 / 2, vy[i] + Q1 / 2)

        K3 = h * fx(t[i] + h / 2, x[i] + K2 / 2, y[i] + L2 / 2, vx[i] + S2 / 2, vy[i] + Q2 / 2)
        L3 = h * fy(t[i] + h / 2, x[i] + K2 / 2, y[i] + L2 / 2, vx[i] + S2 / 2, vy[i] + Q2 / 2)
        S3 = h * fvx(t[i] + h / 2, x[i] + K2 / 2, y[i] + L2 / 2, vx[i] + S2 / 2, vy[i] + Q2 / 2)
        Q3 = h * fvy(t[i] + h / 2, x[i] + K2 / 2, y[i] + L2 / 2, vx[i] + S2 / 2, vy[i] + Q2 / 2)

        K4 = h * fx(t[i] + h, x[i] + K3, y[i] + L3, vx[i] + S3, vy[i] + Q3)
        L4 = h * fy(t[i] + h, x[i] + K3, y[i] + L3, vx[i] + S3, vy[i] + Q3)
        S4 = h * fvx(t[i] + h, x[i] + K3, y[i] + L3, vx[i] + S3, vy[i] + Q3)
        Q4 = h * fvy(t[i] + h, x[i] + K3, y[i] + L3, vx[i] + S3, vy[i] + Q3)

        x.append(x[i] + (K1 + 2 * K2 + 2 * K3 + K4) / 6)
        y.append(y[i] + (L1 + 2 * L2 + 2 * L3 + L4) / 6)
        vx.append(vx[i] + (S1 + 2 * S2 + 2 * S3 + S4) / 6)
        vy.append(vy[i] + (Q1 + 2 * Q2 + 2 * Q3 + Q4) / 6)


for i in range(1, int((b - a) // h) + 1):
    t.append(i * h)

RungeKutta()

x.pop()
y.pop()
vx.pop()
vy.pop()

#print
print(t)
print(y)

# Вывод графика
plt.figure("Mathematical modeling")
plt.title("Modelling by Runge-Kutta method")
plt.grid(True)
#plt.plot(t, x, 'b', label='x', linewidth=2)
#plt.plot(t, y, 'r', label='y', linewidth=2)
#plt.plot(t, vx, 'g', label='vx', linewidth=2)
#plt.plot(t, vy, 'y', label='vy', linewidth=2)

plt.plot(x, y, 'b', label='trajectory', linewidth=2)
plt.legend(loc = 'lower right')

plt.show()
