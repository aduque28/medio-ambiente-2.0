import pandas as pd
import matplotlib.pyplot as plt 
from data.generators.generadorAire import  generarDatosCalidadAire
#se utliza crear tabla para generar una tabla y en el archivo rear tablahtml se jala 
from helpers.crearTablaHTML import crearTabla

def construirAireDataFrame():
    datosAire = generarDatosCalidadAire()  # Agregué paréntesis aquí

    aireDataFrame = pd.DataFrame(datosAire, columns=['nombre', 'comuna', 'ica', 'fecha', 'correo'])

    #Generamos el recurso HTML
    crearTabla(aireDataFrame,'Datos Aire')
    #limpiando el dataframe
    #remplazando valores 
    aireDataFrame.replace('sin',pd.NA,inplace=True)
    #Elimino los registros que no cumplen el criterio 
    aireDataFrame.dropna(inplace=True)
    

    #Filtrar para que nos permita analizar datos de DF 
    
    filtroCalidadAireBueno=aireDataFrame.query("(ica>=10)and(ica<20)")
    filtroCalidadAireMedio=aireDataFrame.query("(ica>=40)and(ica<50)")
    filtroCalidadAireMalo=aireDataFrame.query("(ica>=50)and(ica<80)")
 

    #ORDENENANDO LOS DATOS PARA GRAFICARLOS 
    datosOrdenadosDeAire =aireDataFrame.groupby('comuna')['ica'].mean()
    print(datosOrdenadosDeAire)

    #GRAFICO LA INFORMACION 
    plt.figure(figsize=(10,6))
    datosOrdenadosDeAire.plot(kind='bar',color='green')
    plt.title('Calidad del Aire en Comunas por medellin')
    plt.xlabel('Comunas')
    plt.ylabel('ica')
    plt.grid(True)
    plt.savefig('./assets/img/calidadaire.png',format='png',dpi=300)


construirAireDataFrame()