#include <stdio.h>
#include <stdlib.h>

int main()
{
    int number_flags;
    scanf("%d", &number_flags);

    int total_cost = 0;
    total_cost = 900*number_flags;
    printf("%d\n", total_cost);
}