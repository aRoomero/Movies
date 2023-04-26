# rank,name,year,rating,genre,certificate,run_time,tagline,budget,box_office,casts,directors,writers

from collections import Counter

def get_keys_values(dict_in):
    
    years = tuple(map(lambda item: item["year"], dict_in))
    keys = set(years)
    values = []

    for x in keys:
        values.append(Counter(years)[x])
                
    return keys, values