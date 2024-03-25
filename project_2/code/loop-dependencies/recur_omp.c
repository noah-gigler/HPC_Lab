#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "walltime.h"
#include <omp.h>

int main(int argc, char *argv[]) {
  int N = 2000000000;
  double up = 1.00000001;
  double Sn = 1.00000001;
  int n;
  /* allocate memory for the recursion */
  double *opt = (double *)malloc((N + 1) * sizeof(double));
  if (opt == NULL) {
    perror("failed to allocate problem size");
    exit(EXIT_FAILURE);
  }

  double time_start = walltime();

  #pragma omp parallel private(n)
  {
    int nthreads = omp_get_num_threads();
    int tid = omp_get_thread_num();
    int chunk = N / nthreads;
    int start = tid * chunk;
    int end = (start + chunk < N) ? start + chunk : N+1;
    double local_Sn = pow(up, start + 1);
    for (n = start; n < end; ++n) {
      opt[n] = local_Sn;
      local_Sn *= up;
    }
    if(tid == nthreads - 1){
      Sn = local_Sn;
    }
  }
  printf("Parallel RunTime  :  %f seconds\n", walltime() - time_start);
  printf("Final Result Sn   :  %.17g \n", Sn);

  double temp = 0.0;
  for (n = 0; n <= N; ++n) {
    temp += opt[n] * opt[n];
  }
  printf("Result ||opt||^2_2 :  %f\n", temp / (double)N);
  printf("\n");

  return 0;
}
