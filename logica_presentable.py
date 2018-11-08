
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


#arange (inicio,fin,paso)
x_calidad = np.arange(0, 11, 1)
x_servicio = np.arange(0, 11, 1)
x_tip  = np.arange(0, 26, 1)


#fuzz.trimf(funcion a trabajar,[inicio,medio,fin]) de forma triangular
calidad_baja = fuzz.trimf(x_calidad, [0, 0, 5])
calidad_media = fuzz.trimf(x_calidad, [0, 5, 10])
calidad_alta = fuzz.trimf(x_calidad, [5, 10, 10])
servicio_bajo = fuzz.trimf(x_servicio, [0, 0, 5])
servicio_medio = fuzz.trimf(x_servicio, [0, 5, 10])
servicio_alto = fuzz.trimf(x_servicio, [5, 10, 10])
tip_bajo = fuzz.trimf(x_tip, [0, 0, 13])
tip_medio = fuzz.trimf(x_tip, [0, 13, 25])
tip_alto = fuzz.trimf(x_tip, [13, 25, 25])

#Grafica de las Funciones
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_calidad, calidad_baja, 'b', linewidth=1.5, label='Mala')
ax0.plot(x_calidad, calidad_media, 'g', linewidth=1.5, label='Decente')
ax0.plot(x_calidad, calidad_alta, 'r', linewidth=1.5, label='Buena')
ax0.set_title('Calidad de Comida')
ax0.legend()

ax1.plot(x_servicio, servicio_bajo, 'b', linewidth=1.5, label='Pobre')
ax1.plot(x_servicio, servicio_medio, 'g', linewidth=1.5, label='Aceptable')
ax1.plot(x_servicio, servicio_alto, 'r', linewidth=1.5, label='Asombrosa')
ax1.set_title('Calidad de Servicio')
ax1.legend()

ax2.plot(x_tip, tip_bajo, 'b', linewidth=1.5, label='Bajo')
ax2.plot(x_tip, tip_medio, 'g', linewidth=1.5, label='Medio')
ax2.plot(x_tip, tip_alto, 'r', linewidth=1.5, label='Alto')
ax2.set_title('Cantidad de propina')
ax2.legend()

#probando operacion and
probando_and = fuzz.fuzzy_and(x_calidad,calidad_alta,x_servicio,servicio_alto)

# desaparece los cuadros de arriba y derecha (mas kawaii)
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()


#Se eligieron reglas para definir el conjunto , tal como se explica a continuacion


#encontrando el grado de membresia entre x_calidad y calidad baja
#Matriz R = A x B
calidad_level_lo = fuzz.interp_membership(x_calidad, calidad_baja, 6.5)
calidad_level_md = fuzz.interp_membership(x_calidad, calidad_media, 6.5)
calidad_level_hi = fuzz.interp_membership(x_calidad, calidad_alta, 6.5)

servicio_level_lo = fuzz.interp_membership(x_servicio, servicio_bajo, 9.8)
servicio_level_md = fuzz.interp_membership(x_servicio, servicio_medio, 9.8)
servicio_level_hi = fuzz.interp_membership(x_servicio, servicio_alto, 9.8)


active_rule1 = np.fmax(calidad_level_lo, servicio_level_lo)

tip_activation_lo = np.fmin(active_rule1, tip_bajo) 

# For rule 2 we connect acceptable servicioice to medium tipping
tip_activation_md = np.fmin(servicio_level_md, tip_medio)

# For rule 3 we connect high servicioice OR high food with high tipping
active_rule3 = np.fmax(calidad_level_hi, servicio_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_alto)
tip0 = np.zeros_like(x_tip)

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(x_tip, tip0, tip_activation_lo, facecolor='b', alpha=0.7)
ax0.plot(x_tip, tip_bajo, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_tip, tip0, tip_activation_md, facecolor='g', alpha=0.7)
ax0.plot(x_tip, tip_medio, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_tip, tip0, tip_activation_hi, facecolor='r', alpha=0.7)
ax0.plot(x_tip, tip_alto, 'r', linewidth=0.5, linestyle='--')
ax0.set_title('Output membership activity')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

plt.show()
