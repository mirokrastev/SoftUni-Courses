#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
    int num_one, num_two, num_tree;
    scanf("%d%d%d", &num_one, &num_two, &num_tree);
    bool num_one_b = false;
    bool num_two_b = false;
    bool num_three_b = false;

   if (num_one == num_two){
       num_one_b = true;
   } if (num_one == num_tree){
       num_two_b = true;
   } if (num_two == num_tree){
       num_three_b = true;
   }

   if (num_one_b == true && num_two_b == true && num_three_b == true){
       printf("yes");
   }
   else{
        printf("no");
    }
}