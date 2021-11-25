#include <stdio.h>
#include <string.h>

//credits: https://www.thegeekstuff.com/2013/06/buffer-overflow/

int main(void)
{
    int pass = 0;
    char buff[8];


    printf("\n Enter the password : \n");
    gets(buff);

    if(pass)
    {
       /* Now Give root or admin rights to user*/
        printf ("Correct password! \nFlag={hello_world_pwn}\n");
    }
    else{
      printf("Wrong password. Status%d\n", pass);
    }

    return 0;
}
