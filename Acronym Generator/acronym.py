print("Welcome to Acronym Python Program")
all = []
while True:
    will = input("Would you like to do acronym(yes/no): ")
    if will != "yes":
        break
    else:
        user_input = input("Enter a sentence to do ancronym: ")

        text = user_input.split()
        acronym = ""

        for i in text:
            acronym += i[0].upper()
            all.append(acronym)
        # acronym = ".".join(acronym)    
        print(acronym)  
all = ",".join(all)         
print(all)            