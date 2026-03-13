# Create a dictionary that maps stock names to prices, which will keep insertion
# order.Find minimum price, maximum price and sort items according to their prices in
# first dictionary using itemgetter or lambda function. Create another second stock
# dictionary. Find items that are only in first dictionary and find items whose prices do
# not match. Remove duplicate items from first dictionary. Sort both dictionaries for
# incrementing prices. Group items in first dictionary by price in multiple of 500. Find
# an item with price=800 from both dictionaries.
import operator
from collections import defaultdict


def get_stock_data(dict_name):
    stocks = {}
    print(f"Enter data for {dict_name} (type 'exit' as name to stop):")
    while True:
        name = input("Stock name: ").strip()
        if name.lower() == "exit":
            break
        price_input = input(f"Price for {name}: ").strip()
        stocks[name] = int(price_input)
    return stocks


dict1 = get_stock_data("First Dictionary")
print("\n")
dict2 = get_stock_data("Second Dictionary")

min_item = min(dict1.items(), key=operator.itemgetter(1))
max_item = max(dict1.items(), key=operator.itemgetter(1))

sorted_dict1_initial = dict(sorted(dict1.items(), key=lambda x: x[1]))

only_in_dict1 = {k: dict1[k] for k in dict1.keys() - dict2.keys()}

mismatched_prices = {
    k: (dict1[k], dict2[k]) for k in dict1.keys() & dict2.keys() if dict1[k] != dict2[k]
}

seen_prices = set()
unique_dict1 = {}
for k, v in dict1.items():
    if v not in seen_prices:
        unique_dict1[k] = v
        seen_prices.add(v)
dict1 = unique_dict1

dict1 = dict(sorted(dict1.items(), key=operator.itemgetter(1)))
dict2 = dict(sorted(dict2.items(), key=operator.itemgetter(1)))

grouped_by_500 = defaultdict(dict)
for k, v in dict1.items():
    group_key = (v // 500) * 500
    grouped_by_500[group_key][k] = v

price_800_items = []
for d in (dict1, dict2):
    for k, v in d.items():
        if v == 800:
            price_800_items.append(k)

print("\n--- Results ---")
print("Min Price in Dict 1:", min_item)
print("Max Price in Dict 1:", max_item)
print("Dict 1 Sorted (Initial):", sorted_dict1_initial)
print("Items ONLY in Dict 1:", only_in_dict1)
print("Mismatched Prices (Dict 1, Dict 2):", mismatched_prices)
print("Dict 1 (Duplicates removed, Sorted):", dict1)
print("Dict 2 (Sorted):", dict2)
print("Dict 1 Grouped by 500s:", dict(grouped_by_500))
print("Items with Price == 800:", price_800_items)
