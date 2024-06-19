import pandas as pd
import matplotlib.pyplot as plt
from data.contaminacionsonora import generarDatosContaminacionSonora
from helpers.crearTablaHTML import crearTabla

def GeneradorDatos():
    datos = generarDatosContaminacionSonora()
    df = pd.DataFrame(datos, columns=['comuna','nombre','correo','fecha','direccion','decibeliosdiurnos','decibeliosnocturnos'])
    
    crearTabla(df, 'Contaminacion_Sonora')
    df.replace('sin', pd.NA, inplace=True)

    filtroCalidadSonoraBueno = df.query("(decibeliosdiurnos >= 10) and (decibeliosnocturnos < 20)")    
    filtroCalidadSonoraMedio = df.query("(decibeliosdiurnos >= 30) and (decibeliosnocturnos < 40)")
    filtroCalidadSonoraMalo = df.query("(decibeliosdiurnos >= 40) and (decibeliosnocturnos < 60)")

    datosOrdenadosSonido = df.groupby('comuna')['nombre'].mean()
    print(datosOrdenadosSonido)

    plt.figure(figsize=(10, 6))
    datosOrdenadosSonido.plot(kind='bar', color='green')
    plt.title('Contaminación Sonora en Comunas de Medellín')
    plt.xlabel('Decibelios Diurnos y Nocturnos')
    plt.ylabel('Promedio de Decibelios')
    plt.grid(True)
    plt.savefig('./assets/img/ContaminacionSonora.png', format='png', dpi=300)

GeneradorDatos()
