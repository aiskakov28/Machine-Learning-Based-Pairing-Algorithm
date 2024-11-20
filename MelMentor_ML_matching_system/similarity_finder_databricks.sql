-- Drop existing tables and views
DROP TABLE IF EXISTS student_profiles;
DROP TABLE IF EXISTS student_profiles_delta;
DROP VIEW IF EXISTS potential_mentors;
DROP VIEW IF EXISTS potential_mentees;
DROP VIEW IF EXISTS mentor_recommendations;
DROP TABLE IF EXISTS model_logs;

-- Create the initial student_profiles table
CREATE TABLE IF NOT EXISTS student_profiles_databricks (
    full_name VARCHAR(100),
    major VARCHAR(50),
    class_year INT,
    academic_interests VARCHAR(100),
    hobbies VARCHAR(100)
);

-- Insert data
INSERT INTO student_profiles_databricks (full_name, major, class_year, academic_interests, hobbies)
VALUES
    ('John Doe', 'Computer Science', 2024, 'Artificial Intelligence', 'Chess'),
    ('Jane Smith', 'Biology', 2025, 'Genetics', 'Hiking'),
    ('Alex Johnson', 'Mathematics', 2026, 'Number Theory', 'Photography'),
    ('Emily Brown', 'Economics', 2027, 'Behavioral Economics', 'Painting'),
    ('Michael Lee', 'Political Science', 2028, 'International Relations', 'Soccer'),
    ('Sarah Wilson', 'Chemistry', 2024, 'Organic Chemistry', 'Guitar'),
    ('David Taylor', 'Business', 2025, 'Entrepreneurship', 'Cooking'),
    ('Emma Davis', 'Computer Science', 2026, 'Machine Learning', 'Yoga'),
    ('Ryan Anderson', 'Biology', 2027, 'Ecology', 'Writing'),
    ('Olivia Martinez', 'Mathematics', 2028, 'Cryptography', 'Debate'),
    ('William Chen', 'Economics', 2024, 'Financial Modeling', 'Basketball'),
    ('Sophia Patel', 'Political Science', 2025, 'Comparative Politics', 'Gardening'),
    ('Ethan Kim', 'Chemistry', 2026, 'Biochemistry', 'Stargazing'),
    ('Ava Nguyen', 'Business', 2027, 'Marketing Analytics', 'Volunteering'),
    ('Daniel Garcia', 'Computer Science', 2028, 'Cybersecurity', 'Drone Flying'),
    ('Isabella Rodriguez', 'Biology', 2024, 'Marine Biology', 'Cycling'),
    ('Noah Thompson', 'Mathematics', 2025, 'Graph Theory', 'Puzzle Solving'),
    ('Mia Jackson', 'Economics', 2026, 'Development Economics', 'Running'),
    ('James Wilson', 'Political Science', 2027, 'Public Policy', 'Film Making'),
    ('Charlotte Davis', 'Chemistry', 2028, 'Materials Science', 'Community Organizing'),
    ('Benjamin Lee', 'Business', 2024, 'Supply Chain Management', 'Gaming'),
    ('Amelia Chen', 'Computer Science', 2025, 'Data Science', 'Playing Piano'),
    ('Lucas Kim', 'Biology', 2026, 'Neurobiology', 'Rock Climbing'),
    ('Harper Patel', 'Mathematics', 2027, 'Topology', 'Meditation'),
    ('Elijah Brown', 'Economics', 2028, 'Game Theory', 'Ethical Hacking'),
    ('Evelyn Taylor', 'Political Science', 2024, 'Environmental Policy', '3D Printing'),
    ('Alexander Johnson', 'Chemistry', 2025, 'Analytical Chemistry', 'Chess'),
    ('Abigail Martinez', 'Business', 2026, 'International Business', 'Baking'),
    ('Sebastian Garcia', 'Computer Science', 2027, 'Natural Language Processing', 'Theater'),
    ('Elizabeth Wilson', 'Biology', 2028, 'Immunology', 'Ethnographic Photography'),
    ('Christopher Lee', 'Mathematics', 2024, 'Applied Mathematics', 'Tennis'),
    ('Sofia Rodriguez', 'Economics', 2025, 'Econometrics', 'Scuba Diving'),
    ('Matthew Kim', 'Political Science', 2026, 'Political Economy', 'Photography'),
    ('Scarlett Nguyen', 'Chemistry', 2027, 'Physical Chemistry', 'Yoga'),
    ('Andrew Thompson', 'Business', 2028, 'Business Analytics', 'Upcycling'),
    ('Chloe Davis', 'Computer Science', 2024, 'Artificial Neural Networks', 'Swimming'),
    ('Joseph Chen', 'Biology', 2025, 'Molecular Biology', 'Data Visualization'),
    ('Grace Patel', 'Mathematics', 2026, 'Differential Equations', 'Martial Arts'),
    ('Samuel Jackson', 'Economics', 2027, 'Labor Economics', 'Podcasting'),
    ('Zoe Brown', 'Political Science', 2028, 'International Relations', 'Activism'),
    ('Laura Martinez', 'Computer Science', 2024, 'Quantum Computing', 'Robotics'),
    ('Kevin Wang', 'Biology', 2025, 'Genomics', 'Bird Watching'),
    ('Rachel Kim', 'Mathematics', 2026, 'Algebraic Geometry', 'Violin'),
    ('Thomas Brown', 'Economics', 2027, 'Microeconomics', 'Painting'),
    ('Sophia Lee', 'Political Science', 2028, 'Geopolitics', 'Model UN'),
    ('Nathan Wilson', 'Chemistry', 2024, 'Computational Chemistry', '3D Printing'),
    ('Olivia Taylor', 'Business', 2025, 'Digital Marketing', 'Origami'),
    ('Daniel Davis', 'Computer Science', 2026, 'Computer Vision', 'Gardening'),
    ('Emma Anderson', 'Biology', 2027, 'Plant Biology', 'Creative Writing'),
    ('Jacob Martinez', 'Mathematics', 2028, 'Chaos Theory', 'Debate'),
    ('Ava Chen', 'Economics', 2024, 'Behavioral Finance', 'Photography'),
    ('Ethan Patel', 'Political Science', 2025, 'Urban Politics', 'Yoga'),
    ('Mia Kim', 'Chemistry', 2026, 'Nanotechnology', 'Chess'),
    ('William Nguyen', 'Business', 2027, 'Entrepreneurship', 'Meditation'),
    ('Isabella Garcia', 'Computer Science', 2028, 'Internet of Things', 'Sketching'),
    ('Alexander Rodriguez', 'Biology', 2024, 'Conservation Biology', 'Hiking'),
    ('Sophie Thompson', 'Mathematics', 2025, 'Optimization', 'Puzzle Solving'),
    ('Lucas Jackson', 'Economics', 2026, 'International Trade', 'Cooking'),
    ('Emily Wilson', 'Political Science', 2027, 'Human Rights', 'Blogging'),
    ('Michael Davis', 'Chemistry', 2028, 'Green Chemistry', 'Podcasting'),
    ('Zoe Lee', 'Business', 2024, 'Strategic Management', 'Gaming'),
    ('David Chen', 'Computer Science', 2025, 'Artificial Intelligence Ethics', 'Piano'),
    ('Lily Kim', 'Biology', 2026, 'Biotechnology', 'Rock Climbing'),
    ('Aiden Patel', 'Mathematics', 2027, 'Discrete Mathematics', 'Tutoring'),
    ('Chloe Brown', 'Economics', 2028, 'Environmental Economics', 'Data Visualization'),
    ('Ryan Taylor', 'Political Science', 2024, 'Diplomacy', 'Synthetic Biology'),
    ('Hannah Johnson', 'Chemistry', 2025, 'Medicinal Chemistry', 'Board Games'),
    ('Noah Martinez', 'Business', 2026, 'Financial Planning', '3D Printing'),
    ('Grace Garcia', 'Computer Science', 2027, 'Cybersecurity', 'Public Speaking'),
    ('Liam Wilson', 'Biology', 2028, 'Microbiology', 'Documentary Filmmaking'),
    ('Ella Lee', 'Mathematics', 2024, 'Mathematical Physics', 'Robotics'),
    ('Benjamin Rodriguez', 'Economics', 2025, 'Macroeconomics', 'Surfing'),
    ('Avery Kim', 'Political Science', 2026, 'Political Psychology', 'Astrophotography'),
    ('Scarlett Nguyen', 'Chemistry', 2027, 'Electrochemistry', 'True Crime Podcasts'),
    ('Owen Thompson', 'Business', 2028, 'Risk Management', 'Solar Panel Installation'),
    ('Madison Davis', 'Computer Science', 2024, 'Quantum Algorithms', 'Brain-Computer Interfaces'),
    ('Joseph Chen', 'Biology', 2025, 'Evolutionary Biology', 'Sports Analytics'),
    ('Abigail Patel', 'Mathematics', 2026, 'Topology', 'Sustainable Crafting'),
    ('Samuel Jackson', 'Economics', 2027, 'Health Economics', 'Language Learning'),
    ('Zoe Brown', 'Political Science', 2028, 'Environmental Policy', 'Community Gardening'),
    ('Evelyn Martinez', 'Chemistry', 2024, 'Polymer Chemistry', 'Cybersecurity Competitions'),
    ('Andrew Wang', 'Business', 2025, 'International Business', 'Wildlife Photography'),
    ('Sofia Kim', 'Computer Science', 2026, 'Machine Learning', 'Science Communication'),
    ('Jack Brown', 'Biology', 2027, 'Neuroscience', 'Leadership Workshops'),
    ('Victoria Lee', 'Mathematics', 2028, 'Stochastic Processes', 'Stock Market Simulation'),
    ('Charles Wilson', 'Economics', 2024, 'Behavioral Economics', 'Model Rocketry'),
    ('Amelia Taylor', 'Political Science', 2025, 'Comparative Politics', 'Mathematical Art'),
    ('Henry Davis', 'Chemistry', 2026, 'Inorganic Chemistry', 'Plastic Recycling'),
    ('Mila Anderson', 'Business', 2027, 'Organizational Behavior', 'Poetry Writing'),
    ('Leo Martinez', 'Computer Science', 2028, 'Robotics', 'Policy Analysis'),
    ('Aria Chen', 'Biology', 2024, 'Genetics', 'Drone Racing'),
    ('Lucas Patel', 'Mathematics', 2025, 'Combinatorics', 'Urban Farming'),
    ('Zoe Kim', 'Economics', 2026, 'Development Economics', 'Music Production'),
    ('Ethan Nguyen', 'Political Science', 2027, 'Public Administration', 'Mindfulness Coaching'),
    ('Chloe Garcia', 'Chemistry', 2028, 'Analytical Chemistry', 'Kayaking'),
    ('Isaac Rodriguez', 'Business', 2024, 'Sustainable Business', 'Nature Conservation'),
    ('Sophia Thompson', 'Computer Science', 2025, 'Natural Language Processing', 'Algorithmic Trading'),
    ('Oliver Jackson', 'Biology', 2026, 'Marine Biology', 'Microscopy'),
    ('Ava Wilson', 'Mathematics', 2027, 'Number Theory', 'Backpacking'),
    ('Gabriel Davis', 'Economics', 2028, 'Econometrics', 'Social Media Analysis'),
    ('Emma Lee', 'Political Science', 2024, 'International Relations', 'UX Design'),
    ('Daniel Chen', 'Chemistry', 2025, 'Physical Chemistry', 'Brain Training Games'),
    ('Maya Kim', 'Business', 2026, 'Project Management', 'Geological Expeditions'),
    ('Liam Patel', 'Computer Science', 2027, 'Data Mining', 'Market Research'),
    ('Harper Brown', 'Biology', 2028, 'Ecology', 'Machine Learning Projects');

-- Using Delta Lake for reliable data storage
CREATE TABLE IF NOT EXISTS student_profiles_delta
USING DELTA
AS SELECT * FROM student_profiles;

-- Create a view of potential mentors (upperclassmen)
CREATE OR REPLACE VIEW potential_mentors AS
SELECT *
FROM student_profiles_delta
WHERE class_year < 2027;

-- Create a view of potential mentees (first-year students)
CREATE OR REPLACE VIEW potential_mentees AS
SELECT *
FROM student_profiles_delta
WHERE class_year = 2028;

-- Create a function to calculate similarity
CREATE OR REPLACE FUNCTION calculate_similarity(mentee_interests STRING, mentor_interests STRING)
RETURNS DOUBLE
RETURN (
  SIZE(ARRAY_INTERSECT(SPLIT(mentee_interests, ' '), SPLIT(mentor_interests, ' '))) /
  CAST(SIZE(ARRAY_UNION(SPLIT(mentee_interests, ' '), SPLIT(mentor_interests, ' '))) AS DOUBLE)
);

-- Generate mentor recommendations for each mentee
CREATE OR REPLACE VIEW mentor_recommendations AS
SELECT
  m.full_name AS mentee_name,
  m.major AS mentee_major,
  m.academic_interests AS mentee_interests,
  p.full_name AS mentor_name,
  p.major AS mentor_major,
  p.academic_interests AS mentor_interests,
  calculate_similarity(m.academic_interests, p.academic_interests) AS similarity_score
FROM potential_mentees m
CROSS JOIN potential_mentors p
ORDER BY m.full_name, similarity_score DESC;

-- Create a table for model logging
CREATE TABLE IF NOT EXISTS model_logs (
  model_name STRING,
  version INT,
  timestamp TIMESTAMP,
  details STRING
);

-- Log the model details
INSERT INTO model_logs
VALUES ('mentor_recommendation_model', 1, CURRENT_TIMESTAMP(), 'Initial model based on Jaccard similarity of academic interests');

-- Test the recommendation system
SELECT * FROM mentor_recommendations
LIMIT 10;

-- Query to show top mentee-mentor matches with highest similarity scores
SELECT
  mentee_name,
  mentee_major,
  mentee_interests,
  mentor_name,
  mentor_major,
  mentor_interests,
  similarity_score
FROM (
  SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY mentee_name ORDER BY similarity_score DESC) as rank
  FROM mentor_recommendations
)
WHERE rank = 1
ORDER BY similarity_score DESC;