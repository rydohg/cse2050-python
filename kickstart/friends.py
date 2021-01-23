from sys import stdin, stdout

num_test_cases = int(stdin.readline())
letter_matrix = []
for i in range(26):
    letter_matrix.append([])
name_array = []

count = 1
recursion_depth = 1


def recursively_find(index, query_index):
    for char in name_array[index - 1]:
        for name in letter_matrix[ord(char.lower()) - 97]:
            for search_name_char in name_array[query_index - 1]:
                if search_name_char in name:
                    return 1
    global count
    count += 1
    global recursion_depth
    if recursion_depth >= 26:
        return -1
    recursion_depth += 1
    recursively_find(letter_matrix[index - 1], query_index)


def run_query(start, end):
    if start == end:
        return 0
    for char in name_array[start - 1]:
        if char in name_array[end - 1]:
            return 2
    return count if recursively_find(start - 1, end - 1) else -1


for i in range(num_test_cases):
    n_and_q = [int(num) for num in stdin.readline().rstrip().split()]
    for name in stdin.readline().split():
        name_array.append(name)
        for letter in name:
            letter_matrix[ord(letter.lower()) - 97].append(len(name_array) - 1)

    for letter in letter_matrix:
        letter.sort(key=lambda index: name_array[index])

    stdout.write(f"Case #{i + 1}: ")
    for q in range(n_and_q[1]):
        query = [int(num) for num in stdin.readline().rstrip().split()]
        distance = run_query(query[0], query[1])
        stdout.write(f"{distance} ")
