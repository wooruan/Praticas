
#ifndef GRAFO_H
#define GRAFO_H

#define MAX_VERTICES 100
#define MAX_NOME 100

typedef struct No {
    int destino;
    float peso;
    struct No *proximo;
} No;

typedef struct Lista {
    No *inicio;
} Lista;

typedef struct Grafo {
    int quantidadeVertices;
    int quantidadeRAs;
    int direcionado;

    char nomes[MAX_VERTICES][MAX_NOME];
    Lista adjacencia[MAX_VERTICES];
} Grafo;

void inicializarGrafo(Grafo *g, int vertices, int direcionado);
void adicionarAresta(Grafo *g, int origem, int destino, float peso);
void definirNome(Grafo *g, int vertice, const char *nome);
void mostrarGrafo(Grafo *g);
void liberarGrafo(Grafo *g);


int calcularGrau(Grafo *g, int vertice);
void buscaProfundidade(Grafo *g, int vertice, int visitados[]);
int contarComponentes(Grafo *g);

#endif
