# -*- coding: utf-8 -*-
     
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
      
# Problema: Gerando Permutações Ordenadas Rapidamente
# Nivel: 3
 
def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
   
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
   
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True
 
n = int(raw_input())
 
for i in xrange(n):
     
    l = list(raw_input())
    l.sort()
     
    print "".join(l)
    while next_permutation(l):
        print "".join(l)
 
    print