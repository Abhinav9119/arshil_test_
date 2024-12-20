import pymysql
import json

class EmployeeDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        try:
            conn = pymysql.connect(
                host=self.host, 
                user=self.user, 
                password=self.password, 
                database=self.database
            )
            return conn
        except pymysql.MySQLError as err:
            print(f"Database connection failed: {err}")
            return None

    def add_employee(self, first_name, last_name, email, department, joining_date, salary):
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                query = "insert into employee (first_name, last_name, email, department, joining_date, salary) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (first_name, last_name, email, department, joining_date, salary))
                conn.commit()
                print("employee added successfully.")
            except pymysql.MySQLError as err:
                print(f"error adding employee: {err}")
            finally:
                cursor.close()
                conn.close()

    def update_salary(self, employee_id, new_salary):
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("select * from employee where employee_id = %s", (employee_id,))
                if cursor.fetchone():
                    query = "update employee set salary = %s where employee_id = %s"
                    cursor.execute(query, (new_salary, employee_id))
                    conn.commit()
                    print("salary updated successfully.")
                else:
                    print("employee not found.")
            except pymysql.MySQLError as err:
                print(f"error updating salary: {err}")
            finally:
                cursor.close()
                conn.close()

    def delete_employee(self, employee_id):
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("select * from employee where employee_id = %s", (employee_id,))
                if cursor.fetchone():
                    query = "delete from employee where employee_id = %s"
                    cursor.execute(query, (employee_id,))
                    conn.commit()
                    print("employee deleted successfully.")
                else:
                    print("employee not found.")
            except pymysql.MySQLError as err:
                print(f"error deleting employee: {err}")
            finally:
                cursor.close()
                conn.close()

    def display_employees(self):
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            try:
                cursor.execute("select * from employee")
                employees = cursor.fetchall()
                print(json.dumps(employees, indent=4, default=str))
            except pymysql.MySQLError as err:
                print(f"error retrieving employees: {err}")
            finally:
                cursor.close()
                conn.close()
