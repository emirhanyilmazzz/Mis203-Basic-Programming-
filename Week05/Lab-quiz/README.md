# Week 5 Lab: Reusable Shipping Quote

**Test Run:** I ran the program with an order subtotal of $49.99 to verify the shipping threshold boundary. The assert check passed, confirming it correctly charged $10.0 for shipping instead of making it free.

**Change After Testing:** Initially, I didn't use floats for my boundaries. After testing, I changed `99` to `99.99` and `49` to `49.99` in my assert statements to ensure decimal inputs near the threshold are handled correctly.

