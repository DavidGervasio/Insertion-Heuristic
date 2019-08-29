#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programação Matemática

 
print('	Programação Matemática					')	
print('	Exercício Heurística					')


print('')
print('     O objetivo desta heurística consiste em encontrar um ciclo no grafo que inicie e finalize ')
print('             no mesmo vértice, minimizando a função objetivo abaixo: ')
print('')
print('###################################################################################################################')
print('#                                                                                                                 #')
print('#   MINIMIZE sum(custos das arestas entre os vértices conectados) + sum(penalidades de vértices não conectados)   #')
print('#   s. a:                                                                                                         #')
print('#      Os vértices conectados devem formar um ciclo, logo o ciclo deverá iniciar e fechar no mesmo vértice        #')
print('#      A quantidade de vértices do ciclo deve ser menor ou igual a quantidade de vértices do problema             #')
print('#      A solução deve garantir que os prêmios coletados devem atingir pelo menos 50% do total de prêmios do grafo #')
print('#                                                                                                                 #')
print('###################################################################################################################')
print('')
print('')
print('')
print('')

import time
from array import array

# Início do tempo de execução da heurística
inicioHeuristica = time.time()

# Vetores que armazenam os dados do problema
premios = []
penalidades = []
matrizDeCustos = []

# Leitura do arquivo
str =""
arquivo = open('test-files/v100b.txt', 'r')
for linha in arquivo:
   str += linha

# Tratamento do arquivo para extração de dados
linhas = str.split('\n')
primeiraLinha =  linhas[0].split()

# Quantidade de Nós do problema
quantidadeDeNos = primeiraLinha[3]
# Conversão para inteiro
quantidadeDeNos = int (quantidadeDeNos) 

# Vetor de prêmios
premios = linhas[3].split()
# Conversão para inteiro
premios = map(int, premios)

# Vetor de penalidades
penalidades = linhas[6].split()
# Conversão para inteiro
penalidades = map(int, penalidades)

# Segundo o arquivo de entrada, a matriz de custos começa na linha 9 e na coluna 0
linha = 9
coluna = 0

# Inserção dos valores da matriz de custos (pesos das arestas)
while linha < quantidadeDeNos+9  :
    linhasDosCustos = linhas[linha].split()
    matrizDeCustos.append([])
    colunaAux = 0
    while  colunaAux < quantidadeDeNos :
        matrizDeCustos[ linha-9 ].append( int( linhasDosCustos[colunaAux] ) )
        colunaAux+= 1
    linha+= 1

# Vetor que armazena a sequência de ligações entre os vértices conectados, ou seja, a sequência de vértices da solução
solucao = [] 
# Vetor armazena os vértices do problema e marca quais já foram conectados (-1 = não-conectado e 1 = conectado)
pontosConectados = [] 

# Inicializa o vetor de pontos conectados, marcando todos como não-conectados
i = 0
while i < quantidadeDeNos:
    pontosConectados.append( -1 )
    i+=1

# Segundo as especificações do projeto, uma condição para solucionar o problema é alcançar pelo menos metade do total 
### de prêmios de todos os vértices
# Calcula a porcentagem mínima de prêmios
soma = 0 
for p in premios:
    soma +=  p
metadeDoTotalDePremios = (soma*50)/100

# Calcula o total de penalidades do problema
somaDeTodasPenalidades = 0
for p in penalidades:
    somaDeTodasPenalidades +=  p

# Segundo a Heurística de Inserção Mais Próxima, dois vértices quaisquer devem ser escolhidos a fim de iniciar o grafo

# O objetivo desta heurística é minimizar o total de custos associados aos vértices conectados acrescidos das penalidades
### dos vértices não-conectados
# Então, para iniciar o grafo adotamos uma medida gulosa, a qual determina que os dois vértices iniciais são os quais 
### apresentam as maiores penalidades, caso não sejam conectados

# Encontra o vértice com a maior penalidade
primeiraMaiorpenalidades = max(penalidades)
# Encontra a posição do vértice com maior penalidade
posPrimeiraMaiorpenalidades = penalidades.index(primeiraMaiorpenalidades)

# Encontra uma sub-lista sem o vértice de maior penalidade
penalidadesAux = []		
for p in penalidades:
	if p < primeiraMaiorpenalidades:
		penalidadesAux.append(p)

# Encontra o vértice com a segunda maior penalidade
segundaMaiorpenalidades = max(penalidadesAux)
# Encontra a posição do vértice com a segunda maior penalidade
posSegundaMaiorpenalidades = penalidades.index(segundaMaiorpenalidades)

# Inicialização dos dois vértices iniciais
primeiroNo = posPrimeiraMaiorpenalidades
segundoNo = posSegundaMaiorpenalidades
# Definição de um parâmetro muito grande para iniciar a comparação de custos de inserção
INFINITO = 9999999

# Inserção dos nós iniciais na solução
solucao.append(primeiroNo)
solucao.append(segundoNo)

# Cálculo do custo inicial das arestas
custo = matrizDeCustos[primeiroNo][segundoNo] + matrizDeCustos[segundoNo][primeiroNo]

# O primeiro e o segundo nó são marcados como conectados 
pontosConectados [primeiroNo] = 1
pontosConectados [segundoNo] = 1

# Contador para os vértices já conectados
quantidadeDePontosConectados = 2

# Calcula a penalidade inicial
somaDeTodasPenalidades =  somaDeTodasPenalidades - penalidades[primeiroNo] - penalidades[segundoNo]
# Calcula a premiação inicial
somaDePremios  = premios[ primeiroNo] + premios[segundoNo]

# Estrutura de repetição que determina o grafo do problema, a qual está condicionada à inserção de no máximo todos os vértices do problema e à coleta de pelo menos 50% da premiação total
while quantidadeDePontosConectados  < quantidadeDeNos and somaDePremios <= metadeDoTotalDePremios:
    
    # Inicialização da variável que irá armazenar os vértices a serem inseridos
    verticeDeMenorCusto = -1 
    # Inicialização da variável que irá armazenar as posições dos vértices a serem inseridos
    posVerticeDeMenorCusto = -1 
    # Inicialização de parâmetro para iniciar a comparação entre os custos de inserção
    menorCustoDeInsercao = INFINITO
    # Índice para verificação qual nó não está conectado dentre todos os nós do problema 
    indiceDePontoNaoConectado = 0

    # Verificação dentre todos os vértices do problema
    while  indiceDePontoNaoConectado < quantidadeDeNos:
    	
    	# A operação de busca por vértices a serem inseridos é realizada somente para vértices não-conectados, caso o índiceDePontoNaoConectado atual seja referente a um ponto conectado
    	### então esse índice é incrementado até que todos os vértices do problema sejam verificados
        if pontosConectados[indiceDePontoNaoConectado] == -1:
            indiceNaSolucao = 0
           
            # Para cada vértice já conectado é realizada a seguinte operação
            while indiceNaSolucao < quantidadeDePontosConectados :

                no_antecessor = solucao[indiceNaSolucao]
                
                # Se o no_antecessor for o último nó inserido, o primeiro nó inserido no problema seŕa o no_sucessor  
                no_sucessor = solucao[(indiceNaSolucao+1) % quantidadeDePontosConectados]

                # Dado um ciclo, a cada dois vértices é verificado qual outro vértice pode ser inserido entre os mesmos de forma a obter o menor custo possível       
                # Para a escolha do vértice são considerados os custos das arestas para inserção e o quanto essa inserção reduzirá a penalidade total até o momento
                
                custoDeInsercao = matrizDeCustos[no_antecessor][indiceDePontoNaoConectado] + matrizDeCustos[indiceDePontoNaoConectado][no_sucessor] - matrizDeCustos[no_antecessor][no_sucessor] + somaDeTodasPenalidades - penalidades[indiceDePontoNaoConectado]
                
                # A melhor solução atual tem seus dados armazenados de forma provisória
                # Esta comparação de custos de inserção será realizada para todos os vértice ainda não-conectados
                if custoDeInsercao < menorCustoDeInsercao:
                	
                	# Armazena o vértice com menor custo de inserção atual
                    verticeDeMenorCusto = indiceDePontoNaoConectado 
                    
                    # Posição que o vértice com menor custo atual será inserido na solução
                    posVerticeDeMenorCusto = indiceNaSolucao 
                    
                    # O menor custo de inserção atual é atualizado
                    menorCustoDeInsercao = custoDeInsercao

                indiceNaSolucao+=1
        indiceDePontoNaoConectado+=1


    j = quantidadeDePontosConectados
    solucao.append(solucao[j-1])

    # Ordena-se o vetor de solução, conforme os custos de arestas, a fim de inserir o novo vértice 
    while j  > posVerticeDeMenorCusto+1:
        solucao[j] = solucao[j-1]
        j-=1
       
    # Atualiza o vetor de solução com novo vértice inserido
    solucao[posVerticeDeMenorCusto+1] = verticeDeMenorCusto
   
    # Atualiza o novo total de penalidades, de modo a retirar do montante a penalidade do vértice inserido
    somaDeTodasPenalidades -= penalidades[verticeDeMenorCusto]
   
    # Atualização do custo do problema após a inserção do vértice 
    custo += menorCustoDeInsercao - somaDeTodasPenalidades #custo somente  das harestas
   
    # Atualização do vetor de pontos conectados, marcando como conectado o vértice recentemente inserido
    pontosConectados[verticeDeMenorCusto] = 1
   
    # Atualização da quantidade de vértices inseridos no ciclo
    quantidadeDePontosConectados +=1
   
    # Atualização dos prêmios até então coletados
    somaDePremios += premios[verticeDeMenorCusto]
    
# Custo final das arestas constituintes do grafo acrescido do total de penalidades dos grafos não conectados
custo += somaDeTodasPenalidades

# Fim do tempo de execução da heurística
fimHeuristica = time.time()

print("O grafo gerado é composto pelos seguintes vértices: ")
print(solucao)
print('')
print("O resultado da função objetivo do grafo gerado é: ")
print(custo)
print('')
print("O total de prêmios coletados com o trajeto deste grafo é: ")
print(somaDePremios)
print('')
print "Tempo de Execução em MiliSegundos: ", (fimHeuristica - inicioHeuristica )*1000
