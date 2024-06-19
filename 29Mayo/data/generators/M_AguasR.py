import random
  
def medicionAguasResiduales():
    listaDatos=[]
    for i in range (1000):
        nombre = random.choice(['Belén', 'Laureles', 'El Poblado', 'Envigado', 'Robledo', 'La Candelaria', 'Manrique', 'Buenos Aires', 'San Javier', 'Aranjuez'])
        comuna = random.randint(1,14)
        direccion = random.choice(['Calle 10 #45-67, Medellín, Antioquia','Carrera 15 #23-45, Medellín, Antioquia','Avenida 7 #12-34, Medellín, Antioquia','Carrera 4 #12-56, Medellín, Antioquia'])
        tipodefuente = random.choice(['Río', 'Lago', 'Arroyo', 'Embalse', 'Estanque'])
        composicionquimica=random.choice(['Contaminación por aguas residuales domésticas', 'Contaminación por aguas residuales industriales', 'Contaminación por vertidos de petróleo', 'Contaminación por metales pesados', 'Contaminación por pesticidas y herbicidas', 'Contaminación por residuos sólidos', 'Contaminación por productos químicos tóxicos', 'Contaminación por microplásticos', 'Contaminación por nutrientes (eutrofización)', 'Contaminación por organismos patógenos'])
        medicion=[nombre,direccion,tipodefuente,composicionquimica]

        listaDatos.append(medicion)
    return listaDatos

