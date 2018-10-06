# Inteligencia Aritifial - BMF

## Introducción
Implementación de agentes inteligentes haciendo ahora la búsqueda de una casa en común para todos ellos, simulando una BMF ( Búsqueda en el mundo fantasia ), donde se coloca un casa en algún punto del mapa y un origen de donde se haya un entrenamiento para todos los agentes de este mundo, donde cada uno de ellos consta de habilidades diferentes para desplazarse por el mapa, el entrenamiento se realizara por medio de recorridos aleatorios sobre el mapa donde se castigara y premiara a las rutas escogidas dependiendo de si su diferencia es positiva o negativa con la media de resultados previos obtenidos.
## Desarrollo e implementación
La actividad fue realizada en Python con Processing
Que básicamente es un lienzo en el que tiene que dibujar absolutamente todo, incluso botones.
Para esta actividad se agrego la posibilidad de agregar entre 0 - 100 % de obstáculos disponibles en el campo, menos 2 que son el origen y el destino.
Los obstáculos son de 4 tipos:
- Muros
- Agua
- Montañas
- Fosas  

Se hace uso de un entrenamiento de hasta 10000 repeticiones aleatorias sobre el mapa donde se califican rutas encontradas hacia la casa, donde después con un algoritmo greedy, programación dinámica o de recorridos mínimos en grafos, se debe encontrar el camino a la casa a partir de los valores previamente encontrados en el entrenamiento

<img width="604" alt="captura de pantalla 2018-10-06 a la s 0 00 14" src="https://user-images.githubusercontent.com/28017456/46567581-c8244700-c8fa-11e8-9631-82556ba2543c.png">


## Diagrama de Funciones
<img width="661" alt="captura de pantalla 2018-10-06 a la s 0 01 26" src="https://user-images.githubusercontent.com/28017456/46567585-dd997100-c8fa-11e8-949d-1dbd495436e7.png">

La inicialización formal de todos las variables se realiza dentro del setup

Todo el funcionamiento de processing se basa en el siguiente paso: el draw
Que itera sin parar repitiendo una y otra vez todo lo que este dentro de el, de esta manera pueden hacerse animaciones y dibujos dentro del lienzo.
Nada puede forzar ni alterar de ninguna manera una iteración del draw, asi que hace falta organización para poder lograr la visualización paso a paso. 

Dentro del draw se llaman únicamente dos funciones: entrenamiento e interface

El entrenamiento se llama por el draw, pero únicamente cuando una bandera es actividad al presionar el boton, entonces, comienza a funcionar el entrenamiento paso a paso y dependiendo de otra bandera de dibujo, es si se plasmara o no en el lienzo, cosa que también afecta a los delay y entonces al tiempo total que le tomara terminar el entrenamiento

``` Python
def training():
    global posm, qm, posp, qp, posl, ql,played,time
    inix=0
    iniy=0
    endx=0
    endy=0
    for i in range(sz):
        for j in range(sz):
            if grid[i][j]==1:
                inix=i
                iniy=j
            if grid[i][j]==9:
                endx=i
                endy=j

    lucas.restart()
    ql=[]
    for i in range(100):
        lucas.active=True
        ql+=lucas.train(inix,iniy,0,i)
        lucas.vis=[ [False]*sz for _ in range (sz) ]
    print "LUCAS"
    print ' '
    for i in lucas.pon:
        print i
    posl=0
```

Esta actividad esta basada en una matriz de nxn que se declara al inicio de la ejecución y todo alrededor de esta esta armado a “escala”, permitiendo así poder aumentar o disminuir el tamaño de la matriz sin ningún problema y manteniendo la funcionalidad.

La matriz puede contener alguno de los siguientes valores:
``` Python
#0: backgImg,
#1: originImg,
#2: wallImg,
#3: waterImg,
#4: ravineImg,
#5: mountainImg,
#6: lucasImg,
#7: momboImg,
#8: piroloImg,
#9: houseImg
```

De esta manera, dentro de las funciones donde se toman decisiones sobre el recorrido, únicamente es necesario alterar el valor de la matriz y la función update se encargara de redibujar todo en base a las reglas anteriores

Por ultimo se utilizaron 2 funciones que operan de manera independiente al draw:
mousePressed y mouseDragged que actúan en función a indicaciones recibidas por medio del mouse, que estas a su vez manejan las funciones putObstacles y lever, que van directamente relacionadas la una a la otra.

Levers son las barras disponibles para que el usuario pueda modificar el porcentaje de obstaculos con solo deslizar el mouse, esta llama a putObstacles cada vez que sus valores son alterados y se dibujan elementos de manera aleatoria sobre el campo.


Link del Video:
https://www.youtube.com/watch?v=v8GgOgVuNdc


