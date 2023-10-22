from decimal import Decimal

# Функция для расчета частот символов в строке
def calculate_frequencies(s):
    frequencies = {}
    total = len(s)

    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    for char, count in frequencies.items():
        frequencies[char] = Decimal(count) / Decimal(total)

    return frequencies

# Функция для выполнения арифметического кодирования
def arithmetic_coding(s):
    frequencies = calculate_frequencies(s)

    low = {}
    high = {}
    cumul_prob = 0

    for char, freq in frequencies.items():
        low[char] = cumul_prob
        high[char] = cumul_prob + freq
        cumul_prob += freq

    lower_bound = 0
    upper_bound = 1

    for char in s:
        range_size = upper_bound - lower_bound
        upper_bound = lower_bound + range_size * high[char]
        lower_bound = lower_bound + range_size * low[char]

    return (lower_bound + upper_bound) / 2

s = "Винни шагал мимо сосен и елок, шагал по склонам, заросшим можжевельником и репейником, шагал по крутым берегам ручьев и речек, шагал среди груд камней и снова среди зарослей, и вот наконец, усталый и голодный, он вошел в Дремучий Лес, потому что именно там, в Дремучем Лесу, жила Сова"

result = arithmetic_coding(s)
print("Arithmetic:",result)


def bwt_transform(s):
    n = len(s)
    suffixes = [s[i:] + s[:i] for i in range(n)]
    suffixes.sort()
    bwt = ''.join(suffix[-1] for suffix in suffixes)
    return bwt

def move_to_front(sequence):
    alphabet = list(set(sequence))  # Создание алфавита на основе уникальных символов
    alphabet.sort()  # Сортировка алфавита в соответствии с реальным алфавитом

    encoded_sequence = []  # Инициализация закодированной последовательности

    for char in sequence:
        # Поиск индекса символа в алфавите
        index = alphabet.index(char)
        encoded_sequence.append(str(index))  # Добавление индекса в закодированную последовательность

        # Перемещение символа в начало алфавита
        alphabet.remove(char)
        alphabet.insert(0, char)

    return ''.join(map(str, encoded_sequence))



input_phrase = "ИИККЕКВАУЦСРННН"
bwt_result = bwt_transform(input_phrase)
mtf_result = move_to_front(bwt_result)

print("BWT:", bwt_result)
print("MtF:", mtf_result)
