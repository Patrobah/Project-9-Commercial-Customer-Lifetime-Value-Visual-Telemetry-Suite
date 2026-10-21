import os
import random
import pandas as pd
from datetime import datetime, timedelta


def build_b2c_telemetry_tables():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. Establish Configuration Parameters
    regions = ['Nairobi-KE', 'Lagos-NG', 'London-UK', 'NewYork-US', 'Berlin-DE']
    channels = ['Google_SEO', 'Meta_Ads', 'YouTube_Influencer', 'Referral']
    plans = ['Basic_Monthly', 'Pro_Monthly', 'Premium_Monthly']
    plan_prices = {'Basic_Monthly': 9.99, 'Pro_Monthly': 19.99, 'Premium_Monthly': 49.99}

    # 2. Generate Dim_Customers (3,000 Unique Consumer Accounts)
    print("👥 Engineering 3,000 unique consumer profiles...")
    customer_records = []
    for i in range(5001, 8001):
        cust_id = f"CUST-{i}"
        customer_records.append({
            'Customer_ID': cust_id,
            'Region': random.choices(regions, weights=[0.4, 0.2, 0.15, 0.15, 0.1], k=1)[0],
            'Acquisition_Channel': random.choice(channels),
            'Signup_Age': random.randint(18, 60)
        })
    df_customers = pd.DataFrame(customer_records)

    # 3. Generate Fact_Subscriptions (Dense Transaction Ledger Streams)
    print("📈 Compiling transactional fact tables across historical boundaries...")
    fact_records = []
    start_date = datetime(2025, 1, 1)
    tx_counter = 100001

    # Simulate data logs day-by-day to capture realistic user retention lifetimes
    for day in range(600):
        current_date = start_date + timedelta(days=day)

        # Select a slice of active buyers making automated subscription renewals
        sampled_customers = df_customers.sample(n=random.randint(150, 300))

        for _, cust in sampled_customers.iterrows():
            plan = random.choice(plans)
            base_price = plan_prices[plan]

            # Add realistic corporate overhead parameters
            operational_cost = base_price * random.uniform(0.15, 0.35)

            fact_records.append({
                'Transaction_ID': f"TXN-{tx_counter}",
                'Date': current_date.strftime('%Y-%m-%d'),
                'Customer_ID': cust['Customer_ID'],
                'Plan_Type': plan,
                'Invoice_Amount_USD': base_price,
                'Operational_Cost_USD': round(operational_cost, 2)
            })
            tx_counter += 1

    df_facts = pd.DataFrame(fact_records)

    # 4. Save tables out as separate clean CSV files for relational mapping
    df_customers.to_csv(os.path.join(base_dir, 'dim_customers.csv'), index=False)
    df_facts.to_csv(os.path.join(base_dir, 'fact_subscriptions.csv'), index=False)

    print(f"🎉 Success! 'fact_subscriptions.csv' ({len(df_facts)} rows) and 'dim_customers.csv' successfully exported.")


if __name__ == '__main__':
    build_b2c_telemetry_tables()
