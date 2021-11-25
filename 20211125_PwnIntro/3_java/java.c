/*
 * Authors:
 * + Andrea Fioraldi <andreafioraldi@gmail.com>
 * + Pietro Borrello <pietro.borrello95@gmail.com>
 */

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

struct programmer_t
{
    char favourite_lang[32];
    void (*call)();
};
typedef struct programmer_t programmer_t;

void python()
{
    printf("Maybe you want a python shell...\n");
    sleep(3);
    execlp("/bin/sh", "/bin/sh", "-c", "echo 'python shell'", NULL);
}

void bash()
{
    printf("Opening bash shell...\n");
    sleep(3);
    printf("are you sure you don't prefer java?\n");
    if(rand() != 328347) return;
    // if only there was a way to jump here...
    execlp("/bin/sh", "/bin/sh", NULL);
}

void nothing()
{
    execlp("/bin/sh", "/bin/sh", "-c", "", NULL);
}


int main(int argc, char** argv)
{
    programmer_t user = {0};

    printf("Enter your favourite programming language: ");
    fflush(stdout);
    int i = 0;
    char c;
    while ((c = getchar()) != '\n')
        user.favourite_lang[i++] = c;

    if(!strncmp(user.favourite_lang, "java", 4)) {
        printf("Just another Java noob...\n");
    }
    else if (!strncmp(user.favourite_lang, "python", 6)) {
        user.call = python;
    }
    else if (!strncmp(user.favourite_lang, "bash", 4)) {
        user.call = bash;
    }
    else {
        user.call = nothing;
    }
    if(user.call) user.call();
    return 0;
}
