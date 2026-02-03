# Silver Layer — Definition & Contract

## Purpose

The Silver layer transforms technically valid data from the Bronze layer into
**semantically consistent, typed and analytics-ready entities**.

Silver focuses on **meaning, structure and usability**, not on technical cleansing.

---

## Core Principle

> **Silver does not fix technical issues.**  
> **Silver organizes business meaning.**

All technical validations, null handling and deduplication must already be
resolved in the Bronze layer.

---

## Input Source

- **Upstream Layer:** Bronze
- **Primary Dataset:** amazon_sales_report (cleaned and validated)

The Silver layer assumes that:
- mandatory fields are present
- dates are valid
- duplicates were already removed
- payload integrity is guaranteed

---

## Main Entity

### Entity Name
`sales_transaction`

---

## Grain

> **One row per SKU sold per day.**

This represents a factual sales transaction, no longer an event stream.

---

## Logical Business Keys

- sale_date
- sku
- asin (optional, product-level identifier)

No surrogate keys are introduced at this stage.

---

## Responsibilities of the Silver Layer

- Explicit data typing
- Semantic normalization
- Column renaming and standardization
- Preparation for analytical consumption
- Stability of meaning across consumers

---

## Expected Fields (Initial Version)

| Field Name     | Description                                      |
|----------------|--------------------------------------------------|
| sale_date      | Date of the sale                                 |
| sku            | Stock Keeping Unit                               |
| asin           | Amazon Standard Identification Number            |
| category       | Product category                                 |
| size           | Product size                                     |
| style          | Product style or design                          |
| fulfilment     | Fulfillment method                               |
| qty            | Quantity sold                                    |
| amount         | Transaction amount                               |
| currency       | Transaction currency                             |
| is_b2b         | Business-to-business indicator                   |
| status         | Sales transaction status                         |

---

## What Silver Explicitly Does NOT Do

- Calculate revenue or profit
- Aggregate metrics
- Determine current order status
- Join multiple domains
- Enrich data with external sources
- Apply business KPIs

These responsibilities belong to downstream layers (Gold / Features).

---

## Data Quality Guarantees

The Silver layer guarantees:

- Consistent column naming
- Correct data types
- Stable semantic meaning
- Reproducible transformations

It does **not** guarantee business correctness beyond its scope.

---

## Testing Strategy

- Unit tests validate semantic transformations
- Integration tests validate Bronze → Silver flow
- End-to-end tests validate final Silver output

All transformations are implemented using TDD.

---

## Evolution Strategy

The Silver layer is designed to evolve safely:

- New fields can be added without breaking consumers
- Semantic changes require contract updates
- Downstream layers must not rely on implementation details

---

## Final Note

The Silver layer represents the **first analytics-ready version of the data**.
It is intentionally conservative to ensure long-term stability and trust.
