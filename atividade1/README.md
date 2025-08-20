# Atividade 1 – Selection Sort em Python

Este repositório contém a implementação do algoritmo Selection Sort em Python, conforme solicitado na atividade da disciplina.

## Como usar

- Execute o script `selection_sort.py`
- Digite uma lista de números separados por espaço
- O programa mostrará a lista original e a lista ordenada
- Durante a execução, serão exibidos os detalhes das trocas realizadas e as iterações do algoritmo

## 🔍 Análise dos testes

O algoritmo foi testado com diferentes listas para garantir seu funcionamento:

- **Lista desordenada:**  
  Entrada: [7, 3, 5, 1] → Saída: [1, 3, 5, 7]

- **Lista já ordenada:**  
  Entrada: [1, 2, 3, 4] → Saída: [1, 2, 3, 4]  
  Nenhuma troca foi realizada.

- **Lista invertida:**  
  Entrada: [9, 7, 5, 3] → Saída: [3, 5, 7, 9]  
  Houve troca em todas as iterações.

- **Lista com elementos repetidos:**  
  Entrada: [4, 2, 2, 1] → Saída: [1, 2, 2, 4]
