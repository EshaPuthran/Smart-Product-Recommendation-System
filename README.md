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

##Dataset Fields

| Field | Description |
|---|---|
| `id` | Unique product identifier |
| `title` | Product name |
| `brand` | Product brand |
| `category` | Product category |
| `price` | Product price |
| `rating` | Product rating |
| `stock` | Available stock |

## 🔎 Features

### 1. Product Search

Users can enter a product name or keyword.

Example:

```text
Enter product name or keyword: lipstick

