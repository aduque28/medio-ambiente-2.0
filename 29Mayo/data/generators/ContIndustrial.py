import random

def ContaminacionIndustrial ():
    contaminacion = []
    for i in range(100):
        comuna = random.randint(1,14)
        escalacontaminacion=random.randint(1,30)
        empresa = random.choice(['Grupo Éxito', 'Bancolombia', 'Ecopetrol', 'Grupo Sura', 'Avianca'])
        fecha=random.choice(['2024-05-15','2024-05-16','sin'])
        tipomuestra=random.choice(['Aire','Fuentes hidricas','Muestra de Hojas','Muestra Suelo',])
        encuesta=[empresa,comuna,fecha,correo,tipomuestra]
        contaminacion.append(encuesta)
        return contaminacion
    
