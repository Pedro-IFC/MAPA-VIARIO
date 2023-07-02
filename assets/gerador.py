def create_matrix(string):
    lines = string.split('\n')
    rows = len(lines)
    cols = len(lines[0])
    matrix = [[None] * cols for _ in range(rows)]
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            matrix[i][j] = char
            
    return matrix

string = '''O==+=====1
^##v#####"
^##v#####"
^##v#####"
^##+=====+
^##v#####"
^##v#####"
^##v#####"
^##v#####"
^<<2<<<<<+'''

matrix = create_matrix(string)
print(matrix)
