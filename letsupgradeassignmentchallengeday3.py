# -*- coding: utf-8 -*-
"""letsupgradeassignmentchallengeday3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10DVh1xgUnLW2MHUQ1bxl1xhWpN2piFn4
"""



alt = int(input("Enter the altitude for plane landing"))
print("Your altitude is:",alt)
if alt == 3000:
  print("You are landing safe :)")
elif 3000 < alt < 6000:
  print("Come down to 3000ft and open the landing gear.")
elif alt > 6000:
  print("Go around,Do not land!!")
else:
  print("You are below the ideal landing range :(")