#kipkoech brian
#CIT-227-126/2024

% --- FACTS (Genders) ---
male(john).      % Grandfather
male(bob).       % Parent/Uncle
male(charlie).   % Parent/Uncle
male(david).     % Child/Cousin
female(mary).    % Grandmother
female(alice).   % Parent/Aunt
female(susan).   % Parent/Aunt
female(emily).   % Child/Cousin

% --- FACTS (Parents: parent(Parent, Child)) ---
parent(john, bob).
parent(john, alice).
parent(mary, bob).
parent(mary, alice).

parent(bob, david).
parent(susan, david).

parent(charlie, emily).
parent(alice, emily).

% --- RULES ---
% Core relationships
father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).

% Grandparents & Grandchildren
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
grandfather(GF, GC) :- grandparent(GF, GC), male(GF).
grandmother(GM, GC) :- grandparent(GM, GC), female(GM).
grandchild(GC, GP) :- grandparent(GP, GC).

% Siblings
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(B, S) :- sibling(B, S), male(B).
sister(S, B) :- sibling(S, B), female(S).

% Uncles & Aunts
uncle(U, N) :- parent(P, N), brother(U, P).
aunt(A, N) :- parent(P, N), sister(A, P).

% Cousins
cousin(C1, C2) :- parent(P1, C1), parent(P2, C2), sibling(P1, P2).
