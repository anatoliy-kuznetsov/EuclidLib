Sets
i Steiner points / 1*13 /
j terminals / 1*15 /
k dimensions / 1*4 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.3078067547337774; terminals('1', '2') = 0.5779578771750392; terminals('1', '3') = 0.26561803541817575; terminals('1', '4') = 0.8078960514329893; 
terminals('2', '1') = 0.4672172210012604; terminals('2', '2') = 0.33251980673741144; terminals('2', '3') = 0.8967525962082569; terminals('2', '4') = 0.7924119898695275; 
terminals('3', '1') = 0.8596136949374525; terminals('3', '2') = 0.6658137355569159; terminals('3', '3') = 0.1854598161134392; terminals('3', '4') = 0.3899285200718041; 
terminals('4', '1') = 0.23942936687819738; terminals('4', '2') = 0.7931287877223899; terminals('4', '3') = 0.009184110257544176; terminals('4', '4') = 0.7905476817951573; 
terminals('5', '1') = 0.1667763675050825; terminals('5', '2') = 0.30614199209589266; terminals('5', '3') = 0.6286784916754126; terminals('5', '4') = 0.6749145697726233; 
terminals('6', '1') = 0.5123965188595846; terminals('6', '2') = 0.556215195448374; terminals('6', '3') = 0.5888863209509851; terminals('6', '4') = 0.6003058073162648; 
terminals('7', '1') = 0.10830095398871686; terminals('7', '2') = 0.301870958131248; terminals('7', '3') = 0.020499027923741364; terminals('7', '4') = 0.5668022276384451; 
terminals('8', '1') = 0.29450295704025886; terminals('8', '2') = 0.24215631594412912; terminals('8', '3') = 0.2744568069724159; terminals('8', '4') = 0.9412593709117075; 
terminals('9', '1') = 0.1282338254681593; terminals('9', '2') = 0.9019460548181631; terminals('9', '3') = 0.9031736614711603; terminals('9', '4') = 0.2037984038273466; 
terminals('10', '1') = 0.829797266931312; terminals('10', '2') = 0.19575994148177733; terminals('10', '3') = 0.645872503285497; terminals('10', '4') = 0.12203855440196454; 
terminals('11', '1') = 0.318405760895906; terminals('11', '2') = 0.4938036901276964; terminals('11', '3') = 0.37642068481077395; terminals('11', '4') = 0.8256324717799948; 
terminals('12', '1') = 0.6465433247102469; terminals('12', '2') = 0.033522650784374886; terminals('12', '3') = 0.5581254938339517; terminals('12', '4') = 0.0912916889874551; 
terminals('13', '1') = 0.17497888842654896; terminals('13', '2') = 0.38968471952782524; terminals('13', '3') = 0.3152812984667659; terminals('13', '4') = 0.5561379670293034; 
terminals('14', '1') = 0.9831483568003972; terminals('14', '2') = 0.7793186335882816; terminals('14', '3') = 0.545443726285844; terminals('14', '4') = 0.8394599012498352; 
terminals('15', '1') = 0.16871130717858907; terminals('15', '2') = 0.7158922205435296; terminals('15', '3') = 0.9716203470560987; terminals('15', '4') = 0.9419601863446189; 
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
