-- Monthly total sales
SELECT strftime('%Y-%m', order_date) as month, SUM(total_price) as total_sales
FROM sales
GROUP BY month;

-- Top 5 products
SELECT product, SUM(quantity) as total_sold
FROM sales
GROUP BY product
ORDER BY total_sold DESC
LIMIT 5;

-- Repeat customers
SELECT customer_id, COUNT(DISTINCT order_id) as orders
FROM sales
GROUP BY customer_id
HAVING orders > 1;
