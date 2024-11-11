from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'formularioExemplo/home.html')

def mostra(request):
    userName = request.GET.get('userName')
    password = request.GET.get('password')
    city = request.GET.get('city')
    server = request.GET.get('server')
    role = request.GET.get('role')
    mail = request.GET.get('mail')
    payroll = request.GET.get('payroll')
    selfService = request.GET.get('selfService')   
    # Use a list to check and assign the server
    options = ['Apache', 'IIS', 'Tomcat']
    opcion = options[int(server)-1]
    # Create a string with the values of the checkboxes
    signon = ""
    if mail:
        signon = signon + mail
    if payroll:
        signon = signon + " " + payroll
    if selfService:
        signon = signon + " " + selfService
    datos = {'userName':userName,
             'password':password,
             'city':city,
             'server':opcion,
             'role':role,
             'signon':signon}
    return render(request, 'formularioExemplo/mostra.html', datos)

