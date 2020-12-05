% Autor:
% Datum: 05.10.2020

% Fakten zu Städten an Flüssen

staedte_am_fluss(mosel, [metz, konz, trier, bernkastel, cochem, koblenz]).
staedte_am_fluss(saar, ['Saarbrücken', saarburg, konz]).
staedte_am_fluss(rhein, [basel, mannheim, mainz, koblenz, 'Köln', 'Düsseldorf']).
staedte_am_fluss(donau, [ulm, ingolstadt, regensburg, wien, budapest]).
staedte_am_fluss(main, [bischberg, 'Würzburg', offenbach, frankfurt, mainz]).


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

% Flussfahrt
muendet_in(Fluss1, Fluss2, Stadt) :-
  staedte_am_fluss(Fluss1, ListeStaedteFluss1),
  staedte_am_fluss(Fluss2, ListeStaedteFluss2),
  letztes_element(ListeStaedteFluss1, Stadt),
  element(Stadt, ListeStaedteFluss2),
  Fluss1 \== Fluss2.

liegen_am_selben_fluss(StadtA, StadtB) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(StadtA, ListeStaedteFluss),
  element(StadtB, ListeStaedteFluss).

liegen_am_selben_fluss_flussabwaerts(StadtA, StadtB) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(StadtA, ListeStaedteFluss),
  element(StadtB, ListeStaedteFluss),
  StadtA \== StadtB,
  teilliste_von_element_bis_element(ListeStaedteFluss, StadtA, StadtB, Liste),
  Liste \== [].

liegen_flussabwaerts(StadtA, StadtB) :-
  liegen_am_selben_fluss_flussabwaerts(StadtA, StadtB).

liegen_flussabwaerts(StadtA, StadtB) :-
  liegt_am_fluss(StadtA, Fluss1),
  muendet_in(Fluss1, Fluss2, StadtC),
  liegen_am_selben_fluss_flussabwaerts(StadtA, StadtC),
  liegen_flussabwaerts(StadtC, StadtB).

liegen_flussaufwaerts(StadtA, StadtB) :-
  liegen_flussabwaerts(StadtB, StadtA).

liegen_flussabwaerts_flussaufwaerts(StadtA, StadtB, StadtC) :-
  not(liegen_flussabwaerts(StadtA, StadtB)),
  not(liegen_flussaufwaerts(StadtA, StadtB)),
  liegen_flussabwaerts(StadtA, StadtC),
  liegen_flussaufwaerts(StadtC, StadtB).

liegen_am_fluss(StadtA, StadtB, Fluss) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(StadtA, ListeStaedteFluss),
  element(StadtB, ListeStaedteFluss).

liegt_am_fluss(Stadt, Fluss) :-
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  element(Stadt, ListeStaedteFluss).

fahrt_abwaerts_ueber_denselben_fluss(StadtA, StadtB, ListeStaedteAB) :-
  liegen_am_fluss(StadtA, StadtB, Fluss),
  staedte_am_fluss(Fluss, ListeStaedteFluss),
  teilliste_von_element_bis_element(ListeStaedteFluss, StadtA, StadtB, ListeStaedteAB).

fahrt_abwaerts_von_ueber_nach(StadtA, Fluss, StadtB, ListeStaedteAB) :-
  liegen_am_selben_fluss(StadtA, StadtB),
  fahrt_abwaerts_ueber_denselben_fluss(StadtA, StadtB, ListeStaedteAB).

fahrt_abwaerts_von_ueber_nach(StadtA, Fluss, StadtB, ListeStaedteAB) :-
  not(liegen_am_selben_fluss(StadtA, StadtB)),
  muendet_in(Fluss, Fluss2, StadtC),
  fahrt_abwaerts_ueber_denselben_fluss(StadtA, StadtC, ListeStaedteAC),
  fahrt_abwaerts_von_ueber_nach(StadtC, Fluss2, StadtB, ListeStaedteCB),
  zusammenfuegen(ListeStaedteAC, ListeStaedteCB, ListeStaedteAB).

fahrt_abwaerts(StadtA, StadtB, ListeStaedteAB) :-
  liegen_am_selben_fluss(StadtA, StadtB),
  fahrt_abwaerts_ueber_denselben_fluss(StadtA, StadtB, ListeStaedteAB).

fahrt_abwaerts(StadtA, StadtB, ListeStaedteAB) :-
  not(liegen_am_selben_fluss(StadtA, StadtB)),
  liegen_flussabwaerts(StadtA, StadtB),
  liegt_am_fluss(StadtA, Fluss1),
  muendet_in(Fluss1, Fluss2, StadtC),
  fahrt_abwaerts_ueber_denselben_fluss(StadtA, StadtC, ListeStaedteAC),
  fahrt_abwaerts_von_ueber_nach(StadtC, Fluss2, StadtB, ListeStaedteCB),
  zusammenfuegen(ListeStaedteAC, ListeStaedteCB, ListeStaedteAB).

fahrt_aufwaerts(StadtA, StadtB, ListeStaedteAB) :-
  fahrt_abwaerts(StadtB, StadtA, ListeStaedteBA),
  umkehren(ListeStaedteBA, ListeStaedteAB).

fahrt(StadtA, StadtB, ListeStaedteAB) :-
  liegen_flussabwaerts(StadtA, StadtB),
  fahrt_abwaerts(StadtA, StadtB, ListeStaedteAB).
  %write_fahrt(ListeStaedteAB).

fahrt(StadtA, StadtB, ListeStaedteAB) :-
  liegen_flussaufwaerts(StadtA, StadtB),
  fahrt_aufwaerts(StadtA, StadtB, ListeStaedteAB).
  %write_fahrt(ListeStaedteAB).

fahrt(StadtA, StadtB, ListeStaedteAB) :-
  liegen_flussabwaerts_flussaufwaerts(StadtA, StadtB, StadtC),
  fahrt_abwaerts(StadtA, StadtC, ListeStaedteAC),
  fahrt_aufwaerts(StadtC, StadtB, ListeStaedteCB),
  vorletztes_element(ListeStaedteAC, E1),
  zweites_element(ListeStaedteCB, E2),
  E1 \== E2,
  zusammenfuegen(ListeStaedteAC, ListeStaedteCB, ListeStaedteAB).
  %write_fahrt(ListeStaedteAB).

write_fahrt([]).
write_fahrt([K|R]) :- write(K), nl, write_fahrt(R).