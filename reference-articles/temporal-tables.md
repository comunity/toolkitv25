---
description: >-
  Temporal Tables are useful in scenarios that require tracking of data changes
  in a database environment
---

# Temporal Tables

Use cases for temporal tables include any of the following scenarios:

### Data audit <a href="#data-audit" id="data-audit"></a>

Use temporal system-versioning on tables that store critical information for which you need to keep track of what has changed and when, and to perform data forensics at any point in time.

### Point-in-time analysis (time travel) <a href="#point-in-time-analysis-time-travel" id="point-in-time-analysis-time-travel"></a>

Unlike a data audit, where the focus is typically on changes that occurred to individual records, in time travel scenarios users want to see how entire data sets changed over time.&#x20;

### Anomaly detection <a href="#anomaly-detection" id="anomaly-detection"></a>

Anomaly detection is the identification of items that do not conform to an expected pattern or other items in a dataset.&#x20;

### Slowly-changing dimensions <a href="#slowly-changing-dimensions" id="slowly-changing-dimensions"></a>

Dimensions in data warehousing typically contain relatively static data about entities such as geographical locations, customers, or products.

### Repairing row-level data corruption <a href="#repairing-row-level-data-corruption" id="repairing-row-level-data-corruption"></a>

You can rely on historical data in system-versioned temporal tables to quickly repair individual rows to any of the previously captured states.&#x20;



For more information, go to [Temporal Tables - SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables?view=sql-server-ver15)
