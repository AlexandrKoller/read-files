def reading_file(name_file_list):
    file_length = {}
    for name_file in name_file_list:
        count = 0
        with open(name_file, 'r', encoding='utf-8') as file:
            for line in file:
                count += 1
        file_length[count] = name_file
    return file_length


name_file_list = ['1.txt', '2.txt', '3.txt']
len_file = reading_file(name_file_list)
sorted_key = sorted(len_file)

file_recode = open('Ended_file.txt', 'w', encoding='utf-8')
for key in sorted_key:
    with open(len_file[key], 'r', encoding='utf-8') as file:
        file_recode.write(f'{len_file[key]}\n')
        file_recode.write(f'{str(key)}\n')
        for string in file:
            file_recode.write(string)
file_recode.close()
