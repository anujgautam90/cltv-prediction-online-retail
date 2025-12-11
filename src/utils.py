import pandas as pd
import numpy as np
from datetime import timedelta


def load_data(path: str) -> pd.DataFrame:
    """
    Load the Online Retail II dataset from a CSV/Excel file.
    """
    df = pd.read_csv(path, encoding="unicode_escape")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning:
    - remove cancelled invoices (Invoice starting with 'C')
    - drop rows with missing CustomerID
    - filter out non-positive quantities and prices
    - create TotalPrice column
    """
    df = df.copy()

    # Remove cancelled invoices
    df = df[~df["Invoice"].astype(str).str.startswith("C")]

    # Drop rows without CustomerID
    df = df.dropna(subset=["Customer ID"])

    # Filter out non-sensical values
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

    # Convert date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Total price
    df["TotalPrice"] = df["Quantity"] * df["Price"]

    return df


def build_customer_features(df: pd.DataFrame, reference_date=None) -> pd.DataFrame:
    """
    Aggregate transaction-level data into customer-level features.
    """
    df = df.copy()
    if reference_date is None:
        reference_date = df["InvoiceDate"].max() + timedelta(days=1)

    # Group by customer
    grouped = df.groupby("Customer ID")

    recency = (reference_date - grouped["InvoiceDate"].max()).dt.days
    frequency = grouped["Invoice"].nunique()
    monetary = grouped["TotalPrice"].sum()
    avg_basket_value = grouped["TotalPrice"].mean()

    features = pd.DataFrame({
        "CustomerID": recency.index,
        "recency": recency.values,
        "frequency": frequency.values,
        "monetary_value": monetary.values,
        "avg_basket_value": avg_basket_value.values,
    })

    return features


def create_target_cltv(df: pd.DataFrame,
                       reference_date,
                       horizon_days: int = 90) -> pd.DataFrame:
    """
    Create target variable: total spend in the next `horizon_days` after reference_date.
    """
    df = df.copy()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    start = reference_date
    end = reference_date + timedelta(days=horizon_days)

    mask = (df["InvoiceDate"] >= start) & (df["InvoiceDate"] < end)
    future = df.loc[mask]

    future_agg = (
        future.groupby("Customer ID")["TotalPrice"]
        .sum()
        .reset_index()
        .rename(columns={"TotalPrice": f"cltv_next_{horizon_days}d",
                         "Customer ID": "CustomerID"})
    )

    return future_agg
