Sets
i Steiner points / 1*3 /
j terminals / 1*5 /
k dimensions / 1*4 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.9056396761745207; terminals('1', '2') = 0.6862541570267026; terminals('1', '3') = 0.7665092563626442; terminals('1', '4') = 0.9046162378132736; 
terminals('2', '1') = 0.2598274474889769; terminals('2', '2') = 0.6357258696059892; terminals('2', '3') = 0.9049456946664788; terminals('2', '4') = 0.8721303740697106; 
terminals('3', '1') = 0.5729406692492218; terminals('3', '2') = 0.1693780871255699; terminals('3', '3') = 0.4115230620409567; terminals('3', '4') = 0.9938380127773296; 
terminals('4', '1') = 0.10324779991117994; terminals('4', '2') = 0.31913914884928973; terminals('4', '3') = 0.9500391079535002; terminals('4', '4') = 0.4494007558523254; 
terminals('5', '1') = 0.20865257233244294; terminals('5', '2') = 0.316903983245593; terminals('5', '3') = 0.9086358448961127; terminals('5', '4') = 0.33556881046847387; 
Parameter bigM / 2.0 /;
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
