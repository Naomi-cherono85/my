students={"Naomi", "Enock" ,"Bett","Nicho",}
students1={"Naomi", "Sylvia" ,"Bett","Purity"}
male_students={"Enock", "Nicho", "Bett"}
female_students={"Naomi","Purity"}



if students.issuperset (male_students):
    print("students is a superset of male_students")
else:
    print("students is not a superset of male_students")
