Sets
i Steiner points / 1*8 /
j terminals / 1*10 /
k dimensions / 1*4 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.4586067093870614; terminals('1', '2') = 0.87786790373901; terminals('1', '3') = 0.031846480408982525; terminals('1', '4') = 0.2824261461537926; 
terminals('2', '1') = 0.9617911699198027; terminals('2', '2') = 0.664318734454616; terminals('2', '3') = 0.12837236942357588; terminals('2', '4') = 0.3483892327332404; 
terminals('3', '1') = 0.8797493185344203; terminals('3', '2') = 0.4407622204637107; terminals('3', '3') = 0.028632026370586927; terminals('3', '4') = 0.8961816708493071; 
terminals('4', '1') = 0.12987407341084578; terminals('4', '2') = 0.6412660792617741; terminals('4', '3') = 0.619579856895807; terminals('4', '4') = 0.4606660816810936; 
terminals('5', '1') = 0.961985163786831; terminals('5', '2') = 0.17655246550171377; terminals('5', '3') = 0.6047448911757226; terminals('5', '4') = 0.11360377259896981; 
terminals('6', '1') = 0.9655977884311789; terminals('6', '2') = 0.14480662928012233; terminals('6', '3') = 0.5130519321619571; terminals('6', '4') = 0.8326159829153793; 
terminals('7', '1') = 0.883249714790512; terminals('7', '2') = 0.0975661904170092; terminals('7', '3') = 0.8772861663183649; terminals('7', '4') = 0.8426509635375616; 
terminals('8', '1') = 0.31576362796828894; terminals('8', '2') = 0.7564780588144951; terminals('8', '3') = 0.22707288516812119; terminals('8', '4') = 0.15382194005106342; 
terminals('9', '1') = 0.16260363549282186; terminals('9', '2') = 0.30874561291554403; terminals('9', '3') = 0.8262479177966031; terminals('9', '4') = 0.46182111490147704; 
terminals('10', '1') = 0.9890392657963852; terminals('10', '2') = 0.8938422544755473; terminals('10', '3') = 0.2104608453213448; terminals('10', '4') = 0.4334176146710601; 
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
