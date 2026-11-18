from database import DatabaseManager

db = DatabaseManager()


def total_sales():
    query = """
    SELECT ROUND(SUM(sales),2) AS total_sales
    FROM orders;
    """
    return db.execute_query(query)


def total_profit():
    query = """
    SELECT ROUND(SUM(profit),2) AS total_profit
    FROM orders;
    """
    return db.execute_query(query)


def total_orders():
    query = """
    SELECT COUNT(*) AS total_orders
    FROM orders;
    """
    return db.execute_query(query)


def total_customers():
    query = """
    SELECT COUNT(DISTINCT customer_id) AS customers
    FROM orders;
    """
    return db.execute_query(query)

def sales_by_region():
    query = """
    SELECT
        region,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY region
    ORDER BY total_sales DESC;
    """
    return db.execute_query(query)

def sales_by_category():
    query = """
    SELECT
        category,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY category
    ORDER BY total_sales DESC;
    """
    return db.execute_query(query)
def sales_by_subcategory():
    query = """
    SELECT
        sub_category,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY sub_category
    ORDER BY total_sales DESC;
    """
    return db.execute_query(query)
def sales_by_segment():
    query = """
    SELECT
        segment,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY segment
    ORDER BY total_sales DESC;
    """
    return db.execute_query(query)
def sales_by_market():
    query = """
    SELECT
        market,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY market
    ORDER BY total_sales DESC;
    """
    return db.execute_query(query)

def sales_by_country():
    query = """
    SELECT
        country,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY country
    ORDER BY total_sales DESC
    LIMIT 10;
    """
    return db.execute_query(query)
def monthly_sales():
    query = """
    SELECT
        strftime('%Y-%m', order_date) AS month,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY month
    ORDER BY month;
    """
    return db.execute_query(query)
def yearly_sales():
    query = """
    SELECT
        year,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY year
    ORDER BY year;
    """
    return db.execute_query(query)


    def sales_by_segment():
    query = """
    SELECT
        segment,
        ROUND(SUM(sales),2) AS total_sales
    FROM orders
    GROUP BY segment
    ORDER BY total_sales DESC;
    """
    return db.execute_query(query)