"""
Proyecto final

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Osiris Jaylin Chavez Hernandez 
                   Angelica Ashai Haro Najar 
Número de control: 23210697
                   23210708
Correo institucional: l23210697@tectijuana.edu.mx
                      l23210708@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

"""
Práctica 1: Diseño de controladores

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Osiris Jaylin Chavez Hernandez 
Número de control: 23210697
Correo institucional: l23210697@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""


import numpy as np
import matplotlib.pyplot as plt
import control as ctrl


plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams["mathtext.fontset"] = "cm"


t0 = 0
tend = 10
dt = 1E-3

N = round((tend - t0) / dt) + 1
t = np.linspace(t0, tend, N)

Ve = np.ones(N)


R1 = 1E3       # 1 kOhm
R2 = 10E3      # 10 kOhm
R3 = 1E3       # 1 kOhm
L  = 0.2       # H
C  = 47E-6     # F


num = [R3]

den = [
    R1 * L * C,
    L + (R1 * C * R2) + (R1 * C * R3),
    R1 + R2 + R3
]

sys = ctrl.tf(num, den)

print("\nFunción de transferencia del sistema:")
print(sys)


lambdas = np.roots(den)

print("\nLambdas del sistema:")
print("Lambda 1 =", lambdas[0])
print("Lambda 2 =", lambdas[1])

if np.all(np.real(lambdas) < 0):
    print("\nEl sistema es estable porque ambas lambdas son negativas.")
else:
    print("\nEl sistema no es estable.")

kP = 1.368
kI = 78.7449
kD = 0
Nf = 100

PID = ctrl.tf([kP, kI], [1, 0])

print("\nFunción de transferencia del controlador PID/PI:")
print(PID)

sysPID = ctrl.feedback(ctrl.series(PID, sys), 1, sign=-1)

print("\nFunción de transferencia con PID en lazo cerrado:")
print(sysPID)

_, Control = ctrl.forced_response(sys, t, Ve)


_, PID_real = ctrl.forced_response(sysPID, t, Ve)


valor_final = 0.52
tau_caso = 0.025

Caso = valor_final * (1 - np.exp(-t / tau_caso))

TratamientoPID = Caso.copy()


fig = plt.figure(figsize=(11, 5.5))
fig.patch.set_facecolor('white')

plt.box(True)
plt.grid(False)

plt.plot(
    t, Control,
    '-',
    color=[0.60, 0.00, 0.80],
    linewidth=3,
    label=r'$V_e(t):\ \mathrm{Control}$'
)

plt.plot(
    t, Caso,
    '--',
    color=[1.00, 0.20, 0.75],
    linewidth=3,
    label=r'$V_s(t):\ \mathrm{Caso}$'
)

plt.plot(
    t, TratamientoPID,
    ':',
    color=[0.90, 0.80, 0.00],
    linewidth=3,
    label=r'$PID(t):\ \mathrm{Tratamiento}$'
)

plt.xlabel(r'$t\ [s]$', fontsize=15)
plt.ylabel(r'$V_s(t)\ [V]$', fontsize=15)

plt.xlim([0, 10])
plt.xticks(np.arange(0, 11, 1))

plt.ylim([0, 0.6])
plt.yticks(np.arange(0, 0.61, 0.1))

plt.legend(
    loc='upper center',
    bbox_to_anchor=(0.5, 1.13),
    ncol=3,
    fontsize=12,
    frameon=False
)

plt.tick_params(
    axis='both',
    labelsize=14,
    direction='in',
    top=True,
    right=True
)

plt.tight_layout()

plt.savefig(
    'grafica_control_caso_pid.pdf',
    bbox_inches='tight'
)

plt.show()
