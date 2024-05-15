Sets
i Steiner points / 1*3 /
j terminals / 1*5 /
k dimensions / 1*5 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.376962302390386; terminals('1', '2') = 0.9267885077263207; terminals('1', '3') = 0.8434467391322422; terminals('1', '4') = 0.21404576995204339; terminals('1', '5') = 0.8717081122454375; 
terminals('2', '1') = 0.6364617457506916; terminals('2', '2') = 0.04239212615820076; terminals('2', '3') = 0.9529720601244589; terminals('2', '4') = 0.25568366821646715; terminals('2', '5') = 0.305900980269444; 
terminals('3', '1') = 0.4240801565062292; terminals('3', '2') = 0.5885140140252595; terminals('3', '3') = 0.1243916494838736; terminals('3', '4') = 0.686677304871223; terminals('3', '5') = 0.8322405233765763; 
terminals('4', '1') = 0.5123190504571955; terminals('4', '2') = 0.7944608177634946; terminals('4', '3') = 0.6249799602888791; terminals('4', '4') = 0.8248125234140684; terminals('4', '5') = 0.18093878439654187; 
terminals('5', '1') = 0.358677331460587; terminals('5', '2') = 0.46939438227304753; terminals('5', '3') = 0.1039841315397021; terminals('5', '4') = 0.9731064575430529; terminals('5', '5') = 0.6360295241926393; 
Parameter bigM / 2.23606797749979 /;
Positive Variables distance_Steiner_Steiner(i,ii), distance_Steiner_terminal(i,j), Steiner_points(i,k);
Steiner_points.up(i,k) = 1; distance_Steiner_Steiner.up(i,ii) = bigM; distance_Steiner_terminal.up(i,j) = bigM;
Binary Variables is_connected_Steiner_Steiner(i,ii), is_connected_Steiner_terminal(i,j);
Variable objective;
Equations objective_definition, distance_Steiner_Steiner_def(i,ii), distance_Steiner_terminal_def(i,j), assignment(j), cardinality(i), Steiner_connectivity(i);
objective_definition.. objective =e= sum(i, sum(ii$(ord(i)<ord(ii)), distance_Steiner_Steiner(i,ii)) + sum(j, distance_Steiner_terminal(i,j)));
distance_Steiner_Steiner_def(i,ii)$(ord(i)<ord(ii)).. distance_Steiner_Steiner(i,ii) =g= sqrt(sum(k, power(Steiner_points(i,k) - Steiner_points(ii,k), 2))) - bigM * (1 - is_connected_Steiner_Steiner(i,ii));
distance_Steiner_terminal_def(i,j).. distance_Steiner_terminal(i,j) =g= sqrt(sum(k, power(Steiner_points(i,k) - terminals(j,k), 2))) - bigM * (1 - is_connected_Steiner_terminal(i,j));
assignment(j).. sum(i, is_connected_Steiner_terminal(i,j)) =e= 1;
cardinality(i).. sum(j, is_connected_Steiner_terminal(i,j)) + sum(ii$(ord(ii)<ord(i)), is_connected_Steiner_Steiner(ii,i)) + sum(ii$(ord(i)<ord(ii)), is_connected_Steiner_Steiner(i,ii)) =e= 3;
Steiner_connectivity(i)$(ord(i)>1).. sum(ii$(ord(ii)<ord(i)), is_connected_Steiner_Steiner(ii,i)) =e= 1;
Model m / all /;
Solve m using minlp minimizing objective;
