# select_rois
Programa que ayuda a seleccionar regiones de interés (ROIS) en un directorio
de imágenes y almacena sus posiciones en un fichero csv
## Instrucciones
### Instalación
- Descargar programa de: https://github.com/ftornay/select_rois
- Instalar python3: https://www.python.org/downloads/
- Nota: la instalación requiere el paquete setuptools:
    Si no se instala automáticamente con python, descargar de
    https://pypi.org/project/setuptools/
- Entrar en el directorio descargado: "select_rois"
- Ejecutar python setup install
### Uso
- Entrar en el directorio select_rois
- Para iniciar el programa ejecutar:
    > python select_rois/select_rois.pyw
- En Windows puede usarse en vez de eso (no saca ventana de terminal):
    > pythonw select_rois/select_rois.pyw
- La aplicación pide primero elegir un directorio con imágenes térmicas
- Y después, rellenar información sobre el vídeo:
    Si es de alguien diciendo la verdad o mintiendo (o no se sabe)
    Qué procedimiento experimental se usó: estrés, ecológico u otro
- Después va presentando cada imagen (fotograma) del directorio en una ventana
- Cada región de interés corresponde con una tecla.
    Tras pulsar la tecla aparece el nombre de la región en la parte inferior de la ventana y se puede elegir dónde está esa región con ayuda del ratón
- Puede volverse a cualquier región ya elegida volviendo a pulsar la tecla correspondiente. El programa muestra las regiones ya elegidas con puntos azules y
la región actual con puntos rojos.
- Las teclas para cada región son las siguientes
(las minúsculas indican el lado derecho y las mayúsculas el izquierdo)
    - z: nariz
    - n: fosa nasal derecha
    - N: fosa nasal izquierda
    - d: dedo derecho (indicar punta del dedo medio)
    - D: dedo izquierdo (indicar punta del dedo medio)
    - j: ojo derecho
    - J: ojo izquierdo
    - b: lado derecho de la boca (comisura)
    - B: lado izquierdo de la boca (comisura)
    - m: mejilla derecha
    - M: mejilla izquierda
    - r: lado derecho de la frente (marcar el centro de la mitad derecha)
    - R: lado izquierdo de la frente (marcar el centro de la mitad izquierda)
- Si se pulsa la tecla _h_ aparece una ventana de ayuda con todas las teclas
- Pulsando ENTER se graban los datos de la imagen actual y se pasa a la siguiente. El nombre de la imagen aparece en la parte superior de la misma.
- Para salir, cerrar la ventana de la aplicación. También se termina automáticamente cuando se graban los datos de la última imagen.
- Cuando el program comienza comprueba si existen datos ya grabados y solo presenta las imágenes que falta por etiquetar
- Los datos se graban en un fichero con el mismo nombre del directorio y la extensión _csv_

