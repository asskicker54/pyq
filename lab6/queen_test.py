import pytest
import numpy as np

l = list('abcdefjh')
board = np.chararray((8, 8), itemsize=2, unicode=True)
for i in range(len(l)):
    for j in range(len(l)):
        board[j][i] = f'{l[i]}{j+1}'
        
#print(board)

def is_under_queen_attack(position, queen_position):
    if type(position) != str:
        raise TypeError(f'Expected str, got {type(position)}')
    elif position not in board:
        raise ValueError(f'No such position coordinate')
    
    if type(queen_position) != str:
        raise TypeError(f'Expected str, got {type(queen_position)}')
    elif queen_position not in board:
        raise ValueError(f'No such queen position coordinate')
    
    if(position[0] == queen_position[0]) or (position[1] == queen_position[1]):
        return True
    
    if (position[0] == queen_position[0]) or (position[1] == queen_position[1]):
        return True

    queen_pos_let, queen_pos_num = np.where(board == queen_position) # get queen board position (returns [row], [col] indexes in the ndarray board)
    if position in np.diag(board, k=(queen_pos_num[0] - queen_pos_let[0])):
        return True
    
    return False

print(is_under_queen_attack("b3", "e6"))

def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(None, 42)


def test_wrong_coordinate():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "42")


def test_wrong_coordinate2():
    with pytest.raises(ValueError):
        is_under_queen_attack('c3', 'd4d')


def test_wrong_coordinate_out_of_bounds():
    with pytest.raises(ValueError):
        is_under_queen_attack("e1", "e9")


def test_attack_same_field():
    assert is_under_queen_attack("e5", "e5")


def test_attack_same_row():
    assert is_under_queen_attack("a1", "e1")


def test_attack_same_column():
    assert is_under_queen_attack("a1", "a8")


def test_attack_diagonal():
    assert is_under_queen_attack("b3", "e6")


def test_no_attack():
    assert not is_under_queen_attack("c4", "e5")
    