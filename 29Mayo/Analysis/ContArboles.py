import pandas as pd
import matplotlib.pyplot as plt
from data.generators.conteoarboles import ContadordeArboles
from helpers.crearTablaHTML import crearTabla

def contruirDataArbol():
    DataArbol = ContadordeArboles()

    RecolectorDato = pd.DataFrame(DataArbol, columns=['nombre', 'corregimiento', 'correo', 'fecha', 'hectareas_sembradas', 'especie_sembrada'])
    
    crearTabla(RecolectorDato, 'Data_Arboles')
    print(RecolectorDato)
    
    RecolectorDato.replace('sin', pd.NA, inplace=True)
    # Elimino los registros que no cumplen con el criterio
    RecolectorDato.dropna(inplace=True)
    print(RecolectorDato)

    # Filtros
    filtroHectareas = RecolectorDato.query("hectareas_sembradas > 10")
    filtroEspecie = RecolectorDato[RecolectorDato['especie_sembrada'] == 'pino']

    # Operaciones adicionales si lo deseas
    promedioHectareas = RecolectorDato['hectareas_sembradas'].mean()
    especiesUnicas = RecolectorDato['especie_sembrada'].unique()

    # Puedes realizar más operaciones con los datos aquí si lo deseas

    # Ejemplo de gráfico
    plt.figure(figsize=(10, 10))
    plt.hist(RecolectorDato['hectareas_sembradas'], bins=20, color='blue')
    plt.title('Distribución de Hectáreas Sembradas')
    plt.xlabel('Hectáreas')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.savefig('./assets/img/distribucion_hectareas.png', format='png', dpi=300)

contruirDataArbol()
