from colorpoint import ColorPoint  # Import base class


class AdvancedPoint(ColorPoint):
    """
    AdvancedPoint extends ColorPoint with additional color management,
    validation, and utility methods.
    """

    COLORS = ["red", "blue", "green", "black", "white"]  # Default allowed colors

    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint with x, y coordinates and a color.

        Args:
            x (int | float): X coordinate.
            y (int | float): Y coordinate.
            color (str): Color of the point, must be in COLORS.

        Raises:
            TypeError: If x or y is not numeric.
            ValueError: If color is not in allowed COLORS list.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")  # Corrected error message
        if color not in self.COLORS:
            raise ValueError(f"color must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @classmethod
    def add_color(cls, new_color):
        """
        Add a new color to the class-level COLORS list.

        Args:
            new_color (str): The new color to be added.
        """
        cls.COLORS.append(new_color)

    @property
    def x(self):
        """Return the x-coordinate of the point."""
        return self._x

    @property
    def y(self):
        """Return the y-coordinate of the point."""
        return self._y

    @property
    def color(self):
        """Get the current color of the point."""
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Set a new color for the point if it's in the allowed COLORS list.

        Args:
            new_color (str): New color to set.

        Raises:
            ValueError: If color is not in COLORS.
        """
        if new_color not in self.COLORS:
            raise ValueError(f"color must be one of {self.COLORS}")
        self._color = new_color

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Compute the Euclidean distance between two AdvancedPoint instances.

        Args:
            p1 (AdvancedPoint): First point.
            p2 (AdvancedPoint): Second point.

        Returns:
            float: The distance between p1 and p2.
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    @staticmethod
    def from_dictionary(dict_):
        """
        Create an AdvancedPoint instance from a dictionary.

        Args:
            dict_ (dict): Dictionary with keys 'x', 'y', 'color'.

        Returns:
            AdvancedPoint: A new point with extracted values or defaults.
        """
        x = dict_.get("x", 10)
        y = dict_.get("y", 20)
        color = dict_.get("color", "black")
        return AdvancedPoint(x, y, color)


# Example usage
AdvancedPoint.add_color("amber")  # Extend color palette
p2 = AdvancedPoint(1, 2, "amber")  # Create a point with new color
p1 = AdvancedPoint(3, 4, "red")  # Create a standard point
print(p2)  # Output representation (you can customize __str__)
