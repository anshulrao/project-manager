# Project Manager

## About
A simple application for assigning projects to employees that I had built as an 
independent project during my first year of college.

The user enters the information about employee's skills and project's requirements
and the application returns the project allocation result after using an algorithm internally to decide
which employee is to be assigned to which project.


## Features
- [Input](#input) : We have two panels in the application where the user can add employee and project data.
- [Output](#output) : The project allocation is diplayed on the right side along with a pie chart displaying the current 
status of allocations (how many are allocated/vacant). 
- The data is dumped as pickle files so it is not lost across various runs.
- We have a refresh button which will re-allocate the projects after new emplpoyee/project data is added.
- There is a clear button that clears all data and is to be used when the user wants to start over.


## Input

### Employee Information
Name | Skills (Languages, Domains, Types)
---- | --------------------------------

### Project Information
Name | Language | Domain | Type
---- | -------- | ------ | ----

- Language(s) can be Python, Java, C++.
- Domain(s) can be Payments, Inventory, Tracking.
- Type(s) can be Front-end, Back-end, Mobile App: iOS, Mobile App: Android.


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

A graph whose vertices can be divided into two disjoint and independent sets.

Let the two disjoint sets be `E` and `P`. `E` for employees and
`P` for projects.

- Every employee becomes a node in set `E`.
- Every project is split based on headcount, i.e., if two people
will work on project X then we will have two projects X1 and X2.
Each of these will form a unique node in set `P`.
- There is an edge from a node **e** in `E` to a node **p** in `P`, if and only if,
at least two skills of employee **e** match the requirements of the project **p**.

Once the bipartite graph is constructed, we use a recursive approach to 
find the maximum matching from `E` to `P`.

- If employee **e** fits the requirements of project **p** and **p** has
not yet been assigned to anyone then we assign **p** to **e**.

- Else, if another employee **e'** has been assigned **p** already then
we recursively look for another project for **e'** other than **p** 
so that we are able to assign **p** to **e**.


## Example

**Employees**:

- **E**rica - (`E`)
- **N**athan - (`N`)
- **A**llen - (`A`)
- **G**eorgia - (`G`)
- **K**iara - (`K`)


**Projects**:

NOTE: We have split the projects based on headcount.

- **I**ntegrate Wallets (Paytm, Amazon Pay) - (`I`)
- **M**igrate Database from SQL to NoSQL - (`M1`,` M2`)
- **R**evamp 'Product Addition' Infrastructure - (`R1`, `R2`)

### Construct a bipartite graph using input data

#### Nodes
- `Employee Set: {E, N, A, G, K}`
- `Project Set: {I, M1, M2, R1, R2}`

#### Edges
From [algorithm](#algorithm) we know that we get an edge from employee to project if there are at least two matches
between skills (of employee) and requirements (of project).

Employee | Skills
-------- | ------
E | `['python', 'tracking', 'frontend']`
N | `['python', 'java', 'android', 'frontend', 'inventory']`
A | `['cpp', 'android', 'ios', 'payments']`
G | `['python', 'android', 'tracking', 'ios']`
K | `['cpp', 'tracking', 'java', 'backend']`

Project | Requirements
------- | ------------
I | `['android', 'java', 'payments']`
M1, M2 | `['python', 'tracking', 'backend']`
R1, R2 | `['python', 'inventory', 'backend']`

```diff
- E -> I : []
+ E -> M1, M2 : ['python', 'tracking']
- E -> R1, R2 : ['python']

+ N -> I : ['java', 'android']
- N -> M1, M2 : ['python']
+ N -> R1, R2 : ['python', 'inventory']

+ A -> I : ['android', 'payments']
- A -> M1, M2 : []
- A -> R1, R2 : []

- G -> I : ['android']
+ G -> M1, M2 : ['python', 'tracking']
- G -> R1, R2 : ['python']

- K -> I : ['java']
+ K -> M1, M2 : ['tracking', 'backend']
- K -> R1, R2 : ['backend']
```

#### Graph

![Bipartite Graph](https://github.com/anshulrao/project-manager/blob/main/extras/example_graph.png)


### Allocate projects by recursively matching employee nodes to project nodes with the aim to maximize the number of matches

#### Matrix Representation of Graph
```
[
[0, 1, 1, 0, 0], 
[1, 0, 0, 1, 1], 
[1, 0, 0, 0, 0], 
[0, 1, 1, 0, 0], 
[0, 1, 1, 0, 0]
]
```

#### Algorithm's Flow
- `E` is assigned `M1`.
- `N` is assigned `I`.
- `A` is assigned `I` after `N` is assigned `R1`.
- `G` is assigned `M1` after `E` is assigned `M2`.
- `K` is not assigned any project since `E` and `G` have already
been assigned `M1` and `M2` and neither of them(`E` or `G`) can be assigned 
anything else.

##### The screen recording below confirms the above

![Screen Recording](https://github.com/anshulrao/project-manager/blob/main/extras/screen%20capture.gif)

