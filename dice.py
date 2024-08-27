from itertools import product
single_dice = [str(outcome) for outcome in list(range(1,7))]

outcomes_of_two_rolls = [outcome for outcome in product(single_dice,single_dice)]

print(len(outcomes_of_two_rolls))
print("\n\n\n")

i =0
for outcome in outcomes_of_two_rolls:
    print(outcome,end=" ")
    i+=1
    if(i==6):
        print(" ")
        i=0
    
