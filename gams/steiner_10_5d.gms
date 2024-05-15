Sets
i Steiner points / 1*8 /
j terminals / 1*10 /
k dimensions / 1*5 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.4975365687586023; terminals('1', '2') = 0.2661737230725406; terminals('1', '3') = 0.6374111614436909; terminals('1', '4') = 0.24247975418376266; terminals('1', '5') = 0.4731685799874552; 
terminals('2', '1') = 0.9703361491117534; terminals('2', '2') = 0.08518806501099674; terminals('2', '3') = 0.31737891751820513; terminals('2', '4') = 0.6764439534894834; terminals('2', '5') = 0.0852413172296076; 
terminals('3', '1') = 0.15331752856953773; terminals('3', '2') = 0.8252738498040315; terminals('3', '3') = 0.9797228526139108; terminals('3', '4') = 0.3193386437176482; terminals('3', '5') = 0.18896898678495433; 
terminals('4', '1') = 0.9723752503414661; terminals('4', '2') = 0.3289191945502741; terminals('4', '3') = 0.6037845231084645; terminals('4', '4') = 0.6074942084317443; terminals('4', '5') = 0.6349887556504961; 
terminals('5', '1') = 0.9153921598736201; terminals('5', '2') = 0.9624532167911902; terminals('5', '3') = 0.6931477606588518; terminals('5', '4') = 0.8249037141670215; terminals('5', '5') = 0.7938285744978436; 
terminals('6', '1') = 0.6431235882103946; terminals('6', '2') = 0.43029214446042363; terminals('6', '3') = 0.2272211040366383; terminals('6', '4') = 0.26618017106327707; terminals('6', '5') = 0.9300172137798001; 
terminals('7', '1') = 0.7000659032477788; terminals('7', '2') = 0.10579514653289779; terminals('7', '3') = 0.9108122843705956; terminals('7', '4') = 0.2710858352944323; terminals('7', '5') = 0.6924618004350633; 
terminals('8', '1') = 0.4599922159807449; terminals('8', '2') = 0.26966362910775055; terminals('8', '3') = 0.2092539856889395; terminals('8', '4') = 0.5790755087347463; terminals('8', '5') = 0.41176567735033565; 
terminals('9', '1') = 0.624441898539622; terminals('9', '2') = 0.6959821132167042; terminals('9', '3') = 0.8194404253180085; terminals('9', '4') = 0.8531850128548369; terminals('9', '5') = 0.625463849213158; 
terminals('10', '1') = 0.9664042707070908; terminals('10', '2') = 0.4961049365022576; terminals('10', '3') = 0.8875502088481517; terminals('10', '4') = 0.8149762714789975; terminals('10', '5') = 0.8175560360701905; 
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
