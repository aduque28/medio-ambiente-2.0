import random

def generarDatosCalidadAire():
    
    listaDatos=[]
    for i in range(1000):
        nombre=random.choice(['Camila P','Luciana M','Marthe D','Jose B','Karen F'])
        comuna = random.randint(1,14)
        ica=random.randint(10,80)
        fecha=random.choice(['2024-05-15','2024-05-16','sin'])
        correo=random.choice(['notiene@correo.com','notiene1@correo.com','notiene2@correo.com','notiene3@correo.com'])
        encuesta=[nombre,comuna,ica,fecha,correo]

        listaDatos.append(encuesta)
    return listaDatos

