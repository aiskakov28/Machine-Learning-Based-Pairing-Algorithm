# Machine-Learning-Based-Pairing-Algorithm
## 🎯 Project Overview

An innovative AI matching system developed during the Dandyhacks Hackathon that connects freshmen with upperclassmen based on their profiles. This solution earned recognition from Fidelity Investments for its innovative approach to student mentorship.

## 🏆 Key Features

- Intelligent data preprocessing and cleaning pipeline
- Advanced TF-IDF vectorization for academic profiles
- Sophisticated cosine similarity matching algorithm
- Smart weighting system for major and interest matching
- Automated generation of optimal mentor-mentee pairs

## 📁 Project Structure

```
project/
├── ml_analysis_for_matching.py    # Main matching algorithm
├── student_profiles.csv           # Input data (DataBricks generated)
└── mentor_matches.csv            # Output matching results
```

## 🔬 Methodology

The matching system employs Natural Language Processing techniques:

- TF-IDF (Term Frequency-Inverse Document Frequency) analysis
- Cosine Similarity calculations
- Weighted profile matching

## 📊 Visualizations

The system generates comprehensive visual analytics:

- Similarity Heatmap (similarity_heatmap.png)
- Top 10 Matches Bar Plot (top_10_matches.png)
- Similarity Scatter Plot (similarity_scatter.png)
- Mentor Major Distribution (mentor_majors_pie.png)
- Matching Network Graph (matching_network.png)

## ⚙️ Dependencies

```
pandas
numpy
matplotlib
seaborn
scikit-learn
networkx
```

## 🚀 Getting Started

1. Install required dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn networkx
```

1. Set up the project:
- Place student_profiles.csv in the project directory
- Run the main script: python ml_analysis_for_matching.py
- Check generated visualizations and mentor_matches.csv

## 📈 Results

The algorithm produces:

- Ranked mentor-mentee matches with similarity scores
- Detailed visualization suite for match analysis
- Comprehensive matching statistics

## 🔮 Future Enhancements

- Implementation of advanced NLP algorithms
- Development of user-friendly interface
- Integration of feedback-based learning system
- Real-time matching capabilities
