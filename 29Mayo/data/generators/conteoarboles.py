import random

def ContadordeArboles():
    listaDatos = []
    for i in range(1000):
        nombre = random.choice(['Camila P', 'Luciana M', 'Marthe D', 'Jose B', 'Karen F'])
        corregimiento = random.randint(1, 14)
        correo = random.choice(['notiene@correo.com', 'notiene1@correo.com', 'notiene2@correo.com', 'notiene3@correo.com'])
        fecha = random.choice(['2024-05-sin', '2024-05-16', '2024-05-17','sin'])
        hectareas_sembradas = random.randint(0, 120)
        especie_sembrada = random.choice(['Pino', 'Roble', 'Cedro', 'Arce', 'Palma'])
        encuesta = [nombre, corregimiento, correo, fecha, hectareas_sembradas, especie_sembrada]
        listaDatos.append(encuesta)
    return listaDatos
