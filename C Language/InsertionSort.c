#include <stdio.h>

int main()
{
    int num1;
    int num2;
    int num3;
    float avg;

    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    avg = (num1 + num2 + num3) / 3.0;
    printf("%f", avg);
    return 0;
}