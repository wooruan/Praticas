#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "grafo.h"
#include "analise_nacional.h"
#include "dados_nacionais.h"

void busca_largura_propagacao_fronteiras(
    Grafo *g_terr,
    int estado_origem
) {
    if (g_terr == NULL ||
        estado_origem < 0 ||
        estado_origem >= g_terr->quantidadeVertices) {
        printf("Grafo ou estado de origem invalido!\n");
        return;
    }

    int visitados[MAX_VERTICES] = {0};
    int distancia[MAX_VERTICES];
    int fila[MAX_VERTICES];

    int inicio = 0;
    int fim = 0;

    for (int i = 0; i < g_terr->quantidadeVertices; i++) {
        distancia[i] = -1;
    }

    visitados[estado_origem] = 1;
    distancia[estado_origem] = 0;

    fila[fim++] = estado_origem;

    printf("\nBUSCA EM LARGURA - FRONTEIRAS\n");
    printf("----------------------------------------\n");
    printf("Estado de origem: %s\n",
           g_terr->nomes[estado_origem]);

    while (inicio < fim) {
        int atual = fila[inicio++];

        printf("%s | Nivel: %d\n",
               g_terr->nomes[atual],
               distancia[atual]);

        No *vizinho = g_terr->adjacencia[atual].inicio;

        while (vizinho != NULL) {
            int destino = vizinho->destino;

            if (!visitados[destino]) {
                visitados[destino] = 1;
                distancia[destino] = distancia[atual] + 1;
                fila[fim++] = destino;
            }

            vizinho = vizinho->proximo;
        }
    }

    printf("\nEstados alcancados: %d\n", fim);
}


static void dfs_cluster(
    Grafo *g,
    int vertice,
    int visitados[],
    float limiar
) {
    visitados[vertice] = 1;

    printf("  %s\n", g->nomes[vertice]);

    No *atual = g->adjacencia[vertice].inicio;

    while (atual != NULL) {
        int destino = atual->destino;

        if (!visitados[destino] &&
            atual->peso >= limiar) {

            dfs_cluster(g, destino, visitados, limiar);
        }

        atual = atual->proximo;
    }
}

void busca_profundidade_clusters(
    Grafo *g_pres,
    float limiar_corte
) {
    if (g_pres == NULL ||
        limiar_corte < 0.0f ||
        limiar_corte > 1.0f) {

        printf("Grafo ou limiar invalido!\n");
        return;
    }

    int visitados[MAX_VERTICES] = {0};
    int clusters = 0;

    printf("\nCLUSTERS DE SIMILARIDADE - DFS\n");
    printf("----------------------------------------\n");
    printf("Limiar: %.2f\n", limiar_corte);

    for (int i = 0; i < g_pres->quantidadeVertices; i++) {
        if (!visitados[i]) {
            clusters++;

            printf("\nCluster %d:\n", clusters);

            dfs_cluster(
                g_pres,
                i,
                visitados,
                limiar_corte
            );
        }
    }

    printf("\nTotal de clusters: %d\n", clusters);
}


#include <stdlib.h>

typedef struct {
    int origem;
    int destino;
    float peso;
} ArestaKruskal;

static int compararArestas(const void *a, const void *b) {
    const ArestaKruskal *x = a;
    const ArestaKruskal *y = b;

    if (x->peso < y->peso) return -1;
    if (x->peso > y->peso) return 1;
    return 0;
}

static int encontrarRaiz(int pai[], int v) {
    if (pai[v] != v) {
        pai[v] = encontrarRaiz(pai, pai[v]);
    }
    return pai[v];
}

void calcular_mst_eleitoral_kruskal(Grafo *g_pres) {
    if (g_pres == NULL) {
        printf("Grafo invalido!\n");
        return;
    }

    int n = g_pres->quantidadeVertices;
    int capacidade = 0;

    for (int i = 0; i < n; i++) {
        No *atual = g_pres->adjacencia[i].inicio;

        while (atual != NULL) {
            if (i < atual->destino) {
                capacidade++;
            }
            atual = atual->proximo;
        }
    }

    ArestaKruskal *arestas =
        malloc((capacidade > 0 ? capacidade : 1) *
               sizeof(ArestaKruskal));

    if (arestas == NULL) {
        printf("Erro de memoria!\n");
        return;
    }

    int quantidade = 0;

    for (int i = 0; i < n; i++) {
        No *atual = g_pres->adjacencia[i].inicio;

        while (atual != NULL) {
            if (i < atual->destino) {
                arestas[quantidade].origem = i;
                arestas[quantidade].destino = atual->destino;
                arestas[quantidade].peso = atual->peso;
                quantidade++;
            }

            atual = atual->proximo;
        }
    }

    qsort(arestas, quantidade,
          sizeof(ArestaKruskal), compararArestas);

    int pai[MAX_VERTICES];
    int tamanho[MAX_VERTICES];

    for (int i = 0; i < n; i++) {
        pai[i] = i;
        tamanho[i] = 1;
    }

    int selecionadas = 0;
    float custoTotal = 0.0f;

    printf("\nARVORE GERADORA MINIMA - KRUSKAL\n");
    printf("----------------------------------------\n");

    for (int i = 0;
         i < quantidade && selecionadas < n - 1;
         i++) {

        int origem = arestas[i].origem;
        int destino = arestas[i].destino;

        int raizA = encontrarRaiz(pai, origem);
        int raizB = encontrarRaiz(pai, destino);

        if (raizA != raizB) {
            if (tamanho[raizA] < tamanho[raizB]) {
                int temp = raizA;
                raizA = raizB;
                raizB = temp;
            }

            pai[raizB] = raizA;
            tamanho[raizA] += tamanho[raizB];

            printf("%s -- %s | Peso: %.2f\n",
                   g_pres->nomes[origem],
                   g_pres->nomes[destino],
                   arestas[i].peso);

            custoTotal += arestas[i].peso;
            selecionadas++;
        }
    }

    printf("\nArestas selecionadas: %d\n", selecionadas);
    printf("Peso total: %.2f\n", custoTotal);

    if (selecionadas != n - 1) {
        printf("Grafo desconexo: resultado e uma floresta minima.\n");
    }

    free(arestas);
}


Grafo* construir_grafo_territorial(const char* arquivo_csv) {
    const char *ufs[] = {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF",
        "ES", "GO", "MA", "MT", "MS", "MG", "PA",
        "PB", "PR", "PE", "PI", "RJ", "RN", "RS",
        "RO", "RR", "SC", "SP", "SE", "TO"
    };

    FILE *arquivo = fopen(arquivo_csv, "r");

    if (arquivo == NULL) {
        printf("Erro ao abrir: %s\n", arquivo_csv);
        return NULL;
    }

    Grafo *g = malloc(sizeof(Grafo));

    if (g == NULL) {
        fclose(arquivo);
        return NULL;
    }

    inicializarGrafo(g, 27, 0);

    for (int i = 0; i < 27; i++) {
        definirNome(g, i, ufs[i]);
    }

    char linha[128];
    int arestas = 0;

    // Ignorar o cabecalho
    fgets(linha, sizeof(linha), arquivo);

    while (fgets(linha, sizeof(linha), arquivo)) {
        char origem[3];
        char destino[3];

        if (sscanf(linha, " %2[A-Z];%2[A-Z]",
                   origem, destino) != 2) {
            continue;
        }

        int indiceOrigem = -1;
        int indiceDestino = -1;

        for (int i = 0; i < 27; i++) {
            if (strcmp(ufs[i], origem) == 0) {
                indiceOrigem = i;
            }

            if (strcmp(ufs[i], destino) == 0) {
                indiceDestino = i;
            }
        }

        if (indiceOrigem >= 0 &&
            indiceDestino >= 0 &&
            indiceOrigem != indiceDestino) {

            adicionarAresta(
                g,
                indiceOrigem,
                indiceDestino,
                1.0f
            );

            arestas++;
        }
    }

    fclose(arquivo);

    printf("\nGRAFO TERRITORIAL CONSTRUIDO\n");
    printf("----------------------------------------\n");
    printf("UFs: %d\n", g->quantidadeVertices);
    printf("Fronteiras carregadas: %d\n", arestas);

    return g;
}


Grafo* construir_grafo_eleitoral_nacional(
    const char* arquivo_csv
) {
    const char *ufs[TOTAL_UFS] = {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF",
        "ES", "GO", "MA", "MT", "MS", "MG", "PA",
        "PB", "PR", "PE", "PI", "RJ", "RN", "RS",
        "RO", "RR", "SC", "SP", "SE", "TO"
    };

    FILE *arquivo = fopen(arquivo_csv, "r");

    if (arquivo == NULL) {
        printf("Erro ao abrir: %s\n", arquivo_csv);
        return NULL;
    }

    VotacaoUF votacoes[TOTAL_UFS] = {0};

    for (int i = 0; i < TOTAL_UFS; i++) {
        snprintf(votacoes[i].uf, 3, "%s", ufs[i]);
    }

    char candidatos[MAX_CANDIDATOS][MAX_NOME] = {{0}};
    int qtdCandidatos = 0;
    int registros = 0;
    int erro = 0;

    char linha[512];

    if (fgets(linha, sizeof(linha), arquivo) == NULL) {
        fclose(arquivo);
        return NULL;
    }

    while (fgets(linha, sizeof(linha), arquivo)) {
        char *uf = strtok(linha, ";");
        char *candidato = strtok(NULL, ";");
        char *votos = strtok(NULL, ";");
        char *percentual = strtok(NULL, ";\r\n");

        if (!uf || !candidato || !votos || !percentual) {
            erro = 1;
            break;
        }

        int indiceUF = -1;
        int indiceCandidato = -1;

        for (int i = 0; i < TOTAL_UFS; i++) {
            if (strcmp(ufs[i], uf) == 0) {
                indiceUF = i;
                break;
            }
        }

        if (indiceUF < 0) {
            erro = 1;
            break;
        }

        for (int i = 0; i < qtdCandidatos; i++) {
            if (strcmp(candidatos[i], candidato) == 0) {
                indiceCandidato = i;
                break;
            }
        }

        if (indiceCandidato < 0) {
            if (qtdCandidatos >= MAX_CANDIDATOS) {
                erro = 1;
                break;
            }

            indiceCandidato = qtdCandidatos++;

            snprintf(
                candidatos[indiceCandidato],
                MAX_NOME,
                "%s",
                candidato
            );
        }

        votacoes[indiceUF].percentuais[indiceCandidato] =
            (float)atof(percentual) / 100.0f;

        registros++;
    }

    fclose(arquivo);

    if (erro || qtdCandidatos == 0 ||
        registros != TOTAL_UFS * qtdCandidatos) {
        printf("Erro: dados presidenciais incompletos "
               "ou invalidos.\n");
        return NULL;
    }

    Grafo *g = malloc(sizeof(Grafo));

    if (g == NULL) {
        return NULL;
    }

    inicializarGrafo(g, TOTAL_UFS, 0);

    for (int i = 0; i < TOTAL_UFS; i++) {
        definirNome(g, i, ufs[i]);
    }

    int arestas = 0;

    for (int i = 0; i < TOTAL_UFS; i++) {
        for (int j = i + 1; j < TOTAL_UFS; j++) {
            float soma = 0.0f;

            for (int k = 0; k < qtdCandidatos; k++) {
                float diferenca =
                    votacoes[i].percentuais[k] -
                    votacoes[j].percentuais[k];

                soma += diferenca * diferenca;
            }

            float distancia = sqrtf(soma);

            adicionarAresta(g, i, j, distancia);
            arestas++;
        }
    }

    printf("\nGRAFO ELEITORAL NACIONAL CONSTRUIDO\n");
    printf("----------------------------------------\n");
    printf("UFs: %d\n", TOTAL_UFS);
    printf("Candidatos: %d\n", qtdCandidatos);
    printf("Registros: %d\n", registros);
    printf("Arestas: %d\n", arestas);

    return g;
}
