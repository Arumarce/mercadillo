import estilos

# Aquí deberías importar las librerías de Python que necesites

grande =  ".grande" # Aquí deberías asignar el elemento HTML de ".grande" utilizando las librerías de Python para manejo del DOM
puntos = ".punto"  # Aquí deberías asignar todos los elementos HTML de ".punto" utilizando las librerías de Python para manejo del DOM

# Cuando CLICK en punto
for i in range(len(puntos)):
    punto = puntos[i]
    punto.addEventListener('click', lambda: {
        posicion = i
        # Cuando la posición 0 transforX=0
        # Cuando la posición es 1 transformX=-50
        operacion = posicion * -50

        grande.style.transform = 'translateX({}%)'.format(operacion)

        for j in range(len(puntos)):
            cadaPunto = puntos[j]
            cadaPunto.classList.remove('activo')

        punto.classList.add('activo')
    })
