"""Você deve desenvolver um programa, em qualquer linguagem de programação .com
exceção de pseudo-código), que, dado um conjunto de pontos de coleta e suas respectivas
quantidades de resíduos acumulados, determine a ordem de atendimento dos caminhões
de coleta. O objetivo é garantir que os pontos com maior quantidade de resíduos sejam
atendidos primeiro, otimizando assim a operação.
Requisitos do Programa:
Entrada de Dados:
•
•
Um número inteiro N, que representa a quantidade de pontos de coleta
Uma lista contendo:
o Nome do ponto de coleta no formato texto
Quantidade de resíduos acumulados no formato inteiro (em quilogramas)
o
Saída de Dados:
Nome do ponto de coleta no formato texto
o Ordem de atendimento no formato inteiro, onde I representa 0 primeiro ponto a
ser atendido
Regras de negócio:
A ordem de atendimento deve ser determinada pela quantidade de resíduos
o
acumulados, em ordem decrescente (os pontos com mais resíduos devem ser
atendidos primeiro)
o Se dois ou mais pontos tiverem a mesma quantidade de resíduos, a ordem de
atendimento entre eles deve ser definida pela ordem alfabética dos nomes
Dicas de Implementação.
Ordenação: Utilize um algoritmo de ordenação para ordenar os pontos de coleta pela
quantidade de resíduos em ordem decrescente.
Empate: Em caso de empate na quantidade de resíduos, use a ordem alfabética dos
nomes dos pontos de coleta como critério de desempate.
Atribuição da Ordem: Após a ordenação, atribua os números correspondentes à ordem
de atendimento."""
   
from operator import itemgetter

def ordena(pontos):    
    
    map(int, pontos[1]) # Remapeia o segundo item para um inteiro, para poder ordenar numeros com dois ou mais algarismos             

    pontos = sorted(pontos, key = itemgetter(0)) # Ordena por ordem alfabetica
    pontos = sorted(pontos, key = itemgetter(1), reverse=1) # Depois, ordena por numero de residuos, por ser sempre o primeiro da lista o escolhido, mantem a ordem alfabetica
        
        
    return pontos

def main():
    pontos = []

    while True:  
        
        ponto = input("Digite: nome do ponto, quantidade de resíduos (deixe em branco para parar): ").split(', ') 
        
        if ponto == ['']:
            break
        
        else:        
            pontos.append(ponto)  # Junta os dados ja obitidos numa unica lista
            
    pontos = ordena(pontos)

    print("\nOrdem de coleta")
    
    i=1 # Inicializa contador para printar o numero da ordem
    for p in pontos:         
           
        print( f'\n     Ordem: {i}',
                '\n     Ponto:', p[0],
                '\n     Quantidade de resíduos:', p[1])
        i+=1
        
    print(f"\nNumero de pontos: {len(pontos)}")

if __name__ == '__main__':
    main()