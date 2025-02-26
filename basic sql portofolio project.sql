SELECT *
FROM customers
WHERE customer_id = 1;
-- ORDER BY first_name


-- select first-last customers name to see discount factor 
SELECT 
	first_name, 
    last_name,
    points,
    (points + 10) * 100 AS 'discount factor' 
FROM customers;


-- distinct to remove duplicates in state column 
SELECT DISTINCT state
FROM customers;


-- set new price to our products
SELECT
	name,
	unit_price,
    unit_price *1.1 AS 'new price'
FROM products;


-- orders placed in 2019+
SELECT *
FROM orders
WHERE order_date >= '2019_01_01';


-- get items for order 6, where the total price is grater than 30 
SELECT *
FROM order_items
WHERE order_id = 6 AND (unit_price * quantity) > 30;


-- get products with quantity in stock = 49 38 72 
SELECT *
FROM products
WHERE quantity_in_stock IN ( 49 , 38 , 72);

-- select customers bor between 1/1/1990 & 1/1/2000
SELECT * 
FROM customers 
WHERE birth_date BETWEEN '1990-1-1' AND '2000-1-1';

-- get customers with rst names are ELKA or AMBUR last names end with ey or on last names start with my or contains se and last names contains b followed by u or r 

SELECT *
FROM customers 
WHERE first_name REGEXP 'elka|ambur';

SELECT *
FROM customers 
WHERE last_name REGEXP 'ey$|on$';

SELECT *
FROM customers 
WHERE last_name REGEXP '^my|se';

SELECT *
FROM customers 
WHERE last_name REGEXP 'br|bu';

-- get orders that not shipped 

SELECT *
FROM orders
WHERE shipped_date IS NULL;

-- sorted order items with id = 2 by total price 

SELECT *, quantity * unit_price AS total_price
FROM order_items 
WHERE order_id = 2 
ORDER BY quantity * unit_price DESC;

-- get the top 3 loyal customers 

SELECT * 
FROM customers 
ORDER BY points DESC 
LIMIT 3;

-- joins 

SELECT order_id, o.product_id, quantity, o.unit_price
FROM order_items o
JOIN products p ON o.product_id = p.product_id;

-- join table across multiple databases sql_store + sql_inventory 

SELECT * 
FROM order_items oi 
JOIN sql_inventory.products p 
	ON oi.product_id = p.product_id;
    

SELECT 
	e.employee_id,
    e.first_name,
    m.first_name AS manager
FROM employees e
JOIN employees m
	ON 	e.reports_to = m.employee_id;
    
    
-- in sql invoicing join payment table to get date, invoice id, amount, name 

SELECT 
	p.date,
    p.invoice_id,
    p.amount,
    cl.name 
FROM payments p
JOIN clients cl
	ON p.client_id = cl.client_id 
JOIN payment_methods pm 
	ON p.payment_method = pm.payment_method_id;

-- JOIN products with order items get a table with all products id even if no ordered

SELECT 
	p.product_id,
    p.name,
    oi.quantity
FROM products p 
LEFT JOIN order_items oi 
	ON p.product_id = oi.product_id;
    
    
-- get a table (customer_id, first_name, points, type) bronze<2000 2000< silver< 3000 gold>3000

SELECT 
	customer_id,
    first_name, 
    points,
    'bronze' AS type
FROM customers  
WHERE points < 2000
UNION 
SELECT 
	customer_id,
    first_name, 
    points,
    'silver' AS type
FROM customers  
WHERE points BETWEEN 2000 AND  3000
UNION 
SELECT 
	customer_id,
    first_name, 
    points,
    'gold' AS type
FROM customers  
WHERE points > 3000
ORDER BY first_name;


-- insert information on customers table 

INSERT INTO customers 
VALUES (
DEFAULT,
'john',
'smith',
'1990-01-01',
NULL,
'address',
'city',
'CA',
DEFAULT);

-- sql statement than give all above 1990 +50 points 

UPDATE customers 
SET points = points + 50 
WHERE birth_date < '1990-01-01' 
