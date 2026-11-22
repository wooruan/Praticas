#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "grafo.h"

Grafo* construir_grafo_bipartido_df(const char* arquivo_csv) {
    FILE *arquivo = fopen(arquivo_csv, "r");

    if (arquivo == NULL) {
        printf("Erro ao abrir: %s\n", arquivo_csv);
        return NULL;
    }

    char linha[512];
    char ras[40][MAX_NOME] = {{0}};
    char candidatos[20][MAX_NOME] = {{0}};
    int qtdRas = 0;
    int qtdCandidatos = 0;

    fgets(linha, sizeof(linha), arquivo);

    while (fgets(linha, sizeof(linha), arquivo)) {
        char *ra = strtok(linha, ";");
        char *candidato = strtok(NULL, ";");

        if (ra == NULL || candidato == NULL) {
            continue;
        }

        int existe = 0;

        for (int i = 0; i < qtdRas; i++) {
            if (strcmp(ras[i], ra) == 0) {
                existe = 1;
                break;
            }
        }

        if (!existe && qtdRas < 40) {
            snprintf(ras[qtdRas++], MAX_NOME, "%s", ra);
        }

        existe = 0;

        for (int i = 0; i < qtdCandidatos; i++) {
            if (strcmp(candidatos[i], candidato) == 0) {
                existe = 1;
                break;
            }
        }

        if (!existe && qtdCandidatos < 20) {
            snprintf(candidatos[qtdCandidatos++], MAX_NOME, "%s", candidato);
        }
    }

    Grafo *g = malloc(sizeof(Grafo));

    if (g == NULL) {
        fclose(arquivo);
        return NULL;
    }

    inicializarGrafo(g, qtdRas + qtdCandidatos, 0);
    g->quantidadeRAs = qtdRas;

    for (int i = 0; i < qtdRas; i++) {
        definirNome(g, i, ras[i]);
    }

    for (int i = 0; i < qtdCandidatos; i++) {
        definirNome(g, qtdRas + i, candidatos[i]);
    }

    rewind(arquivo);
    fgets(linha, sizeof(linha), arquivo);

    while (fgets(linha, sizeof(linha), arquivo)) {
        char *ra = strtok(linha, ";");
        char *candidato = strtok(NULL, ";");
        char *percentual = strtok(NULL, ";\r\n");

        if (!ra || !candidato || !percentual) {
            continue;
        }

        int indiceRa = -1;
        int indiceCandidato = -1;

        for (int i = 0; i < qtdRas; i++) {
            if (strcmp(ras[i], ra) == 0) {
                indiceRa = i;
                break;
            }
        }

        for (int i = 0; i < qtdCandidatos; i++) {
            if (strcmp(candidatos[i], candidato) == 0) {
                indiceCandidato = qtdRas + i;
                break;
            }
        }

        if (indiceRa >= 0 && indiceCandidato >= 0) {
            adicionarAresta(
                g,
                indiceRa,
                indiceCandidato,
                (float)atof(percentual)
            );
        }
    }

    fclose(arquivo);

    printf("GRAFO BIPARTIDO DO DF CONSTRUIDO\n");
    printf("----------------------------------------\n");
    printf("Regioes Administrativas: %d\n", qtdRas);
    printf("Candidatos: %d\n", qtdCandidatos);
    printf("Vertices totais: %d\n", g->quantidadeVertices);

    return g;
}



void candidatos_dominantes_por_ra(Grafo* g) {
    if (g == NULL) {
        printf("Grafo invalido!\n");
        return;
    }

    printf("\nCANDIDATOS COM MAIOR PERCENTUAL POR RA\n");
    printf("----------------------------------------\n");

    for (int i = 0; i < g->quantidadeRAs; i++) {
        No *atual = g->adjacencia[i].inicio;

        int melhorCandidato = -1;
        float maiorPercentual = -1.0f;

        while (atual != NULL) {
            if (atual->peso > maiorPercentual) {
                maiorPercentual = atual->peso;
                melhorCandidato = atual->destino;
            }

            atual = atual->proximo;
        }

        if (melhorCandidato >= 0) {
            printf("%-25s | %-35s | %.2f%%\n",
                   g->nomes[i],
                   g->nomes[melhorCandidato],
                   maiorPercentual);
        } else {
            printf("%s | Sem dados\n", g->nomes[i]);
        }
    }
}


Grafo* gerar_grafo_similaridade_ra(
    Grafo* g_bipartido,
    float limiar_similaridade
) {
    if (g_bipartido == NULL ||
        limiar_similaridade < 0.0f ||
        limiar_similaridade > 1.0f) {
        return NULL;
    }

    int n = g_bipartido->quantidadeRAs;
    int total = g_bipartido->quantidadeVertices;
    int candidatos = total - n;

    if (n <= 0 || candidatos <= 0) {
        return NULL;
    }

    Grafo *similaridade = malloc(sizeof(Grafo));

    if (similaridade == NULL) {
        return NULL;
    }

    inicializarGrafo(similaridade, n, 0);

    for (int i = 0; i < n; i++) {
        definirNome(similaridade, i, g_bipartido->nomes[i]);
    }

    int arestas = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            float produto = 0.0f;
            float normaA = 0.0f;
            float normaB = 0.0f;

            for (int k = n; k < total; k++) {
                float a = 0.0f;
                float b = 0.0f;

                No *atual = g_bipartido->adjacencia[i].inicio;

                while (atual != NULL) {
                    if (atual->destino == k) {
                        a = atual->peso;
                        break;
                    }
                    atual = atual->proximo;
                }

                atual = g_bipartido->adjacencia[j].inicio;

                while (atual != NULL) {
                    if (atual->destino == k) {
                        b = atual->peso;
                        break;
                    }
                    atual = atual->proximo;
                }

                produto += a * b;
                normaA += a * a;
                normaB += b * b;
            }

            if (normaA > 0.0f && normaB > 0.0f) {
                float valor = produto / sqrtf(normaA * normaB);

                if (valor >= limiar_similaridade) {
                    adicionarAresta(similaridade, i, j, valor);
                    arestas++;
                }
            }
        }
    }

    printf("\nGRAFO DE SIMILARIDADE ENTRE RAs\n");
    printf("----------------------------------------\n");
    printf("Regioes: %d\n", n);
    printf("Candidatos considerados: %d\n", candidatos);
    printf("Limiar: %.4f\n", limiar_similaridade);
    printf("Arestas: %d\n", arestas);

    return similaridade;
}
