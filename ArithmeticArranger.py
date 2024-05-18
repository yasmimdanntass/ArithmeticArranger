def arithmetic_arranger(problems, show_answers=False):
    list = []
    linha1 = ''
    linha2 = ''
    linha3 = ''
    linha4 = ''
    answer = ''
    if len(problems) <= 5:
        for i in problems:
            list = i.split()   
            num1, op, num2 = i.split() 
            if not (num1.isdigit() and num2.isdigit()):
                return 'Error: Numbers must only contain digits.'
            if not (len(num1) <= 4 and len(num2)) <= 4:
                return 'Error: Numbers cannot be more than four digits.'
            if op not in ["-", "+"]:
                return "Error: Operator must be '+' or '-'."
            tamanho_barras = len(max(list, key=len)) + 2
            barras = tamanho_barras * '-'
            texto_justificado = list[0].rjust(tamanho_barras)
            linha1 += texto_justificado + "    "
            texto_justificado = f'{list[1]}{list[2].rjust(tamanho_barras -1)}'
            linha2 += texto_justificado + "    "
            linha3 += barras + "    "
            if show_answers:
                if op == "-":
                    answer = int(num1) - int(num2)
                elif op == "+":
                    answer = int(num1) + int(num2)
                answer = str(answer)
                linha4 += answer.rjust(tamanho_barras) + "    "
        linha1 = linha1.rstrip(linha1[-4:])
        linha2 = linha2.rstrip(linha2[-4:])
        linha3 = linha3.rstrip(linha3[-4:])
        problems = linha1 + '\n' + linha2 + '\n' + linha3 
        if show_answers:
            linha4 = linha4.rstrip(linha4[-4:])
            problems += '\n'
            problems += linha4
        return problems
    else:
        return "Error: Too many problems."
    
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])}')
