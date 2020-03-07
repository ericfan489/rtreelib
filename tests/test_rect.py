from unittest import TestCase
from rtreelib import Rect


class TestRect(TestCase):
    """Rect class tests"""

    def test_init(self):
        """Basic test ensuring a Rect can be instantiated"""
        r = Rect(0, 1, 5, 9)
        self.assertEqual(0, r.min_x)
        self.assertEqual(1, r.min_y)
        self.assertEqual(5, r.max_x)
        self.assertEqual(9, r.max_y)

    def test_union_disjoint(self):
        """Tests union of two disjoint (non-intersecting) rectanges"""
        # Arrange
        r1 = Rect(min_x=0, min_y=-1, max_x=3, max_y=3)
        r2 = Rect(min_x=2, min_y=5, max_x=6, max_y=8)
        # Act
        rect = r1.union(r2)
        # Assert
        self.assertEqual(Rect(min_x=0, min_y=-1, max_x=6, max_y=8), rect)

    def test_union_intersecting(self):
        """Tests union of two intersecting rectanges"""
        # Arrange
        r1 = Rect(min_x=0, min_y=0, max_x=3, max_y=3)
        r2 = Rect(min_x=-2, min_y=-2, max_x=2, max_y=2)
        # Act
        rect = r1.union(r2)
        # Assert
        self.assertEqual(Rect(min_x=-2, min_y=-2, max_x=3, max_y=3), rect)

    def test_union_contains(self):
        """Tests union of two rectanges where one contains the other"""
        # Arrange
        r1 = Rect(min_x=1, min_y=1, max_x=3, max_y=3)
        r2 = Rect(min_x=-2, min_y=-2, max_x=5, max_y=5)
        # Act
        rect = r1.union(r2)
        # Assert
        self.assertEqual(Rect(min_x=-2, min_y=-2, max_x=5, max_y=5), rect)

    def test_intersection_area_disjoint(self):
        """
        Tests getting the intersection area of two completely disjoint (non-intersecting) rectangles with no overlap in
        either dimension.
        """
        # Arrange
        r1 = Rect(min_x=0, min_y=0, max_x=3, max_y=3)
        r2 = Rect(min_x=5, min_y=5, max_x=8, max_y=8)
        # Act
        area = r1.get_intersection_area(r2)
        # Assert
        self.assertEqual(0, area)

    def test_intersection_area_disjoint_x_overlap(self):
        """
        Tests getting the intersection area of two disjoint rectangles where there is overlap in the x-dimension but not
        in the y-dimension.
        """
        # Arrange
        r1 = Rect(min_x=0, min_y=-1, max_x=3, max_y=3)
        r2 = Rect(min_x=2, min_y=5, max_x=6, max_y=8)
        # Act
        area = r1.get_intersection_area(r2)
        # Assert
        self.assertEqual(0, area)

    def test_intersection_area_disjoint_y_overlap(self):
        """
        Tests getting the intersection area of two disjoint rectangles where there is overlap in the y-dimension but not
        in the x-dimension.
        """
        # Arrange
        r1 = Rect(min_x=0, min_y=0, max_x=2, max_y=4)
        r2 = Rect(min_x=2, min_y=2, max_x=3, max_y=3)
        # Act
        area = r1.get_intersection_area(r2)
        # Assert
        self.assertEqual(0, area)

    def test_intersection_area(self):
        """Tests getting the intersection area of two intersecting rectangles"""
        # Arrange
        r1 = Rect(min_x=0, min_y=0, max_x=4, max_y=4)
        r2 = Rect(min_x=2, min_y=2, max_x=5, max_y=5)
        # Act
        area = r1.get_intersection_area(r2)
        # Assert
        self.assertEqual(4, area)
