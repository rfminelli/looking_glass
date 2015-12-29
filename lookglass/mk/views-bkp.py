from django.shortcuts import render, render_to_response
from paramiko import SSHClient, AutoAddPolicy
import time

def index(request):
    return render(request, "index.html")


def obtem(request):

    lista_tudo = []
    
# host
    host = ("192.168.155.19")
# username
    user = ("admin")
# userpassword
    password = (" ")

    sshCli = SSHClient()
    sshCli.set_missing_host_key_policy(AutoAddPolicy())

    pega_param = request.GET.get('')

    ListaIPs = "ip route print detail where dst-address in 10.10.0.0/20"

    sshCli.connect(str(host), port=22, username=str(user), password=str(password))
    stdin, stdout, stderr = sshCli.exec_command(ListaIPs)
    
    line = enumerate(stdout)
#    for i, line in enumerate(stdout):
#        line = line.rstrip()
        #print("%s" % (line))
        
        #break    
#    return render(request, 'saida.html', {'line': line})
    return render_to_response('saida.html', {'line': line})


#        if i > 50:
#            break

#    print(i, line)


 
    time.sleep(1)
    sshCli.close()
    
    
