import random
import secrets


def save_stats(content):
    import datetime
    datetime = datetime.datetime.now()
    file_name = ("%s-%s-%s" % (datetime.hour, datetime.minute, datetime.second)) + "--" + (
                "%s-%s-%s" % (datetime.day, datetime.month, datetime.year))
    print("\nIf you want to save the file press [Y]")
    choice = str(input("$ "))
    if choice.upper() == "Y":
        save_txt = open(f"./saved/{file_name}", "w")
        save_txt.write(content)
    else:
        exit()


def calc(short, contents, letter_count, percentage_list, searched_word):
    calc = 0
    for i in range(26):
        letter = short[calc]
        counted_letters = contents.count(short[calc])
        calculated_percentage = (counted_letters / letter_count) * 100
        rounded_calculated_percentage = round(calculated_percentage)
        percentage_list.append(
            f"{letter}: {counted_letters}x / {rounded_calculated_percentage}% / {calculated_percentage}%")
        calc += 1

    # list_element_count = (len(contents.split(searched_word))) - 1 <--- I didn´t know the count() definition -_-
    list_element_count = contents.count(searched_word)
    percentage_list.insert(0,
                           f"from: {letter_count} / percent rounded / percent default / found searched word({searched_word}) {list_element_count} times\n")
    stats_txt = open("./stats.txt", "w")
    contents_stats = "\n".join(map(str, percentage_list))
    stats_txt.write(contents_stats)

    save_stats(contents_stats)


def search_in_mass_random(countdown):
    searched_word = str(input("word: "))

    letter_count = int(input("letters: "))

    letter_list = []
    percentage_list = []

    while countdown != letter_count:
        short = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
        short = short.split(',')
        random_letter = short[random.randrange(0, 26)]
        letter_list.append(random_letter)
        countdown += 1

    else:
        result_txt = open("./result.txt", "w")
        contents = "".join(map(str, letter_list))
        result_txt.write(contents)
        print(f"\ncreated successful {letter_count} random letters")

    calc(short, contents, letter_count, percentage_list, searched_word)


def search_in_mass_secrets(countdown):
    searched_word = str(input("word: "))

    letter_count = int(input("letters: "))

    letter_list = []
    percentage_list = []

    while countdown != letter_count:
        short = list('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,)
        random_letter = secrets.choice(short)
        letter_list.append(random_letter)
        countdown += 1

    else:
        result_txt = open("./result.txt", "w")
        contents = "".join(map(str, letter_list))
        result_txt.write(contents)
        print(f"\ncreated successful {letter_count} random letters")

    calc(short, contents, letter_count, percentage_list, searched_word)


lib = str(input("Which libary do you want? random[R] or secrets[S]"))
if lib.upper() == "R":
    search_in_mass_random(0)
if lib.upper() == "S":
    search_in_mass_secrets(0)
if lib.upper() != "R" or "S":
    exit()
