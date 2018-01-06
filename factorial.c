#include <cs50.h>
#include <stdio.h>

// write a program the returns the factorial of user input for positive integers
int main(void)
{
    printf("Input: ");

    int x = get_int();
    if (x > 0)
    {
        int count = x;
        for(int y = x - 1; y > 0; y--)
        {
            count *= y;
        }
        printf("Output: %i\n", count);

    }
}