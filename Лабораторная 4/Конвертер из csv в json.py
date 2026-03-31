import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []

    with open(INPUT_FILENAME, "r", encoding="utf-8") as file:
        lines = file.read().split("\n")

    headers = lines[0].split(",")

    for line in lines[1:]:
        if not line:
            continue

        values = line.split(",")

        if len(values) != len(headers):
            continue

        row_dict = {}
        for i in range(len(headers)):
            row_dict[headers[i]] = values[i]

        data.append(row_dict)

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")