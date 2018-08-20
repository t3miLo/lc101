
# Write a function that will return a string of country codes from an argument that is a
# string of prices (containing dollar amounts following the country codes).
# Your function will take as an argument a string of prices like the following:
# "US$40, AU$89, JP$200".
# In this example, the function would return the string "US, AU, JP".


def get_country_codes(prices):
    # your code here
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    price_list = list(prices.split("$"))
    country_code = ''

    for each_word in price_list:
        for each_letter in each_word:
            if each_letter in alpha:
                country_code += each_letter

        country_code += ', '
    print(country_code)
    new_country = country_code[-1::-1].replace(',', '', 2)
    print(new_country[:1:-1])


# don't include these tests in Vocareum


get_country_codes("NZ$300, KR$1200, DK$5")
get_country_codes("US$40, AU$89, JP$200")
get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2")
get_country_codes("CA$40")
