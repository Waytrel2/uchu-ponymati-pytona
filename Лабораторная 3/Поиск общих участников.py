def find_common_participants(participants1, participants2, separator=","):
    list1 = participants1.split(separator)
    list2 = participants2.split(separator)

    common = []
    for name in list1:
        if name in list2:
            common.append(name)

    common.sort()

    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)