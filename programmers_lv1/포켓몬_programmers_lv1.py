def solution(nums):    
    answer = 0
    pokemons = len(nums)
    my_pokemon = pokemons//2
    set_nums = set(nums)
    poke_types = len(set_nums)
    # print(my_pokemon,poke_types)
    return min(my_pokemon,poke_types)