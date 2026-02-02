HNI Investment Decision Support System
Project Overview
This project is a Minimum Viable Product (MVP) designed to support High Networth Individuals (HNIs) in making informed investment decisions using financial data analysis, classification, and scoring models.

Objectives
Classify companies based on market capitalization
Suggest best companies for investment
Calculate overall financial health score of a company
Visualize insights using charts
Data Sources
Live Data:

Yahoo Finance API
Alpha Vantage API
Historical Data:

Kaggle datasets
CSV financial statements
System Architecture
API / CSV → Python ETL → Financial Models → Scoring → Visualization

Part 1: Investment Classification
Companies are categorized into:

Magnificent Seven
Market Cap > USD 500B (Top 5)
Market Cap USD 100–500B (Top 7)
Market Cap < USD 100B (Top 10)
Part 2: Company Health Analysis
Input: Company Name or Symbol
Output: Health Score (%) with Pros & Cons

Financial Models Used
Statistical: CAGR, Moving Average, Z-Score
Machine Learning: Linear Regression, Random Forest
Deep Learning (Future Scope): LSTM / RNN
Technologies Used
Python, Pandas, NumPy
Scikit-learn
Matplotlib
GitHub
Future Enhancements
Real-time dashboards
Deep learning price forecasting
Portfolio optimization
