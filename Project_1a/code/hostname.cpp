#include <unistd.h>
#include <limits.h>

char hostname[HOST_NAME_MAX];
gethostname(hostname, HOST_NAME_MAX);