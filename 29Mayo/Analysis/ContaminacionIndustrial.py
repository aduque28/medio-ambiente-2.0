import pandas as pd 
import matplotlib.pyplot as plt
from data.generators.ContIndustrial import ContaminacionIndustrial
from helpers.crearTablaHTML import crearTabla

def contaminacionDataFrame():
    datosIndustriales = ContaminacionIndustrial()

    industriaDataframe = pd.DataFrame(datosIndustriales,columns=    ['comuna','escalacontaminacion','fecha','tipomuestra','empresa'])

    crearTabla(industriaDataframe,'Datos Industriales')

    industriaDataframe.replace('sin',pd.NA,inplace=True)
    industriaDataframe.dropna(inplace=True)

    filtroCalidadIndustrialBueno=industriaDataframe.query('(escalacontaminacion=>1)and(escalacontaminacion<10))')
    filtroCalidadIndustrialMedio=industriaDataframe.query('(escalacontaminacion=>10)and(escalacontaminacion<20))')
    filtroCalidadIndustrialMalo=industriaDataframe.query('(escalacontaminacion=>20)and(escalacontaminacion<30))')

    datosOrdenadosIndustria = industriaDataframe.groupby('comuna')['escalacontaminacion'].mean()
    
    plt.figure(figsize=(10,6))
    datosOrdenadosIndustria.plot(kind='bar',color='green')
    plt.title('Calidad de empresas por comuna')
    plt.xlabel('Comunas')
    plt.ylabel('escalacontaminacion')
    plt.grid(True)
    plt.savefig('./assets/img/calidadindustrial.png',format='png',dpi=300)

contaminacionDataFrame()