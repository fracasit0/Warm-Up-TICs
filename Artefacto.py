import os
import math
import sys

#Iniciamos variables en 99 para evitar conflictos

version = "1.1v"
ax = 99
sueldobase = 99
AFP = 99
AFPdcto = 0
contrato = 99
contratodcto = 0
salud = 99
saludcto = 0
planuf = 99

#Funciones: titulo() - datos() - calculiq() - calcubrut() - bruto() - liquido()

def titulo():
    #Funcion que es el "banner" del programa
    os.system("CLS")
    print ("\nBienvenido al asistente de sueldos!, creado por Agustin Carmona & Tomas Orellana")
    print ("Tecnologias de informacion y comunicacion, profesor Jorge Eliott")
    print ("Version: {}\n\n".format(version))


def datos():
    #Funcion que presenta los datos ingresados al iniciar el programa
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


    print ("Los datos Ingresados al sistema son:\n")
    print("AFP: {}".format(afpname))
    print("contrato: {}".format(contname))
    print("plan de salud: {}".format(suelname))
    if salud == 1: print("plan en UF: {}".format(planuf))
    print ("\n")

def opcion():
    print ("Porfavor eligir la opcion para continuar:")
    print ("[1] Calcular sueldo Liquido ; [2] Calcular sueldo bruto ; [3] Atras")
    ax = int(input(">>: "))

    if ax == 1:
        liquido()
    elif ax == 2:
        bruto()
    elif ax == 3:
        print ("back")

def bruto():
    titulo()
    print ("IMPORTANTE: La calculadora solo considera casos normales chilenos de 12 sueldos anuales,")
    print ("es decir, sin bonos, items no imponibles, beneficios, descuentos y otras variables voluntarias.")
    print ("Ingrese a continuacion su sueldo liquido a trabajar; sin comas, puntos ni guiones:")
    sueldo = int(input(">>: "))

    if salud == 1:
        sueldo = sueldo+planuf

    if sueldo >= 4831038:
        f=0.35
        k=1117494
    elif sueldo < 4831037 and sueldo >= 3835459:
        f=0.304
        k=852976
    elif sueldo < 3835458 and sueldo >= 3101172:
        f=0.23
        k=533828
    elif sueldo < 3101171 and sueldo >= 2276290:
        f=0.135
        k=215160
    elif sueldo < 2276289 and sueldo >= 1398960:
        f=0.08
        k=83380
    elif sueldo < 1398959 and sueldo >= 643693:
        f=0.04
        k=25747
    elif sueldo < 643693:
        f=0
        k=0

    if AFP == 0: #Modelo 10,77%
        AFPdcto = 0.1077
    elif AFP == 1: #ProVida 11,45%
        AFPdcto = 0.1145
    elif AFP == 2: #Plan Vital 10,41%
        AFPdcto = 0.1041
    elif AFP == 3: #Habitat 11,27%
        AFPdcto = 0.1127
    elif AFP == 4: #Cuprum 11,44%
        AFPdcto = 0.1144
    elif AFP == 5: #Capital 11,44%
        AFPdcto = 0.1144

    saludcto = 0.07

    if contrato == 0: #plazo indefinido
        contratodcto = 0.024
    elif contrato == 1: #plazo fijo
        contratodcto = 0.03
    elif contrato == 2: #plazo 11 meses o mas
        contratodcto = 0.008

    bruto = (sueldo-k)/((1.0-AFPdcto-saludcto-contratodcto)*(1.0-f))


    titulo()
    print ("El resultado del calculo es:\n")
    print("sueldo liquido: {}".format(sueldo))
    print("descuento AFP: {}".format(bruto*AFPdcto))
    if salud == 0:
        print("descuento salud: {}".format(bruto*saludcto))
    elif salud == 1:
        print("descuento salud: {}".format(bruto*saludcto+planuf))
    print("seguro de cesantia: {}".format(bruto*contratodcto))
    print("impuestos: {}\n".format(bruto*(1.0-f)))
    print("***Sueldo bruto: {}".format(bruto))
    print ("\n")
    opcion()


def liquido():
    titulo()
    print ("IMPORTANTE: La calculadora solo considera casos normales chilenos de 12 sueldos anuales,")
    print ("es decir, sin bonos, items no imponibles, beneficios, descuentos y otras variables voluntarias.")
    print ("Porfavor considerar esto al calcular su sueldo liquido.\n")
    print ("Ingrese a continuacion su sueldo base o BRUTO; sin comas, puntos ni guiones:")
    sueldoimponible = int(input(">>: "))

    #Aqui solo ocupamos las formulas para el calculo del sueldo liquido

    if AFP == 0: #Modelo 10,77%
        AFPdcto = sueldoimponible*0.1077
    elif AFP == 1: #ProVida 11,45%
        AFPdcto = sueldoimponible*0.1145
    elif AFP == 2: #Plan Vital 10,41%
        AFPdcto = sueldoimponible*0.1041
    elif AFP == 3: #Habitat 11,27%
        AFPdcto = sueldoimponible*0.1127
    elif AFP == 4: #Cuprum 11,44%
        AFPdcto = sueldoimponible*0.1144
    elif AFP == 5: #Capital 11,44%
        AFPdcto = sueldoimponible*0.1144

    saludcto = sueldoimponible*0.07

    if contrato == 0: #plazo indefinido
        contratodcto = sueldoimponible*0.024
    elif contrato == 1: #plazo fijo
        contratodcto = sueldoimponible*0.03
    elif contrato == 2: #plazo 11 meses o mas
        contratodcto = sueldoimponible*0.008

    totaldcto = AFPdcto + saludcto + contratodcto
    impuestounico = sueldoimponible - totaldcto

    if impuestounico < 646920:
        impuesto = 0
    elif impuestounico > 646920 and impuestounico < 1437600:
        impuesto = impuestounico*0.04 - 25876
    elif impuestounico > 1437600 and impuestounico < 2396000:
        impuesto = impuestounico*0.08 - 83380
    elif impuestounico > 2396000 and impuestounico < 3354400:
        impuesto = impuestounico*0.135 - 215160
    elif impuestounico > 3354400 and impuestounico < 4318000:
        impuesto = impuestounico*0.23 - 523828
    elif impuestounico > 4318000 and impuestounico < 5750400:
        impuesto = impuestounico*0.304 - 852976
    elif impuestounico > 5750400:
        impuesto = impuestounico*0.35 - 1117494

    totaldcto = totaldcto + impuesto
    sueldoliquido = sueldoimponible - totaldcto
    if salud == 1:
        sueldoliquido = sueldoliquido - planuf

    titulo()
    print ("El resultado del calculo es:\n")
    print("sueldo bruto: {}".format(sueldoimponible))
    print("descuento AFP: {}".format(AFPdcto))
    if salud == 0:
        print("descuento salud: {}".format(saludcto))
    elif salud == 1:
        print("descuento salud: {}".format(saludcto+planuf))
    print("seguro de cesantia: {}".format(contratodcto))
    print("impuestos: {}\n".format(impuesto))
    print("***Sueldo liquido: {}".format(sueldoliquido))
    print ("\n")
    opcion()

#------------------------- Inicio de interfaz al abrir:
titulo()
print ("Facilitanos la informacion solicitada a continuacion, recuerda no usar espacios, puntos, comas,")
print ("ni reglones en tus respuestas. Esta informacion es necesaria para calcular tu sueldo, ademas")
print ("recuerda que si te equivocas en algun dato luego podras editarlo, muchas gracias.")
print ("\nIngresa tu AFP:")
print ("(0) Modelo ; (1) ProVida ; (2) PlanVital ; (3) Habitat ; (4) Cuprum ; (5) Capital")
AFP = int(input("[1] AFP: "))
while(AFP > 5 or AFP < 0):
    AFP = int(input("AFP invalida: "))
print ("\nIngresa tu tipo de contrato:")
print ("(0) Plazo indefinido ; (1) Plazo fijo ; (2) Plazo indefinido 11 anos o mas")
contrato = int(input("[2] contrato: "))
while(contrato > 2 or contrato < 0):
    contrato = int(input("contrato invalido: "))
print ("\nIngresa tu plan de salud:")
print ("(0) fonasa ; (1) isapre")
salud = int(input("[3] salud: "))
while(salud > 1 or salud < 0):
    salud = int(input("salud invalido: "))
if salud == 1:
    planuf = int(input("Ingresa plan en UF: "))
    planuf = planuf*29168

while ax != 0:
    datos()
    print ("Si deseas modificar alguna informacion anterior, utiliza las siguientes opciones:")
    print ("[1] AFP ; [2] tipo de contrato ; [3] plan de salud ; [0] continuar")
    ax = int(input(">>: "))
    if ax == 1:
        print ("\nIngresa tu AFP:")
        print ("(0) Modelo ; (1) ProVida ; (2) PlanVital ; (3) Habitat ; (4) Cuprum ; (5) Capital")
        AFP = int(input("[1] AFP: "))
        while(AFP > 5 or AFP < 0):
            AFP = int(input("AFP invalida: "))
    if ax == 2:
        print ("\nIngresa tu tipo de contrato:")
        print ("(0) Plazo indefinido ; (1) Plazo fijo ; (2) Plazo indefinido 11 anos o mas")
        contrato = int(input("[2] contrato: "))
        while(contrato > 2 or contrato < 0):
            contrato = int(input("contrato invalido: "))
    if ax == 3:
        print ("\nIngresa tu plan de salud:")
        print ("(0) fonasa ; (1) isapre")
        salud = int(input("[3] salud: "))
        while(salud > 1 or salud < 0):
            salud = int(input("salud invalido: "))
        if salud == 1:
            planuf = int(input("Ingresa plan en UF: "))
            planuf = planuf*29168
ax = 0
while ax != 3:
    datos()
    opcion()
