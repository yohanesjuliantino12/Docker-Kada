import pandas as pd
import random

NUM_USERS = 10000
MAX_LOANS_PER_USER = 3

users = []
loans = []
payments = []

loan_id_counter = 1
payment_id_counter = 1

for i in range(NUM_USERS):

    user_id = f"U{i}"

    income = random.randint(2000,15000)
    credit_score = random.randint(500,800)

    users.append({
        "user_id": user_id,
        "age": random.randint(21,60),
        "income": income,
        "city": random.choice(["Jakarta","Bandung","Surabaya","Medan"]),
        "employment": random.choice(["employee","freelancer","business"]),
        "credit_score": credit_score
    })

    num_loans = random.randint(1,MAX_LOANS_PER_USER)

    for _ in range(num_loans):

        loan_id = f"L{loan_id_counter}"
        loan_id_counter += 1

        loan_amount = random.randint(1000,10000)

        # probabilitas default berdasarkan credit score
        if credit_score < 600:
            loan_status = random.choices(
                ["paid","default"],weights=[0.6,0.4])[0]
        else:
            loan_status = random.choices(
                ["paid","default"],weights=[0.9,0.1])[0]

        loans.append({
            "loan_id": loan_id,
            "user_id": user_id,
            "loan_amount": loan_amount,
            "interest_rate": random.choice([0.1,0.12,0.15]),
            "loan_status": loan_status
        })

        # generate payment schedule
        num_payments = random.randint(3,12)

        for _ in range(num_payments):

            late = random.choices(
                ["yes","no"],weights=[0.2,0.8])[0]

            payments.append({
                "payment_id": f"P{payment_id_counter}",
                "loan_id": loan_id,
                "payment_amount": loan_amount/num_payments,
                "late_payment": late
            })

            payment_id_counter += 1

# save dataset
pd.DataFrame(users).to_csv("../dataset/users.csv",index=False)
pd.DataFrame(loans).to_csv("../dataset/loans.csv",index=False)
pd.DataFrame(payments).to_csv("../dataset/payments.csv",index=False)

print("Dataset generated successfully")