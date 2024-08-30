# funcao para inverter uma string sem usar funcoes prontas
def inverter_string(string):
    string_invert = ""
    for caractere in string:
        string_invert = caractere + string_invert
    return string_invert


# entrada da string
entrada = input("informe uma string para ser invertida: ")


# invertendo a string
resultado = inverter_string(entrada)


# exibindo o resultado
print(f"string invertida: {resultado}")

