
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

    adicionarAresta(&g, 0, 1, 0.95f);
    adicionarAresta(&g, 1, 2, 0.90f);
    adicionarAresta(&g, 2, 3, 0.60f);
    adicionarAresta(&g, 3, 4, 0.88f);

    busca_profundidade_clusters(&g, 0.80f);

    liberarGrafo(&g);

    return 0;
}
