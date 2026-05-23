[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/)

# Proyecto Final: Modelado del Sistema Respiratorio con Enfoque en Asma


<p align="center">
  <img width="650" alt="OSIRISASHIA" src="https://github.com/user-attachments/assets/a6e9cb9f-a22e-434a-bab8-e0df91c53079" />
</p>

## Información de las estudiantes

Osiris Jaylin Chavez Hernandez [23210697]; l23210697@tectijuana.edu.mx  

Angélica Ashia Haro Najar [23210708]; l23210708@tectijuana.edu.mx  

Modelado de Sistemas Fisiológicos  

Ingeniería Biomédica  

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx  

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Información general

En el estudio de los sistemas fisiológicos, el modelado matemático y computacional permite representar el comportamiento dinámico de diferentes órganos y procesos del cuerpo humano. A través de modelos análogos, es posible analizar la respuesta de un sistema biológico ante condiciones normales y patológicas, facilitando la comprensión de los cambios fisiológicos que ocurren durante una enfermedad.

En este proyecto se desarrolló un modelo del sistema respiratorio con enfoque en el asma, una enfermedad inflamatoria crónica que afecta las vías respiratorias. Durante una crisis asmática, los bronquios se estrechan debido a la broncoconstricción, la inflamación bronquial y la producción excesiva de moco. Esto provoca un aumento en la resistencia al flujo de aire, dificultando la ventilación pulmonar y reduciendo la eficiencia del intercambio gaseoso.

Para representar este comportamiento, se utilizó una analogía eléctrica tipo RLC, donde la presión respiratoria se relaciona con el voltaje, el flujo de aire con la corriente, la resistencia de las vías aéreas con una resistencia eléctrica, la compliance pulmonar con una capacitancia y la inertancia del aire con una inductancia. Esta analogía permite estudiar el sistema respiratorio como un sistema dinámico y comparar su respuesta bajo diferentes condiciones.

## Objetivo del proyecto

Modelar el comportamiento dinámico del sistema respiratorio mediante una analogía eléctrica RLC para analizar los efectos del asma sobre el flujo de aire, comparando la respuesta del sistema en condición control, caso asmático y tratamiento mediante controlador PID.

El sistema respiratorio tiene como función principal permitir el intercambio de gases entre el organismo y el ambiente. En condiciones normales, el aire entra a través de las vías respiratorias y llega hasta los alvéolos, donde ocurre el intercambio de oxígeno y dióxido de carbono. Sin embargo, en el asma, el estrechamiento de las vías aéreas aumenta la resistencia respiratoria y disminuye el flujo de aire.

La simulación del sistema permite observar cómo cambia la respuesta respiratoria cuando se modifican los parámetros del modelo. En el caso asmático, el aumento de la resistencia representa la dificultad del aire para circular por los bronquios. Posteriormente, se implementa un controlador PID con el propósito de mejorar la respuesta del sistema y acercarla al comportamiento del caso control.

#### Palabras clave: Asma; Broncoconstricción; Inflamación bronquial; Resistencia respiratoria; Flujo de aire.

## Analogía fisiológica-eléctrica

| Sistema respiratorio | Circuito eléctrico |
|---|---|
| Presión respiratoria | Voltaje |
| Flujo de aire | Corriente |
| Resistencia de las vías aéreas | Resistencia |
| Compliance pulmonar | Capacitancia |
| Inertancia del aire | Inductancia |

## Condiciones analizadas

### Control

Representa el comportamiento normal del sistema respiratorio. En esta condición, las vías respiratorias mantienen un diámetro adecuado, permitiendo un flujo de aire estable y una ventilación eficiente.

### Sistema control

| Componente | Parámetro | Componente fisiológico / neuronal | Unidad fisiológica equivalente | Valor control |
|---|---|---|---|---|
| R1 | Resistencia de las vías respiratorias principales | Tráquea y bronquios principales | cmH₂O·s/L | 1 kΩ |
| R2 | Resistencia en bronquios o vías respiratorias internas | Bronquios | cmH₂O·s/L | 2 kΩ |
| R3 | Resistencia en bronquiolos y tejido pulmonar | Bronquiolos y tejido pulmonar | cmH₂O·s/L | 10 kΩ |
| L | Inertancia del aire | Flujo de aire en las vías respiratorias | cmH₂O·s²/L | 0.2 H |
| C | Compliance pulmonar | Pulmones / capacidad de expansión pulmonar | L/cmH₂O | 47 µF |

### Caso: Asma

Representa una condición patológica en la que existe inflamación bronquial, contracción del músculo liso y acumulación de moco. Estos factores provocan un aumento en la resistencia respiratoria, dificultando el paso del aire hacia los pulmones.

### Sistema caso asmático

| Componente | Parámetro | Componente fisiológico / neuronal | Unidad fisiológica equivalente | Valor caso |
|---|---|---|---|---|
| R1 | Resistencia de las vías respiratorias principales | Tráquea y bronquios principales | cmH₂O·s/L | 8 kΩ |
| R2 | Resistencia en bronquios o vías respiratorias internas | Bronquios | cmH₂O·s/L | 12 kΩ |
| R3 | Resistencia en bronquiolos y tejido pulmonar | Bronquiolos y tejido pulmonar | cmH₂O·s/L | 4.7 kΩ |
| L | Inertancia del aire | Flujo de aire en las vías respiratorias | cmH₂O·s²/L | 1.5 H |
| C | Compliance pulmonar | Pulmones / capacidad de expansión pulmonar | L/cmH₂O | 4.7 µF |

### Tratamiento PID

Se implementa un controlador PID con el objetivo de mejorar la respuesta del sistema asmático. Este controlador busca reducir el error, estabilizar la señal y acercar la respuesta del caso patológico al comportamiento del sistema control.

## Modelo de ecuaciones integro-diferenciales

El sistema respiratorio se representa mediante un circuito RLC, donde los componentes eléctricos permiten describir la dinámica del flujo de aire, la presión respiratoria y la resistencia de las vías respiratorias.

Para este modelo se consideran dos corrientes principales: $i_1(t)$ e $i_2(t)$. La corriente $i_1(t)$ representa el flujo asociado a la entrada del sistema, mientras que $i_2(t)$ se relaciona con la respuesta del sistema respiratorio. La diferencia entre ambas corrientes, $i_1(t)-i_2(t)$, está asociada al efecto de almacenamiento producido por la compliance pulmonar $C$.

Las ecuaciones que describen el comportamiento del sistema son:

$$
R_1 i_1(t) + \frac{1}{C}\int [i_1(t)-i_2(t)]dt = V_e(t)
$$

$$
L\frac{di_2(t)}{dt} + (R_2+R_3)i_2(t) =
\frac{1}{C}\int [i_1(t)-i_2(t)]dt
$$

$$
F_s(t)=V_{R3}(t)=R_3 i_2(t)
$$

Donde:

- $R_1$ representa la resistencia inicial de las vías respiratorias.
- $R_2$ representa una resistencia adicional del sistema respiratorio.
- $R_3$ representa la resistencia asociada a la salida del sistema.
- $L$ representa la inertancia del aire.
- $C$ representa la compliance pulmonar.
- $V_e(t)$ representa la presión respiratoria de entrada.
- $i_1(t)$ representa la corriente o flujo de entrada.
- $i_2(t)$ representa la corriente o flujo de salida del sistema.
- $F_s(t)$ representa la señal de salida del sistema.
- $V_{R3}(t)$ representa el voltaje en la resistencia $R_3$, equivalente a la salida del modelo.

A partir de estas ecuaciones se puede obtener la función de transferencia del sistema, relacionando la entrada $V_e(t)$ con la salida $F_s(t)$. Esto permite analizar la respuesta respiratoria del modelo ante diferentes condiciones, como el caso control y el caso con alteración en las vías respiratorias.

## Función de transferencia

La función de transferencia permite relacionar la salida del sistema con la entrada aplicada. Para el sistema respiratorio análogo RLC, se considera una respuesta dinámica dependiente de los valores de resistencia, inductancia y capacitancia.

Por lo tanto, la función de transferencia final es:

$$
\boxed{
\frac{F_s(s)}{V_e(s)} =
\frac{R_3}
{R_1LCs^2 + \left[L + R_1C(R_2 + R_3)\right]s + (R_1 + R_2 + R_3)}
}
$$

Esta expresión permite comparar el comportamiento del sistema respiratorio en estado normal y en condición asmática. Al aumentar la resistencia, la respuesta del sistema cambia, representando la obstrucción del flujo de aire característica del asma.

## Error en estado estacionario

$$
e_{ss} =
\lim_{s \to 0}
\left(
1 -
\frac{\displaystyle R_3}
{\displaystyle R_1LCs^2 + \left[L + R_1C(R_2+R_3)\right]s + (R_1+R_2+R_3)}
\right)
$$

$$
e_{ss} =
1 -
\frac{\displaystyle R_3}
{\displaystyle R_1+R_2+R_3}
$$

$$
e_{ss} =
\frac{\displaystyle R_1+R_2}
{\displaystyle R_1+R_2+R_3}
$$

## Caso

Sustituyendo los valores del caso:

$$
e_{ss} =
\lim_{s \to 0}
\left(
1 -
\frac{\displaystyle 18}
{\displaystyle 12 + 4.7 + 18}
\right)
$$

$$
e_{ss} =
1 -
\frac{\displaystyle 18}
{\displaystyle 34.7}
$$

$$
e_{ss} =
\frac{\displaystyle 12 + 4.7}
{\displaystyle 12 + 4.7 + 18}
$$

$$
e_{ss} =
\frac{\displaystyle 16.7}
{\displaystyle 34.7}
$$

$$
e_{ss} = 0.48
$$

## Control

Sustituyendo los valores del control:

$$
e_{ss} =
\lim_{s \to 0}
\left(
1 -
\frac{\displaystyle 10}
{\displaystyle 1 + 1 + 10}
\right)
$$

$$
e_{ss} =
1 -
\frac{\displaystyle 10}
{\displaystyle 12}
$$

$$
e_{ss} =
\frac{\displaystyle 1 + 1}
{\displaystyle 1 + 1 + 10}
$$

$$
e_{ss} =
\frac{\displaystyle 2}
{\displaystyle 12}
$$

$$
e_{ss} = 0.167
$$
## Control

Sustituyendo los valores del control:

$$
e_{ss} =
\lim_{s \to 0}
\left(
1 -
\frac{10}
{1 + 1 + 10}
\right)
$$

$$
e_{ss} =
1 -
\frac{10}{12}
$$

$$
e_{ss} =
\frac{1+1}{1+1+10}
$$

$$
e_{ss} =
\frac{2}{12}
$$

$$
e_{ss} = 0.167
$$

## Estabilidad del sistema

### Control

El sistema de control es **estable con respuesta sobreamortiguada**, debido a que sus raíces son reales, negativas y diferentes.

$$
\lambda_1 = -23.2116
$$

$$
\lambda_2 = -54998.065
$$

Por lo tanto, el sistema **no presenta oscilaciones** y tiende a estabilizarse con el tiempo.

### Caso

El sistema del caso también es **estable con respuesta sobreamortiguada**, ya que sus raíces son reales, negativas y diferentes.

$$
\lambda_1 = -580057
$$

$$
\lambda_2 = -11329.8731
$$

Por lo tanto, el sistema **no presenta oscilaciones** y su respuesta converge de manera estable.

## BioRender

El diagrama elaborado en BioRender permite visualizar la comparación entre el sistema respiratorio en condición control y en caso asmático. En la sección de control se representa un flujo aéreo adecuado, resistencia bronquial normal y una respuesta respiratoria estable. En el caso asmático se muestra el aumento de la resistencia en las vías respiratorias, la disminución del flujo de aire y la alteración de la respuesta del sistema.

<img width="3000" height="3000" alt="Diagrama fisiológico sistema respiratorio asma" src="https://github.com/user-attachments/assets/7a1dc2dc-fb96-418e-8d7d-4b801620dd0b" />

## Herramientas utilizadas

- MATLAB
- Simulink
- Spyder
- Scientific WorkPlace
- BioRender

## Desarrollo general

El desarrollo del proyecto inició con la identificación de las variables fisiológicas principales del sistema respiratorio. Posteriormente, se estableció la analogía entre dichas variables y los elementos de un circuito eléctrico RLC. Con base en esta relación, se definieron los parámetros correspondientes para el sistema control y el caso asmático.

Después, se obtuvo la función de transferencia del sistema y se realizaron simulaciones computacionales para observar la respuesta dinámica. Las gráficas permitieron comparar el comportamiento del sistema control, el caso asmático y la respuesta con tratamiento PID.

Finalmente, se elaboró un diagrama fisiológico en BioRender para representar visualmente las diferencias entre una vía respiratoria normal y una vía respiratoria afectada por asma, destacando los cambios en la resistencia, el flujo de aire y la obstrucción bronquial.

## Resultados esperados

Se espera que el sistema control presente una respuesta estable, representando una ventilación pulmonar adecuada. En cambio, el caso asmático debe mostrar una respuesta alterada debido al aumento de la resistencia respiratoria, lo que puede reflejarse en una disminución del flujo de aire, una respuesta más lenta o una mayor dificultad para alcanzar el estado estable.

Con la implementación del controlador PID, se espera mejorar la respuesta del sistema asmático, reduciendo el error y acercando la señal a la condición control. Esto permite interpretar el tratamiento como una estrategia de regulación para disminuir los efectos provocados por la obstrucción de las vías respiratorias.

## Conclusión

El modelado del sistema respiratorio mediante una analogía RLC permite representar de manera simplificada los cambios dinámicos que ocurren durante una condición asmática. A través de la comparación entre el caso control y el caso patológico, se observa que el aumento de la resistencia respiratoria es uno de los factores principales que afectan el flujo de aire.

La implementación de un controlador PID permite analizar una posible mejora en la respuesta del sistema, ayudando a estabilizar la señal y reducir el error. Este tipo de modelado resulta útil para comprender el comportamiento fisiológico del asma desde una perspectiva matemática, computacional y biomédica.

## Referencias

[1] Global Initiative for Asthma. (2024). Global Strategy for Asthma Management and Prevention. Disponible en: https://ginasthma.org/

[2] Hall, J. E. (2021). Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier.

[3] West, J. B. (2021). West's Respiratory Physiology: The Essentials. 11th ed. Wolters Kluwer.

[4] Ogata, K. (2010). Modern Control Engineering. 5th ed. Prentice Hall.

[5] MathWorks. (n.d.). Simulink Documentation. Disponible en: https://www.mathworks.com/help/simulink/
