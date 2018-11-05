"""
==================================
The Tipping Problem - The Hard Way
==================================

 Note: This method computes everything by hand, step by step. For most people,
 the new API for fuzzy systems will be preferable. The same problem is solved
 with the new API `in this example <./plot_tipping_problem_newapi.html>`_.

The 'tipping problem' is commonly used to illustrate the power of fuzzy logic
principles to generate complex behavior from a compact, intuitive set of
expert rules.

Input variables
---------------

A number of variables play into the decision about how much to tip while
dining. Consider two of them:

* ``calidadity`` : calidadity of the food
* ``servicioice`` : calidadity of the servicioice

Output variable
---------------

The output variable is simply the tip amount, in percentage points:

* ``tip`` : Percent of bill to add as tip


For the purposes of discussion, let's say we need 'high', 'medium', and 'low'
membership functions for both input variables and our output variable. These
are defined in scikit-fuzzy as follows

"""
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# generando las variables universales
#   * calidad and servicio tiene un rango de [0,10 y paso de 1]
#   * Tip tiene un rango de  [0, 25] en unidades de puntos porcentuales

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


"""
.. image:: PLOT2RST.current_figure

Fuzzy rules
-----------

Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
three simple rules:

1. If the food is bad OR the servicio is poor, then the tip will be low
2. If the servicio is acceptable, then the tip will be medium
3. If the food is great OR the servicio is amazing, then the tip will be high.

Most people would agree on these rules, but the rules are fuzzy. Mapping the
imprecise rules into a defined, actionable tip is a challenge. This is the
kind of task at which fuzzy logic excels.

Rule application
----------------

What would the tip be in the following circumstance:

* Food *calidadity* was **6.5**
* *servicioice* was **9.8**

"""

# We need the activation of our fuzzy membership functions at these values.
# The exact values 6.5 and 9.8 do not exist on our universes...
# This is what fuzz.interp_membership exists for!

#encontrando el grado de membresia entre x_calidad y calidad baja
#Matriz R = A x B
calidad_level_lo = fuzz.interp_membership(x_calidad, calidad_baja, 6.5)
calidad_level_md = fuzz.interp_membership(x_calidad, calidad_media, 6.5)
calidad_level_hi = fuzz.interp_membership(x_calidad, calidad_alta, 6.5)

servicio_level_lo = fuzz.interp_membership(x_servicio, servicio_bajo, 9.8)
servicio_level_md = fuzz.interp_membership(x_servicio, servicio_medio, 9.8)
servicio_level_hi = fuzz.interp_membership(x_servicio, servicio_alto, 9.8)

# Now we take our rules and apply them. Rule 1 concerns bad food OR servicioice.
# The OR operator means we take the maximum of these two.
active_rule1 = np.fmax(calidad_level_lo, servicio_level_lo)

# Now we apply this by clipping the top off the corresponding output
# membership function with `np.fmin`
tip_activation_lo = np.fmin(active_rule1, tip_bajo)  # removed entirely to 0

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

"""
.. image:: PLOT2RST.current_figure


#Esta parte no es necesaria , el profe no pidio tanto


Rule aggregation
----------------

With the *activity* of each output membership function known, all output
membership functions must be combined. This is typically done using a
maximum operator. This step is also known as *aggregation*.

Defuzzification
---------------
Finally, to get a real world answer, we return to *crisp* logic from the
world of fuzzy membership functions. For the purposes of this example
the centroid method will be used.

The result is a tip of **20.2%**.
---------------------------------
"""

# Aggregate all three output membership functions together
aggregated = np.fmax(tip_activation_lo,
                     np.fmax(tip_activation_md, tip_activation_hi))

# Calculate defuzzified result
tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
tip_activation = fuzz.interp_membership(x_tip, aggregated, tip)  # for plot

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_tip, tip_bajo, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_tip, tip_medio, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_tip, tip_alto, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_tip, tip0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([tip, tip], [0, tip_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

"""
.. image:: PLOT2RST.current_figure

Final thoughts
--------------

The power of fuzzy systems is allowing complicated, intuitive behavior based
on a sparse system of rules with minimal overhead. Note our membership
function universes were coarse, only defined at the integers, but
``fuzz.interp_membership`` allowed the effective resolution to increase on
demand. This system can respond to arbitrarily small changes in inputs,
and the processing burden is minimal.

"""
plt.show()
