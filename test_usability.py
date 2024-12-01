import pytest
import asyncio
import os
from async_sqlserver_lib.decorators import (
    create_db_connection,
    close_db_connection
    )   
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()

# Replace with your actual database connection data from .env
DB_CONFIG = {
    "driver": os.getenv('DB_DRIVER'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASS'),
    "host": os.getenv('DB_HOST'),
    "port": int(os.getenv('DB_PORT')),
    "database": os.getenv('DB_NAME'),
}

@create_db_connection(
    driver=DB_CONFIG["driver"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    database=DB_CONFIG["database"],
)
@close_db_connection
@pytest.mark.asyncio
async def test_fetch_data(db_manager=None):
    """
    Test function to fetch data from a SQL Server database.

    :param db_manager: The DBManager instance (injected by the decorator).
    :return: List of rows fetched from the database.
    """
    try:
        query = "SELECT TOP 5 * FROM your_table"  # Replace `your_table` with an actual table name
        async with db_manager.get_session() as session:
            result = await session.execute(text(query))
            rows = result.fetchall()
            print("Fetched rows:", rows)
            return rows
    except Exception as e:
        print("Error during fetch:", str(e))
        return []

@create_db_connection(
    driver=DB_CONFIG["driver"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
    host=DB_CONFIG["host"],
    port=DB_CONFIG["port"],
    database=DB_CONFIG["database"],
)
@close_db_connection
@pytest.mark.asyncio
async def test_insert_data(db_manager=None):
    """
    Test function to insert data into a SQL Server database.

    :param db_manager: The DBManager instance (injected by the decorator).
    :return: None
    """
    try:
        query = """
        INSERT INTO your_table (column1, column2)
        VALUES ('TestValue1', 'TestValue2')
        """  # Replace `your_table` and column names with actual table/columns
        async with db_manager.get_session() as session:
            await session.execute(text(query))
            print("Insert operation successful.")
    except Exception as e:
        print("Error during insert:", str(e))

async def main():
    """
    Main function to run the test cases.
    """
    print("Testing fetch operation:")
    await test_fetch_data()

    print("\nTesting insert operation:")
    await test_insert_data()

# Run the test cases
if __name__ == "__main__":
    asyncio.run(main())