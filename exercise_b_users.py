users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
twitter_handle = users["Jonathan"]["twitter"]
print(twitter_handle)

# 2. Get Erik's hometown
erik_hometown =  users["Erik"]["home_town"]
print(erik_hometown)

# 3. Get the list of Erik's lottery numbers
erik_lottery = users["Erik"]["lottery_numbers"]
print(erik_lottery)

# 4. Get the species of Avril's pet Monty
avril_pets = users["Avril"]["pets"]
monty_species = ""
for avril_pet in avril_pets:
    if avril_pet["name"].lower() == "monty":
        monty_species = avril_pet["species"]
print(monty_species)

# 5. Get the smallest of Erik's lottery numbers
erik_lottery.sort()
smallest = erik_lottery[0]
print(smallest)

# 6. Return an list of Avril's lottery numbers that are even
avril_lottery_nums = users["Avril"]["lottery_numbers"]
avril_even_nums = []
for avril_lottery_num in avril_lottery_nums:
    if avril_lottery_num % 2 == 0:
        avril_even_nums.append(avril_lottery_num)
print(avril_even_nums)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
fluffy = {
    "name": "fluffy",
    "species": "dog"
}
users["Erik"]["pets"].append(fluffy)
print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
users["Tim"] = {
    "twitter": "timohenderson",
    "lottery_numbers": [1, 25, 45, 32, 16, 18],
    "home_town": "Perth",
    "pets": [
      {
        "name": "wendy",
        "species": "dog"
      }
    ]
}
print(users["Tim"])