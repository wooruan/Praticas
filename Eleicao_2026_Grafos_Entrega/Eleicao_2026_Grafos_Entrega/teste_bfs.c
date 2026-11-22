
#include <stdio.h>
#include "grafo.h"
#include "analise_nacional.h"

int main() {
    Grafo g;

    inicializarGrafo(&g, 5, 0);

    definirNome(&g, 0, "Estado A");
    definirNome(&g, 1, "Estado B");
    definirNome(&g, 2, "Estado C");
    definirNome(&g, 3, "Estado D");
    definirNome(&g, 4, "Estado E");

    adicionarAresta(&g, 0, 1, 1.0f);
    adicionarAresta(&g, 0, 2, 1.0f);
    adicionarAresta(&g, 1, 3, 1.0f);
    adicionarAresta(&g, 3, 4, 1.0f);

    busca_largura_propagacao_fronteiras(&g, 0);

    liberarGrafo(&g);

    return 0;
}
