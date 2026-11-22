
#include <stdio.h>
#include <stdlib.h>
#include "grafo.h"
#include "analise_nacional.h"

int main() {
    Grafo *g = construir_grafo_territorial(
        "data/nacional/fronteiras_ufs.csv"
    );

    if (g == NULL) {
        return 1;
    }

    busca_largura_propagacao_fronteiras(g, 6);

    liberarGrafo(g);
    free(g);

    return 0;
}
