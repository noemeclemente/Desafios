# Completar sequências
def completar_sequencia_a():
    sequencia = [1, 3, 5, 7]
    proximo_numero = sequencia[-1] + 2
    sequencia.append(proximo_numero)
    return sequencia

def completar_sequencia_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    proximo_numero = sequencia[-1] * 2
    sequencia.append(proximo_numero)
    return sequencia

def completar_sequencia_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    proximo_numero = len(sequencia)**2
    sequencia.append(proximo_numero)
    return sequencia

def completar_sequencia_d():
    sequencia = [4, 16, 36, 64]
    proximo_numero = (len(sequencia) + 2)**2
    sequencia.append(proximo_numero)
    return sequencia

def completar_sequencia_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    proximo_numero = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo_numero)
    return sequencia

def completar_sequencia_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    ultimo_numero = sequencia[-1]
    proximo_numero = ultimo_numero + 1
    sequencia.append(proximo_numero)
    return sequencia

# Imprimir sequências completadas
print("Sequência a):", completar_sequencia_a())
print("Sequência b):", completar_sequencia_b())
print("Sequência c):", completar_sequencia_c())
print("Sequência d):", completar_sequencia_d())
print("Sequência e):", completar_sequencia_e())
print("Sequência e):", completar_sequencia_f())
