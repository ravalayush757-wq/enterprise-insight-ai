from database import DatabaseManager

db = DatabaseManager()

query = """
SELECT
    region,
    ROUND(SUM(sales),2) AS total_sales
FROM orders
GROUP BY region
ORDER BY total_sales DESC;
"""

print(db.execute_query(query))