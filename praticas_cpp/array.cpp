#include <stdio.h>
#include <string.h>

// Definição da struct
struct Livro {
    char titulo[50];
    int paginas;
    float preco;
};

int main() {
    // Criando a variável
    struct Livro meuLivro;
    
    // Atribuindo valores
    strcpy(meuLivro.titulo, "A Linguagem de Programacao C");
    meuLivro.paginas = 280;
    meuLivro.preco = 59.90;
    
    // Imprimindo valores
    printf("Titulo: %s\n", meuLivro.titulo);
    printf("Paginas: %d\n", meuLivro.paginas);
    printf("Preco: R$ %.2f\n", meuLivro.preco);
    
    return 0;
}
