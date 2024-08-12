parent(marry, bill).
parent(tom, bill).
parent(tom, liz).
parent(bill, ann).
parent(bill, sue).
parent(sue, jim).
woman(marry).
man(tom).
man(bill).
woman(liz).
woman(sue).
woman(ann).
man(jim).

child(Y,X) :- parent(X,Y).
mother(X,Y) :- parent(X,Y),woman(X).
father(X,Y) :- parent(X,Y),man(X).
grandparent(X,Z) :- parent(X,Y),parent(Y,Z).
sister(X, Y):- parent(Z, X), parent(Z, Y), woman(X).

/*
---------------------- | Cau 1 | ------------------
a. ?-parent(jim,X).
false.

b. ?-parent(X,jim).
X = sue.

c. ?-parent(marry,X),parent(X,part).
false.

d. ?-parent(marry,X),parent(X,Y),parent(Y,jim).
X = bill,
Y = sue.
---------------------------------------------------
*/

/*
----------------------- | Cau 2 | -----------------
a. ?-parent(X,bill).
X = marry ;
X = tom.

b. ?-parent(marry,X).
X = bill.

c.

d. ?-grandparent(X,sue).
X = marry ;
X = tom ;
false.
---------------------------------------------------
*/
