# EuclidLib: A library of nonconvex optimization problems involving the Euclidean norm

This repository hosts EuclidLib, a collection of nonconvex optimization problem instances involving the Euclidean norm from various applications across mathematics, science, and engineering.
These problems are known to be particularly challenging for deterministic global optimization solvers due to their inherent symmetries as well as the presence of reverse convex constraints involving the Euclidean norm.
The purpose of EuclidLib is to provide a benchmark to assist in algorithm development.
Instances are provided in GAMS, JuMP, and Pyomo formats.

The following problems are currently included in EuclidLib: 
* The kissing number problem[^1]
* The Euclidean Steiner tree problem[^2]
* The $k$-means clustering problem[^3]
* Lennard-Jones cluster energy minimization[^4]
* Morse cluster energy minimization[^4]
* The Thomson problem[^5]
* The Tammes problem[^6]
* The circle packing problem[^7]
* The planar $p$-median problem[^8]
* The planar capacitated $p$-median problem[^9]
* The planar multiple obnoxious facility location problem[^10]

## Citation

If you use EuclidLib in your work, please cite:
Citation details will go here.

[^1]: S. Kucherenko, P. Belotti, L. Liberti, and N. Maculan. New formulations for the Kissing number problem. *Discrete Applied Mathematics* **155**(14), 1837-1841 (2007).
[^2]: M. Fampa and N. Maculan. Using a conic formulation for finding Steiner minimal trees. *Numerical Algorithms* **35**, 315-330 (2004).
[^3]: H. D. Sherali and J. Desai. A global optimization RLT-based approach for solving the hard clustering problem. *Joural of Global Optimization* **32**, 281-306 (2005).
[^4]: The Cambridge Cluster Database, D. J. Wales, J. P. K. Doye, A. Dullweber, M. P. Hodges, F. Y. Naumkin F. Calvo, J. Hernández-Rojas and T. F. Middleton, URL [http://www-wales.ch.cam.ac.uk/CCD.html](http://www-wales.ch.cam.ac.uk/CCD.html)
[^5]: "Thomson problem", Wikipedia, URL [https://en.wikipedia.org/wiki/Thomson_problem](https://en.wikipedia.org/wiki/Thomson_problem)
[^6]: "Tammes problem", Wikipedia, URL [https://en.wikipedia.org/wiki/Tammes_problem](https://en.wikipedia.org/wiki/Tammes_problem)
[^7]: E. Specht. Packomania, URL [http://packomania.com/](http://packomania.com/)
[^8]: P. Chen, P. Hansen, B. Jaumard, and H. Tuy. Weber's problem with attraction and repulsion. *Journal of Regional Science* **32**, 467-486 (1992).
[^9]: H. D. Sherali and C. H. Tuncbilek. A squared-Euclidean distance location-allocation problem. *Naval Research Logistics* **39**, 447-469 (1992).
[^10]: Z. Drezner, P. Kalczynski, and S. Salhi. The planar multiple obnoxious facilities location problem: A Voronoi based heuristic. *Omega* **87**, 105-116 (2019).