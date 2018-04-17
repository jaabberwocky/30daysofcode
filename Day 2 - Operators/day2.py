import sys

def total_cost_meal(price,tip_pct,tax_pct):
    tip = float(price) *(int(tip_pct)/100)
    tax = float(price) * (int(tax_pct)/100)
    return int(round(float(price)+float(tip)+float(tax)))

arr = []

for line in sys.stdin:
    arr.append(line)
    
print("The total meal cost is %d dollars." %( total_cost_meal(*arr)))