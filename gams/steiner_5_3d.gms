Sets
i Steiner points / 1*3 /
j terminals / 1*5 /
k dimensions / 1*3 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.965242141552123; terminals('1', '2') = 0.011654693792141124; terminals('1', '3') = 0.7359916197968754; 
terminals('2', '1') = 0.15801272476474815; terminals('2', '2') = 0.9863394516628233; terminals('2', '3') = 0.016880654207976242; 
terminals('3', '1') = 0.8794912681346712; terminals('3', '2') = 0.6813506644014146; terminals('3', '3') = 0.8573423824815248; 
terminals('4', '1') = 0.9998162341661194; terminals('4', '2') = 0.23971518216378862; terminals('4', '3') = 0.33807775725669986; 
terminals('5', '1') = 0.7081943329851277; terminals('5', '2') = 0.28058168584313725; terminals('5', '3') = 0.2633142571474607; 
Parameter bigM / 1.7320508075688772 /;
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
