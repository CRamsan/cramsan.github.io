---
title: States
layout: page
---

This page will document the different states that a character can be in as well
as the possible transitions. All the frame data is based on Marth frame data.

 #Wait
 - Idle state for the character.
 - If input is jump button go into **PreJump** state
 - If input is attack go into into **PreAttack** state
 - If input is shield go into **Shielding** state
 - If input for stickX can into **SlowWalk**, **MidWalk**, **FastWalk** or **Dashing**.
   -  **DEFINE LOGIC FOR EACH TRANSITION**

 # Dashing:
 - **Dashing** is the state after the input is pulled far enough to start running. This state is the transition between walking/idle and running. 
 - Frames 1-15
   - Cancellable: True
     - Dashing in opposite direction
     - Shielding
       - Will cancel any momentum
     - Jumping
     - Attacking
 - If dash is not cancelled and input is back to neutral
   - Frame 16 will be **DashWait** animation
 - Dash frames 16-27 are not cancellable 
 - If at frame 16 the input remains hold in the direction of the dash
   - Go into **DashRun** state

 # DashWait
 - **DashWait** is 11 frames and it would be frames 16-27 from **Dashing**. This transition happens when the dash animation will change into a walk/idle state.
 - It cannot be cancelled
 - Once completed, go to **Wait** state.
 # DashRun

 # Running
 - Turning will trigger turn animation
   - Turn animation contains 29 frames
   - Frame 9 will freeze animation until momentum is overcome
       - Fast running will have 21 frames of freeze
       - Slow running will have 10 frames of freeze
     - Running can be cancelled by crouching, Shielding, jumping. All of which will retain the momentum. Attacking can also cancel the animation.

References:
 - [https://smashboards.com/threads/marth-movement-mechanics.433988/]
 - [https://docs.google.com/spreadsheets/d/1WqxJWDXbPDDYhjV5Vo34qTiCxmHSqg_Wr6GKKyLrH2M/edit#gid=0]
