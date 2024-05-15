Sets
i Steiner points / 1*13 /
j terminals / 1*15 /
k dimensions / 1*2 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.5390815646058106; terminals('1', '2') = 0.2891964436397205; 
terminals('2', '1') = 0.03003690855112706; terminals('2', '2') = 0.6536357538927619; 
terminals('3', '1') = 0.21000869554973112; terminals('3', '2') = 0.2572769749796092; 
terminals('4', '1') = 0.39719826263322744; terminals('4', '2') = 0.6415781537746728; 
terminals('5', '1') = 0.9888112104037214; terminals('5', '2') = 0.46153301006262504; 
terminals('6', '1') = 0.9934850076016687; terminals('6', '2') = 0.9925719941586278; 
terminals('7', '1') = 0.24267553557344324; terminals('7', '2') = 0.07264511287134134; 
terminals('8', '1') = 0.159901022229618; terminals('8', '2') = 0.8419027314789557; 
terminals('9', '1') = 0.5995547289462685; terminals('9', '2') = 0.9174626648558603; 
terminals('10', '1') = 0.9721691074362717; terminals('10', '2') = 0.6544238205879963; 
terminals('11', '1') = 0.535204782203361; terminals('11', '2') = 0.06763103158333483; 
terminals('12', '1') = 0.023510063056781383; terminals('12', '2') = 0.8052942869277137; 
terminals('13', '1') = 0.6719697138652216; terminals('13', '2') = 0.7630117418529349; 
terminals('14', '1') = 0.5656524680218609; terminals('14', '2') = 0.6738937592389419; 
terminals('15', '1') = 0.6387228188088844; terminals('15', '2') = 0.8951756504920998; 
Parameter bigM / 1.4142135623730951 /;
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
