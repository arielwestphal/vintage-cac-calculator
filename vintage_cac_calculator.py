import streamlit as st

st.title("Customer Vintage CAC Recovery Calculator")

# User Inputs
applications = st.number_input("Number of Applications", min_value=1, value=1000)
approvals = st.number_input("Number of Approvals", min_value=1, max_value=applications, value=400)
conversions = st.number_input("Number of Conversions", min_value=1, max_value=approvals, value=200)
uw_data_cost = st.number_input("Underwriting Data Cost ($)", min_value=0.0, value=5000.0)
marketing_spend = st.number_input("Marketing Spend ($)", min_value=0.0, value=15000.0)
total_originated_dollars = st.number_input("Total Originated Dollars ($)", min_value=0.0, value=10000000.0)
total_dollars_drawn = st.number_input("Total Dollars Drawn ($)", min_value=0.0, max_value=total_originated_dollars, value=min(10000000.0, total_originated_dollars))
apr = st.number_input("APR (as a whole number, e.g. 24 for 24%)", min_value=0.0, max_value=1000.0, value=24.0)
day_of_month = st.number_input("Day of the Month", min_value=1, max_value=31, value=15)

# Prevent division by zero
safe_approvals = approvals if approvals > 0 else 1
safe_conversions = conversions if conversions > 0 else 1
safe_applications = applications if applications > 0 else 1
safe_originated = total_originated_dollars if total_originated_dollars > 0 else 1

# Calculations
approval_rate = approvals / safe_applications
conversion_rate = conversions / safe_approvals
utilization_rate = total_dollars_drawn / safe_originated

total_cac = marketing_spend + uw_data_cost
cost_per_application = total_cac / safe_applications
cost_per_approved = total_cac / safe_approvals
cost_per_conversion = total_cac / safe_conversions

avg_origination_amount = total_originated_dollars / safe_conversions
avg_dollars_drawn = total_dollars_drawn / safe_conversions

monthly_rate = apr / 100 / 12
daily_rate = apr / 100 / 365
total_monthly_revenue = total_dollars_drawn * monthly_rate
total_daily_revenue = total_dollars_drawn * daily_rate
avg_monthly_revenue_per_customer = total_monthly_revenue / safe_conversions
avg_daily_revenue_per_customer = total_daily_revenue / safe_conversions
avg_revenue_after_cac = avg_monthly_revenue_per_customer - cost_per_conversion

total_revenue_to_date = total_daily_revenue * day_of_month
avg_revenue_to_date_per_customer = total_revenue_to_date / safe_conversions

# Output Results
st.header("Calculated Metrics")
st.metric("Approval Rate", f"{approval_rate:.2%}")
st.metric("Conversion Rate", f"{conversion_rate:.2%}")
st.metric("Utilization Rate", f"{utilization_rate:.2%}")

st.metric("Total CAC", f"${total_cac:,.2f}")
st.metric("Cost per Application", f"${cost_per_application:,.2f}")
st.metric("Cost per Approved", f"${cost_per_approved:,.2f}")
st.metric("Cost per Conversion", f"${cost_per_conversion:,.2f}")

st.metric("Avg Origination Amount", f"${avg_origination_amount:,.2f}")
st.metric("Avg Dollars Drawn", f"${avg_dollars_drawn:,.2f}")

st.metric("Total Monthly Revenue", f"${total_monthly_revenue:,.2f}")
st.metric("Avg Monthly Revenue per Customer", f"${avg_monthly_revenue_per_customer:,.2f}")
st.metric("Total Daily Revenue", f"${total_daily_revenue:,.2f}")
st.metric("Avg Daily Revenue per Customer", f"${avg_daily_revenue_per_customer:,.2f}")
st.metric("Total Revenue to Date (Day {day_of_month})", f"${total_revenue_to_date:,.2f}")
st.metric("Avg Revenue to Date per Customer", f"${avg_revenue_to_date_per_customer:,.2f}")
st.metric("Avg Revenue After CAC", f"${avg_revenue_after_cac:,.2f}")
