import requests
import pandas as pd
import streamlit as st


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Smart Product Recommendation System",
    page_icon="🛍️",
    layout="wide"
)


# -------------------------------
# Title
# -------------------------------

st.title("🛍️ Smart Product Recommendation & Analysis System")

st.write(
    "This application retrieves product information from a public REST API "
    "and provides product search, filtering, analysis and recommendations."
)


# -------------------------------
# Fetch Product Data
# -------------------------------

@st.cache_data
def get_products():

    api_url = "https://dummyjson.com/products"

    parameters = {
        "limit": 100
    }

    response = requests.get(
        api_url,
        params=parameters,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    products = pd.DataFrame(data["products"])

    products = products[
        [
            "id",
            "title",
            "brand",
            "category",
            "price",
            "rating",
            "stock"
        ]
    ]

    return products


# -------------------------------
# Load Data
# -------------------------------

try:

    products = get_products()

    st.success(
        f"Successfully loaded {len(products)} products from the API."
    )

except Exception as error:

    st.error(f"Unable to load product data: {error}")

    st.stop()


# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.header("🔎 Product Search")

search_name = st.sidebar.text_input(
    "Enter product name or keyword"
)

max_price = st.sidebar.number_input(
    "Maximum Price",
    min_value=0.0,
    value=1000.0,
    step=10.0
)

min_rating = st.sidebar.slider(
    "Minimum Rating",
    min_value=0.0,
    max_value=5.0,
    value=0.0,
    step=0.1
)

min_stock = st.sidebar.number_input(
    "Minimum Stock",
    min_value=0,
    value=0,
    step=1
)


# -------------------------------
# Filtering
# -------------------------------

filtered_products = products.copy()

if search_name:

    filtered_products = filtered_products[
        filtered_products["title"]
        .str.lower()
        .str.contains(
            search_name.lower(),
            na=False
        )
    ]


filtered_products = filtered_products[
    (filtered_products["price"] <= max_price) &
    (filtered_products["rating"] >= min_rating) &
    (filtered_products["stock"] >= min_stock)
]


# -------------------------------
# Dashboard Statistics
# -------------------------------

st.subheader("📊 Product Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Products",
    len(products)
)

col2.metric(
    "Average Price",
    f"${products['price'].mean():.2f}"
)

col3.metric(
    "Average Rating",
    f"{products['rating'].mean():.2f}"
)

col4.metric(
    "Total Stock",
    int(products["stock"].sum())
)


# -------------------------------
# Search Results
# -------------------------------

st.subheader("🔎 Search & Filter Results")

if filtered_products.empty:

    st.warning(
        "No products match the selected conditions."
    )

else:

    display_data = filtered_products[
        [
            "id",
            "title",
            "brand",
            "category",
            "price",
            "rating",
            "stock"
        ]
    ].copy()

    display_data["price"] = display_data["price"].round(2)
    display_data["rating"] = display_data["rating"].round(2)

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )


# -------------------------------
# Category Analysis
# -------------------------------

st.subheader("📈 Category Analysis")

category_summary = products.groupby("category").agg(
    number_of_products=("id", "count"),
    average_price=("price", "mean"),
    average_rating=("rating", "mean"),
    total_stock=("stock", "sum")
).reset_index()

category_summary["average_price"] = (
    category_summary["average_price"].round(2)
)

category_summary["average_rating"] = (
    category_summary["average_rating"].round(2)
)

st.dataframe(
    category_summary,
    use_container_width=True,
    hide_index=True
)


# -------------------------------
# Recommendation System
# -------------------------------

st.subheader("⭐ Top Product Recommendations")

recommended_products = products[
    (products["price"] <= max_price) &
    (products["rating"] >= min_rating) &
    (products["stock"] >= min_stock)
].copy()


if recommended_products.empty:

    st.info(
        "No products satisfy the selected recommendation criteria."
    )

else:

    recommended_products["recommendation_score"] = (
        recommended_products["rating"] * 20
        + recommended_products["stock"] * 0.5
        - recommended_products["price"] * 0.2
    )

    recommended_products[
        "recommendation_score"
    ] = recommended_products[
        "recommendation_score"
    ].round(2)

    recommended_products = recommended_products.sort_values(
        by="recommendation_score",
        ascending=False
    )

    st.dataframe(
        recommended_products[
            [
                "title",
                "brand",
                "category",
                "price",
                "rating",
                "stock",
                "recommendation_score"
            ]
        ].head(10),
        use_container_width=True,
        hide_index=True
    )


# -------------------------------
# Download Results
# -------------------------------

st.subheader("📥 Download Data")

csv_data = filtered_products.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Filtered Products",
    data=csv_data,
    file_name="filtered_products.csv",
    mime="text/csv"
)
