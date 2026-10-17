# immutable values
immutable_int = 123
lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
greeting = "Hi"
name = "Richard"
profile_info = ("Richard", 30, "Kyiv", "Developer", True)  # tuple is immutable
collection_of_coins = (1, 2, 5, 10, 25, 50, 100)  # tuple (7 items, immutable)

# mutable values
mutable_list_empty = []
mutable_list_numbers = [1, 2]
my_favourite_films = [
    "The Matrix",
    "Inception",
    "Interstellar",
    "The Godfather"
]  # 4 items
marks = [5, 4, 3, 4, 5, 2]  # 6 items

# sorted_variables groups mutable and immutable values
sorted_variables = {
    "mutable": [
        mutable_list_empty,
        mutable_list_numbers,
        my_favourite_films,
        marks
    ],
    "immutable": [
        immutable_int,
        greeting,
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        profile_info,
        collection_of_coins,
    ],
}
