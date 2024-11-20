# Machine-Learning-Based-Pairing-Algorithm
**Project Overview:** 
This project, developed during the Dandyhacks Hackathon, implements an AI matching system to connect freshmen with upperclassmen based on student profiles. Our team won a prize from Fidelity Investments for this innovative solution.

**Files:**
ml_analysis_for_matching.py: Main script for data analysis and mentor-mentee matching
student_profiles.csv: Input data containing student information (generated in DataBricks Cloud Platform)
mentor_matches.csv: Output file with mentor-mentee matches based on NLP techniques

**Methodology:**
The matching algorithm uses Natural Language Processing techniques, specifically TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity, to pair mentees with mentors based on their majors and interests.

**Key Features:**
Data cleaning and preprocessing
TF-IDF vectorization for majors and interests
Cosine similarity calculation for matching
Weighted combination of major and interest similarities
Generation of mentor-mentee pairs with similarity scores

**Visualizations:**
The script generates several visualizations to aid in understanding the matching results:
similarity_heatmap.png: Heatmap showing similarity scores between mentees and mentors
top_10_matches.png: Bar plot of the top 10 mentor-mentee matches based on similarity scores
similarity_scatter.png: Scatter plot comparing major similarity vs. interest similarity
mentor_majors_pie.png: Pie chart showing the distribution of mentor majors
matching_network.png: Network graph visualizing mentor-mentee connections

**Usage:**
Ensure you have the required libraries installed (pandas, numpy, matplotlib, seaborn, scikit-learn, networkx)
Place the student_profiles.csv file in the same directory as the script
Run the ml_analysis_for_matching.py script
Review the output in the console and the generated CSV and PNG files

**Results:**
The script outputs mentor-mentee matches sorted by similarity score, which are saved in the mentor_matches.csv file. Additionally, various visualizations are generated to provide insights into the matching process and results.

**Future Improvements:**
Implement more advanced NLP techniques for better matching
Add user interface for easier interaction with the matching system
Incorporate feedback mechanism to improve matching over time
