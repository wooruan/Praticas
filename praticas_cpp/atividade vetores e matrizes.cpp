#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int encontraMaior(int arr[]){
	int a = arr[0];
	for (int i=0; i<10; i+=1){
		if (arr[i]>a){
			a = arr[i];
		}
	}
	printf("\nO maior Numero do vetor: %d", a);
	return a;
}
int main(){
	srand(time(NULL));
	
    int vetor [10];
    for (int i = 0; i<10; i++){
    	vetor[i] = rand() % 100;
	}
	
	int a = 0;
	printf("Vetor: ");
	while (1){
		printf("[%d] ", vetor[a]);
		a+=1;
		if (a>=10){
			break;
		}
	}	
	encontraMaior(vetor);
}