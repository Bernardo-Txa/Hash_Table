# Tabela Hash

## Introdução

Uma tabela hash, também conhecida como mapa hash, é uma estrutura de dados que implementa uma matriz associativa, um tipo abstrato de dados que pode armazenar pares chave-valor. Hashing é uma técnica usada para mapear um dado de tamanho grande para um dado de tamanho pequeno que pode ser usado como índice para acessar diretamente um elemento desejado.

## Como funciona

Uma tabela hash usa uma função hash para calcular um índice no qual um elemento desejado é encontrado. A função hash é usada para transformar a chave em um valor hash, que é um índice que corresponde a um local na matriz de dados, onde o valor correspondente é armazenado.

### Colisões

As colisões ocorrem quando a função hash gera o mesmo índice para mais de uma chave. Existem várias técnicas para resolver colisões. Duas das mais comuns são o encadeamento separado e a sondagem linear.

#### Encadeamento Separado

No encadeamento separado, cada elemento da matriz de dados é uma lista de itens que têm o mesmo valor hash.

#### Sondagem Linear

Na sondagem linear, se ocorrer uma colisão, a tabela hash verifica o próximo elemento na matriz para ver se está vazio.

## Complexidade de Tempo

A complexidade de tempo para busca, inserção e remoção em uma tabela hash é, na média, O(1). No pior caso, a complexidade de tempo é O(n), onde n é o número de elementos na tabela hash.

## Conclusão

As tabelas hash são uma estrutura de dados eficiente para implementar um tipo de matriz associativa. Elas são usadas em muitos tipos de aplicações, incluindo a implementação de caches, conjuntos de dados únicos e tabelas de símbolos.
