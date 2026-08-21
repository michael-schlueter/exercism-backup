"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass
        
    


#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates
def new_aliens_collection(start_positions):
    """Create a collection of new aliens based on a list of starting positions.

    Parameters:
        start_positions (tuple): The starting positions (x_coordinate and y_coordinate) for the new aliens.
        y_coordinate (int): Position on the y-axis.

    Returns:
        list: List of aliens

    This function should return a list of aliens with their starting positions, health etc.

    """
    aliens = []
    for start_position in start_positions:
        aliens.append(Alien(start_position[0], start_position[1]))

    return aliens