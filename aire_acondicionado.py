
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# generando las variables universales

##### VARIABLES LINGUISTICAS #######

#arange (inicio,fin,paso)

temperatura_ambiente= np.arange(0,30,1)
temperatura_usuario = np.arange(0,30,1)
hora_dia = np.arange(0,24,1)

#variables de salida

fan_speed=np.arange(0,10,1)
modo_operacion=np.arange(0,10,1)

#### VALORES LINGUISTICOS #####
### ENTRADAS
temp_ambiente_caliente = fuzz.trapmf(temperatura_ambiente, [15,25,30,30])
temp_ambiente_templado = fuzz.trapmf(temperatura_ambiente, [10,15,20,25])
temp_ambiente_frio = fuzz.trapmf(temperatura_ambiente, [0,0,10,15])

temp_usuario_calido=fuzz.trapmf(temperatura_usuario, [15,25,30,30])
temp_usuario_fresco=fuzz.trapmf(temperatura_usuario, [10,12,18,20])
temp_usuario_helado=fuzz.trapmf(temperatura_usuario,[0,0,10,15])

hora_dia_manana=fuzz.trapmf(hora_dia, [0,6,10,12])
hora_dia_mediodia=fuzz.trapmf(hora_dia, [10,12,14,18])
hora_dia_noche=fuzz.trapmf(hora_dia, [18,22,24,24])
### SALIDAS
fan_speed_bajo=fuzz.trimf(fan_speed, [0, 0, 3])
fan_speed_mediobajo=fuzz.trimf(fan_speed,[0,3,5])
fan_speed_medio=fuzz.trimf(fan_speed, [3, 5, 7])
fan_speed_medioalto=fuzz.trimf(fan_speed,[5,7,9])
fan_speed_alto=fuzz.trimf(fan_speed, [7, 9, 10])

modo_operacion_negativo=fuzz.trimf(modo_operacion,[0,0,5])
modo_operacion_nulo=fuzz.trimf(modo_operacion,[0,5,10])
modo_operacion_positivo=fuzz.trimf(modo_operacion,[5,10,10])



#Grafica de las Funciones
fig, (ax0, ax1, ax2,ax3 ,ax4) = plt.subplots(nrows=5, figsize=(8, 9))

ax0.plot(temperatura_ambiente, temp_ambiente_frio, 'b', linewidth=1.5, label='Frio')
ax0.plot(temperatura_ambiente, temp_ambiente_templado, 'g', linewidth=1.5, label='Templado')
ax0.plot(temperatura_ambiente, temp_ambiente_caliente, 'r', linewidth=1.5, label='Caliente')
ax0.set_title('Temperatura ambiente')
ax0.legend()

ax1.plot(temperatura_usuario, temp_usuario_calido, 'r', linewidth=1.5, label='Calido')
ax1.plot(temperatura_usuario, temp_usuario_fresco, 'g', linewidth=1.5, label='Fresco')
ax1.plot(temperatura_usuario, temp_usuario_helado, 'b', linewidth=1.5, label='Helado')
ax1.set_title('Temperatura Usuario')
ax1.legend()

ax2.plot(hora_dia, hora_dia_manana, 'r', linewidth=1.5, label='Maniana')
ax2.plot(hora_dia, hora_dia_mediodia, 'g', linewidth=1.5, label='Medio Dia')
ax2.plot(hora_dia, hora_dia_noche, 'b', linewidth=1.5, label='Noche')
ax2.set_title('hora_dia')
ax2.legend()

ax3.plot(fan_speed, fan_speed_bajo, 'r', linewidth=1.5, label='Bajo')
ax3.plot(fan_speed, fan_speed_mediobajo, 'g', linewidth=1.5, label='Medio Bajo')
ax3.plot(fan_speed, fan_speed_medio, 'b', linewidth=1.5, label='Medio')
ax3.plot(fan_speed, fan_speed_medioalto, 'c', linewidth=1.5, label='Medio Altoe')
ax3.plot(fan_speed, fan_speed_alto, 'y', linewidth=1.5, label='Alto')
ax3.set_title('fan_speed')
ax3.legend()

ax4.plot(modo_operacion, modo_operacion_negativo, 'b', linewidth=1.5, label='Negativo')
ax4.plot(modo_operacion, modo_operacion_nulo, 'g', linewidth=1.5, label='Nulo')
ax4.plot(modo_operacion, modo_operacion_positivo, 'r', linewidth=1.5, label='Positivo')
ax4.set_title('modo_operacion')
ax4.legend()



# desaparece los cuadros de arriba y derecha (mas kawaii)
for ax in (ax0, ax1, ax2, ax3, ax4):
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

1. si la temperatura del usuario es helado y la temperatura ambiente es frio y la hora_dia es de  manana entonces el modo de operacion sera nulo y fan_speed sera bajo
2. si la temperatura del usuario es helado y la temperatura ambiente es frio y la hora_dia es de  mediodia entonces el el modo de operacion sera negativo y fan_speed sera bajo
3. si la temperatura del usuario es helado y la temperatura ambiente es frio y la hora_dia es de  noche entonces el modo de operacion sera positivo y fan_speed sera bajo

4. si la temperatura del usuario es helado y la temperatura ambiente es templado y la hora_dia es de  manana entonces el modo de operacion sera negativo y fan_speed sera medio
5. si la temperatura del usuario es helado y la temperatura ambiente es templado y la hora_dia es de  mediodia el modo de operacion sera negatvio y fan_speed sera medio alto
6. si la temperatura del usuario es helado y la temperatura ambiente es templado y la hora_dia es de  noche el modo de operacion sera negativo y fan_speed sera bajo

7. si la temperatura del usuario es helado y la temperatura ambiente es caliente y la hora_dia es de  manana el modo de operacion sera negativo y fan_speed sera medio alto
8. si la temperatura del usuario es helado y la temperatura ambiente es caliente y la hora_dia es de  mediodia el modo de operacion sera negativo y fan_speed sera alto
9. si la temperatura del usuario es helado y la temperatura ambiente es caliente y la hora_dia es de  noche el modo de operacion sera negativo y fan_speed sera medio alto

10. si la temperatura del usuario es fresco y la temperatura ambiente es frio y la hora_dia es de  manana entonces el modo de operacion sera positivo y fan_speed sera bajo medio
11. si la temperatura del usuario es fresco y la temperatura ambiente es frio y la hora_dia es de  mediodia entonces el modo de operacion sera positivo y fan_speed sera  alto
12. si la temperatura del usuario es fresco y la temperatura ambiente es frio y la hora_dia es de  noche entonces el modo de operacion sera positivo y fan_speed sera medio alto

13. si la temperatura del usuario es fresco y la temperatura ambiente es templado y la hora_dia es de  manana entonces el modo de operacion sera nulo y fan_speed sera bajo
14. si la temperatura del usuario es fresco y la temperatura ambiente es templado y la hora_dia es de  mediodia entonces el modo de operacion sera nulo y fan_speed sera bajo medio
15. si la temperatura del usuario es fresco y la temperatura ambiente es templado y la hora_dia es de  noche entonces el modo de operacion sera nulo y fan_speed sera bajo

16. si la temperatura del usuario es fresco y la temperatura ambiente es caliente y la hora_dia es de  manana entonces el modo de operacion sera negativo y fan_speed sera medio
17. si la temperatura del usuario es fresco y la temperatura ambiente es caliente y la hora_dia es de  mediodia entonces el modo de operacion sera negativo y fan_speed sera alto
18. si la temperatura del usuario es fresco y la temperatura ambiente es caliente y la hora_dia es de  noche entonces el modo de operacion sera negativo y fan_speed sera medio alto

19. si la temperatura del usuario es calido y la temperatura ambiente es frio y la hora_dia es de  manana entonces entonces el modo de operacion sera positivo y fan_speed sera medio alto
20. si la temperatura del usuario es calido y la temperatura ambiente es frio y la hora_dia es de  mediodia entonces entonces el modo de operacion sera positivo y fan_speed sera alto
21. si la temperatura del usuario es calido y la temperatura ambiente es frio y la hora_dia es de  noche entonces entonces el modo de operacion sera positivo y fan_speed sera medio alto

22. si la temperatura del usuario es calido y la temperatura ambiente es templado y la hora_dia es de  manana entonces el modo de operacion sera positivo y fan_speed sera medio alto
23. si la temperatura del usuario es calido y la temperatura ambiente es templado y la hora_dia es de  mediodia entonces el modo de operacion sera positivo y fan_speed sera alto
24. si la temperatura del usuario es calido y la temperatura ambiente es templado y la hora_dia es de  noche entonces el modo de operacion sera positivo y fan_speed sera medio medio alto

25. si la temperatura del usuario es calido y la temperatura ambiente es caliente y la hora_dia es de  manana entonces el modo de operacion sera nulo y fan_speed sera bajo
26. si la temperatura del usuario es calido y la temperatura ambiente es caliente y la hora_dia es de  mediodia entonces el modo de operacion sera nulo y fan_speed sera bajo medio
27. si la temperatura del usuario es calido y la temperatura ambiente es caliente y la hora_dia es de  noche entonces el modo de operacion sera nulo y fan_speed sera bajo



Rule application
----------------

What would the propina be in the following circumstance:

* Food *quality* was **6.5**
* *service* was **9.8**

"""

# We need the activation of our fuzzy membership functions at these values.
# The exafsdfct values 6.5 and 9.8 do not exist on our universes...
# This is what fuzz.interp_membership exists for!

#encontrando el grado de membresia entre x_calidad y calidad baja
#Matriz R = A x B
a = float(input("Temperatura del ambiente: "))
b = float(input("Temperatura que desea el usario: "))
c = float(input("Hora del dia: "))

temp_ambiente_cal = fuzz.interp_membership(temperatura_ambiente,
                                           temp_ambiente_caliente, a)
temp_ambiente_tem = fuzz.interp_membership(temperatura_ambiente,
                                           temp_ambiente_templado, a)
temp_ambiente_fri = fuzz.interp_membership(temperatura_ambiente,
                                           temp_ambiente_frio, a)

temp_usuario_cal = fuzz.interp_membership(temperatura_usuario,
                                          temp_usuario_calido, b)
temp_usuario_fre = fuzz.interp_membership(temperatura_usuario,
                                          temp_usuario_fresco, b)
temp_usuario_hel = fuzz.interp_membership(temperatura_usuario,
                                          temp_usuario_helado, b)

hora_dia_ma = fuzz.interp_membership(hora_dia, hora_dia_manana, c)
hora_dia_me = fuzz.interp_membership(hora_dia, hora_dia_mediodia, c)
hora_dia_no = fuzz.interp_membership(hora_dia, hora_dia_noche, c)

##### EJEMPLO DE COMPOSICION #####

# Now we take our rules and apply them. Rule 1 concerns bad food OR servicioice.
# The OR operator means we take the maximum of these two.

regla1 = np.fmin(temp_usuario_hel,np.fmin(hora_dia_ma,temp_ambiente_fri))
#regla1 = np.fmin(regla1,hora_dia_ma)

regla2 = np.fmin(temp_usuario_hel,temp_ambiente_fri)
regla2 = np.fmin(regla1,hora_dia_me)

regla3 = np.fmin(temp_usuario_hel,temp_ambiente_fri)
regla3 = np.fmin(regla1,hora_dia_no)

regla4 = np.fmin(temp_usuario_hel,temp_ambiente_tem)
regla4 = np.fmin(regla1,hora_dia_ma)

regla5 = np.fmin(temp_usuario_hel,temp_ambiente_tem)
regla5 = np.fmin(regla1,hora_dia_me)

regla6 = np.fmin(temp_usuario_hel,temp_ambiente_tem)
regla6 = np.fmin(regla1,hora_dia_no)

regla7 = np.fmin(temp_usuario_hel,temp_ambiente_cal)
regla7 = np.fmin(regla1,hora_dia_ma)

regla8 = np.fmin(temp_usuario_hel,temp_ambiente_cal)
regla8 = np.fmin(regla1,hora_dia_me)

regla9 = np.fmin(temp_usuario_hel,temp_ambiente_cal)
regla9 = np.fmin(regla1,hora_dia_no)

regla10 = np.fmin(temp_usuario_fre,temp_ambiente_fri)
regla10 = np.fmin(regla1,hora_dia_ma)

regla11 = np.fmin(temp_usuario_fre,temp_ambiente_fri)
regla11 = np.fmin(regla1,hora_dia_me)

regla12 = np.fmin(temp_usuario_fre,temp_ambiente_fri)
regla12 = np.fmin(regla1,hora_dia_no)

regla13 = np.fmin(temp_usuario_fre,temp_ambiente_tem)
regla13 = np.fmin(regla1,hora_dia_ma)

regla14 = np.fmin(temp_usuario_fre,temp_ambiente_tem)
regla14 = np.fmin(regla1,hora_dia_me)

regla15 = np.fmin(temp_usuario_fre,temp_ambiente_tem)
regla15 = np.fmin(regla1,hora_dia_no)

regla16 = np.fmin(temp_usuario_fre,temp_ambiente_cal)
regla16 = np.fmin(regla1,hora_dia_ma)

regla17 = np.fmin(temp_usuario_fre,temp_ambiente_cal)
regla17 = np.fmin(regla1,hora_dia_me)

regla18 = np.fmin(temp_usuario_fre,temp_ambiente_cal)
regla18 = np.fmin(regla1,hora_dia_no)

regla19 = np.fmin(temp_usuario_cal,temp_ambiente_fri)
regla19 = np.fmin(regla1,hora_dia_ma)

regla20 = np.fmin(temp_usuario_cal,temp_ambiente_fri)
regla20 = np.fmin(regla1,hora_dia_me)

regla21 = np.fmin(temp_usuario_cal,temp_ambiente_fri)
regla21 = np.fmin(regla1,hora_dia_no)

regla22 = np.fmin(temp_usuario_cal,temp_ambiente_tem)
regla22 = np.fmin(regla1,hora_dia_ma)

regla23 = np.fmin(temp_usuario_cal,temp_ambiente_tem)
regla23 = np.fmin(regla1,hora_dia_me)

regla24 = np.fmin(temp_usuario_cal,temp_ambiente_tem)
regla24 = np.fmin(regla1,hora_dia_no)

regla25 = np.fmin(temp_usuario_cal,temp_ambiente_cal)
regla25 = np.fmin(regla1,hora_dia_ma)

regla26 = np.fmin(temp_usuario_cal,temp_ambiente_cal)
regla26 = np.fmin(regla1,hora_dia_me)

regla27 = np.fmin(temp_usuario_cal,temp_ambiente_cal)
regla27 = np.fmin(regla1,hora_dia_no)

#active_rule1 = np.fmin(calidad_level_lo, servicio_level_lo)

# Now we apply this by clipping the top off the corresponding output
# membership function with `np.fmin`

fan_speed_activation_bajo1 = np.fmin(regla1,fan_speed_bajo)
modo_operacion_activation_nulo1 = np.fmin(regla1,modo_operacion_nulo)

fan_speed_activation_bajo2 = np.fmin(regla2,fan_speed_bajo)
modo_operacion_activation_negativo2 = np.fmin(regla2,modo_operacion_negativo)

fan_speed_activation_bajo3 = np.fmin(regla3,fan_speed_bajo)
modo_operacion_activation_positivo3 = np.fmin(regla3,modo_operacion_positivo)

fan_speed_activation_medio4 = np.fmin(regla4,fan_speed_medio)
modo_operacion_activation_negativo4 = np.fmin(regla4,modo_operacion_negativo)

fan_speed_activation_medioalto5 = np.fmin(regla5,fan_speed_medioalto)
modo_operacion_activation_negativo5 = np.fmin(regla5,modo_operacion_negativo)

fan_speed_activation_bajo6 = np.fmin(regla6,fan_speed_bajo)
modo_operacion_activation_negativo6 = np.fmin(regla6,modo_operacion_negativo)

fan_speed_activation_medioalto7 = np.fmin(regla7,fan_speed_medioalto)
modo_operacion_activation_negativo7 = np.fmin(regla7,modo_operacion_negativo)

fan_speed_activation_medioalto8 = np.fmin(regla8,fan_speed_medioalto)
modo_operacion_activation_negativo8 = np.fmin(regla8,modo_operacion_negativo)

fan_speed_activation_alto9 = np.fmin(regla9,fan_speed_alto)
modo_operacion_activation_negativo9 = np.fmin(regla9,modo_operacion_negativo)

fan_speed_activation_medioalto10 = np.fmin(regla10,fan_speed_medioalto)
modo_operacion_activation_negativo10 = np.fmin(regla10,modo_operacion_negativo)

fan_speed_activation_mediobajo11 = np.fmin(regla11,fan_speed_mediobajo)
modo_operacion_activation_positivo11 = np.fmin(regla11,modo_operacion_positivo)

fan_speed_activation_alto12 = np.fmin(regla12,fan_speed_alto)
modo_operacion_activation_positivo12 = np.fmin(regla12,modo_operacion_positivo)

fan_speed_activation_medioalto13 = np.fmin(regla13,fan_speed_medioalto)
modo_operacion_activation_positivo13 = np.fmin(regla13,modo_operacion_positivo)

fan_speed_activation_bajo14 = np.fmin(regla14,fan_speed_bajo)
modo_operacion_activation_nulo14 = np.fmin(regla14,modo_operacion_nulo)

fan_speed_activation_mediobajo15 = np.fmin(regla15,fan_speed_mediobajo)
modo_operacion_activation_nulo15 = np.fmin(regla15,modo_operacion_nulo)

fan_speed_activation_bajo16 = np.fmin(regla16,fan_speed_bajo)
modo_operacion_activation_nulo16 = np.fmin(regla16,modo_operacion_nulo)

fan_speed_activation_medio17 = np.fmin(regla17,fan_speed_medio)
modo_operacion_activation_negativo17 = np.fmin(regla17,modo_operacion_negativo)

fan_speed_activation_alto18 = np.fmin(regla18,fan_speed_alto)
modo_operacion_activation_negativo18 = np.fmin(regla18,modo_operacion_negativo)

fan_speed_activation_medioalto19 = np.fmin(regla19,fan_speed_medioalto)
modo_operacion_activation_negativo19 = np.fmin(regla19,modo_operacion_negativo)

fan_speed_activation_medioalto20 = np.fmin(regla20,fan_speed_medioalto)
modo_operacion_activation_positivo20 = np.fmin(regla20,modo_operacion_positivo)

fan_speed_activation_alto21 = np.fmin(regla21,fan_speed_alto)
modo_operacion_activation_positivo21 = np.fmin(regla21,modo_operacion_positivo)

fan_speed_activation_medioalto22 = np.fmin(regla22,fan_speed_medioalto)
modo_operacion_activation_positivo22 = np.fmin(regla22,modo_operacion_positivo)

fan_speed_activation_alto23 = np.fmin(regla23,fan_speed_alto)
modo_operacion_activation_positivo23 = np.fmin(regla23,modo_operacion_positivo)

fan_speed_activation_medioalto24 = np.fmin(regla24,fan_speed_medioalto)
modo_operacion_activation_positivo24 = np.fmin(regla24,modo_operacion_positivo)

fan_speed_activation_bajo25 = np.fmin(regla25,fan_speed_bajo)
modo_operacion_activation_nulo25 = np.fmin(regla25,modo_operacion_nulo)

fan_speed_activation_mediobajo26 = np.fmin(regla26,fan_speed_mediobajo)
modo_operacion_activation_nulo26 = np.fmin(regla26,modo_operacion_nulo)

fan_speed_activation_bajo27 = np.fmin(regla27,fan_speed_bajo)
modo_operacion_activation_nulo27 = np.fmin(regla27,modo_operacion_nulo)


#fan speed salida

#bajo
fan_speed_activation_bajo=np.fmax(fan_speed_activation_bajo1,
	np.fmax(fan_speed_activation_bajo2,
		np.fmax(fan_speed_activation_bajo3,
			np.fmax(fan_speed_activation_bajo6,
				np.fmax(fan_speed_activation_bajo14,
					np.fmax(fan_speed_activation_bajo16,
						np.fmax(fan_speed_activation_bajo25,
							fan_speed_activation_bajo27)))))))
#medio bajo
fan_speed_activation_mediobajo=np.fmax(np.fmax(fan_speed_activation_mediobajo11
	,fan_speed_activation_mediobajo15)
,fan_speed_activation_mediobajo26)
#medio
fan_speed_activation_medio=np.fmax(fan_speed_activation_medio4,fan_speed_activation_medio17)
#medio alto
fan_speed_activation_medioalto=np.fmax(fan_speed_activation_medioalto5,
	np.fmax(fan_speed_activation_medioalto7,
		np.fmax(fan_speed_activation_medioalto8,
			np.fmax(fan_speed_activation_medioalto10,
				np.fmax(fan_speed_activation_medioalto13,
					np.fmax(fan_speed_activation_medioalto19,
						np.fmax(fan_speed_activation_medioalto22,
						fan_speed_activation_medioalto24)))))))
#alto
fan_speed_activation_alto=np.fmax(np.fmax(fan_speed_activation_alto9,
	fan_speed_activation_alto12),np.fmax(np.fmax(fan_speed_activation_alto18,
		fan_speed_activation_alto21),fan_speed_activation_alto23))

#Modo Operacion

#nulo
modo_operacion_activation_nulo=np.fmax(modo_operacion_activation_nulo1,
                                       np.fmax(modo_operacion_activation_nulo14,
                                              np.fmax(modo_operacion_activation_nulo15,
                                                     np.fmax(modo_operacion_activation_nulo16,
                                                            np.fmax(modo_operacion_activation_nulo25,
                                                                   np.fmax(modo_operacion_activation_nulo26,
                                                                           modo_operacion_activation_nulo27))))))

#negativo
modo_operacion_activation_negativo=np.fmax(modo_operacion_activation_negativo2,
	np.fmax(modo_operacion_activation_negativo4,
		np.fmax(modo_operacion_activation_negativo5,
			np.fmax(modo_operacion_activation_negativo6,
				np.fmax(modo_operacion_activation_negativo7,
					np.fmax(modo_operacion_activation_negativo8,
						np.fmax(modo_operacion_activation_negativo9,
							np.fmax(modo_operacion_activation_negativo17,
								np.fmax(modo_operacion_activation_negativo18,
									modo_operacion_activation_negativo19)))))))))


#positivo

modo_operacion_activation_positivo=np.fmax(modo_operacion_activation_positivo3,
	np.fmax(modo_operacion_activation_positivo11,
		np.fmax(modo_operacion_activation_positivo12,
			np.fmax(modo_operacion_activation_positivo13,
				np.fmax(modo_operacion_activation_positivo21,
					np.fmax(modo_operacion_activation_positivo22,
								np.fmax(modo_operacion_activation_positivo23,
									modo_operacion_activation_positivo24)))))))


#agregacion

agregacion_fan_speed= np.fmax(fan_speed_activation_bajo,
                     np.fmax(fan_speed_activation_medio,
                             np.fmax(fan_speed_activation_mediobajo,
                                    np.fmax(fan_speed_activation_medioalto,
                                            fan_speed_activation_alto))))


agregacion_modo_operacion=np.fmax(modo_operacion_activation_positivo,
                                  np.fmax(modo_operacion_activation_negativo,
                                          modo_operacion_activation_nulo))


#desfuzificacion

#fan_speed
fan=fuzz.defuzz(fan_speed,agregacion_fan_speed,'som')
fan_activation=fuzz.interp_membership(fan_speed,agregacion_fan_speed,fan)


# Visualize this
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 3))
fan0=np.zeros_like(fan_speed)
ax0.plot(fan_speed, fan_speed_bajo, 'r',linestyle='--', linewidth=1.5, label='Bajo')
ax0.plot(fan_speed, fan_speed_mediobajo, 'g',linestyle='--', linewidth=1.5, label='Medio Bajo')
ax0.plot(fan_speed, fan_speed_medio, 'b',linestyle='--', linewidth=1.5, label='Medio ')
ax0.plot(fan_speed, fan_speed_medioalto, 'c',linestyle='--', linewidth=1.5, label='Medio Alto')
ax0.plot(fan_speed, fan_speed_alto, 'y',linestyle='--', linewidth=1.5, label='Alto')
ax0.fill_between(fan_speed, fan0, agregacion_fan_speed, facecolor='orange', alpha=0.7)
ax0.plot([fan, fan], [0, fan_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('fan_speed resultado (linea)')
ax0.legend()

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

#modo_operacion

modo=fuzz.defuzz(modo_operacion,agregacion_modo_operacion,'som')
modo_activation=fuzz.interp_membership(modo_operacion,agregacion_modo_operacion,modo)

modo0=np.zeros_like(modo_operacion)
ax1.plot(modo_operacion, modo_operacion_nulo, 'r',linestyle='--', linewidth=1.5, label='Nulo')
ax1.plot(modo_operacion, modo_operacion_positivo, 'g',linestyle='--', linewidth=1.5, label='Positivo')
ax1.plot(modo_operacion, modo_operacion_negativo, 'b',linestyle='--', linewidth=1.5, label='Negativo')

ax1.fill_between(modo_operacion, modo0, agregacion_modo_operacion, facecolor='orange', alpha=0.7)
ax0.plot([modo, modo], [0, modo_activation], 'k', linewidth=1.5, alpha=0.9)
ax1.set_title('modo_operacion_activation')
ax1.legend()
# Turn off top/right axes
for ax in (ax0,ax1):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

print ("fan_speed adecuado:",fan,fan_activation)
if(modo>5):
	print ("modo operacion adecuado positivo: ",modo,modo_activation)
elif(modo==5):
	print ("modo operacion adecuado nulo: ",modo,modo_activation)
elif(modo<5):
	print ("modo operacion adecuado negativo: ",modo,modo_activation)



plt.show()



