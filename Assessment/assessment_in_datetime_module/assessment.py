# datetime module ഉപയോഗിച്ച് Yesterday, Today, Tomorrow dates print ചെയ്യുക.


from datetime import date, timedelta
   
today = date.today()

yesterday = today - timedelta(days=1)
tomorrow = today  + timedelta(days=1)
   
print("Yesterday:", yesterday)

print("Today:", today)
print("Tomorrow :", tomorrow)
