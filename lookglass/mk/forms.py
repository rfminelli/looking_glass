from django import forms
import re


LISTA_OPCAO = [['1', 'ip route bgp'],
               ['2', 'ping'],
               ['3', 'traceroute'],
               ['4', 'ping6'],
               ['5', 'traceroute6']]

valido_cidr = re.compile(r'^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.0/[1-2;0-4]{2}$')
valido_ipv4 = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
#valido_ipv6 = re.compile(r'^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}$')
valido_ipv6 = re.compile(r'^((([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}:[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){5}:([0-9A-Fa-f]{1,4}:)?[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){4}:([0-9A-Fa-f]{1,4}:){0,2}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){3}:([0-9A-Fa-f]{1,4}:){0,3}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){2}:([0-9A-Fa-f]{1,4}:){0,4}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|(([0-9A-Fa-f]{1,4}:){0,5}:((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|(::([0-9A-Fa-f]{1,4}:){0,5}((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|([0-9A-Fa-f]{1,4}::([0-9A-Fa-f]{1,4}:){0,5}[0-9A-Fa-f]{1,4})|(::([0-9A-Fa-f]{1,4}:){0,6}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){1,7}:))$')


class FormMK(forms.Form):
#    cidr = forms.IPAddressField(required=False)
    cidr = forms.CharField()
    opcao = forms.ChoiceField(widget=forms.RadioSelect(), choices=LISTA_OPCAO)
    
    
    
    def clean_opcao(self):
        cleaned_opcao = self.cleaned_data.get("opcao")
        cleaned_cidr = self.cleaned_data.get("cidr")
      
        if cleaned_opcao == '1':
            if not valido_cidr.match(str(cleaned_cidr)):
                raise forms.ValidationError("Prefixo incorreto, tente novamente!")
            return cleaned_opcao
        elif cleaned_opcao == '2':
            if not valido_ipv4.match(str(cleaned_cidr)):
                raise forms.ValidationError(u"Endereço IPv4 incorreto, tente novamente!")
            return cleaned_opcao
        elif cleaned_opcao == '3':
            if not valido_ipv4.match(str(cleaned_cidr)):
                raise forms.ValidationError(u"Endereço IPv4 incorreto, tente novamente!")
            return cleaned_opcao
        elif cleaned_opcao == '4':
            if not valido_ipv6.match(str(cleaned_cidr)):
                raise forms.ValidationError(u"Endereço IPv6 incorreto, tente novamente!")
            return cleaned_opcao
        elif cleaned_opcao == '5':
            if not valido_ipv6.match(str(cleaned_cidr)):
                raise forms.ValidationError(u"Endereço IPv6 incorreto, tente novamente!")
            return cleaned_opcao
	  
#    def clean_opcao(self):
#        cleaned_opcao = self.cleaned_data.get("opcao")
#        cleaned_cidr = self.cleaned_data.get("cidr")
      
#        if cleaned_opcao == '2':
#            if not valido_ipv4.match(str(cleaned_cidr)):
#                raise forms.ValidationError(u"Endereço incorreto, tente novamente!")
#            return cleaned_opcao
	  
#    def clean_opcao(self):
#        cleaned_opcao = self.cleaned_data.get("opcao")
#        cleaned_cidr = self.cleaned_data.get("cidr")
      
#        if cleaned_opcao == '3':
#            if not valido_ipv4.match(str(cleaned_cidr)):
#                raise forms.ValidationError(u"Endereço incorreto, tente novamente!")
#            return cleaned_opcao