from wordle_yd2798 import wordle_yd2798
def test_validate_guess():
    assert wordle_yd2798.validate_guess("hello") == True
    assert wordle_yd2798.validate_guess("HELLO") == False
    assert wordle_yd2798.validate_guess("hi") == False
    assert wordle_yd2798.validate_guess("hello!") == False

def test_check_guess_basic():
    result = wordle_yd2798.check_guess("crane", "crane")
    expected = [('c', 'green'), ('r', 'green'), ('a', 'green'), 
                ('n', 'green'), ('e', 'green')]
    assert result == expected

    result = wordle_yd2798.check_guess("crane", "carts")
    expected = [('c', 'green'), ('a', 'yellow'), ('r', 'yellow'), 
                ('t', 'gray'), ('s', 'gray')]
    assert result == expected