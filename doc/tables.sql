CREATE TABLE user (
  id SERIAL PRIMARY KEY,
  login TEXT UNIQUE NOT NULL,
  hash_password TEXT NOT NULL
);

CREATE TABLE post (
  id SERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES user(id),
  title TEXT,
  body TEXT,
  publication_date DATE
);

CREATE TABLE comment (
  id SERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES user(id),
  post_id BIGINT REFERENCES post(id),
  body TEXT,
  publication_date DATE
);

CREATE TABLE subscriber (
  id SERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES user(id),
  subscriber_id BIGINT REFERENCES user(id),
  UNIQUE (user_id, subscriber_id)
);
