def найти_индекс_товара(список, товар):

    for индекс in range(len(список)):
        if список[индекс] == товар:
            return индекс

    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = найти_индекс_товара(items_list, find_item)

    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")