import psycopg2

try:
    connection = psycopg2.connect(user='postgres',
                                  password='8168163',
                                  host='127.0.0.1',
                                  port='5432',
                                  database='test')

    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS category CASCADE')
    cursor.execute('DROP TABLE IF EXISTS discounts CASCADE')
    cursor.execute('DROP TABLE IF EXISTS product CASCADE')

    create_table_category = '''CREATE TABLE category
        (id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        description TEXT NOT NULL);
        '''
    cursor.execute(create_table_category)
    connection.commit()

    create_table_discounts = '''CREATE TABLE discounts
        (id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        percent INT);
        '''
    cursor.execute(create_table_discounts)
    connection.commit()

    create_table_product = '''CREATE TABLE product
        (id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        price INT,
        category_id INT,
        discount_id INT,

        CONSTRAINT FK_Product_Category FOREIGN KEY (category_id)
        REFERENCES category (id)
        ON DELETE CASCADE,

        CONSTRAINT FK_Product_Discounts FOREIGN KEY (discount_id)
        REFERENCES discounts (id)
        ON DELETE CASCADE
        );
        '''

    cursor.execute(create_table_product)
    connection.commit()

    insert_category = 'INSERT INTO category (id, name, description) VALUES (%s, %s, %s)'
    insert_values = [(1, 'table', 'round'), (2, 'table', 'square'), (3, 'chair', 'wooden'), (4, 'chair', 'soft')]
    for record in insert_values:
        cursor.execute(insert_category, record)
    connection.commit()

    cursor.execute('SELECT * FROM category')
    for record in cursor.fetchall():
        print(record)
    print("------------------------------------")

    insert_discounts = 'INSERT INTO discounts (id, name, percent) VALUES (%s, %s, %s)'
    insert_values = [(1, 'table', 30), (2, 'chair', 25)]
    for record in insert_values:
        cursor.execute(insert_discounts, record)
    connection.commit()

    cursor.execute('SELECT * FROM discounts')
    for record in cursor.fetchall():
        print(record)
    print("------------------------------------")
    insert_product = 'INSERT INTO product (id, name, price, category_id, discount_id) VALUES (%s, %s, %s, %s, %s)'
    insert_values = [(1, 'table_r', 200, 1, 1), (2, 'table_s', 150, 2, 1), (3, 'chair_w', 100, 3, 2), (4, 'chair_s', 120, 4, 2)]
    for record in insert_values:
        cursor.execute(insert_product, record)
    connection.commit()

    cursor.execute('SELECT * FROM product')
    for record in cursor.fetchall():
        print(record)
    print("------------------------------------")

    start_price = int(input('Set start price: '))
    final_price = int(input('Set final price: '))

    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT category.name, category.description, product.price, discounts.percent
            FROM product
            RIGHT JOIN category ON product.category_id=category.id
            RIGHT JOIN discounts ON product.discount_id=discounts.id
            WHERE product.price BETWEEN {start_price} AND {final_price}
            """
            )

        records = cursor.fetchall()
        for record in records:
            print(record)

        # АЛЬТЕРНАТИВНЫЙ ВАРИАНТ ВЫВОДА
        # records = cursor.fetchall()
        # for record in records:
        #     print(f"name: {record[6]},"
        #           f"description: {record[7]},"
        #           f"price: {record[2]},"
        #           f"discounts: {record[10]}")

except (Exception, psycopg2.Error) as error:
    print(f'Error when working with PostgreSQL: {error}')
finally:
    if connection:
        connection.close()
        cursor.close()
        print('Connection with PostgreSQL is closed')