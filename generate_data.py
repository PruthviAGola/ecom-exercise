"""
Generate synthetic e-commerce data using Faker and pandas.
Creates CSV files for customers, products, orders, and order_items.
"""

import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()
Faker.seed(42)  # For reproducibility
random.seed(42)

# Configuration
NUM_CUSTOMERS = 100
NUM_PRODUCTS = 50
NUM_ORDERS = 200
MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5

def generate_customers(num_customers):
    """Generate customer data."""
    customers = []
    for i in range(1, num_customers + 1):
        customers.append({
            'customer_id': i,
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address().replace('\n', ', '),
            'city': fake.city(),
            'state': fake.state(),
            'zip_code': fake.zipcode(),
            'created_at': fake.date_time_between(start_date='-2y', end_date='now').isoformat()
        })
    return pd.DataFrame(customers)

def generate_products(num_products):
    """Generate product data."""
    categories = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Toys', 'Food', 'Beauty']
    products = []
    for i in range(1, num_products + 1):
        products.append({
            'product_id': i,
            'name': fake.catch_phrase(),
            'category': random.choice(categories),
            'price': round(random.uniform(10.0, 500.0), 2),
            'description': fake.text(max_nb_chars=200),
            'stock_quantity': random.randint(0, 1000),
            'created_at': fake.date_time_between(start_date='-1y', end_date='now').isoformat()
        })
    return pd.DataFrame(products)

def generate_orders(num_orders, num_customers):
    """Generate order data."""
    orders = []
    start_date = datetime.now() - timedelta(days=365)
    
    for i in range(1, num_orders + 1):
        order_date = fake.date_time_between(start_date=start_date, end_date='now')
        orders.append({
            'order_id': i,
            'customer_id': random.randint(1, num_customers),
            'order_date': order_date.isoformat(),
            'status': random.choice(['pending', 'processing', 'shipped', 'delivered', 'cancelled']),
            'shipping_address': fake.address().replace('\n', ', ')
        })
    return pd.DataFrame(orders)

def generate_order_items(orders_df, products_df):
    """Generate order items data."""
    order_items = []
    item_id = 1
    
    for _, order in orders_df.iterrows():
        num_items = random.randint(MIN_ITEMS_PER_ORDER, MAX_ITEMS_PER_ORDER)
        products_in_order = random.sample(range(1, len(products_df) + 1), min(num_items, len(products_df)))
        
        for product_id in products_in_order:
            product = products_df[products_df['product_id'] == product_id].iloc[0]
            quantity = random.randint(1, 5)
            price = product['price']
            
            order_items.append({
                'item_id': item_id,
                'order_id': order['order_id'],
                'product_id': product_id,
                'quantity': quantity,
                'price': price,
                'subtotal': round(quantity * price, 2)
            })
            item_id += 1
    
    return pd.DataFrame(order_items)

def main():
    """Main function to generate all data files."""
    print("Generating e-commerce data...")
    
    # Generate data
    print("  - Generating customers...")
    customers_df = generate_customers(NUM_CUSTOMERS)
    
    print("  - Generating products...")
    products_df = generate_products(NUM_PRODUCTS)
    
    print("  - Generating orders...")
    orders_df = generate_orders(NUM_ORDERS, NUM_CUSTOMERS)
    
    print("  - Generating order items...")
    order_items_df = generate_order_items(orders_df, products_df)
    
    # Save to CSV files
    print("\nSaving data to CSV files...")
    customers_df.to_csv('data/customers.csv', index=False)
    print("  - Saved data/customers.csv")
    
    products_df.to_csv('data/products.csv', index=False)
    print("  - Saved data/products.csv")
    
    orders_df.to_csv('data/orders.csv', index=False)
    print("  - Saved data/orders.csv")
    
    order_items_df.to_csv('data/order_items.csv', index=False)
    print("  - Saved data/order_items.csv")
    
    print(f"\nData generation complete!")
    print(f"  - {len(customers_df)} customers")
    print(f"  - {len(products_df)} products")
    print(f"  - {len(orders_df)} orders")
    print(f"  - {len(order_items_df)} order items")

if __name__ == '__main__':
    main()

