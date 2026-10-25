name = input ("Full name ? :")
age = int(input ("How old are you ? :"))
language = input ("do you know either : Python or JavaScript.(yes or no)").upper()
project = input ("have built a project (yes or no) ?").upper()
if age >=18 and language == "YES" and project == "YES":
    print (f"Hello {name},")
    print ("you meet the basic requirements.")
else :
    print (f"Hello {name}")
    print("work on more project ")
