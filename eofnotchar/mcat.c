/* mcat.c */
#include <stdio.h>

int main(int argc, char *argv[])
{
  FILE *fp;
  int c;

  if ((fp = fopen(*++argv, "r")) == NULL) {
    printf("mcat: can't open %s\n", *argv);
    return 1;
  }

  while ((c = getc(fp)) != EOF)
    putc(c, stdout);

  fclose(fp);

  return 0;
}
