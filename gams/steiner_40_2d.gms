Sets
i Steiner points / 1*38 /
j terminals / 1*40 /
k dimensions / 1*2 /;
Alias(i,ii);
Parameters terminals(j,k);
terminals('1', '1') = 0.27149111325994557; terminals('1', '2') = 0.5419065944744416; 
terminals('2', '1') = 0.7081303437270102; terminals('2', '2') = 0.958595711147743; 
terminals('3', '1') = 0.36907866869225125; terminals('3', '2') = 0.5327915951705398; 
terminals('4', '1') = 0.37472229469470686; terminals('4', '2') = 0.5500903186325748; 
terminals('5', '1') = 0.8415099527809491; terminals('5', '2') = 0.9928062363216612; 
terminals('6', '1') = 0.9285407455267378; terminals('6', '2') = 0.9383085490615657; 
terminals('7', '1') = 0.05438971809425153; terminals('7', '2') = 0.24130065120390864; 
terminals('8', '1') = 0.9460170382964775; terminals('8', '2') = 0.5628688113018914; 
terminals('9', '1') = 0.1447411064167936; terminals('9', '2') = 0.6212680126015702; 
terminals('10', '1') = 0.9354403775856178; terminals('10', '2') = 0.23124572168213364; 
terminals('11', '1') = 0.35334037685851916; terminals('11', '2') = 0.17301726812257423; 
terminals('12', '1') = 0.9770270434693455; terminals('12', '2') = 0.20391906999469966; 
terminals('13', '1') = 0.25849945841505495; terminals('13', '2') = 0.07904121516982932; 
terminals('14', '1') = 0.10145050777222053; terminals('14', '2') = 0.01587009986403598; 
terminals('15', '1') = 0.003976912424406787; terminals('15', '2') = 0.5274194798699328; 
terminals('16', '1') = 0.2977381864993427; terminals('16', '2') = 0.367737424525461; 
terminals('17', '1') = 0.5792628379534555; terminals('17', '2') = 0.3148267604405873; 
terminals('18', '1') = 0.7415027402508483; terminals('18', '2') = 0.24346894498148042; 
terminals('19', '1') = 0.4970272820035503; terminals('19', '2') = 0.3696100600665041; 
terminals('20', '1') = 0.7406448204257586; terminals('20', '2') = 0.4510775148906421; 
terminals('21', '1') = 0.2777445786682915; terminals('21', '2') = 0.9301161801886195; 
terminals('22', '1') = 0.7808044304655216; terminals('22', '2') = 0.3465008116335996; 
terminals('23', '1') = 0.6746716201897096; terminals('23', '2') = 0.5036007380214363; 
terminals('24', '1') = 0.04082190533094143; terminals('24', '2') = 0.21187529060538512; 
terminals('25', '1') = 0.6563264065117206; terminals('25', '2') = 0.011510812976070262; 
terminals('26', '1') = 0.03885359767054686; terminals('26', '2') = 0.2672265794371722; 
terminals('27', '1') = 0.4807559527169666; terminals('27', '2') = 0.002436932534200298; 
terminals('28', '1') = 0.9785983941032872; terminals('28', '2') = 0.9891740779689651; 
terminals('29', '1') = 0.7776933868243149; terminals('29', '2') = 0.8548802131261678; 
terminals('30', '1') = 0.9110847720968246; terminals('30', '2') = 0.8463753199843561; 
terminals('31', '1') = 0.41944127627181294; terminals('31', '2') = 0.15779333724496403; 
terminals('32', '1') = 0.43677829486144926; terminals('32', '2') = 0.6450749571997122; 
terminals('33', '1') = 0.8415949565903945; terminals('33', '2') = 0.7607189573232341; 
terminals('34', '1') = 0.07298520090604921; terminals('34', '2') = 0.15080448229082866; 
terminals('35', '1') = 0.39648725657485984; terminals('35', '2') = 0.25965723028141596; 
terminals('36', '1') = 0.3397303990917946; terminals('36', '2') = 0.7893066169546663; 
terminals('37', '1') = 0.5325807839552859; terminals('37', '2') = 0.6476715322374964; 
terminals('38', '1') = 0.995775371234062; terminals('38', '2') = 0.46215008341182795; 
terminals('39', '1') = 0.5837682112235952; terminals('39', '2') = 0.9890074817114716; 
terminals('40', '1') = 0.5656346049362667; terminals('40', '2') = 0.8083952541848588; 
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
