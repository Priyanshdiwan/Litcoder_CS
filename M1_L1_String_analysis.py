user_email = input()
def email_analyser(email):
    total_ch=len(email)
    upper_ch=sum(1 for char in email if char.isupper())
    lower_ch=sum(1 for char in email if char.islower())
    digit_ch=sum(1 for char in email if char.isdigit())
    symbol_ch=total_ch-(upper_ch+lower_ch+digit_ch)
    
    upper_percentage=(upper_ch/total_ch)*100
    lower_percentage=(lower_ch/total_ch)*100
    digit_percentage=(digit_ch/total_ch)*100
    symbol_percentage=(symbol_ch/total_ch)*100
    
    print(f"{upper_percentage:.3f}%")
    print(f"{lower_percentage:.3f}%")
    print(f"{digit_percentage:.3f}%")
    print(f"{symbol_percentage:.3f}%")
    
result=email_analyser(user_email)