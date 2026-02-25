word= "bottles"
for beer_num in range (99,0,-1):
    if beer_num==1:
         current_word = "bottle"
    else:
        current_word = "bottles"

    if beer_num - 1 == 1: 
        next_word = "bottle"
    else:
        next_word = "bottles"

    print(beer_num, word, "of beer on the wall")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")

    if beer_num>1:
        print(beer_num-1, "bottles of beer on the wall.")
    else:
        print("No more bottles of beer on the wall.")
#le hice unos cambios para que se, en vez de decir "1 bottle", diga "1 bottle" y en vez de decir "0 bottles", diga "No more bottles"