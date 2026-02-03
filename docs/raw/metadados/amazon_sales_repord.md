# Data Dictionary — amazon_sales_report.csv

## Dataset Overview

- **Dataset Name:** Amazon Sales Report  
- **Layer:** Raw  
- **Source:** Kaggle — Unlock Profits with E-Commerce Sales Data  
- **File:** amazon_sales_report.csv  

### Description
This dataset provides detailed insights into Amazon sales transactions, including product identifiers, fulfillment information, quantities and monetary values. It supports analysis of product performance, sales volume and operational fulfillment.

---

## Grain

**One row per product sale transaction.**

Each record represents the sale of a specific SKU with associated quantity and amount.

---

## Business Keys (Logical)

- SKU  
- Date  
- ASIN  

> No strict primary key is enforced in the Raw layer. Duplicate rows may exist.

---

## Columns

### Category
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Type or category of the product sold.  
- **Examples:** Apparel, Accessories, Footwear  

---

### Size
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Size of the product.  
- **Examples:** S, M, L, XL, Free Size  

---

### Date
- **Type:** Date (may appear as String in raw file)  
- **Nullable:** Yes  
- **Description:** Date when the sale occurred.  
- **Notes:**  
  - Date format may vary  
  - Time information is not included  

---

### Status
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Status of the sale transaction.  
- **Examples:** Shipped, Delivered, Cancelled, Returned  

---

### Fulfilment
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Method used to fulfill the order.  
- **Examples:** Amazon Fulfilled, Merchant Fulfilled  

---

### Style
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Style or design classification of the product.  

---

### SKU
- **Type:** String  
- **Nullable:** No  
- **Description:** Stock Keeping Unit, internal product identifier.  

---

### ASIN
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Amazon Standard Identification Number for the product.  

---

### Courier Status
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Delivery status reported by the courier.  
- **Examples:** In Transit, Delivered, Returned  

---

### Qty
- **Type:** Integer  
- **Nullable:** Yes  
- **Description:** Quantity of units sold in the transaction.  

---

### Amount
- **Type:** Float  
- **Nullable:** Yes  
- **Description:** Monetary value of the sale.  
- **Notes:** Represents transaction value, not necessarily net revenue.  

---

### B2B
- **Type:** Boolean  
- **Nullable:** Yes  
- **Description:** Indicates whether the sale is business-to-business.  
- **Values:**  
  - true → B2B sale  
  - false → B2C sale  

---

### Currency
- **Type:** String  
- **Nullable:** Yes  
- **Description:** Currency used in the transaction.  
- **Examples:** INR, USD  

---

## Data Quality Notes

- Missing values may exist across multiple fields  
- Duplicate records may be present  
- Dates and numeric fields may require standardization  

---

## Out of Scope (Raw Layer)

- Revenue or profit calculations  
- Status consolidation  
- Currency conversion  
- Product normalization  

These responsibilities belong to downstream layers (Bronze and Silver).

---

## Downstream Usage

- **Bronze:** Validation, cleansing, type normalization  
- **Silver:** Analytics-ready models and aggregations  
- **Gold:** KPIs, dashboards and machine learning features
