CREATE TABLE user_tasks (
  user_task_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  task_id INTEGER,
  assigned_date DATE,
  completed_date DATE,
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);
