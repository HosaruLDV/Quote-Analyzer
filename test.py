from select_sorted import select_sorted
import csv
import os

data = {}
cache = {}

def get_page(func):
    top10 = func[0]
    cache_name = func[1]
    if os.path.exists(f'cache/{cache_name}.csv'):
        with open(f'cache/{cache_name}.csv') as cache_file:
            reader = csv.DictReader(cache_file)
            for row in reader:
                print(row)

    else:
        f = open(f'cache/{cache_name}.csv', "w", encoding="utf-8", newline="")
        writer = csv.DictWriter(f, fieldnames=list(top10[0].keys()), delimiter=",", quoting=csv.QUOTE_NONE)
        writer.writeheader()
        for i in top10:
            writer.writerow(i)

        print(top10)

print(get_page(select_sorted(sort_columns="high", limit=10, group_by_name=False, order='desc', filename='dump4.csv')))
print(get_page(select_sorted(sort_columns="high", limit=10, group_by_name=False, order='desc', filename='dump4.csv')))
print(get_page(select_sorted(sort_columns="high", limit=10, group_by_name=False, order='desc', filename='dump4.csv')))