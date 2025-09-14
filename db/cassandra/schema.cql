CREATE KEYSPACE IF NOT EXISTS mentor_match WITH replication = {'class':'SimpleStrategy','replication_factor':1};

CREATE TABLE IF NOT EXISTS mentor_match.students (
  id uuid PRIMARY KEY,
  full_name text,
  major text,
  class_year int,
  academic_interests text,
  hobbies text,
  created_at timestamp
);

CREATE TABLE IF NOT EXISTS mentor_match.matches (
  mentee_id uuid,
  mentor_id uuid,
  score double,
  mentor_major text,
  created_at timestamp,
  PRIMARY KEY ((mentee_id), score, mentor_id)
) WITH CLUSTERING ORDER BY (score DESC, mentor_id ASC);
