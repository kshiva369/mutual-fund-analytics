CREATE TABLE dim_fund (
    fund_key INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    month INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav (
    nav_key INTEGER PRIMARY KEY,
    fund_key INTEGER,
    date_key INTEGER,
    nav REAL,
    FOREIGN KEY(fund_key) REFERENCES dim_fund(fund_key),
    FOREIGN KEY(date_key) REFERENCES dim_date(date_key)
);

CREATE TABLE fact_transactions (
    transaction_key INTEGER PRIMARY KEY,
    fund_key INTEGER,
    amount REAL,
    transaction_type TEXT
);

CREATE TABLE fact_performance (
    performance_key INTEGER PRIMARY KEY,
    fund_key INTEGER,
    return_1yr REAL,
    return_3yr REAL,
    return_5yr REAL,
    expense_ratio REAL
);

CREATE TABLE fact_aum (
    aum_key INTEGER PRIMARY KEY,
    fund_key INTEGER,
    aum_crore REAL
);