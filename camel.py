#intro
input_sentence=input("please enter a sentence to be camel case'd: ")

#splitting into words
input_list=input_sentence.split(" ")

output_string=""

#manipulating words
for i in range(len(input_list)):
    if i ==0:
        output_string+=input_list[i].lower()
    else:
        output_string+=input_list[i].capitalize()

#output
print(f'your original string {input_sentence} in camel case is {output_string}')