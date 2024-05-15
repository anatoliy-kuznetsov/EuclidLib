Sets
i Steiner points / 1*13 /
j terminals / 1*15 /
k dimensions / 1*5 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.45084513414500904; terminals('1', '2') = 0.4366195682760844; terminals('1', '3') = 0.04163444585203002; terminals('1', '4') = 0.7676272579584664; terminals('1', '5') = 0.6734553564483233; 
terminals('2', '1') = 0.670857540712527; terminals('2', '2') = 0.472665488047444; terminals('2', '3') = 0.672731114024884; terminals('2', '4') = 0.8824812534975449; terminals('2', '5') = 0.6920224414883532; 
terminals('3', '1') = 0.3456424258652263; terminals('3', '2') = 0.897323531600062; terminals('3', '3') = 0.3169943908371815; terminals('3', '4') = 0.08378401217902964; terminals('3', '5') = 0.2511840930177276; 
terminals('4', '1') = 0.49653521716587157; terminals('4', '2') = 0.8612924863730758; terminals('4', '3') = 0.3477168575425721; terminals('4', '4') = 0.6615424192381595; terminals('4', '5') = 0.2680635035686557; 
terminals('5', '1') = 0.027492190735120214; terminals('5', '2') = 0.975830678205581; terminals('5', '3') = 0.5725079974762737; terminals('5', '4') = 0.4627928206739904; terminals('5', '5') = 0.676105217625283; 
terminals('6', '1') = 0.13167765137927434; terminals('6', '2') = 0.8772422533001436; terminals('6', '3') = 0.30212459335273456; terminals('6', '4') = 0.9589299306054163; terminals('6', '5') = 0.1684676992378059; 
terminals('7', '1') = 0.4631605820201776; terminals('7', '2') = 0.3075046464306209; terminals('7', '3') = 0.6161047422348818; terminals('7', '4') = 0.06036679498995601; terminals('7', '5') = 0.055585229920206314; 
terminals('8', '1') = 0.32388656731438237; terminals('8', '2') = 0.05792786993199972; terminals('8', '3') = 0.8135525615007164; terminals('8', '4') = 0.11918904488489845; terminals('8', '5') = 0.3074172166187361; 
terminals('9', '1') = 0.5224218716951496; terminals('9', '2') = 0.11445496716294967; terminals('9', '3') = 0.9526471232336744; terminals('9', '4') = 0.29191369035574544; terminals('9', '5') = 0.5653246839270838; 
terminals('10', '1') = 0.21125847741287684; terminals('10', '2') = 0.24527434539791804; terminals('10', '3') = 0.6289970479606978; terminals('10', '4') = 0.7068457529300446; terminals('10', '5') = 0.7943561377121612; 
terminals('11', '1') = 0.9522420339595141; terminals('11', '2') = 0.9326354363859527; terminals('11', '3') = 0.4449382446418748; terminals('11', '4') = 0.018772017414026565; terminals('11', '5') = 0.1570753065990531; 
terminals('12', '1') = 0.8796213188443197; terminals('12', '2') = 0.9757325913906182; terminals('12', '3') = 0.5478578093651233; terminals('12', '4') = 0.00973548730106566; terminals('12', '5') = 0.27048086044812103; 
terminals('13', '1') = 0.7382526421375969; terminals('13', '2') = 0.18734997029644274; terminals('13', '3') = 0.2597432271723712; terminals('13', '4') = 0.42962015792230956; terminals('13', '5') = 0.7073477915737445; 
terminals('14', '1') = 0.7480253586345234; terminals('14', '2') = 0.39775488720466023; terminals('14', '3') = 0.3653805995645427; terminals('14', '4') = 0.5146776625112836; terminals('14', '5') = 0.46172129982047827; 
terminals('15', '1') = 0.9807955797704826; terminals('15', '2') = 0.09734685184548297; terminals('15', '3') = 0.38645671601793696; terminals('15', '4') = 0.33263947083044576; terminals('15', '5') = 0.5052803496499273; 
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
