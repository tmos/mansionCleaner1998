import Game
import Mansion
import Robot


def test_init():
    game = Game.Game()
    assert type(game.instance) is Game.Game


def test_get_game():
    game = Game.Game()
    assert type(game.get_game()) is Game.Game


def test_get_current_mansion():
    game = Game.Game()
    assert type(game.get_current_mansion()) is Mansion.Mansion


def test_get_robot():
    game = Game.Game()
    assert type(game.get_robot()) is Robot.Robot


def test_create_new_robot():
    game = Game.Game()
    assert type(game.create_new_robot(game.get_current_mansion())) is Robot.Robot
