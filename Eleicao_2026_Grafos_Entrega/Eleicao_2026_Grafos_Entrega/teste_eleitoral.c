
#include <stdio.h>
#include <stdlib.h>

#include "grafo.h"
#include "analise_nacional.h"

int main()
{
    Grafo *g = construir_grafo_eleitoral_nacional(
        "data/processed/votacao_presidente_estados_2026.csv");

    if (g == NULL)
    {
        printf("Falha na construcao do grafo.\n");
        return 1;
    }

    int somaGraus = 0;

    for (int i = 0; i < g->quantidadeVertices; i++)
    {
        somaGraus += calcularGrau(g, i);
    }

    printf("\nVALIDACAO\n");
    printf("----------------------------------------\n");
    printf("Vertices: %d\n", g->quantidadeVertices);
    printf("Arestas calculadas: %d\n", somaGraus / 2);

    printf("\nEXECUTANDO KRUSKAL\n");
    printf("----------------------------------------\n");

    calcular_mst_eleitoral_kruskal(g);

    Grafo *g_sim = malloc(sizeof(Grafo));

    if (g_sim == NULL)
    {
        liberarGrafo(g);
        free(g);
        return 1;
    }

    inicializarGrafo(g_sim, g->quantidadeVertices, 0);

    for (int i = 0; i < g->quantidadeVertices; i++)
    {
        definirNome(g_sim, i, g->nomes[i]);
    }

    for (int i = 0; i < g->quantidadeVertices; i++)
    {
        No *atual = g->adjacencia[i].inicio;

        while (atual != NULL)
        {
            int j = atual->destino;

            if (i < j)
            {
                float similaridade =
                    1.0f / (1.0f + atual->peso);

                adicionarAresta(
                    g_sim,
                    i,
                    j,
                    similaridade);
            }

            atual = atual->proximo;
        }
    }

    printf("\nCLUSTERS ELEITORAIS - DFS\n");
    printf("----------------------------------------\n");

    busca_profundidade_clusters(g_sim, 0.97f);

    liberarGrafo(g_sim);
    free(g_sim);

    liberarGrafo(g);
    free(g);

    return 0;
}
