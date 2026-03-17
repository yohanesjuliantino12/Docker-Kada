CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date DATE,
    branch VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    price INT
);