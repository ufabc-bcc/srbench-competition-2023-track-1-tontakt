Andrzej Odrzywołek, andrzej.odrzywolek@uj.edu.pl

I have limited experience with multidimensional functions. Until now, I have primarily worked on the recognition of single, 
two, or at most four variables, and the fitting of functions with up to seven variables. Consequently, my tools and 
strategies were not effective, particularly for datasets 1 & 3. I quickly realized that I lacked the procedures and 
ability to automatically handle data with a varying number of dimensions. Coding 16-variable functions by hand is 
time-consuming, especially when compared to cases with 1 or 2 variables.

I attempted three approaches:

Brute-force enumeration of formulas using virtual RPN-style code.
PySR with a custom set of operators and functions.
Rational function fits.
Regrettably, the brute-force enumeration was not parallelized (in Mathematica code), hence the depth of the search was 
extremely limited. Nonetheless, some "trivial" formulas for dataset 2 were discovered, with R2>0.3. A slightly modified 
search with a free parameter fit was not completed.

PySR often stalled at maximum complexity with not very large R2 values. I attempted to move into complex formula search, 
as I typically do, but encountered technical issues. I realized too late that the scoring system does not penalize free 
parameters, resulting in a search that was far from optimal.

Upon inspecting dataset 2, I noticed that all the data is in the form of rational numbers, with the exception of x6 which 
was multiplied by Pi/45. The only analytical function capable of this is a rational function. Indeed, various order 
rational fits worked exceptionally well, sometimes with R2>0.999 for 250 free parameters. However, the exact form of 
this formula was not discovered. Either the monomial order is much higher than I anticipated, or the formula involves 
some integer functions.

The final formulas are:

Dataset 1: PySR
Dataset 2: RPN-enumeration
Dataset 3: Rational fit

I faced a dilemma when deciding which formula to choose for dataset 2: a very simple one (aiming at simplicity score) 
or a rational fit (aiming at R2). The competition was a lot of fun, and I learned a great deal. I hope to be much 
better prepared next time.
