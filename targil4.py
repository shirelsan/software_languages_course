
split(N,R,R1):-
    N>=1,
    N1 is mod(N,10),
    N2 is N//10,
    split(N2,[N1|R],R1).
split(_,X,X).
split(N,Res):-
    split(N,[],Res).

creat(L,N):-
    creat(L,0,N).
creat([X|Y],N1,N):-
    length(Y,L2),
    N2 is N1+(X*(10**(L2))),
    creat(Y,N2,N).
creat([],N,N).

inter(L1,L2,Z):-
    inter(L1,L2,[],Z).
inter([X1|Y],L2,RES,Z):-
    in(X1,L2),
    inter(Y,L2,[X1|RES],Z).
inter([X1|Y],L2,RES,Z):-
    not(in(X1,L2)),
    inter(Y,L2,RES,Z).
inter([],_,X,X).
in(X,[X1|_]):-
    X=:=X1.
in(X,[_|X2]):-
    in(X,X2).    
    
minus(L1,L2,Z):-
    minus(L1,L2,[],Z).
minus([X1|Y1],L2,RES,Z):-
    not(in(X1,L2)),
    minus(Y1,L2,[X1|RES],Z).
minus([],_,X,X).
minus([X1|Y1],L2,RES,Z):-
    in(X1,L2),
    minus(Y1,L2,RES,Z).


schum(N,Res):-
   schum(N,0,Res).
schum(0,X,X).
schum(N,R,Res):-
    R1 is R+N,
    N1 is N-1,
    schum(N1,R1,Res).

sumd(N,RES):-
    sumd(N,0,RES).
sumd(0,X,X).
sumd(N,R,RES):-
    N1 is mod(N,10),
    N2 is N//10,
    R1 is R+N1,
    sumd(N2,R1,RES)
