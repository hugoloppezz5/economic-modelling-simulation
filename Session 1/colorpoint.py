"""Module to define a ColorPoint class, extending Point, with additional color attribute.
   Demonstrates creating and sorting random ColorPoint instances.
"""

from point import Point
import random


class ColorPoint(Point):
    """
    A class representing a point in 2D space with an associated color.

    Inherits from:
        Point: A base class that provides x and y coordinate functionality.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
        color (str): The color of the point.
    """

    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint with x and y coordinates and a color.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            color (str): The color of the point.
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
        Return a string representation of the ColorPoint.

        Returns:
            str: The formatted string showing coordinates and color.
        """
        return f"<{self.x}, {self.y}>, ({self.color})"


if __name__ == "__main__":
    """
    Demonstrates creation and sorting of random ColorPoint objects.

    - Generates 5 random ColorPoints with random positions and colors.
    - Prints the unsorted and sorted list of points.
    - Sorting assumes the Point class implements comparison based on distance.
    """
    color_points = []
    colors = ["red", "blue", "green", "yellow", "purple"]
    for i in range(5):
        p = ColorPoint(random.randint(-100, 100), random.randint(-100, 100), random.choice(colors))
        color_points.append(p)
    print("random color points: ")
    print(color_points)
    color_points.sort()
    print("color points sorted by distance: ")
    print(color_points)