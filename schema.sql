-- SQLite-compatible schema
-- Users table
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT
);

-- Cars table
CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users (user_id),
    brand TEXT,
    model TEXT,
    year INTEGER,
    mileage INTEGER,
    price INTEGER,
    drive_train TEXT CHECK (
        drive_train IN (
            'Rear Wheel Drive',
            'Front Wheel Drive',
            'All Wheel Drive'
        )
    ),
    horsepower INTEGER,
    torque INTEGER,
    engine REAL,
    gas_type TEXT CHECK (
        gas_type IN ('Gasoline', 'Diesel', 'Hybrid', 'Electric')
    ),
    transmition TEXT CHECK (transmition IN ('Manual', 'Automatic')),
    register TEXT,
    weight INTEGER,
    seating_capacity INTEGER,
    door_count INTEGER,
    description TEXT,
    is_new BOOLEAN
);

-- Car pictures table
CREATE TABLE IF NOT EXISTS car_pictures (
    car_picture_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER REFERENCES cars (car_id),
    picture_data BLOB,
    file_name TEXT
);

-- Brands and their models tables
CREATE TABLE IF NOT EXISTS allBrands (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_name TEXT
);

CREATE TABLE IF NOT EXISTS allModels (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT,
    brand_id INTEGER REFERENCES allBrands (brand_id)
);
