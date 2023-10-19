import numpy as np
import itertools
import collections
import heapq
import pickle

# Функция для считывания двумерного массива из файла
def read_array(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        array = [list(map(int, line.strip().split())) for line in lines]
        return np.array(array)

# (рекурсивный алгоритм)
def flatten_array(array):
    if len(array) == 1:
        return array[0]
    else:
        return np.concatenate((array[0], flatten_array(array[1:])))

# RLE
def rle_encode(array):
    compressed_array = []
    for key, group in itertools.groupby(array):
        compressed_array.append((key, len(list(group))))
    return compressed_array

# Хаффмана
def huffman_encode(array):
    counter = collections.Counter(array)
    heap = [[weight, [symbol, ""]] for symbol, weight in counter.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    huffman_dict = {}
    for pair in heap[0][1:]:
        huffman_dict[pair[0]] = pair[1]
    
    encoded_array = [huffman_dict[symbol] for symbol in array]
    return encoded_array, huffman_dict

# сохранение результатов в файл
def save_results(original_array, flattened_array, rle_compressed_array, huffman_encoded_array, huffman_dict):
    with open("results.txt", 'w') as file:
        file.write("Original Array:\n")
        file.write(str(original_array) + "\n\n")
        
        file.write("Flattened Array:\n")
        file.write(str(flattened_array) + "\n\n")
        
        file.write("RLE:\n")
        file.write(str(rle_compressed_array) + "\n\n")
        
        file.write("Huffman Encoded Array:\n")
        file.write(str(huffman_encoded_array) + "\n\n")
        
        file.write("Huffman Dictionary:\n")
        file.write(str(huffman_dict) + "\n")

# Считывание двумерного квадратного массива из файла
array = read_array("input.txt")

# массив в одномерный
flattened_array = flatten_array(array)

# RLE
rle_compressed_array = rle_encode(flattened_array)

# Хаффман
huffman_encoded_array, huffman_dict = huffman_encode(flattened_array)

# Вывод 
print("Original Array:")
print(array)
print("\nFlattened Array:")
print(flattened_array)

# Вывод RLE 
print("\nRLE Compressed Array:")
print(rle_compressed_array)

# Вывод Хаффмана
print("\nHuffman Encoded Array:")
print(huffman_encoded_array)

# Сохранение результатов в файл
save_results(array, flattened_array, rle_compressed_array, huffman_encoded_array, huffman_dict)
