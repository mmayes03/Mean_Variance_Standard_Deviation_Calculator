
import numpy as np

# ls = np.array([0,1,2,3,4,5,6,7,8]).reshape(3,3)
# a = ls.std(axis=1) #row
# b = ls.std(axis = 0) #column
# print(a, b, ls.mean())
# mean_rows = [ls[0:2].mean(), ls[3:6].mean(), ls[7:8].mean()]
# print(mean_rows)

def calculate(list):
    #posibly do 
    # if len(list) != 9:
    #     raise ValueError("List must contain nine numbers")

    statistics_for_list = {}
    try:
        new_array = np.array(list).reshape(3,3)
    
    except ValueError:
        raise ValueError("List must contain nine numbers")
    else:
        statistics_for_list['mean'] = [(new_array.mean(axis = 0)).tolist(), (new_array.mean(axis = 1)).tolist(), new_array.mean()]
        statistics_for_list['variance'] = [(new_array.var(axis = 0)).tolist(), (new_array.var(axis = 1)).tolist(), new_array.var()]
        statistics_for_list['standard deviation'] = [(new_array.std(axis = 0)).tolist(), (new_array.std(axis = 1)).tolist(), new_array.std()]
        statistics_for_list['max'] = [(new_array.max(axis = 0)).tolist(), (new_array.max(axis = 1)).tolist(), new_array.max()]
        statistics_for_list['min'] = [(new_array.min(axis = 0)).tolist(), (new_array.min(axis = 1)).tolist(), new_array.min()]
        statistics_for_list['sum'] = [(new_array.sum(axis = 0)).tolist(), (new_array.sum(axis = 1)).tolist(), new_array.sum()]
    return statistics_for_list
    



print(calculate([0,1,2,3,4,5,6,7,8]))
#Should return: 
# {
#   'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
#   'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
#   'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
#   'max': [[6, 7, 8], [2, 5, 8], 8],
#   'min': [[0, 1, 2], [0, 3, 6], 0],
#   'sum': [[9, 12, 15], [3, 12, 21], 36]
# }

# print(calculate([0,1,2,3,4,5,6,7,8, 9]))
#Should return: 'ValueError: List must contain nine numbers'
