"""
Test for my functions.

"""

from my_module.functions import *

# Test if start function is callable.
def test_start():
    assert callable(start)
    assert isinstance(start(), str)

# Test if generate function is caallable.
def test_generate():
    assert callable(generate)   
    assert isinstance(generate(), list)
    
# Test if run_game function is callable.
def test_run_game():
    assert callable(run_game)
    assert isinstance(run_game([1]), str)
    
# Test if hint function is callable.
def test_hint():
    assert callable(hint)
    assert isinstance(hint(answer = [1]), tuple)
