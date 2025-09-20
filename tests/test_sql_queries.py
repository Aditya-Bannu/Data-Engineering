import sqlite3

def test_top_products_query():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE orders (region TEXT, product_id INT, sales INT);")
    cur.executemany("INSERT INTO orders VALUES (?, ?, ?);", [
        ("North", 1, 100), ("North", 2, 200), ("North", 3, 50)
    ])

    query = '''
    SELECT product_id, SUM(sales) AS total_sales
    FROM orders
    WHERE region = "North"
    GROUP BY product_id
    ORDER BY total_sales DESC
    LIMIT 1;
    '''
    cur.execute(query)
    result = cur.fetchone()
    assert result[0] == 2  # Product 2 has highest sales
