const char* dgemm_desc = "Blocked dgemm.";

/* This routine performs a dgemm operation
 *
 *  C := C + A * B
 *
 * where A, B, and C are lda-by-lda matrices stored in column-major format.
 * On exit, A and B maintain their input values.
 */
#define min(a, b) ((a) < (b) ? (a) : (b))

void square_dgemm(int n, double* restrict A, double* restrict B, double* restrict C) {
  // TODO: Implement the blocking optimization
  //       (The following is a placeholder naive three-loop dgemm)
  int block_size = 146;
  // #pragma ivdep
  // #pragma vector aligned
  for (int j = 0; j < n; j += block_size) {
    for (int k = 0; k < n; k += block_size) {
      for (int i = 0; i < n; i += block_size) {
        for (int j1 = j; j1 < min(j + block_size, n); j1++) {
          for (int k1 = k; k1 < min(k + block_size, n); k1++) {
            double b = B[k1 + j1 * n];
            for (int i1 = i; i1 < min(i + block_size, n); i1++) {
              C[i1 + j1 * n] += A[i1 + k1 * n] * b;
            }
          }
        }
      }
    }
  }
}
