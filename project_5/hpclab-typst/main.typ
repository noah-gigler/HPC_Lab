#import "hpclab-template.typ": hpclab-report
#show: doc => hpclab-report(
  project-nr: 5,
  due-date: "Monday 13 May 2024, 23:59 (midnight)",
  student-name: "Luis Wirth",
  partner-names: "",
  doc,
)

= Parallel Space Solution of a nonlinear PDE using MPI [in total 60 points]
== Initialize/finalize MPI and welcome message [5 Points]
== Domain decomposition [10 Points]
== Linear algebra kernels [5 Points]
== The diffusion stencil: Ghost cells exchange [10 Points]
== Implement parallel I/O [10 Points]
== Strong scaling [10 Points]
== Weak scaling [10 Points]
== Bonus [20 Points]: Overlapping computation/computation details

= Python for High-Performance Computing [in total 40 points]
== Sum of ranks: MPI collectives [5 Points]
== Ghost cell exchange between neighboring processes [5 Points]
== A self-scheduling example: Parallel Mandelbrot [30 Points]
