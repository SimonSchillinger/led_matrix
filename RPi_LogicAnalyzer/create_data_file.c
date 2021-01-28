/* fwrite example : write buffer */
#include <stdio.h>

int main ()
{
  FILE * pFile;
  char buffer[] = { 'x' , 'y' , 'z' };
  int a = 12;
  pFile = fopen ("myfile.bin", "w");
  fwrite (&a , sizeof(int), sizeof(&a), pFile);
  fclose (pFile);
  return 0;
}
