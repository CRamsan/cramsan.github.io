---
title: State Machine
layout: page
---

All the changes between states can be defined as a state machine. The state machine will have two main parts, one of them is for the changes between states(dashing, jumping, running, etc) and the other one will be for the changes within a single state. 

The idea is to being able to define each character as a list of states. Each state is then defined as a list of properties. The format takes inspiration from the [Melee moveset file format](http://opensa.dantarion.com/wiki/Moveset_File_Format_(Melee))
