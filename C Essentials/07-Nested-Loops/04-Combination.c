#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    int comb = 0;

    for (int x1 = 0; x1 < n+1; x1++){
        for (int x2 = 0; x2 < n+1; x2++){
            for (int x3 = 0; x3 < n+1; x3++){
                for (int x4 = 0; x4 < n+1; x4++){
                    for (int x5 = 0; x5 < n+1; x5++){
                        if (x1+x2+x3+x4+x5 == n){
                            comb += 1;
                        }
                    }
                }
            }
        }
    }

    printf("%d", comb);
}