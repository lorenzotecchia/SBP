---
tags: chain
---
If $x<y$ in $P$ and there is no $z$ with $x<z<y$, then $y$ **covers** $x$ in ($P$), written as $x \prec y$ or $y \succ x$. The **cover relation** is the set of pairs $x,y$ such that $x \prec y$. 

The **cover digraph** is the digraph on the elements of $P$ whose edge set is {$xy: x\prec y$}.

A ***cover diagram*** or (***Hasse Diagram***) of $P$ it obtained by erasing the directions on edges after drawing the cover digraph in the plane such tat each edge points upward.

The ***cover graph*** is the [[graph]] on the elements of $P$ whose edge set is {$xy: x\prec y$ or $y\prec x$}