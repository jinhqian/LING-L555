import sys

# Read in everything from standard input
text = sys.stdin.read()

# replace every full stop '.' followed by a space ' ' with a full stop and a newline character '\n'.
text = text.replace('. ', '.\n')

# Output everything to standard output
sys.stdout.write(text)

