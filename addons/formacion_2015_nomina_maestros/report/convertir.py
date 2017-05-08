def convertir(valor):
    valor=str(valor)
    largo=len(valor)
    pos_invertida = [] #posiciones invertidas
    pos_correcta=[]   #posiciones correctas
    u_d_c=[]  #lista de numeros
    resultado=''
    for posicion in range(largo,0,-3):
        pos_invertida.append(posicion)
    for i in range(len(pos_invertida)-1,-1,-1):
        pos_correcta.append(pos_invertida[i])
    for s in pos_correcta:
        if s<=2:
            u_d_c.append(valor[0:s])
        else:
            u_d_c.append(valor[s-3:s])
    for recorrido in range(len(u_d_c)):
        if recorrido==(len(u_d_c)-1):
            resultado=resultado + str(u_d_c[recorrido])
        else:
            resultado=resultado + str(u_d_c[recorrido]) + '.'
    return resultado