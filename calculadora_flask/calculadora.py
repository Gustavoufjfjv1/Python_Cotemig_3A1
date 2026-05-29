import math


from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]


    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
            return render_template("calculadora.html", etapas = etapas, resultados = resultado)
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        
        num2 = float(num2_valor)
        

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
        elif operacao == "/":
                if num1 <= 0:
                    resultado = "Erro: não é possível dividir por zero"
                    etapas = f"Não existe divisão por 0."
                else:
                    resultado = num1 / num2
                    etapas = f"{num1} / {num2} = {resultado}"
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"
        
        if operacao == "bhaskara":
            num3_valor = request.form.get("num3", "").strip()

            num3 = float(num3_valor)

            delta = (num2 ** 2) - (4 * num1 * num3)

            if num1 == 0:
                resultado = "Erro: número não pode ser zero"
                etapas = f"O numero 1 deve ser diferente de zero."
                return render_template("calculadora.html", etapas = etapas, resultados = resultado)
            elif delta < 0:
                resultado = "A equação não possui raízes reais."
                etapas = f"A equação não possui raízes reais."
                return render_template("calculadora.html", etapas = etapas, resultados = resultado)

            resultado = delta
            etapas = f"({num2} ^ 2) - (4 * {num1} * {num3})"

            return render_template("calculadora.html", etapas = etapas, resultados = resultado)
    
        return render_template("calculadora.html", etapas = etapas, resultados = resultado)
