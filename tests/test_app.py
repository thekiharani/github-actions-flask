from app import index

def test_index():
    assert index() == '<h1>Welcome to The App</h1>'