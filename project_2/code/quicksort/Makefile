CC     = gcc
CFLAGS = -O3 -fopenmp

all: quicksort_par quicksort_seq

quicksort_par: quicksort_par.o walltime.o
	$(CC) $(CFLAGS) $^ -o $@

quicksort_par.o: quicksort_par.c walltime.h
	$(CC) -c $(CFLAGS) $<

quicksort_seq: quicksort_seq.o walltime.o
	$(CC) $(CFLAGS) $^ -o $@

quicksort_seq.o: quicksort_seq.c walltime.h
	$(CC) -c $(CFLAGS) $<

walltime.o: walltime.c walltime.h
	$(CC) -c $(CFLAGS) $<

.PHONY: clean
clean:
	$(RM) *.o quicksort_par quicksort_seq