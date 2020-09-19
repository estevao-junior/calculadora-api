from flask import Flask, request, jsonify
import math
from statistics import mode
from statistics import harmonic_mean
from statistics import mean

app = Flask("Trabalho_Api")

@app.route("/somar", methods=["POST"])
def Somar():
    body = request.get_json()
    resultado = ""
    result = 0


    if("numero1" not in body or "numero2" not in body):
        resultado = "Está faltando um dos números, verifique e tente novamente."
    else:
        result = body["numero1"] + body["numero2"]
        resultado = "O resultado da soma é: "+str(result)+""

    return resultado

@app.route("/subtrair", methods=["POST"])
def Subtrair():
    body = request.get_json()
    resultado = ""
    result = 0

    if("numero1" not in body or "numero2" not in body):
        resultado = "Está faltando um dos números, verifique e tente novamente."
    else:
        result = body["numero1"] - body["numero2"]
        resultado = "O resultado da subtração é: "+str(result)+""
    
    return resultado

@app.route("/dividir", methods=["POST"])
def Dividir():
    body = request.get_json()
    resultado = ""
    result = 0

    if("numero1" not in body or "numero2" not in body):
        resultado = "Está faltando um dos números, verifique e tente novamente."
    else:
        result = body["numero1"] / body["numero2"]
        resultado = "O resultado da divisão é: "+str(result)+""
    
    return resultado

@app.route("/multiplicar", methods=["POST"])
def Multiplicar():
    body = request.get_json()
    resultado = ""
    result = 0

    if("numero1" not in body or "numero2" not in body):
        resultado = "Está faltando um dos números, verifique e tente novamente."
    else:
        result = body["numero1"] * body["numero2"]
        resultado = "O resultado da multiplicação é: "+str(result)+""
    
    return resultado

@app.route("/raiz_quadrada", methods=["POST"])
def Raiz():
    body = request.get_json()
    resultado = ""
    result = 0

    if("numero" not in body):
        resultado = "Número não foi recebido, verifique e tente novamente."
    elif(body["numero"] < 0):
        resultado = "Não existe raiz quadrada de número negativo"
    else:
        result = math.sqrt(body["numero"])
        resultado = "O resultado da raiz quadrada é: "+str(result)+""
    
    return resultado

@app.route("/potencia", methods=["POST"])
def Potencia():
    body = request.get_json()
    resultado = ""
    result = 0

    if("numero" not in body or "potencia" not in body):
        resultado = "Número ou potência não foi recebida, verifique e tente novamente."
    else:
        result = math.pow(body["numero"], body["potencia"])
        resultado = "O resultado da potência é: "+str(result)+""
    
    return resultado

@app.route("/media_aritmetica/<value>", methods=["GET"])
def MediaAritmetica(value):
    try:
        array = [float(numbers) for numbers in value.split(';')]
    except:
        return 'Os valores devem ser apenas numeros.'

    result = {"Resultado": mean(array)}

    return result

@app.route("/media_harmonica/<value>", methods=["GET"])
def MediaHarmonica(value):
    try:
        array = [float(numbers) for numbers in value.split(';')]
    except:
        return 'Os valores devem ser apenas numeros.'

    result = {"Resultado": harmonic_mean(array)}

    return result

@app.route("/moda/<value>", methods=["GET"])
def Moda(value):
    try:
        array = [int(numbers) for numbers in value.split(';')]
    except:
        return 'Os valores devem ser apenas numeros.'

    resultado = mode(array) 
    result = {"Resultado": resultado}

    return result

app.run()