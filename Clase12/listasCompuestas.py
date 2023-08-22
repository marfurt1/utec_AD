#Importado de librerías
import random

#Definición de funciones
def generarEstudiante():
    
    nombres = [
        'Cecilia',
        'Aldo',
        'Ana',
        'Gustavo',
        'Mario',
        'Luis',
        'Homero',
        'Lionel',
        'Cristiano',
        'Andrea'
        ]
    
    apellidos = [
        'Escobar',
        'Simpson',
        'Maradona',
        'Valderrama',
        'Messi',
        'Nader',
        'Suárez',
        'Spiess',
        'Marfurt'
        ]
    
    dominios = [
        'utec.edu.ur',
        'uniandes.edu.co'
        ]
    
    estudiante = []
    
    #Nombre
    estudiante.append( random.choice(nombres) )
    #Apelido
    estudiante.append( random.choice(apellidos) )
    #Correo
    correo = estudiante[0].lower() + '.' + estudiante[1].lower() 
    correo = correo + '@' + random.choice(dominios)
    estudiante.append( correo )
    #Promedio programa
    promedioPrograma = random.randint(0,4) + round(random.randint(0,9)*0.10,1)
    estudiante.append(promedioPrograma)
    #Edad
    edad = random.randint(12,85)
    estudiante.append(edad)
    
    return estudiante   
    
    

def generarListadoEstudiantes():
    numeroEstudiantes = random.randint(15,40)
    listaEstudiantes = []
    
    for _ in range(numeroEstudiantes):
        estudiante = generarEstudiante()
        
        # #Salida de diagnóstico
        # print("-----------------------")
        # print(estudiante)
        # print("-----------------------")
        # input()
        
        listaEstudiantes.append(estudiante)
    
    return listaEstudiantes
    

#Representar un listado de estudiantes
#en listas computestas.
#-Atributos:
#Nombre (str) -> 0
#Apellido (str) -> 1
#Correo electrónico (str) -> 2
#Promedio programa (float)-> 3
#Edad (int)-> 4

# grupoEstudiantes = [
#     ['Luis',
#      'Escobar',
#      'l.escobarf@utec.edu.ur',
#      3.8,
#      37],
#     ['Pedro',
#      'Álvarez',
#      'pedro03@gmail.com',
#      5.0,
#      63],
#     ]

#Generación aleatoria de estudiantes (enriquecer listado compuesto)
grupoEstudiantes = generarListadoEstudiantes()




print("-------------------------------")
for i,estudiante in enumerate(grupoEstudiantes):
    print(f"{i} - {estudiante}")
print("-------------------------------")

