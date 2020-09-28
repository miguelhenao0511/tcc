from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def formulario(request):
    return render(request, "principal.html")

def inicio(request):
    return render(request, "miplantilla.html")

def lecturaDatos(request):

    if request.method == "POST":
        shop = request.POST['shop']
        email = request.POST['email']
        xml_file = request.FILES['xml_file'].read()
        
        return render(request, "gracias.html", {'shop': shop, 'email': email, 'xml_file': xml_file})

    else:
        # render(request, "miplantilla.html")
        mensaje = 'no funciona'
        return HttpResponse(mensaje)
    

def saludo(request): #primera vista
    creator = Persona("Felipe", "Villarreal")

    #doc_externo = open("C:/Users/Usuario/Desktop/Tecoco/PROJECT/PROJECT/plantillas/miplantilla.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = loader.get_template('miplantilla.html')

    #ctx = Context({"nombre_persona": creator.nombre, "apellido_persona": creator.apellido})

    #documento = doc_externo.render({"nombre_persona": creator.nombre, "apellido_persona": creator.apellido})

    return render(request, "miplantilla.html", {"nombre_persona": creator.nombre, "apellido_persona": creator.apellido}) 

def despedida(request):

    return HttpResponse("Chao gonorreas")

def fecha(request):
    fecha_atual = datetime.datetime.now()
    documento= """
    <html>
        <body>
            <h1>
            Fecha y hora actuales %s
            </h1>
        </body>
    </html>
    """ % fecha_atual

    return HttpResponse(documento)

def calculaEdad(request, edad,  year):
    #edadActual = 22
    periodo = year - 2020
    edadFutura = edad + periodo

    documento = """
    <html>
        <body>
        <h2>
        En el año %s tendrás %s años
        </h2>
        </body>
    </html>
    """ %(year, edadFutura)

    return HttpResponse(documento)