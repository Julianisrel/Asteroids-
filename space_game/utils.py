import random

from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound

# image loader
def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
         return loaded_sprite.convert()

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return Sound(path)



def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)


#This will generate a random set of coordinates on a given surface and return the result as a Vector2 instance.
def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )

# moving Asteroid method
def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)
