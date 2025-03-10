import pandas as pd
import random

# Define stock items with their categories
stock_items = [
    ("Apple Juice", "Soft Drinks"), ("Bacardi Blanco", "Spirits"), ("Bira Moretti", "Beer"),
    ("Bombay Gin", "Spirits"), ("Captain Morgan Spiced Rum", "Spirits"), ("Chardonnay", "Wine"),
    ("Coca Cola", "Soft Drinks"), ("Coke Zero", "Soft Drinks"), ("Cointreau", "Spirits"),
    ("Corona", "Beer"), ("Cranberry Juice", "Soft Drinks"), ("Dalmore 12", "Spirits"),
    ("Diet Coke", "Soft Drinks"), ("Disaronno", "Spirits"), ("Havana Club 3", "Spirits"),
    ("Havana Club 7", "Spirits"), ("High Commissioner", "Spirits"), ("Irn Bru", "Soft Drinks"),
    ("J20", "Soft Drinks"), ("Jack Daniels", "Spirits"), ("Kahlua", "Spirits"),
    ("Lemonade", "Soft Drinks"), ("Light Tonic", "Soft Drinks"), ("Limoncello", "Spirits"),
    ("Macallan 12", "Spirits"), ("Malbec", "Wine"), ("Martini Rosso", "Spirits"),
    ("Merlot", "Wine"), ("Moet", "Wine"), ("Orange Juice", "Soft Drinks"),
    ("Passoa", "Spirits"), ("Peroni", "Beer"), ("Pineapple Juice", "Soft Drinks"),
    ("Pink Gin", "Spirits"), ("Pinot Grigio", "Wine"), ("Prosecco", "Wine"),
    ("Rijoca", "Wine"), ("Sauvignon Blanc", "Wine"), ("St Germain", "Spirits"),
    ("Tanqueray 10", "Spirits"), ("Tonic Water", "Soft Drinks")
]

# Define seasons and their impact on stock orders
seasons = ["Winter", "Spring", "Summer", "Fall"]
season_demand_multiplier = {
    "Winter": 0.7,  # Lowest demand
    "Spring": 1.0,  # Moderate demand
    "Summer": 1.3,  # Highest demand
    "Fall": 1.0     # Moderate demand
}

# Generate 50 weeks of data
data = []
for week in range(1, 51):  # 50 weeks
    season = seasons[(week // 13) % 4]  # Rotate seasons every 13 weeks
    demand_multiplier = season_demand_multiplier[season]  # Get season's effect on demand

    for item, category in stock_items:
        # Set stock order range based on category
        if category == "Spirits":
            base_stock = random.randint(2, 5)
        elif category in ["Soft Drinks", "Beer"]:
            base_stock = random.randint(19, 35)
        elif category == "Wine":
            base_stock = random.randint(8, 14)
        else:
            base_stock = random.randint(10, 30)  # Default fallback (shouldn't be needed)

        # Adjust stock order by season
        ordered_stock = int(base_stock * demand_multiplier)

        # Simulate customer projections (higher in busy seasons)
        projected_covers = random.randint(100, 500) * demand_multiplier

        # Simulate leftover stock (some weeks will have leftover stock)
        stock_left = max(0, ordered_stock - random.randint(0, int(ordered_stock * 0.5)))

        data.append([week, item, category, ordered_stock, projected_covers, stock_left, season])

# Create DataFrame
df = pd.DataFrame(data, columns=["Week", "Item Name", "Category", "Ordered Stock", "Projected Covers", "Stock Left", "Season"])

# Save to CSV
df.to_csv("stock_orders_50_weeks.csv", index=False)

print("✅ CSV file 'stock_orders_50_weeks.csv' generated successfully!")
