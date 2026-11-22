#ifndef ANALISE_NACIONAL_H
#define ANALISE_NACIONAL_H

#include "grafo.h"

void busca_largura_propagacao_fronteiras(
    Grafo *g_terr,
    int estado_origem
);

void busca_profundidade_clusters(
    Grafo *g_pres,
    float limiar_corte
);

void calcular_mst_eleitoral_kruskal(
    Grafo *g_pres
);

Grafo* construir_grafo_territorial(
    const char* arquivo_csv
);

Grafo* construir_grafo_eleitoral_nacional(
    const char* arquivo_csv
);

#endif