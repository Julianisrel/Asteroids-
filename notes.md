<!-- steps -->

<!-- main__.py file -->
<!-- This file will take care of creating a new instance of your game and starting it by running main_loop(). It should look like this: -->
"""
Input handling: Input like pressed buttons, mouse motion, and VR controllers position is gathered and then handled. Depending on the game, it can cause objects to change their position, create new objects, request the end of the game, and so on.

handle_input()

Game logic: This is where most of the game mechanics are implemented. Here, the rules of physics are applied, collisions are detected and handled, artificial intelligence does its job, and so on. This part is also responsible for checking if the player has won or lost the game.

process_game_logic()


Drawing: If the game hasn’t ended yet, then this is where the frame will be drawn on screen. It will include all the items that are currently in the game and are visible to the player.


draw_game_elements()
"""



<!-- game.py -->

"""
<!-- handle_event loop  -->
The event you need right now is pygame.QUIT.



"""


<!-- GameObject Class -->
The GameObject class will store the following data:

    position: A point in the center of the object on the 2D screen
    sprite: An image used to display the object
    radius: A value representing the collision zone around the object’s position
    velocity: A value used for movement

Here’s a graphical representation of the game object:


For now, it will store the GameObject class, but later you’ll add classes for asteroids, bullets, and the spaceship.

Both objects are placed in the middle of the screen, using the coordinates (400, 300). Both objects’ position will be updated each frame using _process_game_logic(), and they’ll be drawn using _draw().


<!-- Controlling the Speed -->
how your game will perform on different machines with different processors. Sometimes it’ll run faster, and sometimes it’ll run slower.

run at 60 FPS.


<!-- Spaceship -->
The class you created in the previous step, GameObject, holds some general logic that can be reused by different game objects. However, each game object will also implement its own logic. The spaceship, for example, is expected to rotate and accelerate. It will also shoot bullets, but that comes later.

