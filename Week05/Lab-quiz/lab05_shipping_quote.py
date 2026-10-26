def calculate_subtotal(item_prices):
    """Calculates the sum of items in the cart."""
    return sum(item_prices)

def get_discount_rate(subtotal):
    """Returns 10% discount (0.10) if subtotal is $100 or more, otherwise 0%."""
    if subtotal >= 100.0:
        return 0.10
    return 0.0

def calculate_shipping_fee(subtotal):
    """Returns $0.0 shipping if subtotal is $50 or more, otherwise $10.0."""
    if subtotal >= 50.0:
        return 0.0
    return 10.0

def calculate_final_total(subtotal, discount_rate, shipping_fee):
    """Calculates final price after applying discount and adding shipping fee."""
    discount_amount = subtotal * discount_rate
    return (subtotal - discount_amount) + shipping_fee


assert get_discount_rate(100.0) == 0.10, "Threshold failed: 100 should get 10% discount"
assert get_discount_rate(99.99) == 0.0, "Threshold failed: Just below 100 should get 0% discount"

assert calculate_shipping_fee(50.0) == 0.0, "Threshold failed: 50 should get free shipping"
assert calculate_shipping_fee(49.99) == 10.0, "Threshold failed: Below 50 should pay shipping"

assert calculate_final_total(100.0, 0.10, 0.0) == 90.0, "Math check failed for final total"

print("All assertion tests passed successfully!\n")

def process_and_display_order(order_id, item_prices):
    """Helper function to run the calculations and print for any order."""
    subtotal = calculate_subtotal(item_prices)
    discount_rate = get_discount_rate(subtotal)
    shipping_fee = calculate_shipping_fee(subtotal)
    final_total = calculate_final_total(subtotal, discount_rate, shipping_fee)
    
    print(f"--- Order: {order_id} ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_rate * 100:.0f}%")
    print(f"Shipping: ${shipping_fee:.2f}")
    print(f"Final Total: ${final_total:.2f}\n")

order_1_items = [15.0, 20.0, 10.0]  
order_2_items = [50.0, 60.0]        

process_and_display_order("Sample Order 1", order_1_items)
process_and_display_order("Sample Order 2", order_2_items)

