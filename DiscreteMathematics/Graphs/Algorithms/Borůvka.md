---
author: Lorenzo Tecchia
tags:
  - algorithm
  - to-do/implementation
---
***Borůvka's algorithm*** is a [[greedy]] algorithm for finding a [[minimum spanning tree]] in a [[graph]], or a [[Minimum Spanning Tree#^509260|minimum spanning forest]] in the case of a graph that is not [[connected]].

## proceeding of the algorithm
The algorithm begins by finding the minimum-weight edge [[incident]] to each vertex of the graph, and adding all of those edges to the [[forest]]. Then, it repeats a similar process of finding the minimum-weight edge from each [[tree]] constructed so far to a different tree, and adding all of those edges to the forest. 

---
Each repetition of this process reduces the number of trees, within each connected [[component]] of the graph, to at most half of this former value, so after logarithmically many repetitions the process finishes. When it does, the set of edges forms the minimum spanning forest.

## pseudocode
```
algorithm Borůvka is

    input: A weighted undirected graph _G_ = (_V_, _E_).

    output: _F_, a minimum spanning forest of _G_.

  

    Initialize a forest _F_ to (_V_, _E'_) where _E'_ = {}.

  

    _completed_ := false

    while not _completed_ do

        Find the [connected components](https://en.wikipedia.org/wiki/Component_(graph_theory)) of _F_ and assign to each vertex its component

        Initialize the cheapest edge for each component to "None"

        for each edge _uv_ in _E_, where _u_ and _v_ are in different components of _F_:

            let _wx_ be the cheapest edge for the component of _u_

            if is-preferred-over(_uv_, _wx_) then

                Set _uv_ as the cheapest edge for the component of _u_

            let _yz_ be the cheapest edge for the component of _v_

            if is-preferred-over(_uv_, _yz_) then

                Set _uv_ as the cheapest edge for the component of _v_

        if all components have cheapest edge set to "None" then

            _// no more trees can be merged -- we are finished_

            _completed_ := true

        else

            _completed_ := false

            for each component whose cheapest edge is not "None" do

                Add its cheapest edge to _E'_

  

function is-preferred-over(_edge1_, _edge2_) is

    return (_edge2_ is "None") or

           (weight(_edge1_) < weight(_edge2_)) or

           (weight(_edge1_) = weight(_edge2_) and tie-breaking-rule(_edge1_, _edge2_))

  

function tie-breaking-rule(_edge1_, _edge2_) is

    The tie-breaking rule; returns true if and only if _edge1_

    is preferred over _edge2_ in the case of a tie.
```

## complexity
Borůvka's algorithm can be shown to take $O(logV)$ iterations of the outer loop until it terminates, and therefore to run in time $O(E log V)$, where $E$ is the number of edges, and $V$ is the number of vertices in $G$(assuming $E \geq V$).

## [example](https://en.wikipedia.org/wiki/Bor%C5%AFvka's_algorithm#Example)

## Implementazione
```C
// da implementare
```
