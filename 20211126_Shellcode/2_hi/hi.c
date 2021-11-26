/*
 * Authors:
 * + Andrea Fioraldi <andreafioraldi@gmail.com>
 * + Pietro Borrello <pietro.borrello95@gmail.com>
 */

#include <stdio.h>
#include <string.h>

void print_flag()
{
	puts("Hey, how did you get here?! BTW, flag: ccit{hi_i_am_a_flag}");
}

int main()
{
    char msg[32];

    printf("Enter your name: ");
    fflush(stdout);
    fgets(msg, 0x32, stdin);

    printf("Hello Mr. %s\n", msg);
    fflush(stdout);
    return 0;
}
