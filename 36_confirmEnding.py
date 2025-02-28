def confirm_ending(string, target):
    return string.endswith(target)

# you don't need an argument with this, you use fixtures
def test_confirm_ending():
    # assert is a keyword, not a func
    assert confirm_ending('hi', 'i')
    
