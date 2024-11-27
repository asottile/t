#include <assert.h>
#include <spawn.h>
#include <stdio.h>
#include <sys/wait.h>
#include <time.h>

int main(void) {
    struct timespec ts;
    assert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    unsigned long long t0 = ts.tv_sec * (1000 * 1000 * 1000) + ts.tv_nsec;

    pid_t pid;
    char* argv[] = {"/usr/bin/python3", "-c", "", NULL};
    assert(posix_spawn(&pid, argv[0], NULL, NULL, &argv[0], NULL) == 0);
    int exit_code;
    waitpid(pid, &exit_code, 0);

    assert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    unsigned long long t1 = ts.tv_sec * (1000 * 1000 * 1000) + ts.tv_nsec;

    printf("%lld\n", (t1 - t0));
}
