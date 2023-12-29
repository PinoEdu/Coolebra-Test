CREATE TABLE Product (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sku VARCHAR(8) UNIQUE NOT NULL,
    ean VARCHAR(15) UNIQUE NOT NULL
);

CREATE TABLE Market (
    market_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Price (
    price_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES Product(product_id) ON DELETE CASCADE,
    market_id INT REFERENCES Market(market_id) ON DELETE CASCADE,
    normal_price INT NOT NULL,
    discount_price INT,
    active BOOLEAN NOT NULL,
    create_date DATE NOT NULL
);