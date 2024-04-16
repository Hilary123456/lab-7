import numpy as np
from time import perf_counter

size = 1000000
list1 = [np.random.rand() for _ in range(size)]
list2 = [np.random.rand() for _ in range(size)]
array1 = np.array(list1)
array2 = np.array(list2)

start_list = perf_counter()
result_list = [a * b for a, b in zip(list1, list2)]
end_list = perf_counter()
list_time = end_list - start_list

start_numpy = perf_counter()
result_numpy = np.multiply(array1, array2)
end_numpy = perf_counter()
numpy_time = end_numpy - start_numpy

print("Время выполнения для списков:", list_time,"sec")
print("Время выполнения для массивов NumPy:", numpy_time,"sec")