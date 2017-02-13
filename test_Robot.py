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
    robot.mansion.populate(1)
    assert type(robot.look_for_new_targets()) is list


def test_clean():
    robot = Robot.Robot(Mansion.Mansion())
    robot.mansion.populate(1)
    cell = robot.get_current_cell()

    assert robot.get_current_cell() is not constants.EMPTY
    assert robot.cleaned_dust == 0
    assert robot.stored_jewels == 0
    assert robot.score == 100

    if cell is constants.DUST:
        robot.do_something(constants.CLEAN)
        assert robot.cleaned_dust == 1
    elif cell is constants.JEWEL:
        robot.do_something(constants.TAKE)
        assert robot.stored_jewels == 1

    assert robot.score == 109
    assert robot.get_current_cell() is constants.EMPTY


def test_move():
    robot = Robot.Robot(Mansion.Mansion())

    robot.position = {'x': 2, 'y': 2}
    robot.do_something(constants.UP)
    assert robot.position == {'x': 2, 'y':  1}

    robot.position = {'x': 2, 'y': 2}
    robot.do_something(constants.DOWN)
    assert robot.position == {'x': 2, 'y':  3}

    robot.position = {'x': 2, 'y': 2}
    robot.do_something(constants.LEFT)
    assert robot.position == {'x': 1, 'y': 2}

    robot.position = {'x': 2, 'y': 2}
    robot.do_something(constants.RIGHT)
    assert robot.position == {'x': 3, 'y': 2}
