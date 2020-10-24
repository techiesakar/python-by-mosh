# If applicant has high income AND good credit
#   Eligible for loan
# Otherwise
#   Not Eligible for loan

# AND: Both must True
# OR: Atleast One must True

has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print("The person is eligible for loan")
else:
    print("The person isn't eligible for loan")

# Write a program to find the person is eligible for loan or not
# Person mustn't have any criminal record and he must have good credit amount.
has_good_credit = True
has_not_criminal_record = True
if has_good_credit and not has_not_criminal_record:  # not inverse the decision
    print("The person is eligible for loan")
else:
    print("The person is not eligible for loan")
