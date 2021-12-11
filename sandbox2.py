lines = ''
with open('names.txt') as f:
    lines = f.readlines()
linesString = str(lines)
linesSplit = linesString.split(',')
linesSplit