"""
Implementação do kNN
dataset: http://archive.ics.uci.edu/ml/datasets/Haberman%27+Survival
Descrição do dataset: Sobrevivência de pacientes submetidos a cirurgia de câncer de mama
"""


import math


def dist_euclidiana(v1, v2):
    dim, soma = len(v1), 0
    for i in range(dim - 1):
        soma += math.pow(v1[i] - v2[i], 2)
    return math.sqrt(soma)


def knn(treinamento, nova_amostra, K):
    dists, tam_treino = {}, len(treinamento)

    # calcula a distância euclidiana do conjunto de treinamento
    # todos os outros exemplos do conjunto de treinamento
    for i in range(tam_treino):
        d = dist_euclidiana(treinamento[i], nova_amostra)
        dists[i] = d

    # obtém as chaves (índices) dos k-vizinhos mais próximos
    k_vizinhos = sorted(dists, key=dists.get)[:K]

    # votação majoritária
    qtd_rotulo1, qtd_rotulo2 = 0, 0
    for indice in k_vizinhos:
        if treinamento[indice][-1] == 1:
            qtd_rotulo1 += 1
        else:
            qtd_rotulo2 += 2

    if qtd_rotulo1 > qtd_rotulo2:
        return 1
    else:
        return 2

#
# v1 = [1, 2, 3]
# v2 = [2, 1, 3]
# print(dist_euclidiana(v1, v2))


def info_dataset(amostras, verbose=True):
    if verbose:
        print('Total de amostras: {}'.format(len(amostras)))
    rotulo1, rotulo2 = 0, 0
    for amostra in amostras:
        if amostra[-1] == 1:
            rotulo1 += 1
        else:
            rotulo2 += 1
    if verbose:
        print('Total rótulo 1: {}'.format(rotulo1))
        print('Total rótulo 2: {}'.format(rotulo2))
    return [len(amostras), rotulo1, rotulo2]


amostras = []
with open('haberman.data', 'r') as f:
    for linha in f.readlines():
        atrib = linha.replace('\n', '').split(',')
        amostras.append([
            int(atrib[0]),
            int(atrib[1]),
            int(atrib[2]),
            int(atrib[3])
        ])

# for amostra in amostras:
#     print(amostra)
# print(len(amostras))

# print(info_dataset(amostras))

p = 0.6
_, rotulo1, rotulo2 = info_dataset(amostras, verbose=False)

treinamento, teste = [], []
max_rotulo1, max_rotulo2 = int(p * rotulo1), int(p * rotulo2)
total_rotulo1, total_rotulo2 = 0, 0

for amostra in amostras:
    if (total_rotulo1 + total_rotulo2) < (max_rotulo1 + max_rotulo2):
        treinamento.append(amostra)
        if amostra[-1] == 1 and total_rotulo1 < max_rotulo1:
            total_rotulo1 += 1
        else:
            total_rotulo2 += 1
    else:
        teste.append(amostra)


#
# print(teste[10])
# print(knn(treinamento, teste[10], K=13))

# acertos, K = 0, 15
erros = {}
for K in range(14, 16):
    acertos = 0
    erro = []
    print('|| K: {}'.format(K))
    for i in range(len(teste)):
        classe = knn(treinamento, teste[i], K)
        if teste[i][-1] == classe:
            acertos += 1
        else:
            erro.append(i)
    erros[K] = erro
    print('|| Total de treinamentos: {}'.format(len(treinamento)))
    print('|| Total de testes: {}'.format(len(teste)))
    print('|| Total de acertos: {}'.format(acertos))
    print('|| Total de acertos: {:.2f}%'.format(100 * acertos / len(teste)))
    print('||============================================================')
