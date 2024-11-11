from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Acceder al valor del botón de radio seleccionado
    opcion = request.GET.get('opcion')
    
    # Acceder a los valores seleccionados de los checkboxes (como lista)
    preferencias = request.GET.getlist('preferencias')

    # Puedes procesar los datos, aquí simplemente los mostramos en el navegador
    response_text = f"Botón de radio seleccionado: {opcion}<br>"
    response_text += "Preferencias seleccionadas: " + ", ".join(preferencias)
    return HttpResponse(response_text)
