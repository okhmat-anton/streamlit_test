# import snowflake.connector as snow
import os

PASSWORD = os.getenv('SNOWSQL_PWD')
WAREHOUSE = os.getenv('WAREHOUSE')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


# con = snow.connect(
#     user='XXXX',
#     password='XXXX',
#     account='XXXX',
#     session_parameters={
#         'QUERY_TAG': 'EndOfMonthFinancials',
#     }
# )
# cur.execute("SELECT * FROM testtable")
# print(cur.sfqid)

# conn = snowflake.connector.connect(
#     user=USER,
#     password=PASSWORD,
#     account=ACCOUNT,
#     warehouse=WAREHOUSE,
#     database=DATABASE,
#     schema=SCHEMA
#     )
# con.cursor().execute("ALTER SESSION SET QUERY_TAG = 'EndOfMonthFinancials'")