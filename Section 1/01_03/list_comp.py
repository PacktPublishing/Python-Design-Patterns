numbers = [1,2,3,4,5]
numbers_again = [n for n in numbers]
even_numbers = [n for n in numbers if n%2 == 0]
odd_squares = [n**2 for n in numbers if n%2 == 1]
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened_matrix = [n for row in x for n in row]
