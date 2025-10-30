% --- מגדר ---
male(meni).
male(david).
male(shay).
male(noham).
male(chaim).
male(oded).
male(adam).
male(ido).
male(dan).
male(gal).
male(shai).
male(yoni).
female(liat).
female(ora).
female(dvora).
female(hodaya).
female(chani).
female(karni).
female(ronit).
female(dvora_lea).
female(mika).
female(neta).


% --- נישואין ---
married(ido, dvora_lea).
married(david,dvora).
married(noham, karni).
%---בהנחה שתמיד הגבר נכתב ראשון בנישואין


% --- הורות ---
parent(noham, meni).
parent(karni, meni).

parent(noham, dvora).
parent(karni, dvora).

parent(noham, hodaya).
parent(karni, hodaya).

parent(noham, chani).
parent(karni, chani).
parent(hodaya,mika).
parent(dan,shai).
parent(dan,noham).
parent(ronit,noham).
parent(ora,shai).
parent(liat,david).
parent(liat,dvora_lea).
parent(ronit,neta).
parent(neta,adam).
parent(chaim,ronit).
parent(chaim,oded).
parent(oded,gal).
parent(gal,yoni).



father(X,Y)        :- parent(X,Y), male(X).
mother(X,Y)        :- parent(X,Y), female(X).

son(X,Y)           :- parent(Y,X), male(X).
daughter(X,Y)      :- parent(Y,X), female(X).

grandfather(Z,Y)   :- parent(X,Y), parent(Z,X), male(Z).
grandmother(Z,Y)   :- parent(X,Y), parent(Z,X), female(Z).

grandson(Y,Z)      :- parent(Z,X), parent(X,Y), male(Y).
granddaughter(Y,Z) :- parent(Z,X), parent(X,Y), female(Y).

sibling(X,Y)       :- parent(Z,X), parent(Z,Y), X \\= Y.

uncle(X,Y)         :- sibling(X,Z), parent(Z,Y), male(X),
                      mother(M1,X), mother(M2,Z), M1 \\= M2.

aunt(X,Y)          :- sibling(X,Z), parent(Z,Y), female(X).

niece(X,Y)         :- sibling(Y,Z), parent(Z,X), female(X).

aunt_son(X,Z)      :- male(X), aunt(Y,Z), parent(Y,X).

corps(X,Y)         :- sibling(Z,W), married(X,W), married(Z,Y), male(X).
grand_parent(Z,Y)  :- parent(X,Y), parent(Z,X).
second_cousin(X,Y) :- grand_parent(P1,X),grand_parent(P2,Y),sibling(P1,P2),X\\=Y.

%---חלק שני
reverse(L, Z) :- reverse_acc(L, [], Z).
reverse_acc([], Acc, Acc).
reverse_acc([H|T], Acc, Z) :-
    reverse_acc(T, [H|Acc], Z).
            
my_member(_, []) :- fail.
my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).

palindrome(L) :- reverse(L, L).

sorted([]).
sorted([_]).
sorted([X,Y|T]) :-
    X =< Y,
    sorted([Y|T]).

insert(X, L, [X|L]).                         % הכנסה בתחילת הרשימה
insert(X, [H|T], [H|R]) :- insert(X, T, R).  % דחיפה פנימה עד למיקום הבא


permutaion([], []).                       
permutaion([H|T], P) :-                    
    permutaion(T, T1),                      
    insert(H, T1, P).                        

%---
%
%חלק שלישי:אריתמטיקה
% בסיס: סכום עד 0 הוא 0
scum(0, 0).

% צעד רקורסיבי:
scum(N,Res) :-
    integer(N), N > 0,
    N1 is N - 1,
    scum(N1,Res1),
    Res is Res1 + N.

% בסיס: סכום ספרות של 0 הוא 0
sumDigits(0, 0).

% מקרה כללי: NUM > 0
sumDigits(NUM, SUM) :-
    NUM > 0,
    D  is NUM mod 10,
    N1 is NUM // 10,
    sumDigits(N1, S1),
    SUM is S1 + D.


split(0, [0]).
split(N, Ds) :-
    integer(N), N > 0,
    split_acc(N, [], Ds).    

split_acc(N, Acc, [N|Acc]) :- N < 10, !.
split_acc(N, Acc, Ds) :-
    D  is N mod 10,
    N1 is N // 10,
    split_acc(N1, [D|Acc], Ds).

%---מרשימה למספר
create([], 0).
create([D|T], N) :-
    integer(D), D >= 0, D =< 9,
    create(T, N1),
    N is D + 10*N1.
%---היפוך ספרות
reverse_digits(N, M) :-
    integer(N), N >= 0,
    split(N, Ds),      % 584 -> [5,8,4]
    create(Ds, M).     %      -> 485

%---חיתוך
intersection([], _, []).
intersection([H|T], L2, [H|Z]) :- member(H, L2), !, intersection(T, L2, Z).
intersection([_|T], L2, Z)     :- intersection(T, L2, Z).

%---חיסור
minus([], _, []).
minus([H|T], L2, Z)    :- member(H, L2), !, minus(T, L2, Z).
minus([H|T], L2, [H|Z]):- minus(T, L2, Z).
