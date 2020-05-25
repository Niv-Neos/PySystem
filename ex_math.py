import sys

def det_two(list_i = [0,0], list_ii = [0,0]):
       result = (list_i[0] * list_ii[1]) - (list_i[1] * list_ii[0])

def det_three(list_i = [0,0,0], list_ii = [0,0,0], list_iii = [0,0,0]):
       result = ((list_i[0] * list_ii[1] * list_iii[2]) +
                 (list_i[1] * list_ii[2] * list_iii[0]) +
                 (list_i[2] * list_ii[0] * list_iii[1])) -
                 ((list_i[2] * list_ii[1] * list_iii[0]) +
                  (list_i[0] * list_ii[2] * list_iii[1]) +
                  (list_i[1] * list_ii[0] * list_iii[2]))
       

squirt = 1.4142135623730950488016887242097
