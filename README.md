# Proyecto-Final
Sistema Respiratorio: Asma
# Proyecto Final: Sistema Respiratorio - Asma

## Descripción

Este proyecto presenta el modelado del sistema respiratorio mediante una analogía eléctrica tipo RLC, tomando como caso de estudio el asma. El objetivo principal es analizar cómo cambia la respuesta del sistema cuando existe una alteración en las vías respiratorias, principalmente por el aumento de la resistencia al flujo de aire causado por broncoconstricción, inflamación bronquial y acumulación de mucosidad.

El modelo permite comparar el comportamiento de un sistema respiratorio en condición normal, un sistema con asma y una respuesta con tratamiento mediante controlador PID.

## Sistema fisiológico

El sistema respiratorio permite el intercambio de gases entre el organismo y el ambiente. En condiciones normales, el aire entra por las vías respiratorias y llega hasta los alvéolos, donde ocurre el intercambio de oxígeno y dióxido de carbono.

En el asma, las vías respiratorias se estrechan debido a la inflamación, la contracción del músculo liso y el exceso de moco. Esto provoca una disminución del flujo de aire y un aumento en la dificultad respiratoria.

## Planteamiento del problema

El asma modifica el comportamiento normal del sistema respiratorio al aumentar la resistencia de las vías aéreas. Esta alteración puede representarse mediante un circuito análogo RLC, donde los componentes eléctricos se relacionan con variables fisiológicas.

La comparación entre el caso control y el caso asmático permite observar cómo cambia la respuesta del sistema y cómo un tratamiento puede mejorar su estabilidad.

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

Representa el comportamiento normal del sistema respiratorio. En esta condición, las vías respiratorias tienen una resistencia adecuada y permiten un flujo de aire estable.

### Caso: Asma

Representa una condición patológica en la que existe inflamación bronquial, broncoconstricción y exceso de mucosidad. Esto aumenta la resistencia respiratoria y dificulta el paso del aire hacia los pulmones.

### Tratamiento PID

Se implementa un controlador PID con el propósito de mejorar la respuesta del sistema asmático. El tratamiento busca reducir el error, estabilizar la señal y acercar la respuesta del caso asmático al comportamiento del sistema control.

## Objetivo

Modelar el sistema respiratorio mediante una analogía RLC para analizar la respuesta dinámica de una condición asmática, comparando el sistema en estado control, caso patológico y tratamiento PID.

## Palabras clave

Asma, broncoconstricción, inflamación bronquial, resistencia respiratoria, flujo de aire.

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

El proyecto se desarrolló identificando primero las variables fisiológicas principales del sistema respiratorio y relacionándolas con los componentes de un circuito eléctrico RLC. Posteriormente, se asignaron valores para representar el caso control y el caso asmático.

Después se obtuvo la función de transferencia del sistema y se realizaron simulaciones para analizar su comportamiento. Las respuestas fueron comparadas mediante gráficas del sistema control, caso asmático y tratamiento PID.

Finalmente, se elaboró un diagrama fisiológico para visualizar las diferencias entre una vía respiratoria normal y una vía respiratoria afectada por asma.

## Resultados esperados

Se espera que el sistema con asma presente una respuesta diferente al sistema control debido al aumento de la resistencia respiratoria. Esta alteración puede reflejarse en una disminución del flujo de aire, una respuesta más lenta o una mayor dificultad para alcanzar el estado estable.

Con el controlador PID se espera mejorar la respuesta del sistema, reduciendo el error y acercando el comportamiento del caso asmático al sistema control.

## Conclusión

El modelado del sistema respiratorio mediante una analogía RLC permite representar de manera simplificada el comportamiento dinámico de una condición asmática. Al comparar el sistema control con el caso patológico, se observa la importancia de la resistencia respiratoria en el flujo de aire.

La implementación de un controlador PID permite analizar una posible estrategia de mejora para estabilizar la respuesta del sistema y reducir los efectos provocados por el aumento de resistencia en las vías aéreas.

## Autores

Proyecto final desarrollado para la asignatura de Modelado de Sistemas Fisiológicos.
