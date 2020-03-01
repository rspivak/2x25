/* syscat.c */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  int fd;
  char c;

  fd = open(argv[1], O_RDONLY, 0);

  while (read(fd, &c, 1) != 0)
    write(STDOUT_FILENO, &c, 1);

  return 0;
}
