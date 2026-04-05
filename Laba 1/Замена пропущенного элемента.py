numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
Пропуск = numbers.index(None)
Без_Пропуска = [x for x in numbers if x is not None]
total_sum = sum(Без_Пропуска)
count = len(numbers)
average = total_sum / count
numbers[Пропуск] = average
print("Измененный список:", numbers)
