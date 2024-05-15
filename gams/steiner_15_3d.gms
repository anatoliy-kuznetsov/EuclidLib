Sets
i Steiner points / 1*13 /
j terminals / 1*15 /
k dimensions / 1*3 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.2718754143840908; terminals('1', '2') = 0.48802820785090784; terminals('1', '3') = 0.08187934237116656; 
terminals('2', '1') = 0.33873348699206973; terminals('2', '2') = 0.07233360770535402; terminals('2', '3') = 0.011036367079899967; 
terminals('3', '1') = 0.28385029589876865; terminals('3', '2') = 0.11770636555802805; terminals('3', '3') = 0.3110382248120007; 
terminals('4', '1') = 0.7434707928397064; terminals('4', '2') = 0.0357557155126923; terminals('4', '3') = 0.6249375571804716; 
terminals('5', '1') = 0.13501116090704035; terminals('5', '2') = 0.7950712434655829; terminals('5', '3') = 0.7369676243821022; 
terminals('6', '1') = 0.21101029956774453; terminals('6', '2') = 0.8480765801722641; terminals('6', '3') = 0.7173017220824032; 
terminals('7', '1') = 0.07495132545320449; terminals('7', '2') = 0.4081313844234159; terminals('7', '3') = 0.7004510913580178; 
terminals('8', '1') = 0.9229582476032371; terminals('8', '2') = 0.17221119493742953; terminals('8', '3') = 0.2518629905323574; 
terminals('9', '1') = 0.7750929946094214; terminals('9', '2') = 0.9626723030210862; terminals('9', '3') = 0.09375460752394849; 
terminals('10', '1') = 0.08982827530229975; terminals('10', '2') = 0.7511793846525663; terminals('10', '3') = 0.3169893159261734; 
terminals('11', '1') = 0.38677647485720235; terminals('11', '2') = 0.87633207391825; terminals('11', '3') = 0.7457995156246497; 
terminals('12', '1') = 0.6607159863179267; terminals('12', '2') = 0.8676520260577261; terminals('12', '3') = 0.7320438297162596; 
terminals('13', '1') = 0.8102488868102232; terminals('13', '2') = 0.6432507057061979; terminals('13', '3') = 0.5931582872810908; 
terminals('14', '1') = 0.05986505368858752; terminals('14', '2') = 0.909611607891918; terminals('14', '3') = 0.9117643699770345; 
terminals('15', '1') = 0.35134351369704286; terminals('15', '2') = 0.6263463928446534; terminals('15', '3') = 0.01689904369168782; 
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
