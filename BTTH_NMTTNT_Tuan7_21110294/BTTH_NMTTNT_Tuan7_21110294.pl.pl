%a.
animal(goat, herbivores).
%b.
ferocious(wolf).
%c.
animal(X, carnivores) :- ferocious(X).
%d.
eat(carnivores, meat).
%e.
eat(herbivores, grass).
%f.
eat(carnivores, herbivores).
%g.
drink(carnivores, water).
drink(herbivores, water).
%h.
consume(X,Y,Z) :- animal(X,T), eat(T,Y), drink(T,Z).

%bai 2
check(X,Y,Z) :- ferocious(X), consume(X,Y,Z).

% ?- consume(wolf, Y, Z).
% Y = meat,
% Z = water ;
% Y = herbivores,
% Z = water.

% ?- check(wolf, Y, Z).
% Y = meat,
% Z = water ;
% Y = herbivores,
% Z = water.

% ?- consume(goat, Y, Z).
% Y = grass,
% Z = water ;
% false.

% ?- check(goat, Y, Z).
% false.
