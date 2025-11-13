"""
Ingest CSV data into SQLite database.
Creates tables and loads data from CSV files.
"""

import sqlite3
import pandas as pd
import os

DB_NAME = 'data/ecommerce.db'

def create_tables(cursor):
    """Create database tables."""
    print("Creating database tables...")
    
    # Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            created_at TEXT
        )
    ''')
    
    # Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NULL,
            description TEXT,
            stock_quantity INTEGER,
            created_at TEXT
        )
    ''')
    
    # Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            status TEXT,
            shipping_address TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Order items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            subtotal REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    print("  - Tables created successfully")

def load_data(cursor, conn):
    """Load data from CSV files into database."""
    print("\nLoading data from CSV files...")
    
    # Load customers
    if os.path.exists('data/customers.csv'):
        df = pd.read_csv('data/customers.csv')
        df.to_sql('customers', conn, if_exists='replace', index=False)
        print(f"  - Loaded {len(df)} customers")
    else:
        print("  - Warning: data/customers.csv not found")
    
    # Load products
    if os.path.exists('data/products.csv'):
        df = pd.read_csv('data/products.csv')
        df.to_sql('products', conn, if_exists='replace', index=False)
        print(f"  - Loaded {len(df)} products")
    else:
        print("  - Warning: data/products.csv not found")
    
    # Load orders
    if os.path.exists('data/orders.csv'):
        df = pd.read_csv('data/orders.csv')
        df.to_sql('orders', conn, if_exists='replace', index=False)
        print(f"  - Loaded {len(df)} orders")
    else:
        print("  - Warning: data/orders.csv not found")
    
    # Load order items
    if os.path.exists('data/order_items.csv'):
        df = pd.read_csv('data/order_items.csv')
        df.to_sql('order_items', conn, if_exists='replace', index=False)
        print(f"  - Loaded {len(df)} order items")
    else:
        print("  - Warning: data/order_items.csv not found")

def create_indexes(cursor):
    """Create indexes for better query performance."""
    print("\nCreating indexes...")
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON orders(customer_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_orders_order_date ON orders(order_date)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_items_order_id ON order_items(order_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_items_product_id ON order_items(product_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_products_category ON products(category)')
    print("  - Indexes created successfully")

def main():
    """Main function to ingest data into SQLite."""
    # Remove existing database if it exists
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Removed existing database: {DB_NAME}")
    
    # Connect to SQLite database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # Create tables
        create_tables(cursor)
        
        # Load data
        load_data(cursor, conn)
        
        # Create indexes
        create_indexes(cursor)
        
        # Commit changes
        conn.commit()
        
        print(f"\nData ingestion complete! Database saved to: {DB_NAME}")
        
        # Show summary
        cursor.execute("SELECT COUNT(*) FROM customers")
        num_customers = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM products")
        num_products = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM orders")
        num_orders = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM order_items")
        num_items = cursor.fetchone()[0]
        
        print(f"\nDatabase Summary:")
        print(f"  - {num_customers} customers")
        print(f"  - {num_products} products")
        print(f"  - {num_orders} orders")
        print(f"  - {num_items} order items")
        
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    main()

