## Table Metadata Extractor (Python)
Interview question for secoda in Python. 

Please provide a Python Django application that has one API endpoint which accepts a database connection string from your DB of choice (Redshift, BigQuery, Snowflake, MySQL, Postgres), connects to the database using [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) and returns a list of the `TableMetadata` data objects (see below) for all tables in the database. If you need a database to test on please let Andrew (andrew@secoda.co) know and he can provide one.

```jsx
TableMetadata = {
	columns: List[ColumnMetadata]
	num_rows: int
	schema: str
	database: str
}

ColumnMetadata = {
	col_name: str
	col_type: str
}
```

Bonus points for:

- Instructive error messages for improper connection strings or other invalid input
- A solution that is efficient