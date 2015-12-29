from django import forms

LISTA_OPCAO = (('ip', 'IP'),
               ('bgp_route', 'BGP Route'))

class FormMK(forms.Form):
    cidr = forms.IPAddressField(accept_cidr=True)
    ping = forms.IPAddressField()
    traceroute = forms.IPAddressField()
    ping6 = forms.GenericIPAddressField()
    traceroute6 = forms.GenericIPAddressField()
    opcao = forms.CharField(widget=forms.RadioSelect(choices=LISTA_OPCAO))
    
    