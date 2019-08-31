# Insertion-Heuristic

O objetivo desta heurística consiste em encontrar um ciclo no grafo que inicie e finalize no mesmo vértice,
minimizando a função objetivo abaixo:

MINIMIZE sum(custos das arestas entre os vértices conectados) + sum(penalidades de vértices não conectados)
s. a:
      Os vértices conectados devem formar um ciclo, logo o ciclo deverá iniciar e fechar no mesmo vértice.
      A quantidade de vértices do ciclo deve ser menor ou igual a quantidade de vértices do problema.
      A solução deve garantir que os prêmios coletados devem atingir pelo menos 50% do total de prêmios do grafo.

	
