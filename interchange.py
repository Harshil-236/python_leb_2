def interchange_first_last(input_list):
    if len(input_list) >= 2:
        input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list

input_list = [12, 35, 9, 56, 24]

output_list = interchange_first_last(input_list)

print(output_list)

output:-
![Screenshot (37)](https://github.com/user-attachments/assets/a9d7d13b-0d01-4311-8dbf-1f780743ed3b)

