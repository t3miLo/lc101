# Write a sort_contacts function that takes a dictionary of contacts as a parameter
# and returns a sorted list of those contacts, where each contact is a tuple.

# The contacts dictionary that will be passed into the function has the contact name as its key,
# and the value is a tuple containing the phone number and email for the contact.
#   contacts = {name: (phone, email), name: (phone, email), etc.}

# The sort_contacts function should then create a new, sorted (by last name)
# list of tuples representing all of the contact info (one tuple for each contact)
# that was in the dictionary. It should then return this list to the calling function.

#   For example, given a dictionary argument of:
#       {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
#       "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
#       "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}

#   sort_contacts should return this:
#   [('Freud, Anna', '1-541-754-3010', 'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'), ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')]


def sort_contacts(contacts):
    sorted_list = list()
    for name in contacts:
        sorted_list.append((name, contacts[name][0], contacts[name][1]))
    sorted_list.sort(reverse=False)
    print(sorted_list)


sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
               "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
               "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")})

sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
               "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")})

sort_contacts({"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")})

sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
               "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
               "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"),
               "Kandinsky, Wassily": ("1-333-555-9999", "kandinsky@painters.com")})
