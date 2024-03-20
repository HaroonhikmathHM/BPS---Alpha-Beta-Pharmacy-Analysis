import pandas as pd
import matplotlib.pyplot as plt

invoice_df = pd.read_csv('invoice.csv')
invoice_df.head(10)

#identify the credit sales 
credit_sales = invoice_df[invoice_df['invoiceBalance'] > 0][['invoiceId', 'invoiceBalance']]
number_of_credit_sales = credit_sales.shape[0]
credit_sales, number_of_credit_sales

#identify the total credit amount (assumption - invoice balance is the credit amount)
total_credit_amount1 = invoice_df['invoiceBalance'].sum()
total_credit_amount1

#accounting 
total_revenue = invoice_df['invoiceAmount'].sum()
total_profit = invoice_df['invoiceProfit'].sum()
total_cost = total_revenue - total_profit
profit_margin = (total_profit / total_revenue) * 100
total_discount_amount = invoice_df['invoiceDiscountAmount'].sum()
discount_impact_ratio = (total_discount_amount / total_revenue) * 100
credit_sales_ratio = (total_credit_amount1 / total_revenue) * 100

print('Total Revenue :' , total_revenue)
print('Total Profit :' , total_profit)
print('Total Product Cost :' ,total_cost)
print('Profit Margine :' , profit_margin) 
print('Total Discount Amount :' , total_discount_amount)
print('Discount Impact Ratio :' , discount_impact_ratio)
print('Total Credit Sales :' , total_credit_amount1) 
print('Credit Sales Ratio on total revenue :' , credit_sales_ratio)

#descriptive statics 
invoice_df1 = pd.read_csv('invoice.csv')
invoice_df1 = invoice_df1.drop('invoiceId', axis=1)
descriptive_stats = invoice_df1.describe()
descriptive_stats
