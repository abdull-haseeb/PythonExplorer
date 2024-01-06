#include <stdio.h>

int main() {
    int rows, cols;

    // Get the number of rows and columns from the user
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printf("Enter the number of columns: ");
    scanf("%d", &cols);

    // Print the star pattern
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= cols; ++j) {
            printf("* ");
        }
        printf("\n");
    }

    return 0;
}
