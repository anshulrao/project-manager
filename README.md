# Project Manager

## About
A simple application for assigning projects to employees.

I built this as an independent project during my first year
of college.

## Features
- We have two panels in the application where the user
can add employee and project data.
- The data is dumped as pickle files so it is not lost across
various runs.
- We have a refresh button which will re-allocate the projects
after new data is added.
- There is a clear button that clears all data and is to be used 
when the user wants to start over.


## Input

### Employee Information
Name | Skills (Languages, Domains, Types)
---- | --------------------------------

### Project Information
Name | Language | Domain | Type
---- | -------- | ------ | ----

- Language(s) can be Python, Java, C++
- Domain(s) can be Payments, Inventory, Tracking
- Type(s) can be Front-end, Back-end, Mobile App:iOS, Mobile App: Android


## Output

Allotment of projects to employees based on their skills
and the requirements of the project.

It additionally displays a pie chart to show the status of project
assignments.

```
GREEN: Assigned
RED:   Vacant
```

## Algorithm

We convert the input data into a bipartite graph.

*What is a bipartite graph?*

A graph whose vertices can be divided into two 
disjoint and independent sets.

Let the two disjoint sets be `E` and `P`. `E` for employees and
`P` for projects.

- Every employee becomes a node in set `E`.
- Every project is split based on headcount, i.e., if two people
will work on project X then we will have two different nodes for X 
in set `P`.
- There is an edge from a node **e** in `E` to a node **p** in `P`, if and only if,
at least two skills of employee match the requirements of the project **p**.

Once the bipartite graph is constructed, we use a DFS approach to 
find the maximum matching from `E` to `P`.

If employee **e** fits the requirements of project **p** and **p** has
not yet been assigned to anytone then we assign **p** to **e**.

Else if another employee **e'** has been assigned **p** already then
we recursively look for another project for **e'** other than **p** 
so that we are able to assign **p** to **e**.


#### Example

**Employees**:

- Erica - (`E`)
- Nathan - (`N`)
- Allen - (`A`)
- Georgia - (`G`)
- Kiara - (`K`)


**Projects**:

NOTE: We have split the projects based on headcount.

- Integrate Wallets (Paytm, Amazon Pay) - (`I`)
- Migrate Database from SQL to NoSQL - (`M1`,` M2`)
- Revamp 'Product Addition' Infrastructure - (`R1`, `R2`)

![Bipartite Graph](https://github.com/anshulrao/project-manager/blob/main/extras/example_graph.png)

The matrix representation of the graph:-
```
[
[0, 1, 1, 0, 0], 
[1, 0, 0, 1, 1], 
[1, 0, 0, 0, 0], 
[0, 1, 1, 0, 0], 
[0, 1, 1, 0, 0]
]
```

- `E` fits the requirements of `M1`, `M2`.
- `N` fits the requirements of `I`, `R1`, `R2`.
- `A` fits the requirements of `I`.
- `G` fits the requirements of `M1`, `M2`.
- `K` fits the requirements of `M1`, `M2`.


*How are they assigned via the algorithm?*

- `E` is assigned `M1`.
- `N` is assigned `I`.
- `A` is assigned `I` after `N` is assigned `R1`.
- `G` is assigned `M1` after `E` is assigned `M2`.
- `K` is not assigned any project since `E` and `G` have already
been assigned `M1` and `M2` and neither of them(`E` or `G`) can be assigned 
anything else.

The screen recording below confirms the above:-

![Screen Recording](https://github.com/anshulrao/project-manager/blob/main/extras/screen%20capture.gif)

