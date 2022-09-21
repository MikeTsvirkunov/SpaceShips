import unittest
import pytest
from objects import Object
from move import MoveFront, MoveRotation

# @pytest.mark.usefixtures("db_class")
class TestFrontMoveObj(unittest.TestCase):

    def setUp(self) -> None:
        self.coord = (12, 5)
        self.speed = (-7, 3)
        self.expected = (5, 8)

    def test_mov_object_with_speed_and_coord(self):
        spaceship = Object({"speed": self.speed, "coord": self.coord})
        MoveFront().action(spaceship)
        if spaceship.get_param("coord") != self.expected:
            raise Exception("incorrect")

    @unittest.expectedFailure
    def test_move_obj_without_speed(self):
        spaceship = Object({"coord": self.coord})
        MoveFront().action(spaceship)

    @unittest.expectedFailure
    def test_move_obj_without_coords(self):
        spaceship = Object({"speed": self.speed})
        MoveFront().action(spaceship)

    @unittest.expectedFailure
    def test_move_obj_that_is_static(self):
        spaceship = str()
        MoveFront().action(spaceship)


class TestRotationObj(unittest.TestCase):

    def setUp(self) -> None:
        self.angle = 45
        self.rotation_speed = 90
        self.coord = (12, 5)
        self.speed = (-7, 3)
        self.expected = 135

    def test_mov_object_with_speed_and_angle(self):
        spaceship = Object({"speed": self.speed,
                            "coord": self.coord,
                            "angle": self.angle,
                            "rotation_speed": self.rotation_speed})
        MoveRotation().action(spaceship)
        if spaceship.get_param("angle") != self.expected:
            raise Exception("incorrect")

    @unittest.expectedFailure
    def test_move_obj_without_speed(self):
        spaceship = Object({"speed": self.speed, "coord": self.coord})
        MoveRotation().action(spaceship)

    @unittest.expectedFailure
    def test_move_obj_without_angle(self):
        spaceship = Object({"speed": self.speed, "coord": self.coord})
        MoveRotation().action(spaceship)

    @unittest.expectedFailure
    def test_move_obj_that_is_static(self):
        spaceship = str()
        MoveRotation().action(spaceship)


if __name__ == '__main__':
    unittest.main()
