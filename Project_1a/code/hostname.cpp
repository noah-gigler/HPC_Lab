#include <unistd.h>
#include <limits.h>
#include <iostream>

int main() {
    char hostname[HOST_NAME_MAX];
    gethostname(hostname, HOST_NAME_MAX);
    std::cout << "Hostname: " << hostname << std::endl;
    std::cout << "hi"<< std::endl;
    return 0;
}
