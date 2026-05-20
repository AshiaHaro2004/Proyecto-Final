[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/)

# Proyecto Final: Modelado del Sistema Respiratorio con Enfoque en Asma

<img width="1536" height="1024" alt="Sistema respiratorio asma" src="https://github.com/user-attachments/assets/coloca-aqui-tu-imagen" />

## Instructor

Dr. Paul Antonio Valle Trujillo  

paul.valle@tectijuana.edu.mx  

https://biomath.xyz/  

Departamento de Ingeniería Eléctrica y Electrónica,  
Tecnológico Nacional de México / Instituto Tecnológico de Tijuana,  
Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Información general

En el estudio de los sistemas fisiológicos, el modelado matemático y computacional permite representar el comportamiento dinámico de diferentes órganos y procesos del cuerpo humano. A través de modelos análogos, es posible analizar la respuesta de un sistema biológico ante condiciones normales y patológicas, facilitando la comprensión de los cambios fisiológicos que ocurren durante una enfermedad.

En este proyecto se desarrolló un modelo del sistema respiratorio con enfoque en el asma, una enfermedad inflamatoria crónica que afecta las vías respiratorias. Durante una crisis asmática, los bronquios se estrechan debido a la broncoconstricción, la inflamación bronquial y la producción excesiva de moco. Esto provoca un aumento en la resistencia al flujo de aire, dificultando la ventilación pulmonar y reduciendo la eficiencia del intercambio gaseoso.

Para representar este comportamiento, se utilizó una analogía eléctrica tipo RLC, donde la presión respiratoria se relaciona con el voltaje, el flujo de aire con la corriente, la resistencia de las vías aéreas con una resistencia eléctrica, la compliance pulmonar con una capacitancia y la inertancia del aire con una inductancia. Esta analogía permite estudiar el sistema respiratorio como un sistema dinámico y comparar su respuesta bajo diferentes condiciones.

## Objetivo del proyecto

Modelar el comportamiento dinámico del sistema respiratorio mediante una analogía eléctrica RLC para analizar los efectos del asma sobre el flujo de aire, comparando la respuesta del sistema en condición control, caso asmático y tratamiento mediante controlador PID.

<img width="1387" height="535" alt="Modelo respiratorio" src="https://github.com/user-attachments/assets/coloca-aqui-tu-grafica" />

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

### Caso: Asma

Representa una condición patológica en la que existe inflamación bronquial, contracción del músculo liso y acumulación de moco. Estos factores provocan un aumento en la resistencia respiratoria, dificultando el paso del aire hacia los pulmones.

### Tratamiento PID

Se implementa un controlador PID con el objetivo de mejorar la respuesta del sistema asmático. Este controlador busca reducir el error, estabilizar la señal y acercar la respuesta del caso patológico al comportamiento del sistema control.

## Modelo análogo RLC

El sistema respiratorio se representa mediante un circuito RLC, donde los componentes eléctricos permiten describir la dinámica del flujo de aire y la presión respiratoria.

La ecuación general de un sistema de segundo orden puede expresarse como:

$$
L \frac{d^{2}q(t)}{dt^{2}} + R \frac{dq(t)}{dt} + \frac{1}{C}q(t) = V(t)
$$

Donde:

- $L$ representa la inertancia del aire.
- $R$ representa la resistencia de las vías respiratorias.
- $C$ representa la compliance pulmonar.
- $V(t)$ representa la presión respiratoria de entrada.
- $q(t)$ representa la variable asociada al volumen o desplazamiento del aire.

A partir de esta ecuación, se obtiene una función de transferencia que permite analizar la respuesta del sistema ante una entrada determinada.

## Función de transferencia

La función de transferencia permite relacionar la salida del sistema con la entrada aplicada. Para el sistema respiratorio análogo RLC, se considera una respuesta dinámica dependiente de los valores de resistencia, inductancia y capacitancia.

$$
G(s)=\frac{1}{LCs^{2}+RCs+1}
$$

Esta expresión permite comparar el comportamiento del sistema respiratorio en estado normal y en condición asmática. Al aumentar la resistencia, la respuesta del sistema cambia, representando la obstrucción del flujo de aire característica del asma.

## Herramientas utilizadas

- MATLAB
- Simulink
- Spyder
- Python
- NumPy
- Matplotlib
- Librería Control
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
