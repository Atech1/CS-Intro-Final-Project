# CS-1111-Final-Project
UVA CS 1111 Final Game Project of Alec Ross and Tilden Winston


created a game.py for program execution loop
created UI.py for basically the view handling
created parts of the model so far for that stuff.


things for next time:
    - need to think about how to control units drawn to UI on screen.
    probably needs to just move to the next tile, which means fixing the tile drawing etc.
    so that the player moves in a straight vector to the next tile, which would be the next arrow push...

    - something should be done about figuring out how the player unit is different than the ai unit. the ai unit
    needs more code under the hood probs to work in comparison but means that the player will have to have a
    special controller to the screen to fire and interact properly to the model elements.

    - need to make the nearby tile function work properly so that A* or dikstra's can be implemented for enemy path
    finding.

    - looks like this game will be implemented turn based????

    - more things to ask Tilden.