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

<!-- Rotating the Spaceship -->
In general, image rotation is a complex process that requires recalculating pixels in the new image. During that recalculation, information about the original pixels is lost and the image is deformed a bit. With each rotation, the deformation becomes more and more visible.

Because of that, it might be a better idea to store the original sprite in the Spaceship class and have another sprite, which will be updated every time the spaceship rotates.

For that approach to work, you’ll need to know the angle by which the spaceship is rotated. This can be done in two ways:

    Keep the angle as a floating point value and update it during rotation.
    Keep the vector representing the direction the spaceship is facing and calculate the angle using that vector.

<!-- , create a constant vector called UP i
 -->
 
 <!-- Wrapping Objects Around the Screen -->

from pygame.math import Vector2
wrap_position

<!-- asteroids -->
all the asteroids are created with a position of (0, 0), which represents the top-left corner. You can change this by setting a random position on the screen.

<!-- Randomizing the Position -->
create a method called get_random_position() in the same file:
utils.py


Now use get_random_position() to place all six asteroids in random locations. Modify the constructor of the SpaceRocks class:
    <!-- self.asteroids = [ -->
        <!-- Asteroid(get_random_position(self.screen)) for _ in range(6) -->
    <!-- ] -->

the asteroids were generated in the same area as the spaceship. After you add collisions, this would cause the player to lose immediately after starting the game.


One solution to this problem is to check if the position is too close to the spaceship, and if so, generate a new one until a valid position is found.

Start by creating a constant representing an area that has to remain empty. A value of 250 pixels should be enough:   MIN_ASTEROID_DISTANCE = 250


<!-- Moving the Asteroids -->
creating a method called get_random_velocity() in the space_game/utils.py file:



<!-- Colliding With the Spaceship -->
check the collisions using GameObject.collides_with()
Edit the _process_game_logic() method in the SpaceRocks class like this:



<!-- Bullets -->
In models creating a class called Bullet that inherits from GameObject:

Add a way to keep track of the bullets, similar to what you did for the asteroids. 
    self.bullets = []
Bullets should be treated the same way as other game objects, so edit the _get_game_object() method in SpaceGame:


<!-- Shooting a Bullet -->
There’s a small issue with shooting. Bullets are stored in the main game object, represented by the SpaceRocks class. However, the shooting logic should be determined by the spaceship. It’s the spaceship that knows how to create a new bullet, but it’s the game that stores and later animates the bullets. The Spaceship class needs a way to inform the SpaceRocks class that a bullet has been created and should be tracked.

To fix this, you can add a callback function to the Spaceship class. That function will be provided by the SpaceRocks class when the spaceship is initialized. Every time the spaceship creates a bullet, it will initialize a Bullet object and then call the callback. The callback will add the bullet to the list of all bullets stored by the game.

Start by adding a callback to the constructor of the Spaceship class in the space_game/models.py file:


Then you create an instance of the Bullet class at the same location as the spaceship, using the velocity that was just calculated. Finally, the bullet is added to all the bullets in the game by using the callback method.

Now add the callback to the spaceship when it’s created. Bullets are stored as a list, and the only thing the callback has to do is add new items to that list. Therefore, the append() method should do the job. Edit the constructor of the SpaceRocks class in the space_game/game.py file:

The last thing you need to add is input handling. The bullet should be generated only when Space pressed, so you can use the event loop. The constant for Space is pygame.K_SPACE.

Modify the _handle_input() method in the SpaceGame class:

