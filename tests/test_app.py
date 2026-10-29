from smoke.app import greet


def test_greet() -> None:
    assert greet("ci") == "hello ci"
