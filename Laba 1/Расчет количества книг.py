объем_дискеты = 1.44
страниц = 100
строк = 50
символов = 25
байт_на_символ = 4
total_chars = страниц * строк * символов
book_bytes = total_chars * байт_на_символ
disk_bytes = объем_дискеты * 1024 * 1024
books_count = disk_bytes // book_bytes
print("Количество книг, помещающихся на дискету:", books_count)
