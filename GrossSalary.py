a=int(input('1.Basic=1000\n2.Basic=4567\nEnter Index of your Category : '))
if a==1:
  basic=1000
  grade='A'
else:
  basic=4567
  grade='B'
HRA=20/100*basic
DA=50/100*basic
PF=11/100*basic
if grade=='A':
  Allow=1700
else:
  Allow=1500

GrosssSalary=basic+HRA+DA+Allow-PF
print('Gross Salary is : ',GrosssSalary)
