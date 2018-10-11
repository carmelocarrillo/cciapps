from django.shortcuts import render
from django.http import HttpResponse
from cciapps.forms import ContactForm
import MySQLdb


def index(request):
    return HttpResponse("Hola")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            aplicacion = form.clean_data['aplicacion']
            mes = form.clean_data['mes']
            fecha = form.clean_data['fecha']
            sender = form.clean_data.get('sender', 'noreply@example.com')
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'cciapps/contact.html', {'form': form})

def productividad(request):
    db = MySQLdb.connect(host='localhost', user='cciappsuser', passwd='ks928la7&5%a', db='producxe')
    cursor = db.cursor()
    sql = "SELECT * FROM articulos"
    cursor.execute(sql)
    filas = cursor.fetchall()
#    for registro in filas:
#        print(registro[0], ' ', registro[1])
    return render(request, 'cciapps/productividad.html', {'filas': filas})
