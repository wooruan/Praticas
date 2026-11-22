
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

#ifdef _WIN32
#include <windows.h>
#endif

#include "grafo.h"
#include "analise_df.h"
#include "analise_nacional.h"

int main()
{
#ifdef _WIN32
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
#endif
    setlocale(LC_NUMERIC, "C");

    // =====================================
    // PARTE 1 - ANALISE DO GOVERNADOR DO DF
    // =====================================

    printf("\n========================================\n");
    printf("ANALISE ELEITORAL - DISTRITO FEDERAL\n");
    printf("========================================\n");

    const char *caminhoDF =
        "data/processed/votacao_governador_df_2026.csv";

    Grafo *g = construir_grafo_bipartido_df(caminhoDF);

    if (g == NULL)
    {
        printf("Nao foi possivel construir o grafo do DF.\n");
        return 1;
    }

    int somaGraus = 0;

    printf("\nVERTICES DO GRAFO\n");
    printf("----------------------------------------\n");

    for (int i = 0; i < g->quantidadeVertices; i++)
    {
        int grau = calcularGrau(g, i);

        printf("%d - %s: grau %d\n",
               i, g->nomes[i], grau);

        somaGraus += grau;
    }

    printf("\nRESUMO DF\n");
    printf("----------------------------------------\n");
    printf("Vertices: %d\n", g->quantidadeVertices);
    printf("Arestas: %d\n", somaGraus / 2);

    candidatos_dominantes_por_ra(g);

    Grafo *g_similaridade =
        gerar_grafo_similaridade_ra(g, 0.998f);

    if (g_similaridade != NULL)
    {
        printf("\nCOMPONENTES DE SIMILARIDADE DO DF\n");

        int componentes = contarComponentes(g_similaridade);

        printf("\nTotal de componentes: %d\n", componentes);

        liberarGrafo(g_similaridade);
        free(g_similaridade);
    }

    liberarGrafo(g);
    free(g);

    // =====================================
    // PARTE 2 - GRAFO TERRITORIAL E BFS
    // =====================================

    printf("\n========================================\n");
    printf("ANALISE TERRITORIAL - BRASIL\n");
    printf("========================================\n");

    Grafo *g_territorial = construir_grafo_territorial(
        "data/nacional/fronteiras_ufs.csv"
    );

    if (g_territorial == NULL)
    {
        printf("Erro ao construir grafo territorial.\n");
        return 1;
    }

    printf("\nPROPAGACAO DE FRONTEIRAS A PARTIR DO DF\n");

    int indiceDF = -1;

    for (int i = 0; i < g_territorial->quantidadeVertices; i++)
    {
        if (strcmp(g_territorial->nomes[i], "DF") == 0)
        {
            indiceDF = i;
            break;
        }
    }

    if (indiceDF >= 0)
    {
        busca_largura_propagacao_fronteiras(
            g_territorial,
            indiceDF
        );
    }

    liberarGrafo(g_territorial);
    free(g_territorial);

    // =====================================
    // PARTE 3 - GRAFO ELEITORAL NACIONAL
    // =====================================

    printf("\n========================================\n");
    printf("ANALISE PRESIDENCIAL - BRASIL\n");
    printf("========================================\n");

    Grafo *g_nacional = construir_grafo_eleitoral_nacional(
        "data/processed/votacao_presidente_estados_2026.csv"
    );

    if (g_nacional == NULL)
    {
        printf("Erro ao construir grafo nacional.\n");
        return 1;
    }

    printf("\nARVORE GERADORA MINIMA\n");

    calcular_mst_eleitoral_kruskal(g_nacional);

    // =====================================
    // PARTE 4 - CLUSTERS ELEITORAIS
    // =====================================

    Grafo *g_clusters = malloc(sizeof(Grafo));

    if (g_clusters == NULL)
    {
        liberarGrafo(g_nacional);
        free(g_nacional);
        return 1;
    }

    inicializarGrafo(
        g_clusters,
        g_nacional->quantidadeVertices,
        0
    );

    for (int i = 0; i < g_nacional->quantidadeVertices; i++)
    {
        definirNome(
            g_clusters,
            i,
            g_nacional->nomes[i]
        );
    }

    for (int i = 0; i < g_nacional->quantidadeVertices; i++)
    {
        No *atual = g_nacional->adjacencia[i].inicio;

        while (atual != NULL)
        {
            int j = atual->destino;

            if (i < j)
            {
                float similaridade =
                    1.0f / (1.0f + atual->peso);

                adicionarAresta(
                    g_clusters,
                    i,
                    j,
                    similaridade
                );
            }

            atual = atual->proximo;
        }
    }

    printf("\nCLUSTERS ELEITORAIS - LIMIAR 0.95\n");
    busca_profundidade_clusters(g_clusters, 0.95f);

    printf("\nCLUSTERS ELEITORAIS - LIMIAR 0.97\n");
    busca_profundidade_clusters(g_clusters, 0.97f);

    liberarGrafo(g_clusters);
    free(g_clusters);

    liberarGrafo(g_nacional);
    free(g_nacional);

    printf("\n========================================\n");
    printf("ANALISE ELEITORAL FINALIZADA\n");
    printf("========================================\n");

    return 0;
}
