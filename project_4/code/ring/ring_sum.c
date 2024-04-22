#include <mpi.h> // MPI
#include <stdio.h>

int main(int argc, char *argv[]) {

  // Initialize MPI, get size and rank
  int size, rank;
  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  int sum = 0; // initialize sum
  printf("Process %i: Sum = %i\n", rank, sum);
  int next = (rank + 1) % size;
  int prev = (rank - 1) % size;

  MPI_Status status;
  int p_rank = rank;
  int n_rank;

  for(int i = 0; i < size; ++i) {
    MPI_Send(&p_rank, 1, MPI_INT, next, 0, MPI_COMM_WORLD);
    MPI_Recv(&n_rank, 1, MPI_INT, next, 0, MPI_COMM_WORLD, &status);

    sum += n_rank;
    p_rank = n_rank;
  }

  printf("Process %i: Sum = %i\n", rank, sum);

  // Finalize MPI
  MPI_Finalize();

  return 0;
}
