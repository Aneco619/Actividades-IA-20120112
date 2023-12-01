# Practica 3 Introducción a la Inteligencia Artificial Introspección

### Indicaciones

* Escribir un ensayo de minimo 3 cuartillas acerca de como resolverias el siguiente problema:

Coloca ocho alfiles (cuatro negros y cuatro blancos) en un tablero de ajedrez reducido, tal como se ve en la figura.

![Imagen de ajedrez](ajedrez.png)

El problema consiste en hacer que los alfiles negros intercambien sus posiciones con los blancos, ningún alfil debe atacar en ningún momento otro del color opuesto. Se deben alternar los movimientos, primero uno blanco, luego uno negro, luego uno blanco y así sucesivamente. ¿Cuál es el mínimo número de movimientos en que se puede conseguir?


## Introduccion

El ajedrez considerado como un juego de estrategia, no solo requiere ingenio tactico sino tambien de una profunda compresion de la disposicion y movimiento de sus piezas. La disposicion inicial de los alfiles en el tablero genera un desafio interesante. Como bien sabemos el ajedrez convencional cuenta con 8 piezas o posiciones de largo mientras que en este contexto es de 4, es decir la mitad de las posiciones. Por lo que este escenario, aparentemente simple, encierra una danza estratégica que exploraremos a través de este ensayo.

## Desarrollo

En el vasto universo del ajedrez, cada disposición inicial de piezas engendra posibilidades tácticas únicas, y ninguna otra configuración despierta tanto interés estratégico como el desafío de intercambiar las posiciones de los alfiles negros y blancos sin permitir que se amenacen entre sí. Este escenario plantea un juego sutil que va más allá de la simple captura de piezas

Como primer punto representaremos los blancos con "B" y los negros con "N".
Sin hacer cambios nuestro tablero se ve asi:

| N | N | N | N |
|---|---|---|---|
| . | . | . | . |
| . | . | . | . |
| . | . | . | . |
| B | B | B | B |


En este primer movimiento el alfil blanco de la segunda columna y ultimo renglon se mueve en diagonal hacia arriba, quedando en la tercer columna y penultimo renglon lo cual queda representado de la siguiente forma:

| N | N | N | N |
|---|---|---|---|
| . | . | . | . |
| . | . | . | . |
| . | . | B | . |
| B | . | B | B |

Ahora es turno de los alfiles negros, siendo su movimiento pasar de la tercera columna y primer renglon al segundo renglon de la segunda columna 

| N | N | . | N |
|---|---|---|---|
| . | N | . | . |
| . | . | . | . |
| . | . | B | . |
| B | . | B | B |

Continuando con los blancos, el de la primera columna y ultimo renglon pasara diagonalente hacia arriba quedando su destino como ultima columna y segundo renglon

| N | N | . | N |
|---|---|---|---|
| . | N | . | B |
| . | . | . | . |
| . | . | B | . |
| . | . | B | B |

El siguiente turno de los alfiles negros sera pasar de la ultima columna y primer renglon hacia la primera columna y penultimo renglon

| N | N | . | . |
|---|---|---|---|
| . | N | . | B |
| . | . | . | . |
| N | . | B | . |
| . | . | B | B |

El alfil blanco que se encuentra en la penultima columna y ultimo renglon pasa a estar en la segunda columna y penultimo renglon 

| N | N | . | . |
|---|---|---|---|
| . | N | . | B |
| . | . | . | . |
| N | B | B | . |
| . | . | . | B |