#let hpclab-report(
  project-nr: "PROVIDE ARG `project-nr`",
  due-date: "PROVIDE ARG `due-date`",
  student-name: "PROVIDE ARG `student-name`",
  partner-names: "PROVIDE ARG `partner-names`",
  doc,
) = [
  #set page(paper: "a4")
  #set page(margin: 2cm)
  #set text(11pt)
  #set text(font: "New Computer Modern")
  #show math.equation: set text(font: "New Computer Modern Math")

  #set heading(numbering: "1.1.")
  #show heading: text.with(size: 0.9em, weight: "bold")

  #image("ethz.svg", width: 36%)

  *High-Performance Computing Lab for CSE*
  #h(1fr)
  *2024*

  Student: #student-name
  #h(1fr)
  Discussed with: #partner-names

  #line(length: 100%)
  #text(15pt)[*Solution for Project #project-nr*]
  #h(1fr)
  Due date: #h(1em) #due-date.
  #line(length: 100%)

  #align(center)[#scale(80%)[#block(stroke: black, inset: 1em)[
    #set align(left + top)

    #align(center)[#strong[
      #text(13pt)[HPC Lab for CSE 2024 --- Submission Instructions] \
      (Please, notice that following instructions are mandatory: \
      submissions that don't comply with, won't be considered)
    ]]

    - Assignments must be submitted to #link("https://moodle-app2.let.ethz.ch/
      course/view.php?id=22516")[Moodle] (i.e. in electronic format).
    - Provide both executable package and sources (e.g. C/C++ files, Matlab).
      If you are using libraries, please add them in the file. Sources must be
      organized in directories called: \
      #align(center)[`Project_number_lastname_firstname`]
      and the file must be called: \
      #align(center)[
        `project_number_lastname_firstname.zip` \
        `project_number_lastname_firstname.pdf`
      ]
    - The TAs will grade your project by reviewing your project write-up, and
      looking at the implementation you attempted, and benchmarking your code's
      performance.
    - You are allowed to discuss all questions with anyone you like; however: (i)
      your submission must list anyone you discussed problems with and (ii) you
      must write up your submission independently.
  ]]]

  #doc
]
