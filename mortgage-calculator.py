import tkinter as tk


# Define a function to calculate the monthly repayment amount
def calculate_repayment():
    house_price = float(house_price_entry.get())
    downpayment = float(downpayment_entry.get())
    principal = house_price - downpayment
    interest_rate = float(interest_entry.get()) / 100 / 12
    loan_tenure = int(loan_tenure_entry.get()) * 12

    monthly_repayment = (principal * interest_rate * ((1 + interest_rate) ** loan_tenure)) / (
                ((1 + interest_rate) ** loan_tenure) - 1)

    result_label.config(text="Monthly repayment amount: ${:.2f}".format(monthly_repayment))


# Create a Tkinter window
window = tk.Tk()
window.geometry("1200x500")
window.title("HDB Mortgage Calculator")

# Create input fields and labels for house price, downpayment, interest rate, and loan tenure
house_price_label = tk.Label(window, text="House price:", fg="#801638", font=("Arial", 24))
house_price_label.place(relx=0.1, rely=0.1)

house_price_entry = tk.Entry(window, font=("Arial", 24))
house_price_entry.place(relx=0.4, rely=0.1)

downpayment_label = tk.Label(window, text="Downpayment amount:", fg="#801638", font=("Arial", 24))
downpayment_label.place(relx=0.1, rely=0.2)

downpayment_entry = tk.Entry(window, font=("Arial", 24))
downpayment_entry.place(relx=0.4, rely=0.2)

interest_label = tk.Label(window, text="Interest rate (% p.a.):", fg="#801638", font=("Arial", 24))
interest_label.place(relx=0.1, rely=0.3)

interest_entry = tk.Entry(window, font=("Arial", 24))
interest_entry.place(relx=0.4, rely=0.3)

loan_tenure_label = tk.Label(window, text="Loan tenure (years):", fg="#801638", font=("Arial", 24))
loan_tenure_label.place(relx=0.1, rely=0.4)

loan_tenure_entry = tk.Entry(window, font=("Arial", 24))
loan_tenure_entry.place(relx=0.4, rely=0.4)

# Create a button to calculate the monthly repayment amount
calculate_button = tk.Button(window, text="Calculate", command=calculate_repayment, bg="#801638", fg="white",
                             font=("Arial", 24))
calculate_button.place(relx=0.4, rely=0.6)

# Create a label to display the result
result_label = tk.Label(window, text="", fg="#801638", font=("Arial", 24))
result_label.place(relx=0.1, rely=0.8)

# Start the Tkinter event loop
window.mainloop()
