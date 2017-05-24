---
title: Milestones
layout: page
---

# ~~Phase 1~~
 - ~~Input manager for keyboard & controller~~
 - ~~World collisions~~
 - ~~Read player data from config file~~
 - ~~Movement state change~~
 - ~~Import Marth data~~

# Phase 2
 - Code clean up
 - Improve sprite-sheet

# Phase 3
 - Implement horizontal movement
   - Walking
   - Dashing
   - Running
 - Implement Vertical movement
   - Jumping
   - Short hopping
   - Double jumping
   - Run-jumping
 - Techniques
   - Wave-dashing
   - Foxtrot
   - Dash dancing
   - Directional influence

Need to verify:
 - Dashing needs to be cancellable by:
   - Dashing in opposite direction
   - Shielding
     - Will cancel any momentum
   - Jumping
   - Attacking
 - Running
   - Turning will trigger turn animation
     - Turn animation contains 29 frames
     - Frame 9 will freeze animation until momentum is overcome
       - Fast running will have 21 frames of freeze
       - Slow running will have 10 frames of freeze
     - Running can be cancelled by crouching, Shielding, jumping. All of which will retain the momentum. Attacking can also cancel the animation.
