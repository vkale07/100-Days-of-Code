# Dictionary in python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
}
print(travel_log["France"][1])

# Nested lists
nest_list = ["A", "B", ["C", "D", "E", "F"], "G"]

print(nest_list[2][1])

# Nested dictionaries
travel_log1 = {
    "France":{
        "cities_visited":["Paris", "Lille", "Dijon"],
        "num_times_visited" : 12
         },
    "Germany" : {
        "cities_visited": ["Berlin","Hamburg", "Stuttgart"],
        "num_times_visited" : 5
    }
}

print(travel_log1["Germany"]["cities_visited"][2])

# Quize questions

#Q1: 
starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)


#Q2: Which line of code will produce an error?
    # a. dict["c"] = [1, 2, 3]
    # b.  for key in dict:
#             dict[key] += 1
    # c. dict[1] = 4
    # d. print(dict[1])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# dict["c"] = [1, 2, 3]
# print(dict)

# for key in dict:
#     dict[key] += 1
# print(dict)

# dict[1] = 4
# print(dict)


# Question 3: Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])