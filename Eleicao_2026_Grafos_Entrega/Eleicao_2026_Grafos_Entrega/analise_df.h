
#ifndef ANALISE_DF_H
#define ANALISE_DF_H

#include "grafo.h"

Grafo* construir_grafo_bipartido_df(const char* arquivo_csv);

void candidatos_dominantes_por_ra(Grafo* g);

Grafo* gerar_grafo_similaridade_ra(
    Grafo* g_bipartido,
    float limiar_similaridade
);

#endif
