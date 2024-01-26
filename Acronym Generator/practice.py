print("welcome to acronym program in Python")
def acronym_generator():
    while True:
        user_input = input("Do you want to acronym (yes/no): ")
        if user_input != "yes":
            quit()
        else:

            sentence = input("Enter The Sentence to Acronym: ")
            text = sentence.split() 
            acronym = ""
            for i in text:
                acronym += i[0].upper() 
            print(acronym)  
acronym_generator()        
