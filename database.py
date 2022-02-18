import sqlalchemy as sq


class DB:
    def __init__(self, DB_VK):
        engine = sq.create_engine(DB_VK)
        self.mydb = engine.raw_connection()
        self.mycursor = self.mydb.cursor()

    def black_list_SQL_recording(self, id, liked):
        self.mycursor.execute(f'INSERT INTO parts (vk_id, liked) VALUES({id}, {liked})')
        self.mydb.commit()

    def black_list_SQL_reading(self):
        self.mycursor.execute(
            f'CREATE TABLE IF NOT EXISTS parts (vk_id integer NOT NULL default 0, liked boolean NOT NULL default False)')
        self.mydb.commit()
        self.mycursor.execute('SELECT vk_id FROM parts')
        list = self.mycursor.fetchall()
        black_list = []
        for i in list:
            black_list.append(i[0])
        return black_list
