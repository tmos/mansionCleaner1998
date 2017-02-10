import Game
import Mansion
import Robot

game = Game.Game()


def test_init():
    assert type(game.instance) is Game.Game


def test_get_game():
    assert type(game.get_game()) is Game.Game


def test_get_current_mansion():
    assert type(game.get_current_mansion()) is Mansion.Mansion


def test_get_robot():
    assert type(game.get_robot()) is Robot.Robot


def test_create_new_robot():
    assert type(game.create_new_robot(game.get_current_mansion())) is Robot.Robot
