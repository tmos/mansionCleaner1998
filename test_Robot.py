import Robot
import Mansion
import constants


def test_init():
    robot = Robot.Robot(Mansion.Mansion())
    assert type(robot.mansion) is Mansion.Mansion
    assert robot.position['x'] != -1
    assert robot.position['y'] != -1


def test_look_for_new_targets():
    robot = Robot.Robot(Mansion.Mansion())
    assert robot.look_for_new_targets() is None
    robot.mansion.populate(2)
    assert type(robot.look_for_new_targets()) is list


def test_clean():
    robot = Robot.Robot(Mansion.Mansion())
    robot.mansion.populate(1)
    assert robot.get_current_cell() is not constants.EMPTY
    robot.clean()
    assert robot.get_current_cell() is constants.EMPTY


def test_move():
    robot = Robot.Robot(Mansion.Mansion())

    robot.position = {'x': 2, 'y': 2}
    robot.move(constants.UP)
    assert robot.position == {'x': 1, 'y':  2}

    robot.position = {'x': 2, 'y': 2}
    robot.move(constants.DOWN)
    assert robot.position == {'x': 3, 'y':  2}

    robot.position = {'x': 2, 'y': 2}
    robot.move(constants.LEFT)
    assert robot.position == {'x': 2, 'y': 1}

    robot.position = {'x': 2, 'y': 2}
    robot.move(constants.RIGHT)
    assert robot.position == {'x': 2, 'y': 3}
