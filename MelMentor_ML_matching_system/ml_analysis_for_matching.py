import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('student_profiles.csv')
print("Columns in the CSV file:", df.columns)

# Function to clean major names from 'Science'
def clean_major(major):
    return major.replace(' Science', '').strip().lower()

# Create separate features for major and interests
df['major_feature'] = df['major'].apply(clean_major)
df['interest_feature'] = df['academic_interests'] + ' ' + df['hobbies']

mentees = df[df['class_year'] == df['class_year'].max()]
mentors = df[df['class_year'] < df['class_year'].max()]

# Create TF-IDF vectors for interests and majors
tfidf_interests = TfidfVectorizer(stop_words='english')
tfidf_majors = TfidfVectorizer()

mentee_interest_vectors = tfidf_interests.fit_transform(mentees['interest_feature'])
mentor_interest_vectors = tfidf_interests.transform(mentors['interest_feature'])

mentee_major_vectors = tfidf_majors.fit_transform(mentees['major_feature'])
mentor_major_vectors = tfidf_majors.transform(mentors['major_feature'])

# Calculate cosine similarity for interests and majors
interest_similarity = cosine_similarity(mentee_interest_vectors, mentor_interest_vectors)
major_similarity = cosine_similarity(mentee_major_vectors, mentor_major_vectors)

# Combine similarities with weights (e.g., 80% major, 20% interests)
combined_similarity = 0.8 * major_similarity + 0.2 * interest_similarity

def find_best_mentor(mentee_index):
    mentor_scores = combined_similarity[mentee_index]
    best_match_index = np.argmax(mentor_scores)
    best_mentor = mentors.iloc[best_match_index]
    similarity_score = mentor_scores[best_match_index]

    if mentees.iloc[mentee_index]['major_feature'] != best_mentor['major_feature']:
        print(
            f"Note: {mentees.iloc[mentee_index]['Full_name']} ({mentees.iloc[mentee_index]['major_feature']}) matched with {best_mentor['Full_name']} ({best_mentor['major_feature']}) due to combined similarity.")

    return best_mentor['Full_name'], float(similarity_score), best_mentor['major']

mentor_matches = []
for i in range(len(mentees)):
    best_mentor, similarity_score, mentor_major = find_best_mentor(i)
    mentor_matches.append({
        'Mentee': mentees.iloc[i]['Full_name'],
        'Mentee Major': mentees.iloc[i]['major'],
        'Mentor': best_mentor,
        'Mentor Major': mentor_major,
        'Similarity Score': similarity_score
    })

matches_df = pd.DataFrame(mentor_matches)

sorted_matches = matches_df.sort_values('Similarity Score', ascending=False)

pd.set_option('display.max_columns', None)
print(sorted_matches)

sorted_matches.to_csv('mentor_matches.csv', index=False)
print("Mentor matches have been saved to 'mentor_matches.csv'")

# Create a heatmap of similarity scores
plt.figure(figsize=(12, 8))
sns.heatmap(combined_similarity, cmap='YlOrRd', annot=False)
plt.title('Similarity Scores Heatmap')
plt.xlabel('Mentors')
plt.ylabel('Mentees')
plt.savefig('similarity_heatmap.png')
plt.close()

# Create a bar plot of top 10 matches
top_10_matches = sorted_matches.head(10)
plt.figure(figsize=(12, 6))
plt.bar(range(len(top_10_matches)), top_10_matches['Similarity Score'])
plt.title('Top 10 Mentor-Mentee Matches')
plt.xlabel('Match Rank')
plt.ylabel('Similarity Score')
plt.xticks(range(len(top_10_matches)), [f"{m[:10]}... - {me[:10]}..." for m, me in zip(top_10_matches['Mentor'], top_10_matches['Mentee'])], rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_matches.png')
plt.close()

# Create a scatter plot of major similarity vs interest similarity
plt.figure(figsize=(10, 8))
plt.scatter(major_similarity.flatten(), interest_similarity.flatten(), alpha=0.5)
plt.title('Major Similarity vs Interest Similarity')
plt.xlabel('Major Similarity')
plt.ylabel('Interest Similarity')
plt.savefig('similarity_scatter.png')
plt.close()

# Create a pie chart of mentor majors
mentor_majors = mentors['major'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(mentor_majors.values, labels=mentor_majors.index, autopct='%1.1f%%')
plt.title('Distribution of Mentor Majors')
plt.savefig('mentor_majors_pie.png')
plt.close()

# Create a network graph of matches
import networkx as nx

G = nx.Graph()
for _, row in sorted_matches.iterrows():
    G.add_edge(row['Mentee'], row['Mentor'], weight=row['Similarity Score'])

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=500, font_size=8, font_weight='bold')
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
plt.title('Mentor-Mentee Matching Network')
plt.axis('off')
plt.tight_layout()
plt.savefig('matching_network.png')
plt.close()

print("Visualizations have been saved as PNG files.")