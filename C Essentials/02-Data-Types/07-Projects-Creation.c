#include <stdio.h>
#include <stdlib.h>

int main()
{
    int single_project_h = 3;
    char name[20];
    int building_c;

    scanf("%s%d", name, &building_c);
    printf("The architect %s will need %d hours to complete %d project/s.", name, building_c * single_project_h, building_c);
}