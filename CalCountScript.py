foods = {}


eaten_example = [{'name' : 'hardboiled eggs','Calories per 100g' : 155, 'Consumed' : 150}, 
         {'name' : 'sardines','Calories per 100g' : 208, 'Consumed' : 67}, 
         {'name' : 'chicken breast','Calories per 100g' : 110, 'Consumed' : 100},
         {'name' : 'bell peppers','Calories per 100g' : 26, 'Consumed' : 32},
         {'name' : 'aubergine','Calories per 100g' : 35, 'Consumed' : 120},
         {'name' : 'cherry tomatoes','Calories per 100g' : 18, 'Consumed' : 108},
         {'name' : 'chickpeas','Calories per 100g' : 102, 'Consumed' : 100},
         {'name' : 'almonds','Calories per 100g' : 580, 'Consumed' : 50},
         {'name' : 'chipolatas','Calories per 100g' : 262, 'Consumed' : 125},
         {'name' : 'mushrooms','Calories per 100g' : 108, 'Consumed' : 84},
         {'name' : 'tinned tomatoes','Calories per 100g' : 23, 'Consumed' : 133},
         {'name' : 'greek yoghurt','Calories per 100g' : 107, 'Consumed' : 160},
         {'name' : 'blueberries','Calories per 100g' : 84, 'Consumed' : 83}]

def add_item(list,name,cals,eaten):
    item = {}
    item['name'] = name
    item['Calories per 100g'] = cals
    item['Consumed'] = eaten
    list.append(item)
    if name not in foods:
        foods[name] = {'Calories per 100g' : cals}



def calories(per100, amount):
    total = (per100/100)*amount
    return total

def calorie_total(food_List):
    # calculates number of calories of list entered as parameter
    total = 0
    for i in food_List:
        cals = calories(i['Calories per 100g'],i['Consumed'])
        print(cals)
        total += cals
    return total

# print(calorie_total(eaten_example))

your_list = []

def prompt():
    newlist = []
    add_items = input("Add items? y/n then press enter: ")
    if add_items == "y":
        another = ""
        while another != "n":        
            item_name = input("Name of food? ")
            calper100 = float(input("Calories in 100g? "))
            consumed = float(input("Weight eaten in g? "))
            add_item(newlist,item_name,calper100,consumed)
            another = input("another item? y/n: ")
        see_items = input("Would you like to see the list? y/n: ")
        if see_items == "y":
            print(see_items)
        print("Calorie total is " + str(calorie_total(newlist)) + " calories.")    
    print("Exiting script")

prompt()