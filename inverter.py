def inverter_string(s):
    string_invertida = ''
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

entrada = input("Digite a string que deseja inverter: ")

resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
