DROP DATABASE sandwich_maker_api;
CREATE DATABASE sandwich_maker_api;
USE sandwich_maker_api;

INSERT INTO sandwiches(id, sandwich_name, price, calories, tags)
VALUES
(1, 'BLT', 4.50, 400, 'savory, classic'),
(2, 'Grilled Cheese', 2.50, 250, 'kid-friendly, vegetarian, classic'),
(3, 'Cheeseburger', 4.00, 450, 'savory, meat-lover, classic'),
(4, 'Double Cheeseburger', 6.00, 650, 'savory, meat-lover');

INSERT INTO resources(item, amount)
VALUES
('bread', 40),
('cheese', 20),
('bacon', 10),
('lettuce', 10),
('tomato', 15),
('burger patty', 7);

INSERT INTO promo_codes(code, discount, description, start_date, end_date)
VALUES 
('freeSandwich', 0, 'Get a free sandwich!', NOW(), '2023-12-30'),
('BOGO', .50, 'Buy a sandwich and get one free, or get 1 half off', '2023-11-10', '2023-12-06'),
('MerryChristmas', .75, 'Merry Christmas! enjoy 25% off of your order', '2023-12-24', '2023-12-26');

UPDATE promo_codes
SET discount = 50
WHERE id = 2;

UPDATE promo_codes
SET discount = 75
WHERE id = 3;

UPDATE promo_codes
SET end_date = '2023-12-01'
WHERE id = 2;

INSERT INTO orders (id, customer_name, order_date, description, phone_number, address, order_type, order_status, promo_code_id, payment_type, payment_status, payment_info)
VALUES
(1, 'John Doe', NOW(), '1 blt', '99999999', '123 fakestreet', 'delivery', 'not started', NULL, 'cash during pickup', 'not payed', NULL),
(2, 'Jane Doe', NOW(), '2 grilled cheese', '888888888', '46 craver rd', 'carryout', 'not started', 1, 'debit card', 'processing...', '1111 1111 1111 1111 101');

INSERT INTO orders VALUES (3, 'Scooby Doo', NOW(), '1 grilled cheese', '77777777', 'levile hall', 'delivery', 'non started', NULL, 'cash during pickup', 'not payed', NULL);
INSERT INTO order_details(id, order_id, sandwich_id, amount, review_description, rating)
VALUES
(1, 1, 1, 1, NULL, NULL),
(2, 2, 2, 2, 'Very good!', 5);

INSERT INTO order_details VALUES(3, 3, 2, 1, NULL, NULL);

INSERT INTO recipes (sandwich_id, resource_id, amount)
VALUES
(1, 1, 2),
(1, 3, 3),
(1, 4, 1),
(1, 5, 1);

INSERT INTO recipes (sandwich_id, resource_id, amount)
VALUES
(2, 1, 2),
(2, 2, 2),
(3, 1, 2),
(3, 2, 1),
(3, 6, 1),
(4, 1, 2),
(4, 2, 1),
(4, 6, 2);


