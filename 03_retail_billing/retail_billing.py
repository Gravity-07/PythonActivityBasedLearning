def main():
    items = []
    try:
        count = int(input("How many different products? "))
        if count <= 0:
            raise ValueError("Product count must be greater than zero.")

        subtotal = 0.0
        for index in range(count):
            print(f"\\nProduct {index + 1}")
            name = input("Product name: ").strip()
            category = input("Category (electronics/other): ").strip().lower()
            price = float(input("Unit price (Rs.): "))
            quantity = int(input("Quantity: "))

            if price < 0 or quantity <= 0:
                raise ValueError("Price must be non-negative and quantity positive.")
            if category not in ("electronics", "other"):
                raise ValueError("Category must be electronics or other.")

            line_total = price * quantity
            items.append((name, category, price, quantity, line_total))
            subtotal += line_total

        discount_rate = 0.10 if subtotal >= 2000 else 0
        discount = subtotal * discount_rate
        tax_total = 0.0

        print("\\n================ INVOICE ================")
        for name, category, price, quantity, line_total in items:
            discounted_line = line_total * (1 - discount_rate)
            tax_rate = 0.18 if category == "electronics" else 0.05
            item_tax = discounted_line * tax_rate
            tax_total += item_tax
            print(f"{name}: {quantity} x Rs.{price:.2f} = Rs.{line_total:.2f}")
            print(f"  Tax ({tax_rate * 100:.0f}%): Rs. {item_tax:.2f}")

        total = subtotal - discount + tax_total
        print("-----------------------------------------")
        print(f"Subtotal : Rs. {subtotal:.2f}")
        print(f"Discount : Rs. {discount:.2f}")
        print(f"Tax      : Rs. {tax_total:.2f}")
        print(f"TOTAL    : Rs. {total:.2f}")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
