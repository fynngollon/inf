% Autor:
% Datum: 21.09.2020

% Stadt
stadt(trier).
stadt(mainz).
stadt(koblenz).
stadt(berlin).
stadt('Köln').
stadt('München').
% Land
land('D').
land(deutschland).
land('A').
land(oesterreich).
% Fluss
fluss(mosel).
fluss(rhein).
fluss(spree).
fluss('Isar').
% Eigenschaften
flaeche(deutschland, 357111.91).
flaeche(oesterreich, 83879).
% Beziehungen
liegt_am_fluss(trier, mosel).
liegt_am_fluss(mainz, rhein).
liegt_am_fluss('Köln', rhein).
% Einwohnerzahl eines Landes
einwohnerzahl(deutschland, 8.403, datum(1, 10, 2010)).
einwohnerzahl(oesterreich, 81.751, datum(30, 6, 2010)).
% Nationalfeiertag eines Landes
nationalfeiertag(deutschland, datum(3, 10, Jahr)).
nationalfeiertag(oesterreich, datum(26, 10, Jahr)).
% Geografische Lage einer Stadt
lage(berlin, koordinaten(nord(52), ost(13))).
lage('Köln', koordinaten(nord(51), ost(7))).
% Städte am Fluss
staedte_am_fluss(mosel, [metz,konz, trier, bernkastel, cochem, koblenz]).
staedte_am_fluss(saar, ['Saarbrücken', saarburg, konz]).
staedte_am_fluss(rhein, [basel, mannheim, mainz, koblenz, 'Köln', 'Düsseldorf']).
staedte_am_fluss(donau, [ulm, ingolstadt, regensburg, wien, budapest]).
staedte_am_fluss(main, [schweinfurt, 'Würzburg', offenbach, frankfurt, mainz]).

% Listenverarbeitung

element(E, [K|R]) :- E = K.
element(E, [K|R]) :- E \== K, element(E, R).

zusammenfuegen([], L, L).
zusammenfuegen([K|R], L, [K|RL]) :- zusammenfuegen(R, L, RL).

letztes_element([E], E).
letztes_element([K|R], E) :- letztes_element(R, E).

mit_letztem_element([], E, [E]).
mit_letztem_element([K|R], E, [K|L]) :- mit_letztem_element(R, E, L).

umkehren([], []).
umkehren([K|R], L) :- umkehren(R, U), mit_letztem_element(U, K, L).

vorletztes_element([E1, E2], E1).
vorletztes_element([K1,K2|R], E) :- vorletztes_element([K2|R], E).

zweites_element([E1, E2|R], E2).

teilliste_bis_element([], Element, []).
teilliste_bis_element([K|R], Element, [Element]) :-
  K = Element.
teilliste_bis_element([K|R], Element, [K|Teilliste]) :-
  K \== Element,
  element(Element, R),
  teilliste_bis_element(R, Element, Teilliste).
teilliste_bis_element([K|R], Element, []) :-
  K \== Element,
  not(element(Element, R)).

teilliste_von_element_bis_element(L, Anfang, Ende, []) :- not(element(Anfang, L)).
teilliste_von_element_bis_element(L, Anfang, Ende, []) :- element(Anfang, L), not(element(Ende, L)).
teilliste_von_element_bis_element([K|R], Anfang, Ende, [K|Teilliste])  :-
  element(Anfang, [K|R]), element(Ende, [K|R]),
  K = Anfang,
  element(Ende, R),
  teilliste_bis_element(R, Ende, Teilliste).
teilliste_von_element_bis_element([K|R], Anfang, Ende, [K])  :-
  element(Anfang, [K|R]), element(Ende, [K|R]),
  K = Anfang,
  not(element(Ende, R)).
teilliste_von_element_bis_element([K|R], Anfang, Ende, Teilliste)  :-
  element(Anfang, [K|R]), element(Ende, [K|R]),
  K \== Anfang,
  element(Anfang, R),
  teilliste_von_element_bis_element(R, Anfang, Ende, Teilliste).
  
suchen(FLUSS, STADT):- staedte_am_fluss(FLUSS, L), element(STADT,L).
%1
liegen_am_selben_fluss_flussabwaerts(S1,S2):-S1\==S2, staedte_am_fluss(FLUSS,L),element(S1,L),element(S2,L), teilliste_bis_element(L,S2,ZL),element(S1,ZL).
%2
liegen_flussabwaerts(S1,S2):- liegen_am_selben_fluss_flussabwaerts(S1,S2).
liegen_flussabwaerts(S1,S2):- S1\==S2, suchen(F,S1),
                            staedte_am_fluss(F, L), letztes_element(L,E), S1 \== E, liegen_flussabwaerts(E,S2).
%3
liegen_flussaufwaerts(S1,S2):- liegen_flussabwaerts(S2,S1).
%4
liegen_flussabwaerts_flussaufwaerts(S1,S2,S3):-  liegen_flussabwaerts(S1,S3),liegen_flussaufwaerts(S3,S2),not(liegen_am_selben_fluss_flussabwaerts(S1,S2)).
%5
fahrt_abwaerts_ueber_denselben_fluss(S1,S2,F):- liegen_am_selben_fluss_flussabwaerts(S1,S2),  staedte_am_fluss(FLUSS,L),element(S1,L),element(S2,L), teilliste_von_element_bis_element(L, S1,S2, F).


%6
fahrt_abwaerts(S1,S2,L):-fahrt_abwaerts_ueber_denselben_fluss(S1,S2,L).
fahrt_abwaerts(S1,S2,L):-not(fahrt_abwaerts_ueber_denselben_fluss(S1,S2,L)),staedte_am_fluss(F2, FLUSS), element(S1,FLUSS),
                         letztes_element(FLUSS,E),E\==S1,teilliste_von_element_bis_element(FLUSS,S1,E,ZL),
                         fahrt_abwaerts(E,S2,NL), zusammenfuegen(ZL,NL,L).
%7
fahrt_aufwaerts(S1,S2,L):- fahrt_abwaerts(S2,S1,L1), umkehren(L1,L).
%8
fahrt(S1,S2,F):- fahrt_abwaerts(S1,S2,F).
fahrt(S1,S2,F):- fahrt_aufwaerts(S1,S2,F).
fahrt(S1,S2,F):- liegen_flussabwaerts_flussaufwaerts(S1,S2,S3), fahrt_abwaerts(S1,S3,F1),fahrt_aufwaerts(S3,S2,F2), zusammenfuegen(F1,F2,F).

