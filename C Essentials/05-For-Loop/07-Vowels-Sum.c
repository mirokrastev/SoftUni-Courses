#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char inp[50];
    gets(inp);
    int sum = 0;

    for (int i = 0; i < strlen(inp); i++){
        char current_char = inp[i];

        if (current_char == 'a'){
            sum += 1;
        }
        else if (current_char == 'e'){
            sum += 2;
        }
        else if (current_char == 'i'){
            sum += 3;
        }
        else if (current_char == 'o'){
            sum += 4;
        }
        else if (current_char == 'u'){
            sum += 5;
        }
    }

    printf("%d", sum);
}