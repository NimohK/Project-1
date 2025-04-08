# Sample data for rental houses
houses = [
    {"location": "Nairobi", "price": 30000},
    {"location": "Mombasa", "price": 25000},
    {"location": "Nakuru", "price": 18000},
    {"location": "Kisumu", "price": 22000},
    {"location": "Nairobi", "price": 45000},
]

# Function to search houses by location and price range
def search_houses(location=None, max_price=None):
    results = []
    
    for house in houses:
        if location and house["location"].lower() != location.lower():
            continue  # Skip if the location doesn't match
        if max_price and house["price"] > max_price:
            continue  # Skip if the price is greater than max_price
        
        results.append(house)  # Add the house to results if it matches the criteria
    
    return results

# Example: User search for houses in "Nairobi" with a max price of 35000
search_results = search_houses(location="Nairobi", max_price=35000)

# Display the search results
if search_results:
    print("Search Results:")
    for house in search_results:
        print(f"Location: {house['location']}, Price: {house['price']}")
else:
    print("No houses found matching your criteria.")
