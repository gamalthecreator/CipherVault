def Railfencecipher(cleartext, key):
    result = ""

    matrix = [["" for x in range(len(cleartext))] for y in range(key)]

    increment = 1
    row = 0
    col = 0

    for c in cleartext:
        matrix[row][col] = c
        if row == 0:
            increment = 1
        elif row == key - 1:
            increment = -1

        row += increment
        col += 1

    for list in matrix:
        result += "".join(list)
    return result


def transpose(matrix):
    
    result = [[0 for y in range(len(matrix))] for x in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    
    return result


def Rail_fence_decipher(cipheredtext, key):
    
    result = ""

    matrix = [["" for x in range(len(cipheredtext))] for y in range(key)]

    index = 0
    increment = 1

    for SelectedRow in range(len(matrix)):
        row = 0

        for col in range(len(matrix[ row ])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            
            if row == SelectedRow: 
                matrix[row][col] += cipheredtext[index]
                index += 1
            
            row += increment
    
    matrix = transpose(matrix)

    for list in matrix:
        result+= "".join(list)
    return result
