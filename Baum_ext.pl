suche(SK, SK, ZK).
#suche(SK, SUCHE, ZK):- knoten(SUCHE, SNUM), parent_l_r(SK, KL, KR), 
suche(SK, SUCHE, ZK):- parent_l_r(SK, KL, KR), suche(KL, SUCHE, ZK).
suche(SK, SUCHE, ZK):- parent_l_r(SK, KL, KR), suche(KR, SUCHE, ZK).
