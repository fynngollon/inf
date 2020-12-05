% Autor:
% Datum: 05.10.2020

lage(berlin, nord(52.5), ost(13.0)).
lage('Köln', nord(50.93), ost(6.95)).
lage(mainz, nord(50), ost(8.27)).
lage(frankfurt, nord(50.1), ost(8.68)).
lage('München', nord(48.13), ost(11.57)).
lage(hamburg, nord(53.5), ost(10.0)).

liegt_suedlich_von(StadtA, StadtB) :-
  lage(StadtA, nord(NA), ost(_OA)),
  lage(StadtB, nord(NB), ost(_OB)),
  NA < NB.
  
liegt_oestlich_von(S1,S2):-
  lage(S1,nord(_N1), ost(O1)),
  lage(S2,nord(_N2), ost(O2)),
  O1 > O2 .
  
abstand(StadtA, StadtB, A) :-
  lage(StadtA, nord(NA), ost(OA)),
  lage(StadtB, nord(NB), ost(OB)),
  A is sqrt(((NA-NB)*111)^2 + ((OA-OB)*71)^2).

summe([],0).
summe([K|R], S):-summe(R, S2), S is S2 + K.

laenge_der_route([],0).
laenge_der_route([K,K2|R],S):-R==[], abstand(K,K2,S).
laenge_der_route([K,K2|R],S):-R\==[],abstand(K,K2,S1), laenge_der_route([K2|R],S2), summe([S1,S2],S).

% Aufgabe 1
positivListe([]).
positivListe([K|R]) :- K > 0, positivListe(R).

% Aufgabe 2
quadratzahl(X) :- X\==0, X\== 1, Y is sqrt(X), Y2 is round(Y), Y3 is Y2**2, X =:= Y2.

% Aufgabe 3
expo(Z,0,1).
expo(Z,1,Z).
expo(Z,2,Zahl):- Zahl is Z*Z .
expo(Z,E,Zahl):- E>2,E1 is E -1, expo(Z,E1,Zahl1), Zahl is Zahl1*Z .
