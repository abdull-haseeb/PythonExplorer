#include <stdio.h>

void Draw_Horizontal();
void Draw_Vertical();

int main() {
    Draw_Horizontal();
    Draw_Vertical();
    getchar();  // Using getchar() to wait for a key press instead of getch()
    return 0;
}

void Draw_Horizontal() {
    int i;
    for (i = 0; i <= 25; i++) {
        printf("*");
    }
    printf("\n");  // Add a newline character to move to the next line
}

void Draw_Vertical() {
    int i;
    for (i = 0; i < 10; i++) {
        printf("*\n");
    }
}
