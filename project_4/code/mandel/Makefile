CC=mpicc
CFLAGS=-O3 -lpng 

all: mandel_mpi

mandel_mpi:  mandel_mpi.c pngwriter.c consts.h
	$(CC) $^ $(CFLAGS) -o $@

clean:
	rm -f mandel_mpi

