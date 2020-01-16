from collections import namedtuple
from flask import render_template
from config import app, DB
from models import Log


@app.route("/")
def home():
    # access the task here
    tasks = DB.session.execute('SELECT * FROM tasks')
    Task = namedtuple('Record', tasks.keys())
    task_list = [Task(*t) for t in tasks.fetchall()]

    log = Log(description="Accessed")
    # add log that it has been accessed
    DB.session.add(log)
    DB.session.commit()
    return render_template("tasks.html", tasks=task_list)


if __name__ == "__main__":
    DB.create_all()
    app.run(host='0.0.0.0')
