from django import forms
 
APPS = (
    ('productividad', 'Productividad por empleado'),
    ('escandallo', 'Informe de escandallo de artículo'),
    ('extraerdesglose', 'Extraer desglose de componentes de escandallo presentes en pedidos de venta'),
    ('ordenarlineas', 'Ordenar líneas de pedido por art&iacute;culo'),
)

MESES = (
    ('1', 'Enero'),
    ('2', 'Febrero'),
    ('3', 'Marzo'),
    ('4', 'Abril'),
    ('5', 'Mayo'),
    ('6', 'Junio'),
    ('7', 'Julio'),
    ('8', 'Agosto'),
    ('9', 'Septiembre'),
    ('10', 'Octubre'),
    ('11', 'Noviembre'),
    ('12', 'Diciembre'),
)

class ContactForm(forms.Form):
    aplicacion = forms.ChoiceField(choices = APPS)
    mes = forms.ChoiceField(choices = MESES)
#    mes = forms.CharField()
    fecha = forms.DateTimeField()
    sender = forms.EmailField(widget=forms.Textarea(), initial="Replace with your feedback", required=False)
