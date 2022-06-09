import sqlite3
import generate_json
from generate_json import generate_purchase

with sqlite3.connect('shopping_list.db') as db:
    cursor = db.cursor()
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS shopping_list(
      title TEXT,
      category TEXT,
      quantity INTEGER,
      price INTEGER, 
      surname TEXT
      )
    """)
    cursor.execute("""
    INSERT INTO
       shop_list(title, category, quantity, price, surname)
    VALUES
        (:title, :category, :quantity, :price, :surname)
    """, {
        'title': 'Iphone10',
        'category': 'electronics',
        'quantity': '2',
        'price': '100',
        'surname': 'Kruts'
    })
    cursor.close()
    db.commit()
        
