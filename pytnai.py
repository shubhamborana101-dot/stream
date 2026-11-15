# # this means print variable data ctrl + /

# # name = "priyanshi"

# # num = 56
# # number = 55.8
# # is_valid = False
# # print(name, num, number)

# # city, order, revenue = "jaipur", 123, 67999

# # print(type(order))



# # order = "150"
# # orders = int(order)
# # print(type(order))


# # name = input("Enter your name: ")
# # print("hello, your name is: ", name)
# # age = int(input("Enter your age: "))
# # print("your age is: ", age)

# # course = "Pythonai"
# # city = "pune"
# # qualification = "master"
# # print(f"i live in {city} my qualification is {qualification} ")




# # rev = 150000
# # cost = 110000
# # profit = rev - cost
# # prof_margin = (profit / rev)*100
# # print(prof_margin)



# # a = 78
# # b = 78
# # print(a != b)

# # sales = 120000
# # rating = 4.5

# # print(sales > 1000 or  rating < 4.2)
# # print(not sales > 1000)


# # skills = ["excel", "sql","py"]
# # print("python" not in skills)


# # result2 = (10 + 5) * 2
# # print(result2)



# # achievement = 88

# # if achievement >= 98:
# #     print("excellent")
    
# # elif achievement >= 77:
# #     print("good")
# # else:
# #     print("fail")


# # total_spend = 8000
# # orders = 12

# # if total_spend >= 50000 and orders >= 10:
# #     print("high value customer")
    
# # else :
# #     print("regular customer")


# # department = "sales dep"
# # replresult = department.replace("sales", "designing")
# # print(replresult)


# # names = "sanju ayan riya anjali"
# # parts = names.split(" ")
# # print(parts)

# # names1 = ["Arun","sharma"]
# # print("-".join(names1))

# # email= "abc"
# # print(email.endswith("@gmail.com"))



# # feedback = "good product good ok not ok"
# # print(feedback.count("good"))


# # sales = [12000, 34555, 5667, 6667]
# # total = 0

# # for value in sales:
# #     total = total + value
# #     print(total)
    
# # print(total)
# # for value in sales:
# #     print(value)

# # for num in range(6):
# #     print("number is :",num)

# # city  ="delhi"

# # for letter in city:
# #     print(letter)


# # count  = 1

# # while count <= 5:
    
# #     count = count + 1
# #     print(count)


# # sales =[12000, None, 18000, None, 22000]

# # for sale in sales:
  
    
# #     if sale is None:
# #         continue
        
# #     print(sale)   

# # region = ["north", "south"]
# # products = ["laptop", "mouse"]

# # for regn in region:
# #     for prod in products:
# #         print(regn , "-", prod)

# # prd = ["laptop", "mouse"]

# # prd.append("keyboard")
# # print(prd)
# # prd.insert(1, "monitor")
# # print(prd)

# # prd = ["laptop", "mouse", "keyword"]

# # # prd.remove("mouse")
# # # prd.pop()
# # del prd[1]
# # print(prd)

# # atsskill = ["python", "sql", "excel", "power bi"]

# # userskill = ["python", "sql","excel"]

# # for skill in atsskill:
# #     if skill in userskill:
# #         print(skill, "available")
        
# #     else:
# #         print(skill, "missing")
        
# # sales = [100000, 115000, 108000, 135000]

# # for i in range(1, len(sales)):
# #     prev = sales[i-1]
# #     curr = sales[i]
    
# #     growth = ((curr - prev)/prev)*100
# #     print("growth:  ", round(growth, 2), "%")


# # month = ("jan","jan", "feb", "mar")
# # print(month.count("jan"))
# # print(month.index("feb"))
# # temp = list(month)
# # temp.append("apr")
# # monthtuple = tuple(temp)

# # print(monthtuple)
# # # month.append("apr")
# # print(type(month))


# # cust ={
# #     "name":"riya",
# #     "city":"jaipur",
# #     "order":12
# # }
# # for detail, value in cust.items():
# #     print(detail, "-",value)


# # print(cust.keys())
# # print(cust.values())
# # print(cust.items())

# # print(cust)
# # cust.pop("city")
# # print(cust)
# # del cust["order"]
# # print(cust)
# # print(cust["name"])
# # print(cust.get("city"))

# # cust["segment"] = "gold"
# # print(cust)
# # cust["city"] = "pune"
# # print(cust)


# # cust = {
# #     "c101":{"name":"riya", "spend":3344},
# #     "c102":{"name":"priya", "spend":2244},
# # }

# # print(cust["c101"]["spend"])

# # order = {
# #     "order_id": "ORD101",
# #     "product": "Laptop",
# #     "units": 3,
# #     "price": 55000,
# #     "cost_per_unit": 47000
# # }

# # revenue = order["units"] * order["price"]
# # cost = order["units"] * order["cost_per_unit"]
# # profit = revenue - cost

# # order["revenue"] = revenue
# # order["profit"] = profit

# # if profit >= 20000:
# #     order["status"] = "High Profit"
# # else:
# #     order["status"] = "Normal Profit"

# # for key, value in order.items():
# #     print(key, ":", value)


# # revenue = 100000
# # orders = 0

# # try:
# #     average_order = revenue / orders
# # except ZeroDivisionError:
# #     print("Orders cannot be zero")


# # sales = [1000,333, 34444, 45555]

# # new_Sales = [value * 1.10 for value in sales]
# # print(new_Sales)
# # sales.sort(reverse=True)
# # print(sales)
# # print("total ",sum(sales))
# # print("min ", min(sales))
# # print("max ", max(sales))
# # print("count", len(sales))


# # def greet():
# #     print("welcome to this course data analytics ai powered")
    
# # greet()
# # greet()
# # greet()

# # def prof_margin(rev, profit):
# #     return (profit/rev) *100

# # result = prof_margin(200000, 345555)
# # print(round(result, 2), "%")




# # def employee(name, department, salary):
# #     print("Name:", name)
# #     print("Department:", department)
# #     print("Salary:", salary)

# # employee(
# #     "Analytics",
# #     "Riya",
    
# #     65000
# # )

# # def calsum(n):
# #     if n==0:
        
# #         return
    
# #     calsum(n-1)
# #     print(n)
    
    
# # calsum(5)



# # file = open("sales.txt", "r")

# # content = file.read()

# # print(content)

# # file.close()


# # with open("sales.txt", "r")as file:
# #     content = file.readlines()
# #     print(content)




# # with open("sales.txt","a") as file:
# #     file.write("\nnew data")
    
# # print("data added to file")
# # try:
# #  with open("sale.txt","w") as file:
# #      data = file.write("jvjv")
# #  print(data)

# # except FileNotFoundError:
# #     print("sorry file mili nahi")

# # with open("report.txt", "w")as file:
# #     file.write("new data")

# # def total_sales(sales, index=0):

# #     if index == len(sales):
# #         return 0

# #     return sales[index] + total_sales(sales, index + 1)


# # sales = [12000, 18000, 25000, 15000]

# # print("Total Sales:", total_sales(sales))





# # products = ["Laptop", "Mouse", "Keyboard"]

# # sales = [120000, 45000, 38000]

# # total_sales = sum(sales)

# # average_sales = total_sales / len(sales)

# # highest_sales = max(sales)

# # with open("sales_report.txt","w") as file:
# #     file.write("SALES REPORT\n")
# #     file.write("----------------\n")
    
# #     file.write(f"Total sales: {total_sales}\n")
# #     file.write(f"Average Sales: {average_sales}\n")
# #     file.write(f"Highest Sales: {highest_sales}\n")
# #     file.write("\n Product Performance\n")

# #     for product, sale in zip(products, sales):
# #         file.write(f"{product} : {sale}\n")
        
# # print("report generated successfully")




# # def decimal_to_binary(n):
# #     if n ==0:
# #         return "0"
# #     elif n ==1:
# #         return "1"
    
# #     return decimal_to_binary(n//2) + str(n%2)

# # print(decimal_to_binary(10))



# # import random 

# # print("welcome to gun water snake game")
# # items = ["gun", "water", "snake"]
# # computer = random.choice(items)

# # user = input("Enter ur choice: ").lower()
# # print("computer choose: ",computer)

# # if user == computer:
# #     print("match draw")
# # elif user == "gun":
# #     if computer =="snake":
# #         print("user win")
# #     else:
# #         print("computer win")
        
# # elif user == "water":
# #     if computer == "gun":
# #         print("user win")
# #     else:
# #         print("computer win")

# # elif user == "snake":
# #     if computer == "water":
# #         print("user win")
# #     else:
# #         print("computer win")

# # else:
# #     print()



# # class Employee:
# #     #constructor
# #     def __init__(self, f_name, f_id):
# #         self.name = f_name
# #         self.id = f_id

    

# # employ1 = Employee("harish", 22)
# # print(employ1.name, employ1.id)

# # employ2 = Employee("anjali", 28)
# # print(employ2.name, employ2.id)

# # employ3 = Employee("arun", 28)
# # print(employ3.name, employ3.id)


# # class Carr:
# #     company = "PRMotors"
    
# #     def __init__(self, model):
# #         self.model = model
        
# # c1 = Carr("toyota")
# # print(c1.model,  Carr.company)

# # c2 = Carr("limousine")
# # print(c2.model,  Carr.company)

# # c3 = Carr("farrari")
# # print(c3.model,  Carr.company)


# # class Student:
# #     school = "ABC School"
    
# #     @classmethod
# #     def get_school(cls):
# #         return cls.school
# # print(Student.get_school())
    
    
    
    
# #     @staticmethod
# #     def convert(text):
# #         return text.lower()
    
# # print(Data.convert("HELLO AI"))


# # import json
# # import tkinter as tk
# # from pathlib import Path
# # from tkinter import messagebox, ttk


# # NOTES_FILE = Path(__file__).with_name("notes.json")


# # class NotesApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Notes App")
# #         self.root.geometry("750x500")

# #         self.notes = []
# #         self.selected_index = None

# #         self.load_notes()
# #         self.create_widgets()
# #         self.refresh_notes_list()

# #     def create_widgets(self):
# #         main_frame = ttk.Frame(self.root, padding=10)
# #         main_frame.pack(fill="both", expand=True)

# #         left_frame = ttk.Frame(main_frame)
# #         left_frame.pack(side="left", fill="y", padx=(0, 10))

# #         ttk.Label(left_frame, text="Saved Notes").pack(anchor="w")

# #         self.notes_list = tk.Listbox(left_frame, width=28, height=22)
# #         self.notes_list.pack(fill="y", expand=True)
# #         self.notes_list.bind("<<ListboxSelect>>", self.read_note)

# #         right_frame = ttk.Frame(main_frame)
# #         right_frame.pack(side="right", fill="both", expand=True)

# #         ttk.Label(right_frame, text="Title").pack(anchor="w")
# #         self.title_entry = ttk.Entry(right_frame)
# #         self.title_entry.pack(fill="x", pady=(0, 10))

# #         ttk.Label(right_frame, text="Note").pack(anchor="w")
# #         self.note_text = tk.Text(right_frame, height=15, wrap="word")
# #         self.note_text.pack(fill="both", expand=True)

# #         button_frame = ttk.Frame(right_frame)
# #         button_frame.pack(fill="x", pady=(10, 0))

# #         ttk.Button(button_frame, text="Add", command=self.add_note).pack(
# #             side="left", padx=3
# #         )
# #         ttk.Button(button_frame, text="Update", command=self.update_note).pack(
# #             side="left", padx=3
# #         )
# #         ttk.Button(button_frame, text="Remove", command=self.remove_note).pack(
# #             side="left", padx=3
# #         )
# #         ttk.Button(button_frame, text="Clear", command=self.clear_fields).pack(
# #             side="left", padx=3
# #         )

# #     def load_notes(self):
# #         try:
# #             if NOTES_FILE.exists():
# #                 with open(NOTES_FILE, "r", encoding="utf-8") as file:
# #                     self.notes = json.load(file)
# #         except (json.JSONDecodeError, OSError):
# #             self.notes = []

# #     def save_notes(self):
# #         with open(NOTES_FILE, "w", encoding="utf-8") as file:
# #             json.dump(self.notes, file, indent=4)

# #     def refresh_notes_list(self):
# #         self.notes_list.delete(0, tk.END)

# #         for note in self.notes:
# #             self.notes_list.insert(tk.END, note["title"])

# #     def add_note(self):
# #         title = self.title_entry.get().strip()
# #         content = self.note_text.get("1.0", tk.END).strip()

# #         if not title or not content:
# #             messagebox.showwarning("Missing Data", "Enter both title and note.")
# #             return

# #         self.notes.append({
# #             "title": title,
# #             "content": content
# #         })

# #         self.save_notes()
# #         self.refresh_notes_list()
# #         self.clear_fields()
# #         messagebox.showinfo("Success", "Note added successfully.")

# #     def read_note(self, event=None):
# #         selection = self.notes_list.curselection()

# #         if not selection:
# #             return

# #         self.selected_index = selection[0]
# #         note = self.notes[self.selected_index]

# #         self.title_entry.delete(0, tk.END)
# #         self.title_entry.insert(0, note["title"])

# #         self.note_text.delete("1.0", tk.END)
# #         self.note_text.insert("1.0", note["content"])

# #     def update_note(self):
# #         if self.selected_index is None:
# #             messagebox.showwarning("No Selection", "Select a note to update.")
# #             return

# #         title = self.title_entry.get().strip()
# #         content = self.note_text.get("1.0", tk.END).strip()

# #         if not title or not content:
# #             messagebox.showwarning("Missing Data", "Enter both title and note.")
# #             return

# #         self.notes[self.selected_index] = {
# #             "title": title,
# #             "content": content
# #         }

# #         self.save_notes()
# #         self.refresh_notes_list()
# #         self.clear_fields()
# #         messagebox.showinfo("Success", "Note updated successfully.")

# #     def remove_note(self):
# #         if self.selected_index is None:
# #             messagebox.showwarning("No Selection", "Select a note to remove.")
# #             return

# #         confirm = messagebox.askyesno(
# #             "Confirm Delete",
# #             "Are you sure you want to remove this note?"
# #         )

# #         if confirm:
# #             self.notes.pop(self.selected_index)
# #             self.save_notes()
# #             self.refresh_notes_list()
# #             self.clear_fields()
# #             messagebox.showinfo("Success", "Note removed successfully.")

# #     def clear_fields(self):
# #         self.title_entry.delete(0, tk.END)
# #         self.note_text.delete("1.0", tk.END)
# #         self.notes_list.selection_clear(0, tk.END)
# #         self.selected_index = None


# # root = tk.Tk()
# # app = NotesApp(root)
# # root.mainloop()


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt


# # -------------------------------------------------
# # PAGE CONFIGURATION
# # -------------------------------------------------

# st.set_page_config(
#     page_title="E-Commerce Analytics",
#     page_icon="🛒",
#     layout="wide"
# )


# # -------------------------------------------------
# # LOAD DATA
# # -------------------------------------------------

# df = pd.read_excel("ecommerce_200_orders.xlsx")

# df["OrderDate"] = pd.to_datetime(df["OrderDate"])


# # -------------------------------------------------
# # TITLE
# # -------------------------------------------------

# st.title("🛒 E-Commerce Sales & Profit Analytics")

# st.write(
#     "Interactive Data Analytics Dashboard built using "
#     "Python, Pandas and Streamlit"
# )


# # -------------------------------------------------
# # SIDEBAR FILTERS
# # -------------------------------------------------

# st.sidebar.header("🔎 Dashboard Filters")


# # Category Filter

# categories = ["All"] + sorted(df["Category"].unique().tolist())

# selected_category = st.sidebar.selectbox(
#     "Select Category",
#     categories
# )


# # State Filter

# states = ["All"] + sorted(df["State"].unique().tolist())

# selected_state = st.sidebar.selectbox(
#     "Select State",
#     states
# )


# # City Filter

# cities = ["All"] + sorted(df["City"].unique().tolist())

# selected_city = st.sidebar.selectbox(
#     "Select City",
#     cities
# )


# # Payment Mode Filter

# payments = ["All"] + sorted(df["PaymentMode"].unique().tolist())

# selected_payment = st.sidebar.selectbox(
#     "Payment Mode",
#     payments
# )


# # Return Filter

# returns = ["All"] + sorted(df["Returned"].unique().tolist())

# selected_return = st.sidebar.selectbox(
#     "Returned",
#     returns
# )


# # -------------------------------------------------
# # APPLY FILTERS
# # -------------------------------------------------

# filtered_df = df.copy()


# if selected_category != "All":
#     filtered_df = filtered_df[
#         filtered_df["Category"] == selected_category
#     ]


# if selected_state != "All":
#     filtered_df = filtered_df[
#         filtered_df["State"] == selected_state
#     ]


# if selected_city != "All":
#     filtered_df = filtered_df[
#         filtered_df["City"] == selected_city
#     ]


# if selected_payment != "All":
#     filtered_df = filtered_df[
#         filtered_df["PaymentMode"] == selected_payment
#     ]


# if selected_return != "All":
#     filtered_df = filtered_df[
#         filtered_df["Returned"] == selected_return
#     ]


# # -------------------------------------------------
# # KPI CALCULATIONS
# # -------------------------------------------------

# total_sales = filtered_df["Sales"].sum()

# total_profit = filtered_df["Profit"].sum()

# total_orders = filtered_df["OrderID"].nunique()

# total_quantity = filtered_df["Quantity"].sum()

# average_rating = filtered_df["Rating"].mean()


# # -------------------------------------------------
# # KPI DISPLAY
# # -------------------------------------------------

# col1, col2, col3, col4, col5 = st.columns(5)


# col1.metric(
#     "💰 Total Sales",
#     f"₹{total_sales:,.0f}"
# )


# col2.metric(
#     "📈 Total Profit",
#     f"₹{total_profit:,.0f}"
# )


# col3.metric(
#     "🛒 Total Orders",
#     total_orders
# )


# col4.metric(
#     "📦 Quantity Sold",
#     total_quantity
# )


# col5.metric(
#     "⭐ Avg Rating",
#     f"{average_rating:.2f}"
# )


# st.divider()


# # -------------------------------------------------
# # MONTHLY SALES TREND
# # -------------------------------------------------

# st.subheader("📈 Monthly Sales Trend")


# monthly_sales = (
#     filtered_df
#     .groupby(filtered_df["OrderDate"].dt.to_period("M"))["Sales"]
#     .sum()
# )

# monthly_sales.index = monthly_sales.index.astype(str)

# st.line_chart(monthly_sales)


# # -------------------------------------------------
# # CATEGORY ANALYSIS
# # -------------------------------------------------

# col1, col2 = st.columns(2)


# with col1:

#     st.subheader("📊 Sales by Category")

#     category_sales = (
#         filtered_df
#         .groupby("Category")["Sales"]
#         .sum()
#         .sort_values(ascending=False)
#     )

#     st.bar_chart(category_sales)


# with col2:

#     st.subheader("💰 Profit by Category")

#     category_profit = (
#         filtered_df
#         .groupby("Category")["Profit"]
#         .sum()
#         .sort_values(ascending=False)
#     )

#     st.bar_chart(category_profit)


# # -------------------------------------------------
# # CITY ANALYSIS
# # -------------------------------------------------

# st.subheader("🏙️ Top Cities by Sales")


# city_sales = (
#     filtered_df
#     .groupby("City")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# st.bar_chart(city_sales)


# # -------------------------------------------------
# # PAYMENT MODE ANALYSIS
# # -------------------------------------------------

# col1, col2 = st.columns(2)


# with col1:

#     st.subheader("💳 Sales by Payment Mode")

#     payment_sales = (
#         filtered_df
#         .groupby("PaymentMode")["Sales"]
#         .sum()
#         .sort_values(ascending=False)
#     )

#     st.bar_chart(payment_sales)


# with col2:

#     st.subheader("🔄 Returned vs Non-Returned Orders")

#     return_orders = (
#         filtered_df
#         .groupby("Returned")["OrderID"]
#         .count()
#     )

#     st.bar_chart(return_orders)


# # -------------------------------------------------
# # SALES VS PROFIT
# # -------------------------------------------------

# st.subheader("🎯 Sales vs Profit Analysis")


# scatter_data = filtered_df[["Sales", "Profit"]]

# st.scatter_chart(
#     scatter_data,
#     x="Sales",
#     y="Profit"
# )


# # -------------------------------------------------
# # TOP PRODUCTS
# # -------------------------------------------------

# st.subheader("🏆 Top 10 Products by Sales")


# top_products = (
#     filtered_df
#     .groupby("ProductName")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# st.bar_chart(top_products)


# # -------------------------------------------------
# # DATA TABLE
# # -------------------------------------------------

# st.subheader("📋 Filtered Orders")


# st.dataframe(
#     filtered_df,
#     use_container_width=True
# )


# # -------------------------------------------------
# # DOWNLOAD BUTTON
# # -------------------------------------------------

# csv = filtered_df.to_csv(index=False)

# st.download_button(
#     label="⬇️ Download Filtered Data",
#     data=csv,
#     file_name="filtered_ecommerce_data.csv",
#     mime="text/csv"
# )


# # -------------------------------------------------
# # BUSINESS INSIGHTS
# # -------------------------------------------------

# st.divider()

# st.subheader("💡 Business Insights")


# if len(filtered_df) > 0:

#     best_category = (
#         filtered_df
#         .groupby("Category")["Sales"]
#         .sum()
#         .idxmax()
#     )

#     best_city = (
#         filtered_df
#         .groupby("City")["Sales"]
#         .sum()
#         .idxmax()
#     )

#     best_product = (
#         filtered_df
#         .groupby("ProductName")["Sales"]
#         .sum()
#         .idxmax()
#     )

#     st.write(
#         f"🏆 Highest Sales Category: **{best_category}**"
#     )

#     st.write(
#         f"🏙️ Highest Sales City: **{best_city}**"
#     )

#     st.write(
#         f"📦 Top Product by Sales: **{best_product}**"
#     )

#     st.write(
#         f"💰 Total Revenue: **₹{total_sales:,.2f}**"
#     )

#     st.write(
#         f"📈 Total Profit: **₹{total_profit:,.2f}**"
#     )

# else:

#     st.warning(
#         "No data available for the selected filters."
#     )





# import streamlit as st
# import pandas as pd
# import plotly.express as px


# # -----------------------------
# # PAGE SETTINGS
# # -----------------------------

# st.set_page_config(
#     page_title="Sales Command Center",
#     page_icon="📊",
#     layout="wide"
# )


# # -----------------------------
# # TITLE
# # -----------------------------

# st.title("📊 Sales Command Center")
# st.caption("Interactive Data Analytics Dashboard using Python")


# # -----------------------------
# # FILE UPLOAD
# # -----------------------------

# file = st.file_uploader(
#     "📂 Upload your Excel / CSV file",
#     type=["xlsx", "csv"]
# )


# if file:

#     # Read file
#     if file.name.endswith(".csv"):
#         df = pd.read_csv(file)
#     else:
#         df = pd.read_excel(file)


#     st.success("File loaded successfully!")


#     # -----------------------------
#     # SIDEBAR FILTER
#     # -----------------------------

#     st.sidebar.header("🔎 Filters")


#     # Category filter
#     if "Category" in df.columns:

#         categories = st.sidebar.multiselect(
#             "Select Category",
#             df["Category"].dropna().unique(),
#             default=df["Category"].dropna().unique()
#         )

#         df = df[df["Category"].isin(categories)]


#     # -----------------------------
#     # KPIs
#     # -----------------------------

#     total_sales = df["Sales"].sum()

#     total_profit = df["Profit"].sum()

#     total_orders = len(df)

#     avg_sales = df["Sales"].mean()


#     col1, col2, col3, col4 = st.columns(4)


#     col1.metric(
#         "💰 Total Sales",
#         f"₹{total_sales:,.0f}"
#     )


#     col2.metric(
#         "📈 Total Profit",
#         f"₹{total_profit:,.0f}"
#     )


#     col3.metric(
#         "🛒 Total Orders",
#         f"{total_orders:,}"
#     )


#     col4.metric(
#         "💵 Avg Order Value",
#         f"₹{avg_sales:,.0f}"
#     )


#     st.divider()


#     # -----------------------------
#     # SALES BY CATEGORY
#     # -----------------------------

#     col1, col2 = st.columns(2)


#     with col1:

#         category_sales = (
#             df.groupby("Category")["Sales"]
#             .sum()
#             .reset_index()
#         )


#         fig = px.bar(
#             category_sales,
#             x="Category",
#             y="Sales",
#             title="Sales by Category",
#             text_auto=True
#         )


#         st.plotly_chart(
#             fig,
#             use_container_width=True
#         )


#     # -----------------------------
#     # PROFIT BY CATEGORY
#     # -----------------------------

#     with col2:

#         category_profit = (
#             df.groupby("Category")["Profit"]
#             .sum()
#             .reset_index()
#         )


#         fig = px.bar(
#             category_profit,
#             x="Category",
#             y="Profit",
#             title="Profit by Category",
#             text_auto=True
#         )


#         st.plotly_chart(
#             fig,
#             use_container_width=True
#         )


#     # -----------------------------
#     # TOP PRODUCTS
#     # -----------------------------

#     st.subheader("🏆 Top 10 Products")


#     top_products = (
#         df.groupby("ProductName")["Sales"]
#         .sum()
#         .sort_values(ascending=False)
#         .head(10)
#         .reset_index()
#     )


#     fig = px.bar(
#         top_products,
#         x="Sales",
#         y="ProductName",
#         orientation="h",
#         title="Top 10 Products by Sales",
#         text_auto=True
#     )


#     st.plotly_chart(
#         fig,
#         use_container_width=True
#     )


#     # -----------------------------
#     # DATA TABLE
#     # -----------------------------

#     st.subheader("📋 Sales Data")

#     st.dataframe(
#         df,
#         use_container_width=True
#     )


#     # -----------------------------
#     # DOWNLOAD
#     # -----------------------------

#     csv = df.to_csv(index=False)


#     st.download_button(
#         "⬇️ Download Filtered Data",
#         csv,
#         "filtered_sales.csv",
#         "text/csv"
#     )

# else:

#     st.info(
#         "👆 Upload an Excel or CSV file to start your analysis."
#     )





# # import streamlit as st

# # st.title("My new app😊")
# # st.write("hello welcome to data analytics course")
# # st.header("Sales Analysis")
# # st.subheader("Categories")
# # st.success("Congrats for submitting your form")

# # name = "Rahul"
# # st.write(name)

# # st.divider()
# # st.markdown("## E-comm dashboard😊😊  : $5677")
# # st.markdown("_E-comm dashboard_ : $5677")
# # st.warning("Keep track of profit")

# # st.info("Something imp")

# # name = st.text_input("Enter your name")
# # st.write("Hello, welcome to our website  ", name)

# # age = st.number_input("Enter your age ", min_value=12, max_value=100)
# # st.write("your age is: ", age)

# # age = st.slider("select age ", 1, 100, 25)
# # st.write("selected age ", age)

# # city = st.selectbox("select city", ["indore", "mumbai", "delhi", "pune"])
# # st.write("selected city: ", city)

# # gender = st.radio("select gender", ["male", "female","other"])
# # st.write("selected: ", gender)
# # st.metric("Total Sales", "$234555", "+12%")

# # col1, col2 = st.columns([2,1 ])

# # with col1:
# #     st.header("Sales")
    
# # with col2:
# #     st.metric("Profit", "$33222", "+33%")
    




# # sales = [123, 4556, 677, 6777]
# # total = 0

# # for sal in sales:
# #     total = total + sal
    
# # averge = total / len(sales)
# # print(averge)


# import cv2
# import numpy as np

# # Read image
# image = cv2.imread("priya.png")

# # Check image
# if image is None:
#     print("image not found")
#     exit()

# # Shape
# print("original shape: ")
# print(image.shape)
# # Resize
# resized = cv2.resize(image, (500, 500))
# cv2.imshow("Resized", resized)
# # Crop
# crop = image[100:400 , 100:400]
# cv2.imshow("crop", crop)

# # Flip 1 = horizontal, 0 = vertical , -1 = horizontal & vertical
# flip = cv2.flip(image, 1)
# cv2.imshow("flip", flip)

# # Brightness increase
# # alpha control scaling/contrast, alpha=1  (original)  ,
# # beta control brightness beta=50   Increase pixel brightness by 
# # approximately 50.  
# bright = cv2.convertScaleAbs(image, alpha=1, beta=50)
# cv2.imshow("bright", bright)
# # Brightness decrease

# dark = cv2.convertScaleAbs(image, alpha=1, beta=-50)
# cv2.imshow("dark", dark)

# # Black and White - converts the color image into a grayscale image.
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("black and white", gray)

# cv2.waitKey(0)

# # Without this, the image windows may open and immediately close 
# # when the program finishes.
# cv2.destroyAllWindows()
# #This closes all windows created by OpenCV.









# # arr = np.array([1, 2, 3, 4,5 ])
# # print(np.var(arr))
# # print(np.std(arr))
# # print(np.square(arr))
# # print(np.exp(arr))
# # data = np.array([3,4, np.nan, 7, np.nan])
# # print(np.isnan(data))
# # meanav = np.nanmean(data)

# # clean = np.where(np.isnan(data), meanav, data)
# # print(clean)
# # # import time
# # arr = np.arange(1, 10000000)
# # start = time.time()
# # sq = arr**2
# # end = time.time()
# # print(end-start)
# # b = np.array([12, 33, 0, 2, 44])
# # print(np.sort(b))

# # a = np.array([1, 3, 4])
# # b = np.array([12, 33, 44])
# # result = np.hstack((a, b))
# # print(result)
# # result = np.insert(a,1, 100 )
# # print(result)
# # # final = np.delete(a,3)
# # # print(final)


# # b = np.array([14, 4, 46])
# # # conc = np.concatenate((a, b))
# # print(conc)

# # arr = np.linspace(0, 10, 5)
# # print(arr)

# # arr = np.eye(3, 5)
# # print(arr)

# # arr2d = np.array([[1, 2,3],
# #                   [4, 5, 6]  
# # ])

# # print(arr2d.T)
# # arr =np.arange(6).reshape(2,3)
# # print(arr)
# # arr2d = np.array([[1, 2,3],
# #                   [4, 5, 6]  
# # ])
# # print(arr2d.shape)
# # arr1d = np.array([1, 2, 3, 5])
# # print(arr1d.shape)
# # arr3d = np.array([
# #   [[1, 2, 3], [4,5,6]],
# #   [[7, 8, 9], [55, 66, 77]]  
# # ])

# # # index [ 2d array, row, col]
# # print(arr3d[1, 0, 2])


# # arr = np.array([
# #     [ [1, 2.55, 3 ], [3, 5.333, 6], [4,8,9]],
# #     [[1.44, 4, 5], [6, 7.22, 8], [7, 8.1, 0]]
    
# # ])

# # floatarr = arr.astype(float)
# # print(type(floatarr))
# # print(arr)


# # marks = np.array(list(map(float, input("enter marks seperately by comma: ").split(","))))
# # print("marks: ", marks)
# # print("average marks: ", np.mean(marks))

# # sales = np.array([123, 4556, 677, 6777]) 
# # average = np.mean(sales)
# # print(average)
# # print(type(sales))








# import numpy as np

# # Student marks
# marks = np.array([
#     [85, 90, 78, 88, 95],
#     [76, 82, 91, 80, 79],
#     [92, 94, 89, 96, 91],
#     [65, 70, 72, 68, 74],
#     [88, 85, 90, 87, 89]
# ])

# print("Marks:")
# print(marks)

# # Total marks of each student - axis = 1 = row
# total = np.sum(marks, axis=1)
# print("\nTotal Marks:")
# print(total)

# # Percentage
# percentage = total / 5
# print("\nPercentage:")
# print(percentage)

# # Highest scorer
# highest = np.max(total)
# print("\nHighest Score:", highest)

# # Lowest scorer
# lowest = np.min(total)
# print("Lowest Score:", lowest)

# # Topper Roll Number
# topper_index = np.argmax(total)
# print("Topper Roll Number:", topper_index + 1)

# # Subject-wise average - axis = 0 column
# subject_average = np.mean(marks, axis=0)
# print("\nSubject-wise Average:")
# print(subject_average)

# # Overall average
# overall_average = np.mean(marks)
# print("\nOverall Average:", overall_average)

# # Pass/Fail
# passed = np.all(marks >= 40, axis=1)

# print("\nResult:")
# for i in range(len(marks)):
#     if passed[i]:
#         print("Roll No.", i + 1, "Pass")
#     else:
#         print("Roll No.", i + 1, "Fail")

# # Grade
# print("\nGrades:")

# for i in range(len(percentage)):

#     if percentage[i] >= 90:
#         grade = "A"
#     elif percentage[i] >= 75:
#         grade = "B"
#     elif percentage[i] >= 60:
#         grade = "C"
#     else:
#         grade = "D"

#     print("Roll No.", i + 1, "Grade:", grade)




# import pandas as pd

# # s = pd.Series([10, 17, 67, 89], index=["a", "b", "c", "d"])
# # print(s)

# # data = {"Maths":90, "Science":99}
# # s = pd.Series(data)
# # print(s.dtype)
# # print(s["Maths"])
# # print(s.max())



# # df = pd.DataFrame({
# #     "Name":["Amit", "Riya", "Aman"],
# #     "Age":[23, 78, 45]
# # })
# # print(df)

# df = pd.DataFrame([ [1, 2], [2, 3]], columns=["A", "B"])
# print(df)














# import pandas as pd
# import numpy as np

# # Load Dataset
# df = pd.read_csv("uber_rides.csv")

# print("="*60)
# print("UBER RIDE ANALYTICS PROJECT")
# print("="*60)

# # -------------------------------------------------
# # Basic Information
# # -------------------------------------------------

# print("\nDataset Shape:")
# print(df.shape)

# print("\nFirst 5 Records")
# print(df.head())

# # -------------------------------------------------
# # Average Fare
# # -------------------------------------------------

# average_fare = np.mean(df["Fare"])

# print("\nAverage Fare")
# print(round(average_fare,2))

# # -------------------------------------------------
# # Longest Ride
# # -------------------------------------------------

# print("\nLongest Ride")

# longest = df.loc[df["Distance"].idxmax()]

# print(longest)

# # -------------------------------------------------
# # Average Rating
# # -------------------------------------------------

# average_rating = np.mean(df["Rating"])

# print("\nAverage Rating")
# print(round(average_rating,2))

# # -------------------------------------------------
# # Payment Method Analysis
# # -------------------------------------------------

# print("\nPayment Method Count")

# print(df["Payment"].value_counts())

# # -------------------------------------------------
# # UPI vs Cash Revenue
# # -------------------------------------------------

# print("\nUPI vs Cash Revenue")

# print(df.groupby("Payment")["Fare"].sum())

# # -------------------------------------------------
# # City-wise Revenue
# # -------------------------------------------------

# print("\nCity-wise Revenue")

# city = df.groupby("City")["Fare"].sum()

# print(city)

# # -------------------------------------------------
# # Peak Fare Ride
# # -------------------------------------------------

# print("\nHighest Fare Ride")

# peak = df.loc[df["Fare"].idxmax()]

# print(peak)

# # -------------------------------------------------
# # Most Active Driver
# # -------------------------------------------------

# print("\nMost Active Driver")

# driver = df["Driver"].value_counts()

# print(driver)

# print("\nTop Driver")

# print(driver.idxmax())

# # -------------------------------------------------
# # Average Distance
# # -------------------------------------------------

# print("\nAverage Distance")

# print(round(df["Distance"].mean(),2),"KM")

# # -------------------------------------------------
# # Average Duration
# # -------------------------------------------------

# print("\nAverage Duration")

# print(round(df["Duration"].mean(),2),"Minutes")

# # -------------------------------------------------
# # Highest Rated Ride
# # -------------------------------------------------

# print("\nHighest Rated Ride")

# print(df.loc[df["Rating"].idxmax()])

# # -------------------------------------------------
# # Create Revenue Column
# # -------------------------------------------------

# df["Revenue"] = df["Fare"]

# # -------------------------------------------------
# # Revenue Report
# # -------------------------------------------------

# print("\nRevenue Report")

# print("Total Revenue :",df["Revenue"].sum())

# print("Average Revenue :",round(df["Revenue"].mean(),2))

# print("Maximum Revenue :",df["Revenue"].max())

# print("Minimum Revenue :",df["Revenue"].min())

# # -------------------------------------------------
# # Top 5 Expensive Rides
# # -------------------------------------------------

# print("\nTop 5 Expensive Rides")

# print(df.sort_values("Fare",ascending=False).head())

# # -------------------------------------------------
# # Save Updated Dataset
# # -------------------------------------------------

# df.to_csv("uber_report.csv",index=False)

# print("\nReport Saved Successfully")




# df = pd.read_csv("employee.csv")
# df["Salary"] = df["Salary"].round(0).astype(int)

# data ={
#     "Cities":["Delhi", None, "Mumbai", "Mumbai", "Pune", "Pune"],
#     "Product":["Laptop", "Mobile","Laptop", "Mobile","Laptop", "Mobile" ],
#     "Sales":[34555, 678888, 8976666, None, 45666, 765555],
#     "Quantity": [5, 10, 5, 7, 4, 8]
# }
# # city wise calculate total sales per city

# df = pd.DataFrame(data)
# newdata= pd.DataFrame({
#     "Manager":["Amit", "Riya","Rahul"]
    
    
# }, index=["Delhi", "Mumbai", "Pune"])

# print(df.join(newdata, on="Cities"))
# # print(df.groupby(["Cities","Product"])["Sales"].sum())
# # print(df.groupby("Cities")["Sales"].sum().idxmax())
# # print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False))
# print(df.fillna(0))


# df["Age"] = df["Age"].clip(25, 32)
# df["Name"] = df["Name"].replace("Amit", "Amit S")
# df["JoinDate"] = pd.to_datetime(df["JoinDate"])
# df["salary_normalized"] = df["Salary"] / df["Salary"].max()
# df["Highestsalary"] = np.where(df["Salary"] >= 65000, "Yes", "No") 
# df["Salary"] = df["Salary"] * 1.10
# df["Department"] = df["Department"].map({
#     "IT":"Javascript Dev",
#     "HR": "Sales",
#     "Sales":"BO",
#     "Marketing":"Admin",
#     "Finance": "Bussiness"
# })
# df["AgeGroup"] = df["Age"].apply(lambda x:"Young" if x < 30 else "Senior")

# print(df.iloc[0:4, [0,2]])





# result = df.loc[(df["Salary"]>=55000) & (df["Salary"]<=75000),
#        ["Name", "Salary","Department"]]
# print(result)
# print(df.loc[0:2, ["Name", "Age"]])

# print(df["Department"].value_counts())
# df.replace(" ",pd.NA, inplace=True)
# print(df)
# print(df.duplicated().sum())
# df.columns =df.columns.str.strip()
# print(df)
# print(df.describe())
# print(df.isnull().sum())
# print(df["Department"].value_counts())
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# QUICKKART SMART DELIVERY & CUSTOMER EXPERIENCE DASHBOARD
# Run with: streamlit run quickkart_streamlit_project.py
# ------------------------------------------------------------

st.set_page_config(
    page_title="QuickKart Analytics Dashboard",
    page_icon="📦",
    layout="wide"
)

# ------------------------- LOAD DATA -------------------------
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    return df

st.title("📦 QuickKart Smart Delivery Analytics")
st.caption("Data Analytics Project using NumPy + Pandas + Matplotlib + Streamlit")

uploaded_file = st.sidebar.file_uploader("Upload QuickKart CSV", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
else:
    try:
        df = load_data("quickkart_delivery_dataset.csv")
        st.info("Using default dataset: quickkart_delivery_dataset.csv")
    except FileNotFoundError:
        st.error("Dataset not found. Upload the CSV file from the sidebar.")
        st.stop()

# ------------------------- CLEAN DATA ------------------------
df = df.drop_duplicates().copy()

numeric_cols = [
    "Quantity", "Unit_Price", "Order_Value", "Discount_Pct",
    "Discount_Amount", "Final_Amount", "Distance_KM",
    "Promised_Time_Min", "Actual_Delivery_Time_Min",
    "Customer_Rating", "Support_Tickets"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["Order_ID", "Order_Date", "City", "Category"])

# ----------------------- DERIVED COLUMNS ---------------------
# NumPy: delivery delay
df["Delay_Min"] = np.where(
    df["Order_Status"].eq("Delivered"),
    df["Actual_Delivery_Time_Min"] - df["Promised_Time_Min"],
    np.nan
)

# NumPy: delivery performance label
conditions = [
    df["Delay_Min"] <= 0,
    (df["Delay_Min"] > 0) & (df["Delay_Min"] <= 10),
    df["Delay_Min"] > 10
]
choices = ["On Time", "Slightly Late", "Very Late"]
df["Delivery_Performance"] = np.select(conditions, choices, default="Not Applicable")

# NumPy: high value order threshold using 75th percentile
high_value_threshold = np.nanpercentile(df["Final_Amount"], 75)
df["High_Value_Order"] = np.where(
    df["Final_Amount"] >= high_value_threshold, "Yes", "No"
)

# NumPy: z-score based revenue outlier flag
amount_mean = np.nanmean(df["Final_Amount"])
amount_std = np.nanstd(df["Final_Amount"])
if amount_std == 0:
    df["Amount_ZScore"] = 0
else:
    df["Amount_ZScore"] = (df["Final_Amount"] - amount_mean) / amount_std

df["Revenue_Outlier"] = np.where(np.abs(df["Amount_ZScore"]) > 2, "Yes", "No")

# Smart satisfaction score (0-100)
rating_score = np.where(df["Customer_Rating"] > 0, df["Customer_Rating"] * 15, 0)
delivery_score = np.where(
    df["Delivery_Performance"].eq("On Time"), 25,
    np.where(df["Delivery_Performance"].eq("Slightly Late"), 15,
             np.where(df["Delivery_Performance"].eq("Very Late"), 5, 0))
)
support_penalty = np.minimum(df["Support_Tickets"] * 5, 20)
df["Experience_Score"] = np.clip(rating_score + delivery_score - support_penalty, 0, 100)

# ------------------------- SIDEBAR ---------------------------
st.sidebar.header("🔎 Dashboard Filters")

cities = sorted(df["City"].dropna().unique().tolist())
categories = sorted(df["Category"].dropna().unique().tolist())
statuses = sorted(df["Order_Status"].dropna().unique().tolist())
customer_types = sorted(df["Customer_Type"].dropna().unique().tolist())

selected_cities = st.sidebar.multiselect("City", cities, default=cities)
selected_categories = st.sidebar.multiselect("Category", categories, default=categories)
selected_statuses = st.sidebar.multiselect("Order Status", statuses, default=statuses)
selected_customer_types = st.sidebar.multiselect(
    "Customer Type", customer_types, default=customer_types
)

min_date = df["Order_Date"].min().date()
max_date = df["Order_Date"].max().date()

date_range = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

filtered = df[
    df["City"].isin(selected_cities)
    & df["Category"].isin(selected_categories)
    & df["Order_Status"].isin(selected_statuses)
    & df["Customer_Type"].isin(selected_customer_types)
].copy()

if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
    filtered = filtered[
        (filtered["Order_Date"] >= start_date)
        & (filtered["Order_Date"] <= end_date)
    ]

if filtered.empty:
    st.warning("No records found for the selected filters.")
    st.stop()

# --------------------------- KPIs ----------------------------
delivered = filtered[filtered["Order_Status"] == "Delivered"].copy()
revenue_df = filtered[filtered["Order_Status"] != "Cancelled"].copy()

total_orders = len(filtered)
total_revenue = revenue_df["Final_Amount"].sum()
avg_order_value = revenue_df["Final_Amount"].mean()
delivered_count = len(delivered)
late_rate = (
    (delivered["Late_Delivery"] == "Yes").mean() * 100
    if delivered_count > 0 else 0
)
cancel_rate = (filtered["Order_Status"] == "Cancelled").mean() * 100
valid_ratings = filtered.loc[filtered["Customer_Rating"] > 0, "Customer_Rating"]
avg_rating = valid_ratings.mean() if not valid_ratings.empty else 0

st.subheader("📌 Business KPI Summary")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Orders", f"{total_orders:,}")
c2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
c3.metric("Avg. Order Value", f"₹{avg_order_value:,.0f}")
c4.metric("Avg. Rating", f"{avg_rating:.2f} ⭐")

c5, c6, c7, c8 = st.columns(4)
c5.metric("Delivered Orders", f"{delivered_count:,}")
c6.metric("Late Delivery Rate", f"{late_rate:.1f}%")
c7.metric("Cancellation Rate", f"{cancel_rate:.1f}%")
c8.metric("75th % High-Value Cutoff", f"₹{high_value_threshold:,.0f}")

# ---------------------------- TABS ---------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Revenue",
    "🚚 Delivery",
    "⭐ Customer",
    "🧠 Smart Insights",
    "📄 Data & Export"
])

# ======================= TAB 1: REVENUE ======================
with tab1:
    st.subheader("Revenue & Sales Performance")

    city_revenue = (
        revenue_df.groupby("City")["Final_Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    category_revenue = (
        revenue_df.groupby("Category")["Final_Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(7, 4))
        city_revenue.plot(kind="bar", ax=ax)
        ax.set_title("City-wise Revenue")
        ax.set_xlabel("City")
        ax.set_ylabel("Revenue (₹)")
        ax.tick_params(axis="x", rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(7, 4))
        category_revenue.plot(kind="barh", ax=ax)
        ax.set_title("Category-wise Revenue")
        ax.set_xlabel("Revenue (₹)")
        ax.set_ylabel("Category")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    daily_revenue = (
        revenue_df.set_index("Order_Date")
        .resample("W")["Final_Amount"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(11, 4))
    ax.plot(daily_revenue.index, daily_revenue.values, marker="o")
    ax.set_title("Weekly Revenue Trend")
    ax.set_xlabel("Week")
    ax.set_ylabel("Revenue (₹)")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    payment_share = revenue_df["Payment_Mode"].value_counts()
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.pie(payment_share.values, labels=payment_share.index, autopct="%1.1f%%")
    ax.set_title("Payment Mode Distribution")
    st.pyplot(fig)
    plt.close(fig)

# ====================== TAB 2: DELIVERY ======================
with tab2:
    st.subheader("Delivery Operations Analysis")

    partner_summary = (
        delivered.groupby("Delivery_Partner")
        .agg(
            Orders=("Order_ID", "count"),
            Avg_Delivery_Time=("Actual_Delivery_Time_Min", "mean"),
            Avg_Delay=("Delay_Min", "mean"),
            Avg_Rating=("Customer_Rating", "mean")
        )
        .round(2)
        .sort_values("Avg_Delay")
    )

    st.dataframe(partner_summary, use_container_width=True)

    late_by_city = (
        delivered.assign(
            Late_Flag=np.where(delivered["Late_Delivery"] == "Yes", 1, 0)
        )
        .groupby("City")["Late_Flag"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    late_by_city.plot(kind="bar", ax=ax)
    ax.set_title("Late Delivery Rate by City")
    ax.set_xlabel("City")
    ax.set_ylabel("Late Delivery %")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    if not delivered.empty:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.scatter(
            delivered["Distance_KM"],
            delivered["Actual_Delivery_Time_Min"],
            alpha=0.6
        )
        ax.set_title("Distance vs Actual Delivery Time")
        ax.set_xlabel("Distance (KM)")
        ax.set_ylabel("Actual Delivery Time (Min)")
        ax.grid(alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

# ====================== TAB 3: CUSTOMER ======================
with tab3:
    st.subheader("Customer Experience Analysis")

    customer_summary = (
        filtered.groupby("Customer_Type")
        .agg(
            Orders=("Order_ID", "count"),
            Revenue=("Final_Amount", "sum"),
            Avg_Rating=("Customer_Rating", lambda x: x[x > 0].mean()),
            Avg_Experience_Score=("Experience_Score", "mean"),
            Support_Tickets=("Support_Tickets", "sum")
        )
        .round(2)
    )

    st.dataframe(customer_summary, use_container_width=True)

    rating_counts = (
        filtered[filtered["Customer_Rating"] > 0]["Customer_Rating"]
        .value_counts()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(rating_counts.index.astype(str), rating_counts.values)
    ax.set_title("Customer Rating Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Orders")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    category_exp = (
        filtered.groupby("Category")["Experience_Score"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    category_exp.plot(kind="bar", ax=ax)
    ax.set_title("Average Experience Score by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Experience Score")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ==================== TAB 4: SMART INSIGHTS ==================
with tab4:
    st.subheader("🧠 Smart Business Insights")

    top_city = city_revenue.index[0]
    top_city_revenue = city_revenue.iloc[0]
    top_category = category_revenue.index[0]
    top_category_revenue = category_revenue.iloc[0]

    worst_late_city = late_by_city.index[0] if not late_by_city.empty else "N/A"
    worst_late_rate = late_by_city.iloc[0] if not late_by_city.empty else 0

    best_partner = partner_summary.index[0] if not partner_summary.empty else "N/A"

    high_value_orders = filtered[filtered["High_Value_Order"] == "Yes"]
    outlier_orders = filtered[filtered["Revenue_Outlier"] == "Yes"]

    insight1, insight2 = st.columns(2)

    with insight1:
        st.success(
            f"🏆 Top Revenue City: {top_city} "
            f"(₹{top_city_revenue:,.0f})"
        )
        st.info(
            f"🛍️ Top Category: {top_category} "
            f"(₹{top_category_revenue:,.0f})"
        )
        st.warning(
            f"🚚 Highest Late Delivery City: {worst_late_city} "
            f"({worst_late_rate:.1f}%)"
        )

    with insight2:
        st.success(f"⚡ Best Delivery Partner by Avg. Delay: {best_partner}")
        st.info(f"💎 High-Value Orders: {len(high_value_orders)}")
        st.warning(f"🔍 Revenue Outlier Orders: {len(outlier_orders)}")

    # Rule-based action recommendations
    st.markdown("### Recommended Business Actions")

    recommendations = []

    if cancel_rate > 8:
        recommendations.append(
            "Cancellation rate is high. Review stock availability, payment failures and fulfilment issues."
        )
    else:
        recommendations.append(
            "Cancellation rate is under control. Continue monitoring category-wise cancellations."
        )

    if late_rate > 25:
        recommendations.append(
            f"Late deliveries are high. Focus operational improvement in {worst_late_city} first."
        )
    else:
        recommendations.append(
            "Delivery punctuality is acceptable, but partner-level monitoring should continue."
        )

    if avg_rating < 3.8:
        recommendations.append(
            "Customer rating needs improvement. Investigate delayed orders and support-ticket-heavy cases."
        )
    else:
        recommendations.append(
            "Customer satisfaction is healthy. Protect service quality for premium and returning customers."
        )

    for rec in recommendations:
        st.write("•", rec)

    st.markdown("### High-Value / Outlier Orders")
    st.dataframe(
        filtered.loc[
            (filtered["High_Value_Order"] == "Yes")
            | (filtered["Revenue_Outlier"] == "Yes"),
            [
                "Order_ID", "City", "Category", "Final_Amount",
                "High_Value_Order", "Revenue_Outlier",
                "Order_Status", "Customer_Rating"
            ]
        ].sort_values("Final_Amount", ascending=False),
        use_container_width=True
    )

# ===================== TAB 5: EXPORT DATA ====================
with tab5:
    st.subheader("Filtered Data Preview")
    st.dataframe(filtered, use_container_width=True)

    csv_data = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Filtered Report",
        data=csv_data,
        file_name="quickkart_filtered_report.csv",
        mime="text/csv"
    )

    st.markdown("### Data Quality Check")
    quality_df = pd.DataFrame({
        "Column": filtered.columns,
        "Missing_Values": filtered.isnull().sum().values,
        "Unique_Values": [filtered[col].nunique(dropna=True) for col in filtered.columns]
    })
    st.dataframe(quality_df, use_container_width=True)

# -------------------------- FOOTER ---------------------------
st.markdown("---")
st.caption("QuickKart Data Analytics Assignment | NumPy + Pandas + Matplotlib + Streamlit")
