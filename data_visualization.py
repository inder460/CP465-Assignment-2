def plot_top_customers(spending_data):
sorted_data = dict(sorted(spending_data.items(), key=lambda
item: item[1], reverse=True)[:5])
plt.bar(sorted_data.keys(), sorted_data.values(),
color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Customers")
plt.ylabel("Total Spending ($)")
plt.title("Top 5 Customers by Spending")
plt.show()
plot_top_customers(spending_data)