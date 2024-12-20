
# Async SQL Server Library

A lightweight Python library for managing asynchronous connections to SQL Server databases, designed for modern Python applications requiring robust, reusable, and efficient database management.

This library simplifies SQL Server database interactions using SQLAlchemy's async capabilities and aioodbc. It provides decorators for managing connections, commits, and rollbacks, ensuring clean and consistent database handling across your projects.

---

## Installation

### Using Pip
To install the library, run:
```bash
pip install async-sqlserver-lib
```

### Using Pipenv
If you're using pipenv for dependency management:
```bash
pipenv install async-sqlserver-lib
```

---

## Purpose

### Why Use This Library?
1. **Asynchronous Database Operations**: Ideal for APIs and high-performance Python applications.
2. **Simplified Connection Management**: Provides reusable decorators for creating and closing database connections.
3. **SQLAlchemy and aioodbc Integration**: Leverages SQLAlchemy for ORM and query execution, and aioodbc for async database communication.
4. **Ease of Use**: Write clean, readable, and maintainable database interaction code with minimal setup.

---


# Using the Library

The library allows you to manage asynchronous SQL Server connections with ease. Follow the steps below to start using it:

## Set Up Your Environment Variables

To configure your SQL Server connection, create a `.env` file in your project root with the following details:

```env
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_USER=your_username
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=1433
DB_NAME=your_database
```

---

##  Use the Library in Your Code

Here’s an example of fetching data from a SQL Server database using the library:

```python
import asyncio
from async_sqlserver_lib.decorators import create_db_connection, close_db_connection
from sqlalchemy import text

@create_db_connection(
    driver="ODBC Driver 17 for SQL Server",
    user="your_username",
    password="your_password",
    host="localhost",
    port=1433,
    database="your_database",
)
@close_db_connection
async def fetch_data(db_manager=None):
    """
    Fetch data from the SQL Server database.
    """
    async with db_manager.get_session() as session:
        query = text("SELECT TOP 5 * FROM your_table")  # Replace `your_table` with your table name
        result = await session.execute(query)
        return result.fetchall()

# Run your asynchronous function
async def main():
    data = await fetch_data()
    print("Fetched data:", data)

asyncio.run(main())
```

---


## Running Tests

### Prerequisites
Install testing dependencies:
```bash
pip install pytest pytest-asyncio
```

### Run the Test Suite
Execute all tests with:
```bash
pytest
```

The test suite validates:
1. Connection management.
2. Decorator functionality.
3. Query execution.

---


## Contact and Support

For questions, issues, or contributions, please open an issue or pull request in the [GitHub repository](https://github.com/brandaolu94s/async-sqlserver-lib).

---

## Acknowledgments

This library builds upon the powerful features of:
- [SQLAlchemy](https://www.sqlalchemy.org/) for its async database management capabilities.
- [aioodbc](https://github.com/aio-libs/aioodbc) for asynchronous ODBC driver integration.
