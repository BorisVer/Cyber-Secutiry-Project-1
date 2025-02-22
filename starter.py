from db import db
import json
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash


def make_brands_models():

    print("Filling brands and models")

    with open("allcarlist.json", "r") as f:
        data = json.load(f)

        found_brands = []

        counter_models = 1
        counter_brands = 1
        brand_id = 1

        for car in data:
            # Using .lower() so there are less typo related problems later
            brand = car["Make"].lower()
            model = car["Model"].lower()


            if brand not in found_brands:
                found_brands.append(brand)
                brand_id = counter_brands
                sql_brand = text("INSERT INTO allbrands (brand_name) VALUES (:brand)")
                db.session.execute(sql_brand, {"brand": brand})
                counter_brands += 1
            counter_models += 1
            sql_model = text("INSERT INTO allmodels (model_name, brand_id) VALUES (:model, :brand_id)")
            db.session.execute(sql_model, {"model": model, "brand_id": brand_id})

        db.session.commit()
        print(f"Added {counter_brands - 1} brands with {counter_models - 1} models")



def make_basics_database():
    print("Making basic database")
    # Add the users, made with a random name generator into file

    with open("starterusers.json") as f:
        data = json.load(f)
        for user in data:
            hash_value = user["password"] # generate_password_hash(user["password"])
            sql = text("INSERT INTO users (username, password, email, first_name, last_name, phone_number) VALUES (:username, :password, :email, :first_name, :last_name, :phone_number)")
            db.session.execute(sql, {"username":user["username"], "password":hash_value, "email":user["email"], "first_name":user["first_name"], "last_name":user["last_name"], "phone_number":user["phone_number"]})
            db.session.commit()

    # Add the cars
    with open("startercars.json", "r") as f:
        data = json.load(f)
        for car in data:


            sql = text("""
                INSERT INTO cars (
                    user_id,
                    brand,
                    model,
                    year,
                    mileage,
                    price,
                    drive_train,
                    horsepower,
                    torque,
                    engine,
                    gas_type,
                    transmition,
                    register,
                    weight,
                    seating_capacity,
                    door_count,
                    description,
                    is_new
                ) VALUES (
                    :user_id,
                    :brand,
                    :model,
                    :year,
                    :mileage,
                    :price,
                    :drive_train,
                    :horsepower,
                    :torque,
                    :engine,
                    :gas_type,
                    :transmition,
                    :register,
                    :weight,
                    :seating_capacity,
                    :door_count,
                    :description,
                    :is_new
                )  RETURNING car_id
        """)
            # Inputing info and at the same time returning the car_id
            car_id = db.session.execute(sql, {
                "user_id": car["user_id"],
                "brand": car["brand"],
                "model": car["model"],
                "year": car["year"],
                "mileage": car["mileage"],
                "price": car["price"],
                "drive_train": car["drive_train"],
                "horsepower": car["horsepower"],
                "torque": car["torque"],
                "engine": car["engine"],
                "gas_type": car["gas_type"],
                "transmition": car["transmition"],
                "register": car["register"],
                "weight": car["weight"],
                "seating_capacity": car["seating_capacity"],
                "door_count": car["door_count"],
                "description": car["description"],
                "is_new": car["is_new"]
                }).fetchone()[0]
            print(car_id)
        db.session.commit()


    # For each file they are added to the car_pictures and connected to the cars with the car_id value

    with open("starterimages.json") as f:
        data = json.load(f)
        for image in data:
            with open(image["picture_path"], "rb") as image_file:
                image_data = image_file.read()
            sql = text("INSERT INTO car_pictures (car_id, picture_data, file_name) VALUES (:car_id, :picture_data, :file_name)")
            db.session.execute(sql, {"car_id":image["car_id"], "picture_data":image_data, "file_name":image["file_name"]})
            db.session.commit()
