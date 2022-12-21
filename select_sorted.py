import csv
import os


def get_sorted():
    dd = {1: "open", 3: "high", 4: "low", 2: "close", 5: "volume"}
    s_c = dd[int(input("""
Сортировать по цене 
открытия (1)
закрытия (2)
максимум [3]
минимум (4)
объем (5)
"""))]
    limit = int(input("Ограничение выборки [10]"))
    group_by_name = False
    order = input("Порядок по убыванию [1] / возрастанию (2)")
    filename = input(str("Название файла для сохранения результата [dump.csv]"))

    return select_sorted(s_c, limit, group_by_name, order, filename)

def select_sorted(sort_columns="high", limit=30, group_by_name=False, order='desc', filename='dump.csv'):
    cache_name = "".join(str(sort_columns)) + "".join(str(limit)) + "".join(str(filename)) + "".join(str(order))
    s_c = str(sort_columns)
    f_n = "".join(filename)

    if os.path.exists(f'cache/{cache_name}.csv'):
        with open(f'cache/{cache_name}.csv') as cache_file:
            reader = csv.DictReader(cache_file)
            for row in reader:
                print(
                    f"{row['date']}|{row['open']}|{row['high']}|{row['low']}|{row['close']}|{row['volume']}|{row['Name']}")
            cache_file.close()

    else:
        file_ = open("all_stocks_5yr.csv", "r", encoding="utf-8")
        reader = csv.DictReader(file_, delimiter=',', quotechar='|')
        top10 = sorted(reader, key=lambda x: float(x[s_c] or 0), reverse=True)[:int(limit)]
        file_ = open(f_n, "w", encoding="utf-8", newline="")
        writer = csv.DictWriter(file_, fieldnames=list(top10[0].keys()), delimiter=",", quoting=csv.QUOTE_NONE)
        writer.writeheader()
        f = open(f'cache/{cache_name}.csv', "w", encoding="utf-8", newline="")
        writer = csv.DictWriter(f, fieldnames=list(top10[0].keys()), delimiter=",", quoting=csv.QUOTE_NONE)
        writer.writeheader()
        for row in top10:
            writer.writerow(row)
            print(
                f"{row['date']}|{row['open']}|{row['high']}|{row['low']}|{row['close']}|{row['volume']}|{row['Name']}")

            """Запись в файл"""

        for i in top10:
            writer.writerow(i)
        f.close()
        file_.close()

