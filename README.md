# EuclidLib: A library of nonconvex optimization problems involving the Euclidean norm

This repository hosts EuclidLib, a collection of nonconvex optimization problem instances involving the Euclidean norm from various applications across mathematics, science, and engineering.
These problems are known to be particularly challenging for deterministic global optimization solvers due to their inherent symmetries as well as the presence of reverse convex constraints involving the Euclidean norm.
The purpose of EuclidLib is to provide a benchmark to assist in algorithm development.
Instances are provided in GAMS, JuMP, and Pyomo formats.

There are currently six types of problems represented in EuclidLib: 
* Morse cluster energy minimization[^1]
* Lennard-Jones cluster energy minimization[^1]
* The Thomson problem[^2]
* The planar multiple obnoxious facility location problem[^3]
* The circle packing problem[^4]
* The kissing number problem[^5]

[^1]: The Cambridge Cluster Database, D. J. Wales, J. P. K. Doye, A. Dullweber, M. P. Hodges, F. Y. Naumkin F. Calvo, J. Hernández-Rojas and T. F. Middleton, URL [http://www-wales.ch.cam.ac.uk/CCD.html](http://www-wales.ch.cam.ac.uk/CCD.html)
[^2]: "Thomson problem", Wikipedia, URL [https://en.wikipedia.org/wiki/Thomson_problem](https://en.wikipedia.org/wiki/Thomson_problem)
[^3]: Z. Drezner, P. Kalczynski, and S. Salhi. The planar multiple obnoxious facilities location problem: A Voronoi based heuristic. *Omega* **87**, 105-116 (2019).
[^4]: E. Specht. Packomania, URL [http://packomania.com/](http://packomania.com/)
[^5]: S. Kucherenko, P. Belotti, L. Liberti, and N. Maculan. New formulations for the Kissing number problem. *Discrete Applied Mathematics* **155**(14), 1837-1841 (2007).