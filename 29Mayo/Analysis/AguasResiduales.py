import pandas as pd
import matplotlib.pyplot as plt 
from data.generators.M_AguasR import medicionAguasResiduales
from helpers.crearTablaHTML import crearTabla

def ConstruDataAgua():
    dataAgua = medicionAguasResiduales()
    AguasResiduales = pd.DataFrame(dataAgua, columns=['nombre','comuna','direccion','tipodefuente','composicionquimica'])
    crearTabla(AguasResiduales, 'Aguas_Residuales')    
    AguasResiduales.replace('sin',pd.NA,inplace=True)
    AguasResiduales.dropna(inplace=True)


    FiltroCalidadAguasResiduales=AguasResiduales.query('tipodefuente'=='composicionquimica')

    datosOrdenadosAguasResiduales = AguasResiduales.groupby['nombre']('comuna').mean()
    

    plt.figure(figsize=(10,6))
    datosOrdenadosAguasResiduales.plot(kind='bar',color='green')
    plt.title('Calidad del Aire en Comunas por medellin')
    plt.xlabel('tipodefuente')
    plt.ylabel('composicionquimica')
    plt.grid(True)
    plt.savefig('./assets/img/calidadagua.png',format='png',dpi=300)


ConstruDataAgua()