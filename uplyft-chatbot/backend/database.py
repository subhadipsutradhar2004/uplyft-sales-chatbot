import sqlite3

def search_products(query):
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + query + '%',))
    results = cur.fetchall()
    conn.close()
    return results
