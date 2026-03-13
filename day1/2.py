discount_coupons = {}

days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

print("--- Weekly Coupon Setup ---")

for day in days_of_the_week:

    user_discount = input(f"Enter the discount percentage for {day.capitalize()}: ").strip()

    discount_coupons[day] = f"{user_discount}%"

print("\n--- Final Coupon Dictionary ---")
print(discount_coupons)

# 5. Testing the lookup (just like the previous step)
print("\n--- Customer Lookup ---")
check_day = input("Customer: What day are you shopping? ").strip().lower()

if check_day in discount_coupons:
    print(f"Great! You get a {discount_coupons[check_day]} discount today.")
else:
    print("Sorry, there are no discounts available for that day.")
