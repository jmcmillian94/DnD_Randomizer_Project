#importing pyfiglet for cool ASCII functions
import pyfiglet as fig

#dictionary used for determining and calculating the partys XP threshold
#characterlevel : [easy,medium,hard,deadly]
xp_threshholds = {1: [25,50,75,110],
                  2: [50,100,150,200],
                  3: [75,150,225,400],
                  4: [125,250,375,500],
                  5: [250,500,750,1100],
                  6: [300,600,900,1400],
                  7: [350,750,1100,1700],
                  8: [450,900,1400,2100],
                  9: [550,1100,1600,2400],
                  10: [600,1200,1900,2800],
                  11: [800,166,2400,3600],
                  12: [1000,2000,3000,4500],
                  13: [1100,2200,3400,5100],
                  14: [1250,2500,3800,5700],
                  15: [1400,2800,4300,6400],
                  16: [1600,3200,4800,7200],
                  17: [2000,3900,5900,8800],
                  18: [2100,4200,6300,9500],
                  19: [2400,4900,7300,10900],
                  20: [2800,5700,8500,12,700]
                  }

#based  on the number of mmonsters in an encounter, the total XP of the monsters should be adjusted accordingly
#number of monsters : multiplier
encounter_multipliers = {1: 1,
                         2: 1.5,
                         3: 2,
                         4: 2,
                         5: 2,
                         6: 2,
                         7: 2.5,
                         8: 2.5,
                         9: 2.5,
                         10: 2.5,
                         11: 3,
                         12: 3,
                         13: 3,
                         14: 3,
                         15: 4,
                        }

#lists of all monsters possible to generate, contains 
monster_manual = {'bugbear': {'xp': 700,  },  }

#print out program greeting
#program needs to ask user what they want to do and provide a list of all the tasks the program can do
print(fig.figlet_format("DnD Randomizer"))


#ask how many people are in the party
#ask each players name and level
#assign XP threshold to each character
party_size = int(input("How many adventurers are in your party?"))
party = {}
for i in range(1, party_size + 1):
    print("Adventurer", (i))
    name = input("what is your name?")
    player_class = input("What is your class?")
    lvl = int(input("What is your level?"))
    thresholds = xp_threshholds[lvl]
    player_info = [player_class,lvl,thresholds]
    party[name] = player_info


#total up each players XP threshold into a party threshold
easy_party_xp_threshold = 0
medium_party_xp_threshold = 0
hard_party_xp_threshold = 0
deadly_party_xp_threshold = 0
for i in party:
    easy_party_xp_threshold += party[i][2][0]
    medium_party_xp_threshold += party[i][2][1]
    hard_party_xp_threshold += party[i][2][2]
    deadly_party_xp_threshold += party[i][2][3]




#create a funtion that generates a random encounter
#encounter function should also provide how much exp is granted for each enemy defeated
#encounter should ask if anyone leveled up after each encounter and adjust XP threshold if necessary

#create function that randomizes loot


