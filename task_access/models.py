import datetime
from config import DB


class Log(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    description = DB.Column(DB.String(80), unique=False, nullable=False)
    created_at = DB.Column(DB.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<description: {}>".format(self.description)
