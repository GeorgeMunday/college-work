import pandas as p

def get_valid_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            date = p.to_datetime(date_str, format='%d/%m/%Y')
            return date
        except ValueError:
            print("Invalid date format. Please enter the date in dd/mm/yyyy format.")

def main():
    try:
        data = p.read_csv('Task3_data.csv')
    except FileNotFoundError:
        print("File not found")
        exit()

    date1 = get_valid_date("This is a profit calculator, what date would you like to start at (dd/mm/yyyy): ")
    date2 = get_valid_date("This is a profit calculator, what date would you like to end at (dd/mm/yyyy): ")

    data['Date'] = p.to_datetime(data['Date'], format='%d/%m/%Y')

    filtered_data = data[(data['Date'] >= date1) & (data['Date'] <= date2)]
    filtered_data = filtered_data.sort_values(by='Date')

    filtered_data['Profit'] = (filtered_data['KGs Sold'] * filtered_data['Selling Price']) - (filtered_data['KGs Purchased'] * filtered_data['Purchase Price'])
    total_profit = filtered_data['Profit'].sum()

    try:
        choice = input("Would you like to filter it for a specific product or all products? (specific/all): ")
        if choice == 'specific':
            product = input("What product would you like to see the transactions for: ")
            filtered_data = filtered_data[filtered_data['Product'] == product]
            print("profit for the selected product:")
            print(total_profit)
        elif choice == 'all':
            print("profit for all products within the selected dates:")
            print(total_profit)
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input")
        exit()

if __name__ == '__main__':
    main()