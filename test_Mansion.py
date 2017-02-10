import Mansion
import objects

mansion = Mansion.Mansion(5,5)


def test_init():
    assert len(mansion.board) == 5
    assert len(mansion.board[0]) == 5


def test_def_populate():
    mansion.populate(1)
    lines = range(len(mansion.board))

    for line in lines:
        cases = range(len(mansion.board[line]))

        for case in cases:
            case_content = mansion.board[line][case]
            assert case_content == objects.DUST or case_content == objects.JEWEL


def test_get_mansion_dimensions():
    assert mansion.get_mansion_dimensions() == {'width': 5, 'height': 5}
