import csv
import sqlite3 as sql_lib


class MigrateTask:
    def __init__(self, task_db='TASK.db'):
        """Initialize the class"""
        self.db_name = task_db
        self.connection = sql_lib.connect(task_db)

    def _create_table(self):
        """Create table."""
        c = self.connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks
                (id INTEGER primary key, entry_time TEXT, temperature DECIMAL(10, 5), duration TEXT)''')
        self.connection.commit()
        self.connection.close()

    def save_data(self, task_id, entry_time, temperature, duration):
        """Save data in the database."""
        c = self.connection.cursor()
        c.execute(""" Insert into tasks(id, entry_time, temperature, duration) values (?,?,?,?)
        """, (task_id, entry_time, temperature, duration))
        self.connection.commit()


def migrate_all_rows(path_to_csv):
    """Migrate all data from csv to database"""
    # run through the rows
    line = -1
    with open(path_to_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        db_save_data = MigrateTask()
        for row in csv_reader:
            if line == -1:
                line += 1
                continue
            try:
                db_save_data.save_data(task_id=row[0], entry_time=row[1], temperature=row[2], duration=row[3])
            except sql_lib.IntegrityError:
                continue
            line += 1
    print('{} rows have been saved to the database.'.format(line))


if __name__ == '__main__':
    # setup the database
    new_db = MigrateTask()
    new_db._create_table()
    # migrate task
    migrate_all_rows('task_data.csv')
