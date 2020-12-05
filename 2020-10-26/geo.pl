% Städte mit Geokoordinaten - Version 2
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
  
liegt_oestlich_von(S1, S2) :- lage(S1, nord(N1), ost(O1)), lage(S2, nord(N2), ost(O2)), O1 > O2.

abstand(StadtA, StadtB, A) :- lage(StadtA, nord(NA), ost(OA)),
                              lage(StadtB, nord(NB), ost(OB)),
                              A is sqrt(((NA-NB)*111)^2 + ((OA-OB)*71)^2).
                              
summe([], 0).
summe([E|R], E) :- summe(R, E2), E is E2 + E.

laenge_der_route([], 0).
laenge_der_route([K1, K2|R], L) :- abstand(K1, K2 , A), summe([A, L], L), laenge_der_route([K2,R], L).