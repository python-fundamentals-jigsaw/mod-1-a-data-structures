import pytest
import sys
sys.path.append(".")

from writingcode.index import *

def test_hello_world():
    assert hello_world() == 'hello world alsjs'
