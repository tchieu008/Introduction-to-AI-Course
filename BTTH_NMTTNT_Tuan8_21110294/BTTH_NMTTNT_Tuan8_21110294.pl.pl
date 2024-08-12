% Water Jug problem using DFS in Prolog

% Define the initial state
start(jug(0,0)).

% Define the goal state
goal(jug(_,Z)) :- goal_volume(Z).

% Define the actions that can be taken
action(fill1, jug(_,Y), jug(Vx,Y)) :- jug1_volume(Vx).
action(fill2, jug(X,_), jug(X,Vy)) :- jug2_volume(Vy).
action(empty1, jug(_,Y), jug(0,Y)).
action(empty2, jug(X,_), jug(X,0)).
action(pour1to2, jug(X,Y), jug(X1,Y1)) :- jug2_volume(Vy), X > 0, Y < Vy, Y1 is X + Y, X1 is max(0, Y1 - Vy).
action(pour2to1, jug(X,Y), jug(X1,Y1)) :- jug1_volume(Vx), Y > 0, X < Vx, X1 is X + Y, Y1 is max(0, X1 - Vx).

% Define the DFS algorithm
dfs(State, [], _, _) :- goal(State), !.

dfs(State, [Action|Actions], Visited, History) :-
    action(Action, State, State1),
    State1 \= State,
    \+ member(State1, Visited),
    dfs(State1, Actions, [State1|Visited], [(State,Action)|History]).

% To run the program
solve(Vx, Vy, Z) :-
    assert(jug1_volume(Vx)),
    assert(jug2_volume(Vy)),
    assert(goal_volume(Z)),
    start(State),
    dfs(State, Actions, [State], []),
    (   Actions = [] -> false
    ;   reverse(Actions, Solution),
        write(Solution)
    ),
    retractall(jug1_volume(_)),
    retractall(jug2_volume(_)),
    retractall(goal_volume(_)).
