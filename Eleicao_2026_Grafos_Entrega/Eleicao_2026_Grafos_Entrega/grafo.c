
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "grafo.h"

void inicializarGrafo(Grafo *g, int vertices, int direcionado) {
    g->quantidadeRAs = 0;
    if (vertices < 0 || vertices > MAX_VERTICES) {
        printf("Quantidade de vertices invalida!\n");
        exit(1);
    }

    g->quantidadeVertices = vertices;
    g->direcionado = direcionado;

    for (int i = 0; i < vertices; i++) {
        g->adjacencia[i].inicio = NULL;
        g->nomes[i][0] = '\0';
    }
}

void definirNome(Grafo *g, int vertice, const char *nome) {
    if (vertice < 0 || vertice >= g->quantidadeVertices) {
        return;
    }

    snprintf(g->nomes[vertice], MAX_NOME, "%s", nome);
}

static void inserirNaLista(Grafo *g, int origem, int destino, float peso) {
    No *novo = malloc(sizeof(No));

    if (novo == NULL) {
        printf("Erro de alocacao de memoria!\n");
        exit(1);
    }

    novo->destino = destino;
    novo->peso = peso;
    novo->proximo = g->adjacencia[origem].inicio;
    g->adjacencia[origem].inicio = novo;
}

void adicionarAresta(Grafo *g, int origem, int destino, float peso) {
    if (origem < 0 || origem >= g->quantidadeVertices ||
        destino < 0 || destino >= g->quantidadeVertices) {
        printf("Aresta invalida!\n");
        return;
    }

    inserirNaLista(g, origem, destino, peso);

    if (!g->direcionado && origem != destino) {
        inserirNaLista(g, destino, origem, peso);
    }
}

void mostrarGrafo(Grafo *g) {
    for (int i = 0; i < g->quantidadeVertices; i++) {
        const char *nome = g->nomes[i][0] ? g->nomes[i] : "Sem nome";

        printf("%d - %s: ", i, nome);

        No *atual = g->adjacencia[i].inicio;

        while (atual != NULL) {
            printf("%d(%.4f) -> ", atual->destino, atual->peso);
            atual = atual->proximo;
        }

        printf("NULL\n");
    }
}

void liberarGrafo(Grafo *g) {
    for (int i = 0; i < g->quantidadeVertices; i++) {
        No *atual = g->adjacencia[i].inicio;

        while (atual != NULL) {
            No *proximo = atual->proximo;
            free(atual);
            atual = proximo;
        }

        g->adjacencia[i].inicio = NULL;
    }
}

int calcularGrau(Grafo *g, int vertice) {
    if (vertice < 0 || vertice >= g->quantidadeVertices) {
        return -1;
    }

    int grau = 0;
    No *atual = g->adjacencia[vertice].inicio;

    while (atual != NULL) {
        grau++;
        atual = atual->proximo;
    }

    return grau;
}

void buscaProfundidade(Grafo *g, int vertice, int visitados[]) {
    visitados[vertice] = 1;

    const char *nome = g->nomes[vertice][0]
        ? g->nomes[vertice]
        : "Sem nome";

    printf("%s ", nome);

    No *atual = g->adjacencia[vertice].inicio;

    while (atual != NULL) {
        if (!visitados[atual->destino]) {
            buscaProfundidade(g, atual->destino, visitados);
        }

        atual = atual->proximo;
    }
}

int contarComponentes(Grafo *g) {
    int visitados[MAX_VERTICES] = {0};
    int componentes = 0;

    for (int i = 0; i < g->quantidadeVertices; i++) {
        if (!visitados[i]) {
            componentes++;

            printf("\nComponente %d: ", componentes);
            buscaProfundidade(g, i, visitados);
            printf("\n");
        }
    }

    return componentes;
}
