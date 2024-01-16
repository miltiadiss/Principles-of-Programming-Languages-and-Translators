import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import mysql.connector

root = tk.Tk()
root.title("Python Project")
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Set the window border thickness
root.configure(borderwidth=5)
root.configure(highlightbackground="#333333", highlightcolor="#333333")

# Set the window title font and size
title_font = ("Helvetica", 13, "bold")
root.option_add("*Font", title_font)
root.option_add("*foreground", "#333333")
bold_font = font.Font(family="Arial", size=12, weight="bold")

img = Image.open(r'C:\Users\user\PycharmProjects\pythonProject1\logo.png')
img = img.resize((300, 110))
logo = ImageTk.PhotoImage(img)

text_root = tk.Label(root, text="Εργαστηριακή Άσκηση στην Python\n  Εαρινό Εξάμηνο 2023\n\nΕπεξεργασία Δεδομένων από Αρχείο CSV")
text_root.configure(font=bold_font, foreground="black", background="#f0f0f0")
text_root.pack(padx=10, pady=15)
image_label = tk.Label(root, image=logo)
image_label.pack(padx=15, pady=15)

button_font = font.Font(family="Helvetica", size=12, weight="bold")
button_style = {
    'foreground': '#ffffff',
    'background': '#20bebe',
    'activeforeground': '#ffffff',
    'activebackground': '#45a049',
    'font': button_font,
    'borderwidth': 2,
    'highlightthickness': 2,
    'relief': 'flat',
}

style = ttk.Style()
style.configure("Custom.TFrame", background="#e6e6e6")
frame = ttk.Frame(root, style="Custom.TFrame")
frame.pack(fill=tk.BOTH, expand=True)

mydb = mysql.connector.connect(host="localhost", user="root", passwd="ju59GSX4yn", database="project")
cursor = mydb.cursor()

url = 'https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv'
data = pd.read_csv(url)

def graph_1():
    # Μετατρέπουμε το αλφαριθμητικό που αντιπροσωπεύει την ημερομηνία στη μορφή datetime
    # με format=mixed γιατί δεν είναι της μορφής day-month-year
    data['Date'] = pd.to_datetime(data['Date'], format='mixed')

    # Ομαδοποιούμε τα δεδομένα βάσει μήνα και υπολογίζουμε το τζίρο για κάθε μήνα και measure
    grouped = data.groupby(['Measure', data['Date'].dt.month])['Value'].sum().reset_index()

    # Βρίσκουμε τις διακριτές τιμές του measure
    unique_measures = grouped['Measure'].unique()

    # Διαβάζουμε τα δεδομένα για κάθε διαφορετική τιμή του measure
    for measure in unique_measures:
        # Ομαδοποιούμε τα δεδομένα για κάθε διαφορετική τιμή του measure
        measure_data = grouped[grouped['Measure'] == measure]

        for index, row in measure_data.iterrows():
            month = row['Date']
            value = row['Value']
            cursor.execute("INSERT INTO profit_per_month (Profit, Month, Measure) VALUES (%s, %s, %s)",
                           (value, month, measure))

        # Εισάγουμε τις αλλαγές που πραγματοποιήσαμε στον cursor τη ΒΔ
        mydb.commit()

        # Σχεδιάζουμε τη γραφική παράσταση
        plt.figure(figsize=(10, 6))
        plt.bar(measure_data['Date'], measure_data['Value'])
        plt.title(f"Profit per Month ({measure})")
        plt.xlabel("Months")
        plt.ylabel("Profits")
        plt.xticks(measure_data['Date'])
        plt.tight_layout()
        plt.show()

def graph_2():
    grouped = data.groupby(['Country', 'Measure'])['Value'].sum().reset_index()
    unique_measures = grouped['Measure'].unique()

    for measure in unique_measures:
        measure_data = grouped[grouped['Measure'] == measure]

        for index, row in measure_data.iterrows():
            country = row['Country']
            value = row['Value']
            cursor.execute("INSERT INTO profit_per_country (Profit, Country, Measure) VALUES (%s, %s, %s)",
                           (value, country, measure))

        # Commit the changes and close the connection
        mydb.commit()

        # Plot the sum of values for each month for the current measure
        plt.figure(figsize=(10, 6))
        plt.bar(measure_data['Country'], measure_data['Value'])
        plt.title(f"Profit per Country ({measure})")
        plt.xlabel("Countries")
        plt.ylabel("Profits")
        plt.xticks(measure_data['Country'], rotation=45)
        plt.tight_layout()
        plt.show()

def graph_3():
    grouped = data.groupby(['Transport_Mode', 'Measure'])['Value'].sum().reset_index()
    unique_measures = grouped['Measure'].unique()

    for measure in unique_measures:
        measure_data = grouped[grouped['Measure'] == measure]

        for index, row in measure_data.iterrows():
            transport_mean = row['Transport_Mode']
            value = row['Value']
            cursor.execute(
                "INSERT INTO profit_per_transport_mean (Profit, Transport_Mean, Measure) VALUES (%s, %s, %s)",
                (value, transport_mean, measure))

        # Commit the changes and close the connection
        mydb.commit()

        # Plot the sum of values for each month for the current measure
        plt.figure(figsize=(10, 6))
        plt.bar(measure_data['Transport_Mode'], measure_data['Value'])
        plt.title(f"Profit per Transportation Mode ({measure})")
        plt.xlabel("Transportation Means")
        plt.ylabel("Profits")
        plt.xticks(measure_data['Transport_Mode'], rotation=45)
        plt.tight_layout()
        plt.show()

def graph_4():
    grouped = data.groupby(['Weekday', 'Measure'])['Value'].sum().reset_index()
    unique_measures = grouped['Measure'].unique()

    for measure in unique_measures:
        measure_data = grouped[grouped['Measure'] == measure]

        for index, row in measure_data.iterrows():
            weekday = row['Weekday']
            value = row['Value']
            cursor.execute("INSERT INTO profit_per_weekday (Profit, Weekday, Measure) VALUES (%s, %s, %s)",
                           (value, weekday, measure))

            # Commit the changes and close the connection
        mydb.commit()

        # Plot the sum of values for each month for the current measure
        plt.figure(figsize=(10, 6))
        plt.bar(measure_data['Weekday'], measure_data['Value'])
        plt.title(f"Profit per Weekday ({measure})")
        plt.xlabel("Weekdays")
        plt.ylabel("Profits")
        plt.xticks(measure_data['Weekday'], rotation=45)
        plt.tight_layout()
        plt.show()

def graph_5():
    grouped = data.groupby(['Commodity', 'Measure'])['Value'].sum().reset_index()
    unique_measures = grouped['Measure'].unique()

    for measure in unique_measures:
        measure_data = grouped[grouped['Measure'] == measure]

        for index, row in measure_data.iterrows():
            commodity = row['Commodity']
            value = row['Value']
            cursor.execute("INSERT INTO profit_per_commodity (Profit, Commodity, Measure) VALUES (%s, %s, %s)",
                           (value, commodity, measure))

            # Commit the changes and close the connection
        mydb.commit()

        # Plot the sum of values for each month for the current measure
        plt.figure(figsize=(10, 6))
        plt.bar(measure_data['Commodity'], measure_data['Value'])
        plt.title(f"Profit per Commodity ({measure})")
        plt.xlabel("Commodities")
        plt.ylabel("Profits")
        plt.xticks(measure_data['Commodity'], rotation=45)
        plt.tight_layout()
        plt.show()

def graph_6():
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'], format='mixed')
    grouped = data.groupby(['Measure', data['Date'].dt.month])['Value'].sum().reset_index()

    unique_measures = grouped['Measure'].unique()

    for measure in unique_measures:
        measure_data = grouped[grouped['Measure'] == measure]

        # Find the top 5 months for each measure
        top_5_months = (
        measure_data.groupby('Measure')
        .apply(lambda x: x.reset_index(drop=True).nlargest(5, 'Value'))
        .reset_index(drop=True)
        )

        for _, row in top_5_months.iterrows():
            query = 'INSERT INTO top_5_months (Month, Profit, Measure) VALUES (%s, %s, %s)'
            cursor.execute(query, (row['Date'], row['Value'], measure))
        # Commit the changes and close the connection
        mydb.commit()

        # Create a plot for the current value of the Measure column
        plt.figure(figsize=(10, 6))
        for _, data in top_5_months.iterrows():
            plt.bar(data['Date'], data['Value'])

        plt.title(f"Top 5 Months with the Biggest Profit ({measure})")
        plt.xlabel("Months")
        plt.ylabel("Profits")
        plt.xticks(measure_data['Date'])
        plt.tight_layout()
    plt.show()

def graph_7():
    data = pd.read_csv(url)
    grouped = data.groupby(['Measure', 'Country', 'Commodity'])['Value'].sum().reset_index()

    unique_measures = grouped['Measure'].unique()

    for measure in unique_measures:
        measure_data = grouped[grouped['Measure'] == measure]

        # Find the top 5 commodities with the largest sum per country for each measure
        top_5_commodities = (
            measure_data.groupby(['Measure', 'Country'])
            .apply(lambda x: x.nlargest(5, 'Value'))
            .reset_index(drop=True)
        )

        for _, row in top_5_commodities.iterrows():
            query = 'INSERT INTO top_5_commodities (Country, Commodity, Profit, Measure) VALUES (%s, %s, %s, %s)'
            cursor.execute(query, (row['Country'], row['Commodity'], row['Value'], measure))
        # Commit the changes and close the connection
        mydb.commit()

        # Create a plot for the current value of the Measure column
        plt.figure(figsize=(10, 6))
        for country, data in top_5_commodities.groupby('Country'):
            plt.scatter(data['Commodity'], data['Value'], marker='o', label=f"{country}")

        plt.title(f"Top 5 Commodities with the Biggest Profit per Country ({measure})")
        plt.xlabel("Commodities")
        plt.ylabel("Profits")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
    plt.show()

def graph_8():
    data = pd.read_csv(url)
    grouped = data.groupby(['Measure', 'Commodity', 'Date'])['Value'].sum().reset_index()

    # Find the unique values in the Measure column
    unique_measures = grouped['Measure'].unique()

    # Create separate plots for each value in the Measure column
    for measure in unique_measures:
        # Filter the data for the specific value of the Measure column
        measure_data = grouped[grouped['Measure'] == measure]

        # Find the day with the biggest sum of values for each commodity
        max_days = measure_data.groupby('Commodity')['Value'].idxmax()
        max_days_data = measure_data.loc[max_days]

        for _, row in max_days_data.iterrows():
            query = 'INSERT INTO days_with_biggest_profit (Commodity, Weekday, Profit, Measure) VALUES (%s, %s, %s, %s)'
            cursor.execute(query, (row['Commodity'], row['Date'], row['Value'], measure))
        mydb.commit()

        # Create a plot for the current value of the Measure column
        plt.figure(figsize=(10, 6))
        for commodity, data in max_days_data.groupby('Commodity'):
            plt.plot(data['Date'], data['Value'], marker='o', label=f"{commodity}")

        plt.title(f"Days with the Biggest Profit per Commodity ({measure})")
        plt.xlabel("Days")
        plt.ylabel("Profits")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
    plt.show()

def export_csv():
    query = "SELECT * FROM profit_per_month"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('profits_per_month.csv', index=FALSE)

    query = "SELECT * FROM profit_per_country"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('profits_per_country.csv', index=FALSE)

    query = "SELECT * FROM profit_per_transport_mean"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('profits_per_transport_mode.csv', index=FALSE)

    query = "SELECT * FROM profit_per_weekday"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('profits_per_weekday.csv', index=FALSE)

    query = "SELECT * FROM profit_per_commodity"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('profits_per_commodity.csv', index=FALSE)

    query = "SELECT * FROM top_5_months"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('top_5_months.csv', index=FALSE)

    query = "SELECT * FROM top_5_commodities"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('top_5_commodities.csv', index=FALSE)

    query = "SELECT * FROM days_with_biggest_profit"
    cursor.execute(query)
    res = cursor.fetchall()

    for row in res:
        new_data = pd.read_sql_query(query, mydb)
        new_data.to_csv('days_with_biggest_profit.csv', index=FALSE)

def popup():
    win = Toplevel(root)
    win.title("Graphs")
    win.geometry("1050x1050")

    text = Label(win, text="Graphs")
    button1 = Button(win, text="Profits per Month ($ and Tonnes)", command=lambda: graph_1(), font="Raleway",
                     bg="#20bebe", fg="white", bd=0, relief="sunken", activebackground="#1b1b1b", height=2, width=60)
    button2 = Button(win, text="Profits per Country ($ and Tonnes)", command=lambda: graph_2(), font="Raleway",
                     bg="#20bebe", fg="white", height=2, width=60)
    button3 = Button(win, text="Profits per Transport Mode ($ and Tonnes)", command=lambda: graph_3(), font="Raleway",
                     bg="#20bebe", fg="white", height=2, width=60)
    button4 = Button(win, text="Profits per Weekday ($ and Tonnes)", command=lambda: graph_4(), font="Raleway",
                     bg="#20bebe", fg="white", height=2, width=60)
    button5 = Button(win, text="Profits per Commodity ($ and Tonnes)", command=lambda: graph_5(), font="Raleway",
                     bg="#20bebe", fg="white", height=2, width=60)
    button6 = Button(win, text="Top 5 Months with Biggest Profit ($ and Tonnes)", command=lambda: graph_6(),
                     font="Raleway", bg="#20bebe", fg="white", height=2, width=60)
    button7 = Button(win, text="Top 5 Commodities with Biggest Profit per Country ($ and Tonnes)",
                     command=lambda: graph_7(), font="Raleway", bg="#20bebe", fg="white", height=2, width=60)
    button8 = Button(win, text="Weekday with Biggest Profit per Commodity ($ and Tonnes)", command=lambda: graph_8(),
                     font="Raleway", bg="#20bebe", fg="white", height=2, width=60)
    button9 = Button(win, text="Export Data into CSV Files", command=lambda: export_csv(), font="Raleway", bg="#20bebe",
                     fg="white", height=2, width=60)
    close_button = Button(win, text="Close", command=lambda: win.destroy(), height=1, width=8)

    text.pack(padx=0, pady=0)
    button1.configure(**button_style)
    button1.pack(padx=4, pady=4)
    button2.configure(**button_style)
    button2.pack(padx=4, pady=5)
    button3.configure(**button_style)
    button3.pack(padx=4, pady=6)
    button4.configure(**button_style)
    button4.pack(padx=4, pady=7)
    button5.configure(**button_style)
    button5.pack(padx=4, pady=8)
    button6.configure(**button_style)
    button6.pack(padx=5, pady=4)
    button7.configure(**button_style)
    button7.pack(padx=5, pady=5)
    button8.configure(**button_style)
    button8.pack(padx=5, pady=6)
    button9.configure(**button_style)
    button9.pack(padx=5, pady=7)
    close_button.pack(padx=5, pady=8)

    win.mainloop()

button = Button(root, text="Show Graphs", command=lambda: popup(), font="Raleway", bg="#20bebe", fg="white", height=2,
                width=10)
button.configure(**button_style)
button.pack(padx=10, pady=10)
exit_button = Button(root, text="Exit", command=lambda: root.destroy(), height=1, width=4)
exit_button.pack(padx=10, pady=15)

root.mainloop()
