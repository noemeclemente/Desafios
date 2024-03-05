def inverter_string(string):
    if not string.strip():
        return "Por favor, insira uma string válida."

    caracteres = list(string)

    caracteres = [c for c in caracteres if c.isalpha()]

    string_invertida = ''.join([caracteres[i] for i in range(len(caracteres) - 1, -1, -1)])

    return string_invertida

string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
