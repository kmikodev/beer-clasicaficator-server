from db import get_db


def insert_beer(name, comment):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO beers(name, comment) VALUES (?, ?)"
    cursor.execute(statement, [name, comment])
    db.commit()
    return True


def update_beer(id, name, comment):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE beers SET name = ?, comment = ? WHERE id = ?"
    cursor.execute(statement, [name, comment, id])
    db.commit()
    return True


def delete_beer(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM beers WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, comment FROM beers WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_beers():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, comment FROM beers"
    cursor.execute(query)
    return cursor.fetchall()
