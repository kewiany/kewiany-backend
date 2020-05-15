import sys

VERSION = '0.0.1'

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass
