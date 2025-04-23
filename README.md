El objetivo de esta actividad es aplicar los conceptos de programación concurrente 
para implementar un programa que simule una carrera de caballos, donde cuatro caballos (representados por hilos) 
avanzan aleatoriamente en una carrera y el primero en llegar al 100% es el ganador.
La actualización de cada caballo se refleja en una barra de progreso que avanza conforme al progreso de cada uno. 
El programa cuenta con una interfaz gráfica creada con la biblioteca `tkinter`, que incluye cuatro barras de progreso, 
cada una representando a un caballo. Al pulsar el botón "Iniciar Carrera", se comienzan a ejecutar los hilos,
los cuales avanzan aleatoriamente, y el primero que llegue al 100% será el ganador. 
