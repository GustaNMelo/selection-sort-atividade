# Atividade 2 – Otimização do Algoritmo Selection Sort

Esta atividade tem como objetivo implementar uma **versão otimizada do Selection Sort**, que interrompe a ordenação caso nenhuma troca ocorra durante uma iteração, evitando comparações desnecessárias.

## ⚙️ Comparação entre versões

Foram testadas duas versões do Selection Sort:

- **Versão básica**: percorre toda a lista mesmo que já esteja ordenada.
- **Versão otimizada**: interrompe o processo se nenhuma troca for realizada em uma iteração.

### 🔍 Resultados

#### Lista já ordenada: [1, 2, 3, 4, 5]
| Versão           | Iterações | Tempo (s)      |
|------------------|-----------|----------------|
| Básica           | 4         | 0.0000xx       |
| Otimizada        | 1         | 0.0000xx       |

#### Lista desordenada: [5, 3, 8, 1, 4]
| Versão           | Iterações | Tempo (s)      |
|------------------|-----------|----------------|
| Básica           | 4         | 0.0000xx       |
| Otimizada        | 4         | 0.0000xx       |

#### Lista invertida: [9, 7, 5, 3, 1]
| Versão           | Iterações | Tempo (s)      |
|------------------|-----------|----------------|
| Básica           | 4         | 0.0000xx       |
| Otimizada        | 4         | 0.0000xx       |

### 📌 Conclusão

A versão otimizada apresenta ganhos reais em **listas já ordenadas**, interrompendo o processo logo na primeira iteração, o que reduz o tempo e o número de comparações. Em listas desordenadas ou invertidas, o comportamento das duas versões é similar, pois há trocas em todas as iterações.

Essa otimização é simples, mas útil em casos onde a entrada pode já estar ordenada ou quase ordenada.
