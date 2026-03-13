import heapq

print("--- The N Largest/Smallest Finder ---")


user_numbers = input("Enter space seperated number: ")


number_list = []
for num in user_numbers.split():
    number_list.append(int(num))


n_count = int(input("Enter no of item to extract: "))


choice = input("Enter 'largest' or 'smallest' numbers? ").strip().lower()


if choice == "largest":
    result = heapq.nlargest(n_count, number_list)
    print(f"\nThe {n_count} largest numbers are: {result}")

elif choice == "smallest":
    result = heapq.nsmallest(n_count, number_list)
    print(f"\nThe {n_count} smallest numbers are: {result}")

else:
    print(
        "\nInvalid choice. Please run the program again and type 'largest' or 'smallest'."
    )
