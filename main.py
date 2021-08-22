import json

combinacao = []
coberturas_restantes = []

for i in range(3):
    combinacao.append( [0] * 3)

def gera_combinacoes_recursivo(vaca, coberturas):
    if vaca == 0:
        return
    
    coberta = False
    i = 0
    while (i < num_touros):
        x = 0
        if coberturas_restantes[x] > 0 and coberta == False:
            combinacao[vaca - 1][x] = 1
            coberturas_restantes[x] -= 1
            coberta = True
            i = 3
        i = i + 1
        x += x
        
    return gera_combinacoes_recursivo(vaca - 1, coberturas_restantes)

def gera_solucoes_iterativo(coberturas):
    combinacao = []
    for i in coberturas:
        if coberturas[i] > 0:
            combinacao[i].append(i)

        

def gera_solucoes(Touros, Vacas, x):
    if x == 0:
        print("Imprime solução")
    else:
        print(Vacas[x][0])
        gera_solucoes(Touros, Vacas, x - 1)
    #return

def w(I1, I2, I3, Genero):
    if Genero == "M":
        return 0.2 * float(I1) + 0.3 * float(I2) + 0.5 * float(I3)
    else:
        return 0.3 * I1 + 0.3 * I2 + 0.4 * I3

if __name__ == "__main__":
    arquivo = open('dados.json', 'r')
    dados = json.load(arquivo)

    dados2 = dados.get("dados")
    Touros = dados2.get("Touros")
    Vacas = dados2.get("Vacas")
    Cruzamento = dados2.get("Cruzamento")
    Parentesco = dados2.get("Parentesco")

    num_touros = 0

    for i in dados2["Touros"]:
        #print(i, x)
        Touros[num_touros][0] = i.get("I1")
        Touros[num_touros][1] = i.get("I2")
        Touros[num_touros][2] = i.get("I3")
        #print(Touros[x][0], Touros[x][1], Touros[x][2])
        num_touros += 1

    x = 0

    for i in dados2["Vacas"]:
        #print(i, x)
        Vacas[x][0] = i.get("I1")
        Vacas[x][1] = i.get("I2")
        Vacas[x][2] = i.get("I3")
        #print(Vacas[x][0], Vacas[x][1], Vacas[x][2])
        x += 1

    x = 0

    

    for i in dados2["Cruzamento"]:
        #print(i, x)
        num = 0
        Cruzamento[x][0] = i.get("I1")
        Cruzamento[x][1] = i.get("I2")
        Cruzamento[x][2] = i.get("I3")
        if Cruzamento[x][0] == 1:
            num += 1
        if Cruzamento[x][1] == 1:
            num += 1
        if Cruzamento[x][2] == 1:
            num += 1
        coberturas_restantes.append(num)    
        #print(Cruzamento[x][0], Cruzamento[x][1], Cruzamento[x][2], num)
        x = x + 1

    x = 0

    for i in dados2["Parentesco"]:
        #print(i, x)
        Parentesco[x][0] = i.get("I1")
        Parentesco[x][1] = i.get("I2")
        Parentesco[x][2] = i.get("I3")
        #print(Parentesco[x][0], Parentesco[x][1], Parentesco[x][2])
        x += 1






#print("Contribuição individual Touro 1", w(Touros[0][0], Touros[0][1], Touros[0][2], "M"))
#gera_solucoes(Touros, Vacas, x-1)
#gera_solucoes_iterativo(coberturas_restantes)

gera_combinacoes_recursivo(3, coberturas_restantes)
print("    T1 T2 T3")
print("v1", combinacao[2])
print("v2", combinacao[1])
print("v3", combinacao[0])
print(coberturas_restantes)

#gera_combinacoes_recursivo(3, coberturas_restantes)

#print(combinacao[2])
#print(combinacao[1])
#print(combinacao[0])
#print(x)


#matriz de cruzamentos
#matriz de parentesco


