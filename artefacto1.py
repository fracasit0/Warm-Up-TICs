#--------------------------------------------------------------

#   ____ ____ _ ____ ___ ____ _  _ ___ ____    ___  ____    ____ _  _ ____ _    ___  ____
#  |__| [__  | [__   |  |___ |\ |  |  |___    |  \ |___    [__  |  | |___ |    |  \ |  |
# |  | ___] | ___]  |  |___ | \|  |  |___    |__/ |___    ___] |__| |___ |___ |__/ |__|


# AFP:  (0) Modelo ; (1) ProVida ; (2) PlanVital ; (3) Habitat ; (4) Cuprum ; (5) Capital
# contrato: (0) Plazo indefinido ; (1) Plazo fijo ; (2) Plazo indefinido 11 anos o mas
# salud: (0) fonasa ; (1) isapre

#---------------------------------------------------------------

import os
import math
import sys

ax = 99
sueldobase = 99
AFP = 99
contrato = 99
salud = 99
planuf = 99


def titulo():
    os.system("CLS")
    print "\nBienvenido al asistente de sueldos!, creado por Agustin Carmona & Tomas Orellana"
    print "Tecnologias de informacion y comunicacion, profesor Jorge Eliott\n\n"


def datos():
    titulo()
    if AFP == 0: afpname = "Modelo"
    elif AFP == 1: afpname = "ProVida"
    elif AFP == 2: afpname = "PlanVital"
    elif AFP == 3: afpname = "Habitat"
    elif AFP == 4: afpname = "Cuprum"
    elif AFP == 5: afpname = "Capital"

    if contrato == 0: contname = "Plazo indefinido"
    elif contrato == 1: contname = "Plazo fijo"
    elif contrato == 2: contname = "Plazo 11 anos"

    if salud == 0: suelname = "fonasa"
    elif salud == 1: suelname = "isapre"

    print "Los datos Ingresados al sistema son:\n"
    print("AFP: {}".format(afpname))
    print("contrato: {}".format(contname))
    print("plan de salud: {}".format(suelname))
    if salud == 1: print("plan en UF: {}".format(planuf))
    print "\n"

#-------------------------
titulo()

print "Facilitanos la informacion solicitada a continuacion, recuerda no usar espacios, puntos, comas,"
print "ni reglones en tus respuestas. Esta informacion es necesaria para calcular tu sueldo, ademas"
print "recuerda que si te equivocas en algun dato luego podras editarlo, muchas gracias."
print "\nIngresa tu AFP:"
print "(0) Modelo ; (1) ProVida ; (2) PlanVital ; (3) Habitat ; (4) Cuprum ; (5) Capital"
AFP = int(raw_input("[1] AFP: "))
while(AFP > 5 or AFP < 0):
    AFP = int(raw_input("AFP invalida: "))
print "\nIngresa tu tipo de contrato:"
print "(0) Plazo indefinido ; (1) Plazo fijo ; (2) Plazo indefinido 11 anos o mas"
contrato = int(raw_input("[2] contrato: "))
while(contrato > 2 or contrato < 0):
    contrato = int(raw_input("contrato invalido: "))
print "\nIngresa tu plan de salud:"
print "(0) fonasa ; (1) isapre"
salud = int(raw_input("[3] salud: "))
while(salud > 1 or salud < 0):
    salud = int(raw_input("salud invalido: "))
if salud == 1:
    planuf = int(raw_input("Ingresa plan en UF: "))

while ax != 0:
    datos()
    print "Si deseas modificar alguna informacion anterior, utiliza las siguientes opciones:"
    print "[1] AFP ; [2] tipo de contrato ; [3] plan de salud ; [0] continuar"
    ax = int(raw_input(">>: "))
    if ax == 1:
        print "\nIngresa tu AFP:"
        print "(0) Modelo ; (1) ProVida ; (2) PlanVital ; (3) Habitat ; (4) Cuprum ; (5) Capital"
        AFP = int(raw_input("[1] AFP: "))
        while(AFP > 5 or AFP < 0):
            AFP = int(raw_input("AFP invalida: "))
    if ax == 2:
        print "\nIngresa tu tipo de contrato:"
        print "(0) Plazo indefinido ; (1) Plazo fijo ; (2) Plazo indefinido 11 anos o mas"
        contrato = int(raw_input("[2] contrato: "))
        while(contrato > 2 or contrato < 0):
            contrato = int(raw_input("contrato invalido: "))
    if ax == 3:
        print "\nIngresa tu plan de salud:"
        print "(0) fonasa ; (1) isapre"
        salud = int(raw_input("[3] salud: "))
        while(salud > 1 or salud < 0):
            salud = int(raw_input("salud invalido: "))
        if salud == 1:
            planuf = int(raw_input("Ingresa plan en UF: "))

datos()
print "Muy bien, ya tenemos la informacion necesaria para el calculo, ahora porfavor"
print "eliga la opcion que desea calcular:"
print "[1] Calcular sueldo Liquido ; [2] Calcular sueldo bruto"
while ax < 1 or ax > 2:
    ax = int(raw_input(">>: "))
