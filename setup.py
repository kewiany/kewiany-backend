import sys

VERSION = '2.0.0'

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass
