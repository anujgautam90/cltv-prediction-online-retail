# Customer Lifetime Value (CLTV) Prediction – Online Retail
A story-driven data science project by anujgautam90
## 1. Background  
Modern ecommerce businesses often acquire customers quickly but struggle to understand their long-term value. Without knowing which customers are worth retaining, marketing teams overspend on low-impact audiences while neglecting high-value segments.
The challenge isn't lack of data — the challenge is turning raw transactions into forward-looking intelligence.
This project uses real ecommerce transaction data to predict Customer Lifetime Value (CLTV) and provide data-driven insights for customer retention, segmentation, and budget allocation.

## 2. Business Challenge  
The retailer faces these fundamental questions:
- Which customers are likely to generate the most revenue in the future?  
- How should marketing budgets be allocated across customer segments?  
- Which behavioural signals indicate long-term loyalty or churn?  
- Can machine learning improve customer targeting and profitability?

Traditional RFM segmentation is useful but not predictive.  
Businesses need a system that forecasts future value — not just describes past behaviour.

## 3. Dataset  
- Source: Kaggle / UCI Machine Learning Repository  
- Dataset: Online Retail II (2010–2011)  
- Rows: ~1 Million  
- Fields:  
  - Invoice, StockCode, Description  
  - Quantity, Price  
  - InvoiceDate  
  - CustomerID  
  - Country  
This dataset contains real transaction-level data from an online UK retailer.

> Dataset link: https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

## 4. Technical Approach  
This project is structured like a real industry ML engagement.

### 4.1 Data Cleaning  
- Remove cancelled orders (Invoice starting with `"C"`)  
- Drop rows with missing `CustomerID`  
- Handle outliers in `Quantity` and `Price`  
- Convert `InvoiceDate` to proper datetime  
- Create a `TotalPrice = Quantity  UnitPrice` column  

### 4.2 Exploratory Behaviour Analysis  
- Monthly revenue trends  
- Customer retention curves  
- RFM segmentation (Recency, Frequency, Monetary)  
- Cohort analysis: acquisition → retention patterns  
- Top customers, top SKUs, purchase intervals  

### 4.3 Feature Engineering  
Created customer-level features such as:
•	Feature				           Description
•	recency				           Days since last purchase
•	frequency				         Number of invoices
•	monetary_value			     Total revenue
•	avg_basket_value		     Average spend per order
•	purchase_interval_mean	 Average days between purchases
•	returns_flag			       Whether the customer has returned items
•	country				           Encoded geography
These features form the behavioural DNA of each customer.


### 4.4 CLTV Label Creation  
Target variable:  
Total customer spend in the next 90 days after a chosen reference date.
This mimics real-world forecasting where businesses must estimate short-term customer value for campaign planning.

### 4.5 Predictive Modeling  
Models evaluated:
- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor (final choice)
Evaluation metrics:
- RMSE  
- MAE  
- R²  

### 4.6 Model Explainability  
Using SHAP values, this project explores:
- What makes a customer high-value?  
- Which features predict CLTV the most?  
- What behaviours signal loyalty vs churn?  

Typical patterns:
- Higher purchase frequency → higher future CLTV  
- Shorter purchase intervals → stronger loyalty  
- High basket value → higher CLTV  
- Frequent returns → lower CLTV  

## 5. Key Insights  
1. Small segments drive majority revenue  
   Top 20% of customers generate a large share of predicted CLTV (Pareto pattern).
2. Most powerful behavioural predictors  
   - Purchase frequency  
   - Monetary value  
   - Recent activity (recency)  
   - Basket size  
3. High-value cohorts share specific traits  
   - Purchase cycle < 30 days  
   - High first-order value  
   - Low return rates  
   - Multi-item baskets  
4. Actions for the business  
   - Retention focus on frequent buyers  
   - Churn campaigns for customers whose recency is growing  
   - Bundling/upsell offers for high basket-value customers  
   - Dedicated playbooks for international segments  

## 6. Final Deliverables  
- End-to-end CLTV machine learning workflow  
- Customer segmentation & insights  
- Fully explainable predictive model  
- Reproducible notebook and code  
- Story-driven documentation for business + technical audiences  

## 7. Future Enhancements  
- Streamlit dashboard for interactive customer segmentation  
- Probabilistic CLTV models (BG/NBD + Gamma-Gamma)  
- Longer forecast windows (180 / 360 days)  
- Add marketing cost to estimate channel-level ROI  
- Model deployment as an API  

## 8. How to Run This Project  
1. Clone the repository:
```bash
git clone https://github.com/anujgautam90/cltv-prediction-online-retail.git
cd cltv-prediction-online-retail
