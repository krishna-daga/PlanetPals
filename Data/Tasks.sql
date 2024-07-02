CREATE TABLE tasks (
  task_id INTEGER PRIMARY KEY,
  task_name VARCHAR,
  category_id INTEGER,
  points INTEGER,
  difficulty_level TEXT,
  date DATE
);
