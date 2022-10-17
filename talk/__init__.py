"""
just a few definitions to make the introduction slide more fun
"""
from collections import namedtuple
from pathlib import Path

Degree = type("Degree", (), dict(__init__=lambda *_: None))
Career = type("Career", (), dict(__init__=lambda *_: None))
Session = namedtuple("Session", "name")

DATA_DIR = Path(__file__).parent.parent
