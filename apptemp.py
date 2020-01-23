#import code to convert: currency, weight, energy, age
#average ages, heights
#weight of animals
#amount of minerals in humans
#distance of the moon
#number of limbs


###NOTES
#US ton is called a short ton (short_ton)
import os
import random
import numpy as np
from currency import exchange
import pandas as pd
from measurement.measures import Weight, Volume
import inflect

def pluralize(noun):
    p = inflect.engine()
    seperatename = noun.split()
    lastname = noun.split()[-1]
    fullname = p.plural(noun)
    return fullname
####exchange rate calls currency.py just change abbreviations
#exchange("USD","INR")
def weightconvert():
    weight_1 = Weight(lb=125)
    weight_2 = Weight(kilogram=25)
    addedthem = weight_1 + weight_2
    print("added: " + str(addedthem))
    beans = Volume(us_cup=1.5)
    mtdew = Volume(us_oz=12)
    addedthem = (mtdew * 12) / beans
    print(addedthem)

def animalweight():
    df = pd.read_csv("D:\\App\\converter\\animals.csv")
    # countit = df.shape[0]
    # Get names of indexes for which column weight has value 0
    zeroweight = df[ df['Weight'] == 0 ].index
    # Delete these row indexes from dataFrame
    df.drop(zeroweight , inplace=True)
    count_row = df.shape[0]
    randanimalindex = random.randint(1,count_row-1)
    animalname = df['Animal'][randanimalindex]
    animalweight = df['Weight'][randanimalindex]
    return [animalname, animalweight]

def animal():
    animal1 = animalweight()
    animal2 = animalweight()
    while animal2[1] == animal1[1]:
        animal2 = animalweight()
    if animal2[1] < animal1[1]:
        inside = round(animal1[1] / animal2[1], 0)
        print("the average " + animal1[0] + " weighs " + str(inside) + " times as much as the average " + animal2[0])
    else:
        inside = round(animal2[1] / animal1[1],0)
        print("the average " + animal2[0] + " weighs " + str(inside) + " times as much as the average " + animal1[0])
# animal()


def tragedycount():
    df = pd.read_csv("D:\\App\\converter\\disasters.csv")
    deathcount = df.shape[0]
    # print("deathcount: " + str(deathcount))
    randtragic = random.randint(1,deathcount-1)
    # print("random: " + str(randtragic))
    description = df['Description'][randtragic]
    deathtoll = df['People'][randtragic]
    return [deathtoll, description]
def tragedy():
    wreck1 = tragedycount()
    wreck2 = tragedycount()
    while wreck2[1] == wreck1[1]:
        wreck2 = tragedycount()
    if wreck2[0] < wreck1[0]:
        inside = round(wreck1[0] / wreck2[0],2)
        print("The number of people who " + wreck1[1] + " is " + str(inside) + " times the number of people who " + wreck2[1])
    else:
        inside = round(wreck2[0] / wreck1[0],2)
        print("The number of people who " + wreck2[1] + " is " + str(inside) + " times the number of people who " + wreck1[1])
# tragedy()

def animalhumans():
    animal = animalweight()
    tragedy = tragedycount()
    avghuman = 137
    if animal[1] > 137:
        humans = round(animal[1]/137, 0)
        print("an average " + animal[0] + " weighs " + str(humans) + " times as much as an average human")
    else:
        humans = round(137/animal[1], 0)
        # humans = round(137/animal[1], 0)
        print("an average human weighs " + str(humans) + " times as much as an average " + animal[0])
# animalhumans()

def animaltragedy():
    humanweight = 137
    animal = animalweight()
    pluralize(animal[0])
    badevent = tragedycount()
    if badevent[1] > animal[1]:
        print(badevent[1])


animaltragedy()


#notes
##if a bunch of rats piled on top of each other to weigh the same as a human, 300 rats would have died in the civil war.