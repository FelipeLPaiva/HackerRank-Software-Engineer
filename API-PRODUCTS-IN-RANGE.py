import requests

def getProductsInRange(category, minPrice, maxPrice):
    total_items = 0
    current_page = 1

    while True:
        url = f"https://jsonmock.hackerrank.com/api/inventory?category={category}&page={current_page}"
        response = requests.get(url)
        data = response.json()

        if current_page > data['total_pages']:
            break

        for item in data['data']:
            price = item['price']
            # Check if the item belongs to the specified price range
            if minPrice <= price <= maxPrice:
                total_items += 1

        current_page += 1

    return total_items
