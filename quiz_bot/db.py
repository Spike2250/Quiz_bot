import aiosqlite
import sqlite3
import ast
from prettytable import PrettyTable


DB_NAME = 'quiz_bot.db'


async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        query = '''CREATE TABLE IF NOT EXISTS quiz_state (
                       user_id INTEGER PRIMARY KEY,
                       user_name TEXT,
                       question_index INTEGER,
                       question_order TEXT,
                       current_score INTEGER,
                       top_score INTEGER)'''
        await db.execute(query)
        await db.commit()


async def get_quiz_index(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'SELECT question_index FROM quiz_state WHERE user_id = (?)'
        async with db.execute(query, (user_id, )) as cursor:
            results = await cursor.fetchone()
            if results[0] is not None:
                return results[0]
            return 0


async def update_quiz_index(user_id, index):
    async with aiosqlite.connect(DB_NAME) as db:
        try:
            query = 'INSERT INTO quiz_state (user_id, question_index) VALUES (?, ?)'
            await db.execute(query, (user_id, index))
        except sqlite3.IntegrityError:
            query = 'UPDATE quiz_state SET question_index = ? WHERE user_id = ?'
            await db.execute(query, (index, user_id))
        await db.commit()


async def update_user_name(user_id, user_name):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'UPDATE quiz_state SET user_name = ? WHERE user_id = ?'
        await db.execute(query, (user_name, user_id))
        await db.commit()


async def get_question_order(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'SELECT question_order FROM quiz_state WHERE user_id = (?)'
        async with db.execute(query, (user_id, )) as cursor:
            results = await cursor.fetchone()
            if results[0] is not None:
                return ast.literal_eval(results[0])
            return []


async def update_question_order(user_id, order):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'UPDATE quiz_state SET question_order = ? WHERE user_id = ?'
        await db.execute(query, (str(order), user_id))
        await db.commit()


async def get_current_score(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'SELECT current_score FROM quiz_state WHERE user_id = (?)'
        async with db.execute(query, (user_id, )) as cursor:
            results = await cursor.fetchone()
            if results[0] is not None:
                return results[0]
            return 0


async def update_current_score(user_id, score):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'UPDATE quiz_state SET current_score = ? WHERE user_id = ?'
        await db.execute(query, (score, user_id))
        await db.commit()


async def get_top_score(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'SELECT top_score FROM quiz_state WHERE user_id = (?)'
        async with db.execute(query, (user_id, )) as cursor:
            results = await cursor.fetchone()
            if results[0] is not None:
                return results[0]
            return 0


async def update_top_score(user_id, score):
    async with aiosqlite.connect(DB_NAME) as db:
        query = 'UPDATE quiz_state SET top_score = ? WHERE user_id = ?'
        await db.execute(query, (score, user_id))
        await db.commit()


async def get_records_table() -> str:
    def create_table(results):
        table = PrettyTable()
        fields = ['Место', 'Игрок', 'Счет']
        table.field_names = fields

        for i, unit in enumerate(results):
            table.add_row([i + 1, unit[0], unit[1]])
        return str(table)

    async with aiosqlite.connect(DB_NAME) as db:
        query = 'SELECT user_name, top_score FROM quiz_state ORDER BY top_score DESC LIMIT 10'
        async with db.execute(query) as cursor:
            results = await cursor.fetchall()
            if results is not None:
                return create_table(results)
            return []
