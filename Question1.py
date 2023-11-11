import numpy as np
def matrix(matrix_a, matrix_b):
    for index_a, i in enumerate(matrix_a):
        for index_b, j in enumerate(matrix_b):
            new_matrix[index_a][index_b] = sum(i * j)
    return new_matrix
    
def enumerated_matrix():
  matrix_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

  matrix_b = np.array([[9, 8, 7],
                      [6, 5, 4],
                      [3, 2, 1]])

  # enumerate method
  new_matrix = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])
  useranswer = input("Enter your answer here in the form xx yy zz.....: ") # user input
  a1, a2, a3, b1, b2, b3, c1, c2, c3 = useranswer.split(" ") 
  
  answer = matrix(matrix_a, matrix_b)
  if answer[0] == [int(a1), int(a2), int(a3)] and answer[1] == [int(b1), int(b2), int(b3)] and answer[2] == [int(c1), int(c2), int(c3)]:
    print("You are correct")
  else: print("You are incorrect")
