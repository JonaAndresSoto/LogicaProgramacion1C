Universidad Internacional del Ecuador

Ingenieria en Software

Nombre: Jonathan Sarango

Materia: Logica de programación 

JUEGO DEL AHORCADO 

Objetivo
Desarrollar una juego  interactiva de consola mediante el lenguaje Python, aplicando los fundamentos de
programación aprendidos en este periodo de estudio donde se puso en practica estructuras de datos, para
resolver un problema de lógica algorítmica a través de la implementación del clásico juego del ahorcado. 

Descripción de las Funcionalidades

- El sistema presenta una interfaz de texto inicial que controla el arranque del programa. Permite al
  usuario decidir entre entrar al bucle principal de ejecución 1. jugar o 2. finalizar
- Al iniciar una partida, el programa con la libreria ramdon selecciona una palabra de la tupla que actúa
  como base de datos entonces con la libreria extrae una palabra al azar.
- El sistema evalúa en cada iteración qué caracteres han sido descubiertos y cuáles no. Utilizando
  concatenación de cadenas, construye y muestra en la terminal una representación de las letras adivinas y
  el intentos restantes. 
- Durante el desarrollo de la partida, el programa pausa su ejecución y despliega un submenú que otorga
  control total al usuario, permitiéndole elegir entre cuatro acciones distintas:
  Ingresar una letra para intentar descubrir la palabra.
  Rendirse y solicitar que el sistema revele la respuesta correcta.
  Reiniciar el estado de la partida con una palabra nueva.
  Abandonar la partida y regresar al final del flujo.
- Cuando el usuario selecciona ingresar una letra, el sistema cuenta con un filtro de seguridad. Utiliza
  la función de longitud (len()) para verificar que el usuario introdujo estrictamente un solo carácter.
  Si detecta anomalías, rechaza el ingreso y vuelve a solicitar el dato sin penalizar al jugador.
- Y para finalizar toma la letra validada y verifica si existe en la palabra secreta. Si es un acierto,
  actualiza la lista de progreso y verifica matemáticamente si la palabra ya fue completada para declarar
  la victoria. Si es un error, deduce una unidad del contador de vidas y verifica si este ha llegado a
  cero para declarar el fin del juego.

Cronograma de actividades

- Semana 1: Tipos de problemas, pasos para resolver problemas, uso de computadoras para la resolucion de problemas
- Semana 2: Entorno de la programación, que es depuración y tipos
- Semana 3: Manejo de datos, algoritmos, como hacer diagramas de flujo, almacenamiento de datos
- Semana 4: Herramientas para resolver problemas mediante programación, que es un algoritmo
- Semana 5: Uso de condicionales, estructuras de decisión
- Semana 6: Que son los bucles, como usarlos y en que casos ponerlos en practica
- Semana 7: Estructura de Datos, que son tuplas y como usarlas

 Introducción
   
Este documento detalla el desarrollo del juego del ahorcado que se realizo de una manera interactiva que
fue  desarrollada en el lenguaje Python. El objetivo central del proyecto es aplicar los fundamentos de la
programación estructurada para construir un sistema interactivo que evalúe y responda a las acciones del
usuario en tiempo real. A través de este ejercicio, se busca demostrar la capacidad de traducir un 
diagrama de flujo en código funcional, asegurando una interaccion de agrado para el usuario y la 
validacion de datos en tiempo real.

 Descripción del problema
   
El problema a resolver en este proyecto es el control del flujo de ejecución y la gestión de entradas que
el usuario podria hacer. Al tratarse de un sistema sin interfaz gráfica, toda la interacción depende de lo
que el usuario escriba en la consola. El problema radica en diseñar un menu interactivo donde el usuario
comprenda la logica del programa para procesar lo que el usuario ingrese mediante el teclado, estas
entradas se tiene que validar y que cumplan con los requisitos del sistema  y actualizar inmediatamente 
el estado del juego sin que el programa colapse, caiga en bucles infinitos o genere errores de ejecución.

 Relación con los contenidos de la asignatura
 
Para comenzar primero se analizo el problema a resolver en este caso fue como hacer que la consola juegue
con el usuario y como el usuario ingrese datos al sistema, en este paso se analizo y formulo soluciones.
Este desarrollo fue consolidado con múltiples conceptos aprendidos en la materia de logica de la
programación donde se implemento una programación estructurada y la lógica algorítmica.
El uso intensivo de bucles es fundamental para mantener el ciclo de vida de la aplicación y condicionales
como if, elif, else para analizar las decisiones lógicas según las reglas del juego.
Se implemento listas con palabras mediante el uso de tuplas para almacenar el banco de palabras y una
lista para registrar dinámicamente las letras que el usuario va adivinando.
En esta aplicación se uso comandos que son de gran ayuda para el desarrollo de cualquier proyecto: (len(),
.strip(), .lower()) estas funciones ayudan para limpiar las entradas del usuario y garantizar un
procesamiento efectivo de la aplicación.
El programa esta dividido en separación lógica entre la inicialización de variables, el renderizado de la
interfaz de texto y el bloque de evaluación de jugadas.

Explicación del sistema desarrollado

El software desarrollado funciona mediante una arquitectura de estado continuo (bucle). El flujo inicia
ofreciendo al usuario la opción de arrancar el juego o salir. Al elegir jugar, el sistema con la libreria
ramdon analiza y escoga inmediatamente de la tupla de palabras y selecciona una al azar.
Dentro del ciclo principal, el sistema ejecuta tres procesos secuenciales en cada turno:
Renderizado del estado: Evalúa las letras acertadas contra la palabra secreta y reconstruye visualmente el
progreso en pantalla utilizando guiones y espacios, además de mostrar el contador de vidas actualizado.
Menú de interacción: Presenta un submenú de cuatro opciones donde el usuario puede elegir su siguiente
movimiento: ingresar una letra, pedir que el sistema le muestre la palabra, solicitar una palabra nueva o
salir.
Dependiendo de la opción elegida, el programa evalúa la entrada. Si se adivina una letra,
comprueba si existe en la cadena original y actualiza la lista de aciertos, si la letra es incorrecta,
se baja el contador de vidas. El bucle se rompe únicamente cuando se alcanzan las condiciones de victoria
o cuando el contador de vidas llega a cero.

Reflexión sobre el impacto de la tecnología

El desarrollo de este pequeño juego interactivo permite reflexionar sobre cómo la tecnología transforma
cualquier problema en soluciones inmediatas y eficaces. Aunque este proyecto es un juego corto,nos
demuestra como puede solucionr problemas siempre y cuando tenga una arquitectura correcta  validación de
datos del usuario de igual manera los  bucles ayudan a sostener a las aplicaciones modernas a gran escala. 
La capacidad de abstraer reglas de negocio, plasmarlas en un diagrama de flujo y traducirlas a código 
ejecutable es lo que permite a la ingeniería de software crear herramientas que procesan información de  
forma precisa y eficiente mejorando la forma en que las personas pueden interactuar con computadoras o 
maquinas y se resuelva problemas complejos.
