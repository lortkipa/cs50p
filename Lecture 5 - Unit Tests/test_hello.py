from hello import hello

def test_default():
    assert hello() == 'hello, [NO NAME]!'

def test_argument():
        assert hello('David') == 'hello, David!'