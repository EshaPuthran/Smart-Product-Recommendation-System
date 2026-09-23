# Smart Product Recommendation & Analysis System

## Project Overview

The **Smart Product Recommendation & Analysis System** is a Python-based mini project that retrieves product information from a public REST API and performs data analysis using Pandas.

The project applies concepts such as REST API integration, HTTP GET requests, JSON processing, Pandas DataFrames, filtering, sorting, grouping, aggregation, and CSV export.

A simple rule-based recommendation system is also implemented to recommend products based on price, rating, and stock availability.

---

## Objectives

The main objectives of this project are:

- Retrieve product data from a public REST API.
- Process the JSON response using Python.
- Convert API data into a Pandas DataFrame.
- Search for products using keywords.
- Filter products based on price, rating, and stock.
- Sort products based on price and rating.
- Perform category-wise analysis.
- Generate product recommendations.
- Export processed results to CSV files.

---

## Technologies Used

- Python
- Pandas
- Requests
- REST API
- Google Colab
- GitHub

---

## API Used

The project uses the **DummyJSON Products API**:

```text
https://dummyjson.com/products
```

The API provides product information in JSON format.

The project sends an HTTP GET request to retrieve the product data.

## Project Workflow

```text
Public REST API
       ↓
HTTP GET Request
       ↓
JSON Response
       ↓
Pandas DataFrame
       ↓
Data Selection
       ↓
Search / Filter / Sort
       ↓
Category Analysis
       ↓
Recommendation System
       ↓
CSV Export
```

## Dataset Fields

| Field | Description |
|---|---|
| `id` | Unique product identifier |
| `title` | Product name |
| `brand` | Product brand |
| `category` | Product category |
| `price` | Product price |
| `rating` | Product rating |
| `stock` | Available stock |

## Features

### 1. Product Search

Users can enter a product name or keyword.

**Example:**

```text
Enter product name or keyword: lipstick
```
The system displays matching products.

---

### 2. Price Filtering

Users can enter a maximum price.

**Example:**

```text
Enter maximum price: 50
```
The system displays products within the specified budget.

---

### 3. Rating Filtering

Users can specify a minimum rating.

**Example:**

```text
Users can specify a minimum rating.
```
The system displays products with the required rating or higher.

---

### 4. Stock Filtering

The system identifies products that are currently available in stock.

---

### 5. Product Sorting

Products can be sorted according to:

-Price
-Rating

---

### 6. Category Analysis

The project performs category-wise analysis using Pandas.

The analysis includes:

-Number of products
-Average price
-Average rating
-Total stock

---
### 7. Product Recommendation

The recommendation system allows the user to specify:

-Maximum budget
-Minimum rating
-Minimum stock

The system then identifies products that satisfy the selected conditions.

---
### 8. Recommendation Score

A simple recommendation score is calculated using:

-Product rating
-Product stock
-Product price

Products are ranked according to this score.

---
## Project Files

```text
Smart-Product-Recommendation-System/
│
├── Smart_Product_Recommendation_System.ipynb
├── README.md
├── all_products.csv
├── recommended_products.csv
└── category_summary.csv
```
### File Description

**`Smart_Product_Recommendation_System.ipynb`**

Contains the complete Python implementation of the project.

**`all_products.csv`**

Contains the product data retrieved from the API.

**`recommended_products.csv`**

Contains products selected by the recommendation system.

**`category_summary.csv`**

Contains category-wise product analysis.

**`README.md`**

Contains project documentation.

---

### How to Run
## Using Google Colab
1.Open Google Colab.
2.Upload Smart_Product_Recommendation_System.ipynb.
3.Run the cells sequentially.
4.Enter the requested inputs when prompted.

# Using a Local Python Environment

Install the required libraries:

```text
pip install pandas requests
```
Then open the notebook using Jupyter Notebook or JupyterLab.

---

## Requirements

```text
Python 3.x
pandas
requests
```
---
## 🧪 Example

### Product Search

Example input:

```text
Enter product name or keyword: lipstick
```
The system searches the product dataset and displays matching products.
### Product Recommendation

Example input:

```text
Enter your maximum budget: 50
Enter minimum rating: 4
Enter minimum stock required: 5
```
The system returns products satisfying the specified conditions.

---
## Concepts Demonstrated

This project demonstrates:

REST APIs
HTTP GET requests
Query parameters
JSON
Python Requests library
Pandas DataFrames
Data filtering
Data sorting
Grouping and aggregation
Data analysis
CSV export
Rule-based recommendation

---

## Future Enhancements

Possible future improvements include:

-Interactive data visualization
-Product comparison
-Price range charts
-Rating charts
-Category charts
-Personalized recommendations
-Machine learning-based recommendations
-Web interface using Flask or Streamlit
-Interactive dashboard

---

## Project Type

## Mini Project

Domain: Data Analysis / REST API / Recommendation System

Platform: Google Colab

Language: Python

---
## License

This project is created for educational and academic purposes.
