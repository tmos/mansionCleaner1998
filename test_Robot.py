import Robot
import Mansion

robot = Robot.Robot(Mansion.Mansion())
mansion = robot.mansion


def test_init():
    assert type(robot.mansion) is Mansion.Mansion
    assert robot.position['x'] != -1
    assert robot.position['y'] != -1


def test_look_for_new_targets():
    assert robot.look_for_new_targets() is None
    robot.mansion.populate(2)
    assert type(robot.look_for_new_targets()) is list


def test_clean():
    assert True


def test_move():
    assert True
