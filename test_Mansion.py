import Mansion
import constants


def test_init():
    mansion = Mansion.Mansion(5, 5)
    assert len(mansion.board) == 5
    assert len(mansion.board[0]) == 5


def test_def_populate():
    mansion = Mansion.Mansion(5, 5)
    mansion.populate(1)
    lines = range(len(mansion.board))

    for line in lines:
        cases = range(len(mansion.board[line]))

        for case in cases:
            case_content = mansion.board[line][case]
            assert case_content == constants.DUST or case_content == constants.JEWEL


def test_get_mansion_dimensions():
    mansion = Mansion.Mansion(5, 5)
    assert mansion.get_mansion_dimensions() == {'width': 5, 'height': 5}
