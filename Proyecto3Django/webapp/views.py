from django.shortcuts import render, redirect
from django.http import HttpResponse #Change 1
import requests

endpoint = 'http://localhost:3000{}' # el 5000 es porque Django esta corriendo en 8000 y flask en 3000 y las llaves para utilizar plantillas

# Create your views here.

def index(request): #lo primero que hace es verificar a que metodo se esta accediendo
    #Nota: recordar que siempre que se carga una página se esta cargando su metodo GET, siempre siempre
    if request.method == 'GET': 
        url = endpoint.format('/datos')  #http://localhost:3000/{} -> gracias al format -> http://localhost:3000/datos ver que las llaves se sustituyen por lo que tiene el .format
        data = requests.get(url)  # consulta a la API
        context = {
            'data': data.text, #notar que aquí podemos devolver text o un json
        }
        return render(request, 'index.html', context)
        
    elif request.method == 'POST':
        docs = request.FILES['document'] #nombre del input
        data = docs.read()
        url = endpoint.format('/datos')
        requests.post(url, data)
        return redirect('index') #Este index es el name que esta en la urls, 
                                    #porque el metodo Post por si solo no puede recargar la pagina entonces nos tenemos que rederigir a ella


def reports(request):
    if request.method == 'GET':
        date = request.GET.get('date', None) #OJO: segundo parametro indica el valor por defecto
        code = request.GET.get('code', None)

        context = {
            'date': None,
            'code': None,
        }
        if date is not None:
            context['date'] = date

        if code is not None:
            context['code'] = code
        return render(request, 'reports.html', context)


def calc(request):
    if request.method == 'GET':
        num_1 = request.GET.get('num_1', 0)
        num_2 = request.GET.get('num_2', 0)

        url = endpoint.format('/potencia')

        potencia = requests.get(url, {
            'num_1': num_1,
            'num_2': num_2,
        })

        context = {
            'potencia': potencia.text,
        }

        return render(request, 'calc.html', context)