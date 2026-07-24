balance = 500
withdrawal_amount = float(input("\nHow much do you want to withdraw? "))


if withdrawal_amount <= 0:
    print("\nInvalid amount. You must withdraw more than R0.")
elif withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print(f"\nWithdrawal successful! Remaining balance: R{balance}")
else:
    print("\nDeclined. Insufficient funds!")
