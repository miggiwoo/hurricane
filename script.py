# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

def update_damages(damages):
    improved_damages = []
    for damage in damages:
        if "M" in damage:
            improved_damages.append(float(damage.rstrip("M"))*1000000)
        elif "B" in damage:
            improved_damages.append(float(damage.rstrip("B"))*1000000000)
        else:
            improved_damages.append(damage)
    return improved_damages

damage = update_damages(damages)

def hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damage, deaths):
    new_dict = {}
    for i in range(len(names)):
        new_dict[names[i]] = {"Name": names[i], "Month": months[i], "Years": years[i], "Winds": max_sustained_winds[i], "Areas": areas_affected[i], "Damage": damage[i], "Deaths": deaths[i]}
    return new_dict

hurricanes = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damage, deaths)

def hurricanes_year(hurricanes):
    new_dict={}
    for hurricane in hurricanes:
        year = hurricanes[hurricane]["Years"]
        this_hurricane = hurricanes[hurricane]
        if year not in new_dict:
            new_dict[year] = [this_hurricane]
        else:
            new_dict[year].append(this_hurricane)
    return new_dict

years = hurricanes_year(hurricanes)

def area_count(hurricanes):
    new_dict = {}
    for hurricane in hurricanes:
        for area in hurricanes[hurricane]["Areas"]:
            if area not in new_dict:
                new_dict[area] = 1
            else:
                new_dict[area] += 1
    return new_dict

area_frequency = area_count(hurricanes)

def frequent_area(area_frequency):
    count = 0
    area_name = "" 
    for area in area_frequency:
        if area_frequency[area] > count:
            count = area_frequency[area]
            area_name = area
    
    return count, area_name

most_frequent_count, most_frequent_area = frequent_area(area_frequency)
print(most_frequent_count)

def most_lethal(hurricanes):
    count = 0
    name = ""
    for hurricane in hurricanes:
        if hurricanes[hurricane]["Deaths"] > count:
            count = hurricanes[hurricane]["Deaths"]
            name = hurricane
    return count, name

most_lethal_count, most_lethal_name = most_lethal(hurricanes)

def mortality_scale(hurricanes):
    mortality_dict = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000, 5: 10001}
    new_dict = {k: [] for k, v in mortality_dict.items()}
    for hurricane in hurricanes:
        deaths = hurricanes[hurricane]["Deaths"]
        if deaths == mortality_dict[0]:
            new_dict[0].append(hurricanes[hurricane])
        elif deaths > mortality_dict[0] and deaths <= mortality_dict[1]:
            new_dict[1].append(hurricanes[hurricane])
        elif deaths > mortality_dict[1] and deaths <= mortality_dict[2]:
            new_dict[2].append(hurricanes[hurricane])
        elif deaths > mortality_dict[2] and deaths <= mortality_dict[3]:
            new_dict[3].append(hurricanes[hurricane])
        elif deaths > mortality_dict[3] and deaths <= mortality_dict[4]:
            new_dict[4].append(hurricanes[hurricane])
        else:
            new_dict[5].append(hurricanes[hurricane])
    return(new_dict)

mortality_rating = mortality_scale(hurricanes)

def most_costly(hurricanes):
    count = 0
    name = ""
    for hurricane in hurricanes:
        dam = hurricanes[hurricane]["Damage"]
        if isinstance(dam, str):
            pass
        elif dam > count:
            count = dam
            name = hurricane
    return count, name

most_costly_damage, most_costly_name = most_costly(hurricanes)

def damage_scale(hurricanes):
    damage_dict = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000, 5: 50000000001}
    new_dict = {k: [] for k, v in damage_dict.items()}
    for hurricane in hurricanes:
        dam = hurricanes[hurricane]["Damage"]
        if isinstance(dam, str):
            pass
        elif dam == damage_dict[0]:
            new_dict[0].append(hurricanes[hurricane])
        elif dam > damage_dict[0] and dam <= damage_dict[1]:
            new_dict[1].append(hurricanes[hurricane])
        elif dam > damage_dict[1] and dam <= damage_dict[2]:
            new_dict[2].append(hurricanes[hurricane])
        elif dam > damage_dict[2] and dam <= damage_dict[3]:
            new_dict[3].append(hurricanes[hurricane])
        elif dam > damage_dict[3] and dam <= damage_dict[4]:
            new_dict[4].append(hurricanes[hurricane])
        else:
            new_dict[5].append(hurricanes[hurricane])
    return new_dict

damage_scaled = damage_scale(hurricanes)
print(damage_scaled[5][k: v for k, v in damage_scaled.items()][0])


