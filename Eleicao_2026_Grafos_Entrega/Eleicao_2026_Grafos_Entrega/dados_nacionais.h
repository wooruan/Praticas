
#ifndef DADOS_NACIONAIS_H
#define DADOS_NACIONAIS_H

#define TOTAL_UFS 27
#define MAX_CANDIDATOS 30

typedef struct {
    char uf[3];
    float percentuais[MAX_CANDIDATOS];
} VotacaoUF;

#endif
