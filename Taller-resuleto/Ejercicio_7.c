
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int result = 0;
    int *arreglo;
    // the number of temperatures to analyse
    int n;
    scanf("%d", &n);
    arreglo = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) {
        // a temperature expressed as an integer ranging from -273 to 5526
        int t;
        scanf("%d", &t);
        arreglo[i]=t;
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");
    int menor_positivo = 0;
    int menor_negativo = 0;
    int ban_n = 0;
    int ban_p = 0;
    //Inicializando menor_negativo
    for (int i = 0; i < n; i++){
        if(arreglo[i]<0){
            menor_negativo=arreglo[i];
            ban_n = 1;
            break;
        }
    }
    //Inicializando menor_positivo
    for (int i = 0; i < n; i++){
        if(arreglo[i]>0){
            menor_positivo=arreglo[i];
            ban_p = 1;
            break;
        }
    }
    for (int i = 0; i < n; i++) {
        //Para los datos positivos
        if(arreglo[i]>0){
            if(arreglo[i]<=menor_positivo){
                menor_positivo = arreglo[i];
            }
        }
        //Para los datos Negativos
         if(arreglo[i]<0){
            if(arreglo[i]>menor_negativo){
                menor_negativo = arreglo[i];
            }
        }
    }//Fin del for

    if(menor_negativo<0 && menor_negativo>=-273 && n>0 && menor_positivo>0 && menor_positivo<=5526 && ban_n==1 && ban_p ==1){
        //Primer caso
        if(menor_negativo*-1 < menor_positivo && n>0){
            result = menor_negativo;
        }
        //Segundo caso
        else if(menor_negativo*-1 == menor_positivo && n>0){
            result = menor_positivo;
        }
        //Tercer caso
        else if(menor_negativo*-1 > menor_positivo && n>0){
            result = menor_positivo;
        }
    }
    else if(n<=0 && ban_p==0 && ban_n ==0){
        result = 0;
    }
    else if(menor_negativo <= -274 || menor_positivo>5526){
        result = 0;
    }

    else if(ban_n==1 && ban_p == 0 && menor_negativo > -274 ){
        result = menor_negativo;
    }
    else if(ban_p==1 && ban_n == 0 && menor_positivo<5527 ){
        result = menor_positivo;
    }

    printf("%d",result);
    free(arreglo);
    return 0;
}
