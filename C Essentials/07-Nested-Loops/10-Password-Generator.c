#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n,l;
    scanf("%d %d", &n, &l);

    for (int symb1 = 1; symb1 < n+1; symb1++){
        for (int symb2 = 1; symb2 < n+1; symb2++){
            for (int symb3 = 97; symb3 < 97+l; symb3++){
                for (int symb4 = 97; symb4 < 97+l; symb4++){
                    for (int symb5 = 1; symb5 < n+1; symb5++){
                        if (symb5 > symb1 && symb5 > symb2){
                            printf("%d%d%c%c%d ", symb1, symb2, symb3, symb4, symb5);
                        }
                    }
                }
            }
        }
    }
}