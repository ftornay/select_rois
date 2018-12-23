# select_rois
Programa que ayuda a seleccionar regiones de interés (ROIS) de un directorio
de matrices o de un archivo SEQ y almacena sus posiciones en un fichero csv
## Instrucciones
### Requisitos
- Instalar python3: https://www.python.org/downloads/
- Nota: la instalación requiere el paquete setuptools:
    Si no se instala automáticamente con python, descargar de
    https://pypi.org/project/setuptools/
- Nota: para etiquetar ficheros SEQ es necesario instalar exiftool:
    - Descargar de https://www.sno.phy.queensu.ca/~phil/exiftool/
    - En linux, poner en path
    - En Windows, copiar a C:\Windows\exiftool.exe
### Instalación del programa
- El programa se descarga de: https://github.com/ftornay/select_rois
- Entrar en el directorio descargado: "select_rois"
- Ejecutar python setup install
- Nota: En vez de eso, en Windows puede ejecutarse el script install_select_rois.bat para instalar el programa.
    - El script asume que existe el lanzador C:\Windows\py.exe
### Uso
#### Para etiquetar ficheros mat
- Entrar en el directorio select_rois
- Para iniciar el programa ejecutar:
    > python select_rois/select_rois.pyw
- En Windows puede usarse en vez de eso (no saca ventana de terminal):
    > pythonw select_rois/select_rois.pyw
- La aplicación pide primero elegir un directorio con imágenes térmicas
#### Para etiquetar un fichero SEQ
- Entrar en el directorio select_rois
- Para iniciar el programa ejecutar:
    > python select_rois/rois_from_seq.pyw
- En Windows puede usarse en vez de eso (no saca ventana de terminal):
    > pythonw select_rois/rois_from_seq.pyw
- La aplicación pide primero elegir un fichero SEQ
#### Para las dos posibilidades
- Después de elegir la ruta, rellenar información sobre el vídeo:
    Si es de alguien diciendo la verdad o mintiendo (o no se sabe)
    Qué procedimiento experimental se usó: estrés, ecológico u otro
- Después el programa va presentando cada imagen (fotograma)
- Cada región de interés corresponde con una tecla.
    Tras pulsar la tecla aparece el nombre de la región en la parte inferior de la ventana y se puede elegir dónde está esa región con ayuda del ratón
- Puede volverse a cualquier región ya elegida volviendo a pulsar la tecla correspondiente. El programa muestra las regiones ya elegidas con puntos azules y
la región actual con puntos rojos.
- Las teclas para cada región son las siguientes
(las minúsculas indican el lado izquierdo y las mayúsculas el derecho)
(el lado izquierdo y derecho son con respecto a la imagen)
    - z: nariz
    - n: fosa nasal izquierda (marcar debajo de la fosa, no sobre ella)
    - N: fosa nasal derecha (marcar debajo de la fosa, no sobre ella)
    - d: dedo izquierdo (indicar punta del dedo medio)
    - D: dedo derecho (indicar punta del dedo medio)
    - j: ojo izquierdo (marcar la pupila)
    - J: ojo derecho (marcar la pupila)
    - b: lado izquierdo de la boca (comisura)
    - B: lado derecho de la boca (comisura)
    - m: mejilla izquierda (marcar a la altura de la nariz y por debajo de la esquina externa del ojo)
    - M: mejilla derecha (marcar a la altura de la nariz y por debajo de la esquina externa del ojo)
    - r: lado izquierdo de la frente (por encima de la esquina interna del ojo izquierdo, a la altura de la mitad de la frente o un poco por debajo)
    - R: lado derecho de la frente (por encima de la esquina interna del ojo derecho, a la altura de la mitad de la frente o un poco por debajo)
- Ejemplo de imagen etiquetada:
![ejemplo](https://raw.githubusercontent.com/ftornay/select_rois/master/imagen_marcada.png)
- Si se pulsa la tecla _h_ aparece una ventana de ayuda con todas las teclas
- Pulsando ENTER se graban los datos de la imagen actual y se pasa a la siguiente. El nombre de la imagen aparece en la parte superior de la misma.
- Para salir, cerrar la ventana de la aplicación. También se termina automáticamente cuando se graban los datos de la última imagen.
- Cuando el program comienza comprueba si existen datos ya grabados y solo presenta las imágenes que falta por etiquetar
- Los datos se graban en un fichero con el mismo nombre del directorio o del archivo SEQ y la extensión _csv_

