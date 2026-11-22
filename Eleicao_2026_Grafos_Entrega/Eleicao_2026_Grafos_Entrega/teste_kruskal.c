
#include <stdio.h>
#include "grafo.h"
#include "analise_nacional.h"

int main() {
    Grafo g;

    inicializarGrafo(&g, 4, 0);

    definirNome(&g, 0, "Estado A");
    definirNome(&g, 1, "Estado B");
    definirNome(&g, 2, "Estado C");
    definirNome(&g, 3, "Estado D");

    adicionarAresta(&g, 0, 1, 0.10f);
    adicionarAresta(&g, 0, 2, 0.40f);
    adicionarAresta(&g, 0, 3, 0.50f);
    adicionarAresta(&g, 1, 2, 0.20f);
    adicionarAresta(&g, 1, 3, 0.60f);
    adicionarAresta(&g, 2, 3, 0.30f);

    calcular_mst_eleitoral_kruskal(&g);

    liberarGrafo(&g);

    return 0;
}
