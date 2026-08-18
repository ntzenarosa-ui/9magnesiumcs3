Computational Thinking Exercise
Smart Vending Machine
Name: Nathaniel
Section: Magnesium
Last Name: Zenarosa
Date: 08/18/2026

## Step 1: Identify the Big Problem
### Main Problem

The traditional vending machine system experiences frequent operational delays and transaction errors because product selection, inventory tracking, and payment processing are handled manually without automated real-time verification.

---

## Step 2: Identify the Sub-Problems

1. Users struggle to check if an item is currently in stock before attempting to make a purchase.
2. The machine takes too long to process cash and calculate exact change manually for customers.
3. Multiple similar product options cause user confusion and slow down the selection process.
4. The system does not notify the owner automatically when an item is out of stock.

---

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|

| Users struggle to check stock before purchasing | Abstraction | Hide internal machinery details and display a simple digital light indicator. For example, Green = In Stock, Red = Out of Stock, next to each item. |

| Slow cash processing and manual change calculation | Algorithm Design | Create a step-by-step logic routine that automatically computes item cost and instantly calculates thet change. |

| Confusion from too many similar product options | Pattern Recognition | Group items into clear categories, like Drinks, Snacks, Healthy, based on shared traits so users navigate choices faster. |

| No automated restock notifications for the owner | Decomposition | Break down the inventory process into individual item counter sensors that trigger an alert signal whenever a count reaches zero. |

---

## Step 4: Algorithmic Solution
### Selected Sub-Problem
Slow cash processing and manual change calculation.

### Pseudocode
START
  Display item price to the user
  Get inserted_amount
  
  IF inserted_amount IS GREATER THAN OR EQUAL TO item_price THEN
    Compute change = inserted_amount - item_price
    Dispense selected_item
    Dispese change
    Display "Transaction complete. Thank you!"
  ELSE
    DISPLAY "Insufficient funds. Please insert remaining amount."
    RETURN inserted_amount
  END IF
END