"""
Module that defines a 2D Point class with functionality for:
- Representing the point as a string
- Calculating the distance from the origin
- Comparing points based on their distance from the origin

Includes a demonstration of random Point generation, sorting,
and a simulation checking how often two random points are equal.
"""

import random
from math import *


class Point:
    """
    Class modeling a real-life 2D point with basic comparison operations.

    Attributes:
        x (int or float): X-coordinate of the point.
        y (int or float): Y-coordinate of the point.
    """

    def __init__(self, x, y):
        """
        Initialize a 2D point.

        Args:
            x (int or float): The x-coordinate.
            y (int or float): The y-coordinate.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the point.

        Returns:
            str: Formatted string showing coordinates.
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Return a string representation for use in lists or debugging.

        Returns:
            str: Same as __str__.
        """
        return self.__str__()

    def distance_orig(self):
        """
        Compute the distance of the point from the origin (0, 0).

        Returns:
            float: Euclidean distance from origin.
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other):
        """
        Greater-than comparison based on distance from the origin.

        Args:
            other (Point): Another point to compare to.

        Returns:
            bool: True if this point is farther from origin than the other.
        """
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        """
        Equality comparison based on distance from the origin.

        Args:
            other (Point): Another point to compare to.

        Returns:
            bool: True if distances from the origin are equal.
        """
        return self.distance_orig() == other.distance_orig()


if __name__ == "__main__":
    """
    Demonstrates:
    - Creating and displaying Point instances.
    - Sorting points by distance from the origin.
    - Calculating a point's distance.
    - Running a simulation to check how often two random points are equal 
      in distance from the origin.
    """
    p1 = Point(1, 2)

    points = []
    for i in range(5):
        # Create random points
        p = Point(random.randint(-100, 100), random.randint(-100, 100))
        points.append(p)

    print(points)

    p = Point(12, 5)
    print(p.distance_orig())

    p1 = Point(2, 4)
    p2 = Point(3, 3)

    # Sort points by their distance from origin
    points.sort()
    print(points)

    found = 0
    count = 0

    # Simulation: how often two randomly generated points have the same distance from origin
    while found < 1000:
        count += 1
        p1 = Point(random.randint(-100, 100), random.randint(-100, 100))
        p2 = Point(random.randint(-100, 100), random.randint(-100, 100))
        if p1 == p2:
            found += 1

    print(found / found, count / found)