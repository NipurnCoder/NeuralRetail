CREATE TABLE segments(

customer_id FLOAT,

recency FLOAT,

frequency FLOAT,

monetary FLOAT,

segment INT

);

CREATE TABLE forecast(

date DATE,

sales FLOAT

);

CREATE TABLE churn(

customer_id FLOAT,

churn INT

);

CREATE TABLE inventory(

stockcode TEXT,

annualdemand FLOAT,

eoq FLOAT,

safetystock FLOAT,

rop FLOAT

);