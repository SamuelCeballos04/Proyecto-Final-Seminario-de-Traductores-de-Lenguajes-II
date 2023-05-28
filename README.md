# Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II

Hecho por Samuel Ceballos Murguia para la clase de Seminario-de-Traductores-de-Lenguajes-II, con el profesor Michel Emanuel López Franco, sección D02.

Este proyecto decidí enfocarlo a una parte que me llama mucho la atención que es el manejo, análisis y/o transformación de los datos. Lo dividí en dos partes que me interesaron aprender, la primera parte fue la transformación y análisis de los datos de un archivo Excel sobre información de casos, fechas de infección, países, fechas y muertes por la enfermedad Covid19, haciendo uso de una librería en Python conocida como Pandas. La segunda parte fue el uso de una herramienta conocida como Power BI, en la cual se pueden generar reportes en base a ciertos DataFrames de información contenidos ya sea en un archivo de Excel, en un archivo SQL o importados de algún servidor de bases de datos.

# Primera parte

Comencé creando una interfaz visual para la manipulación de los datos en PyQT5, la idea es que a través de esta interfaz, el usuario pudiese seleccionar el tipo de datos con los que quiere trabajar después, realizando un filtro con Pandas en el cual podía extraer los datos de acuerdo a número de casos, de muertes, países o continentes expecíficos. El objetivo de realizar esta interfaz fue lograr una primera limpieza, filtrado y transformación de los datos.
La interfaz se ve algo así: 
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/interfaz.png)

Poniendo a prueba esta interfaz, generamos un archivo con determinadas condiciones: 
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/generacion.png)

Estos son archivos que ya he generado anteriormente
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/archivos%20generados.png)

Y así es como se ve un DataFrame creado
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/dataframe%20generado.png)

Una vez que determinado archivo ha sido creado, programé una Página web en la cual los usuarios pueden acceder para descargar los archivos que han creado previamente, esa Página web se ve de la siguiente manera: 
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/pagina%20web.png)

Al situarnos encima del nombre de un archivo y hacer clic, este archivo se descarga, tal y como se observa en la siguiente imagen: 
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/descarga.png)

# Segunda parte

La segunda parte de este proyecto consistió en utilizar el DataFrame del COVID para realizar el reporte en Power BI. La primera página de este reporte es un vistazo general de los datos, en el cual se muestra los sitios geográficos de los cuales se sacarán los datos y también una sumatoria de muertes y casos de infección de esta enfermedad: 
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/pag1.png)

La segunda página muestra otro mapa en donde se agrupan el número de muertes por cada territorio geográfico: 
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/pag2.png)
La visualización de los datos me permite generar una hipótesis: América es el territorio con más muertes.

Eso se busca probar en las siguientes páginas: 
Aquí se observa la cantidad total de casos por territorio en una gráfica de barras:
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/pag4.png)

Y en esta otra página se muestra cuáles son los países que presentan más muertes alrededor del mundo: 
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/pag3.png)

Habiendo probado que América es el territorio geográfico con mayor número de muertes respecto al número de casos, me dispuse a seleccionar los países más importantes de este territorio y observar la correlación entre sus casos y sus muertes, tal y como muestre el informe en la parte superior de esta página. El reporte en la parte inferior de la misma muestra cómo el número de muertes fue cambiando de acuerdo a la manera en la que avanzaba el tiempo:
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/pag5.png)

Al observar el gráfico de dispersión noté que todos seguían un comportamiento donde claramente existía una correlación, sin embargo, en el caso de México, existía una clara inclinación hacia el número de muertes respecto a la cantidad de casos totales, lo que planteaba la última hipótesis; la tasa de muertes en México durante el 2020 fue altísima.

Esto se comprobó en la última página de este reporte, donde se plasma de un color los casos que existieron en cada país importante del continente americano y de otro color el número de muertes que hubo respecto a dichos casos, notándose que en el caso de México, es altísimo el número de muertes respecto al número de casos, cosa que quedó evidenciada con las pequeñas tarjetas de información que coloqué en la parte superior, donde podemos comprobar que en México la tasa de mortandad de dicha enfermedad fue de casi el 10%, mientras que en Estados Unidos, uno de los países con más contagios, la tasa fue infinitamente inferior:
![My image](/Proyecto-Final-Seminario-de-Traductores-de-Lenguajes-II/images/pag6.png)
