import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = "sqlite:///{}".format(os.path.join(BASE_DIR, "TASK.db"))