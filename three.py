# 3 - Problem: Combining two lists

list1 = [
    {"positions": [0, 5], "values": ["A"]},
    {"positions": [10, 15], "values": ["B"]},
    {"positions": [4, 8], "values": ["C"]},
]

list2 = [
    {"positions": [12, 18], "values": ["D"]},
    {"positions": [1, 5], "values": ["E"]},
    {"positions": [7, 16], "values": ["F"]},
]

merged_list = list1 + list2

merged_list.sort(key=lambda x: x["positions"][0])

result = []

i = 0

while i < len(merged_list):
    current_element = merged_list[i]
    left_pos = current_element["positions"][0]
    right_pos = current_element["positions"][1]
    values = current_element["values"]

    if i + 1 < len(merged_list):
        next_element = merged_list[i + 1]
        next_left_pos = next_element["positions"][0]
        next_right_pos = next_element["positions"][1]

        # checking for orverlap
        if right_pos > next_left_pos:
            combined_values = values + next_element["values"]
            combined_element = {
                "positions": [left_pos, next_element["positions"][1]],
                "values": combined_values,
            }
            result.append(combined_element)
            # skipping 2 elemets since they are already merged
            i += 2
        else:
            # no overlap condition
            result.append(current_element)
            i += 1
    else:
        # appending last element
        result.append(current_element)
        i += 1

print(result)
