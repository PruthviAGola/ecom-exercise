"""
Run sample queries on the SQLite e-commerce database.
Demonstrates various SQL queries for analysis.
"""

import sqlite3
import pandas as pd

DB_NAME = 'data/ecommerce.db'

def run_query(query, description):
    """Execute a query and display results."""
    conn = sqlite3.connect(DB_NAME)
    try:
        df = pd.read_sql_query(query, conn)
        print(f"\n{'='*60}")
        print(f"Query: {description}")
        print(f"{'='*60}")
        print(df.to_string(index=False))
        print(f"\nRows returned: {len(df)}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()

def main():
    """Run sample queries."""
    print("Running sample queries on e-commerce database...\n")
    
    # Query 1: Total revenue by product category
    query1 = """
        SELECT 
            p.category,
            COUNT(DISTINCT oi.order_id) as num_orders,
            SUM(oi.quantity) as total_quantity_sold,
            SUM(oi.subtotal) as total_revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.category
        ORDER BY total_revenue DESC
    """
    run_query(query1, "Total Revenue by Product Category")
    
    # Query 2: Top 10 customers by total spending
    query2 = """
        SELECT 
            c.customer_id,
            c.name,
            c.email,
            COUNT(DISTINCT o.order_id) as num_orders,
            SUM(oi.subtotal) as total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.customer_id, c.name, c.email
        ORDER BY total_spent DESC
        LIMIT 10
    """
    run_query(query2, "Top 10 Customers by Total Spending")
    
    # Query 3: Monthly sales trend
    query3 = """
        SELECT 
            strftime('%Y-%m', o.order_date) as month,
            COUNT(DISTINCT o.order_id) as num_orders,
            SUM(oi.subtotal) as total_revenue
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY month
        ORDER BY month
    """
    run_query(query3, "Monthly Sales Trend")
    
    # Query 4: Products with low stock
    query4 = """
        SELECT 
            product_id,
            name,
            category,
            stock_quantity,
            price
        FROM products
        WHERE stock_quantity < 50
        ORDER BY stock_quantity ASC
        LIMIT 10
    """
    run_query(query4, "Products with Low Stock (< 50 units)")
    
    # Query 5: Average order value by customer state
    query5 = """
        SELECT 
            c.state,
            COUNT(DISTINCT o.order_id) as num_orders,
            AVG(order_totals.total) as avg_order_value
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN (
            SELECT 
                order_id,
                SUM(subtotal) as total
            FROM order_items
            GROUP BY order_id
        ) order_totals ON o.order_id = order_totals.order_id
        GROUP BY c.state
        HAVING num_orders > 0
        ORDER BY avg_order_value DESC
    """
    run_query(query5, "Average Order Value by Customer State")
    
    # Query 6: Order status distribution
    query6 = """
        SELECT 
            status,
            COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) as percentage
        FROM orders
        GROUP BY status
        ORDER BY count DESC
    """
    run_query(query6, "Order Status Distribution")
    
    # Query 7: Top 5 best-selling products
    query7 = """
        SELECT 
            p.product_id,
            p.name,
            p.category,
            SUM(oi.quantity) as total_quantity_sold,
            SUM(oi.subtotal) as total_revenue
        FROM products p
        JOIN order_items oi ON p.product_id = oi.product_id
        GROUP BY p.product_id, p.name, p.category
        ORDER BY total_quantity_sold DESC
        LIMIT 5
    """
    run_query(query7, "Top 5 Best-Selling Products")
    
    print(f"\n{'='*60}")
    print("All queries completed!")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

