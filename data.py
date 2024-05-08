# query_execution.py
import matplotlib.pyplot as plt
from matplotlib import *
from connect import create_connection

def execute_query(query):
    """
    Executes a given SQL query against the PostgreSQL database and returns the results.
    - query: The SQL query string to execute.
    """
    conn = create_connection()
    cur = conn.cursor()
    result = None
    try:
        cur.execute(query)
        # Fetch the result if it's a SELECT COUNT(*) statement
        if query.strip().upper().startswith("SELECT COUNT"):
            result = cur.fetchone()[0] # Assuming the query returns a single value
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
    return result

# Example usage
if __name__ == "__main__":
    numofcustomer = "SELECT COUNT(cid) FROM loginscred;"
    numofpackage1 = "select count(poid) from productavail where poid = '1';"
    numofpackage2 = "select count(poid) from productavail where poid = '2';"
    numofpackage3 = "select count(poid) from productavail where poid = '3';"
    numofpackage4 = "select count(poid) from productavail where poid = '4';"
    numofpackage5 = "select count(poid) from productavail where poid = '5';"
    numofpackage6 = "select count(poid) from productavail where poid = '6';"
    numofpackage7 = "select count(poid) from productavail where poid = '7';"
    totalpackagebought = "select count(poid) from productavail;"
    package_count1 = execute_query(numofpackage1)
    package_count2 = execute_query(numofpackage2)
    package_count3 = execute_query(numofpackage3)
    package_count4 = execute_query(numofpackage4)
    package_count5 = execute_query(numofpackage5)
    package_count6 = execute_query(numofpackage6)
    package_count7 = execute_query(numofpackage7)
    customer_count = execute_query(numofcustomer)
    total_bought = execute_query(totalpackagebought)
    #select * from customer_name inner join eventinfo
#on customer_name.cid = eventinfo.cid where poid = '3'   #this is for knowing the information
#select * from customer_name inner join
#customer_info on customer_name.cid = customer_info.cid

    if customer_count is not None:
        print(f"Count for Package A Portrait: {package_count1}")
        print(f"Count for Package B Portrait: {package_count2}")
        print(f"Count for Package C Portrait: {package_count3}")
        print(f"Count for Package A Food Entices: {package_count4}")
        print(f"Count for Package B Food Entices: {package_count5}")
        print(f"Count for Package C Food Entices: {package_count6}")
        print(f"Count for Special Currated Package: {package_count7}")
        print(f"Total Packages Bought: {total_bought}")
        print(f"Count: {customer_count}")


#################################


numofcustomer = "SELECT COUNT(cid) FROM loginscred;"
numofpackage1 = "select count(poid) from productavail where poid = '1';"
numofpackage2 = "select count(poid) from productavail where poid = '2';"
numofpackage3 = "select count(poid) from productavail where poid = '3';"
numofpackage4 = "select count(poid) from productavail where poid = '4';"
numofpackage5 = "select count(poid) from productavail where poid = '5';"
numofpackage6 = "select count(poid) from productavail where poid = '6';"
numofpackage7 = "select count(poid) from productavail where poid = '7';"
totalpackagebought = "select count(poid) from productavail;"
package_count1 = execute_query(numofpackage1)
package_count2 = execute_query(numofpackage2)
package_count3 = execute_query(numofpackage3)
package_count4 = execute_query(numofpackage4)
package_count5 = execute_query(numofpackage5)
package_count6 = execute_query(numofpackage6)
package_count7 = execute_query(numofpackage7)
customer_count = execute_query(numofcustomer)
total_bought = execute_query(totalpackagebought)

product_sales = {
    "Portrait A":package_count1,
    "Portrait B":package_count2,
    "Portrait C":package_count3,
    "Food Enticing A":package_count4,
    "Food Enticing B":package_count5,
    "Food Enticing C":package_count6,
    "Currated":package_count7,
}
product_sales1 = {
    "\nPortrait A":package_count1,
    "Portrait B":package_count2,
    "\nPortrait C":package_count3,
    "Food Ent. A":package_count4,
    "\nFood Ent. B":package_count5,
    "Food Ent. C":package_count6,
    "\nCurrated":package_count7,
    "Total Sales":total_bought
}
#Progress percentage

progress_done = "select count(status) from pstatus where status='Done';"
progress_inprog = "select count(status) from pstatus where status='Inprogress';"
progress_cancel = "select count(status) from pstatus where status='Cancelled';"
progress_total = "select count(status) from pstatus;"


progress1 = execute_query(progress_done)
progress2 = execute_query(progress_inprog)
progress3 = execute_query(progress_cancel)
total_prog = execute_query(progress_total)

prog1percent = (progress1 / total_prog) * 100
prog2percent = (progress2/ total_prog) * 100
prog3percent = (progress3/ total_prog) * 100
totalss = (total_prog/ total_prog) * 100

percentprog1 = round(prog1percent, 2)
percentprog2 = round(prog2percent, 2)
percentprog3 = round(prog3percent, 2)


progress_work = {
    "Done":percentprog1,
    "Inprogress":percentprog2,
    "Cancelled":percentprog3,
}
