# https://github.com/tejado/pgoapi/tree/8cafd56fb2fde52f1617fe13d7e75e01bc1f529b
# pgoapi 1.1.6
# PogoExtractor 1.0 by joaodragao

# --- Location class ---
class Location:

    def __init__(self, latitude, longitude, altitude = 0.0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
    
    def description(self):
        return 'Latitude  : ' + str(self.latitude) + \
             '\nLongitude : ' + str(self.longitude) + \
             '\nAltitdue  : ' + str(self.altitude)


# --- import ---
import os
import csv
import json
import sys
import argparse
from datetime import datetime
import pprint
from pgoapi import pgoapi
from pgoapi import exceptions


# --- global variables ---
pokemon_list = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'NidoranF', 'Nidorina', 'Nidoqueen', 'NidoranM', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew']
move_list = {'0': 'Move Unset', '1': 'Thunder Shock', '2': 'Quick Attack', '3': 'Scratch', '4': 'Ember', '5': 'Vine Whip', '6': 'Tackle', '7': 'Razor Leaf', '8': 'Take Down', '9': 'Water Gun', '10': 'Bite', '11': 'Pound', '12': 'Double Slap', '13': 'Wrap', '14': 'Hyper Beam', '15': 'Lick', '16': 'Dark Pulse', '17': 'Smog', '18': 'Sludge', '19': 'Metal Claw', '20': 'Vice Grip', '21': 'Flame Wheel', '22': 'Megahorn', '23': 'Wing Attack', '24': 'Flamethrower', '25': 'Sucker Punch', '26': 'Dig', '27': 'Low Kick', '28': 'Cross Chop', '29': 'Psycho Cut', '30': 'Psybeam', '31': 'Earthquake', '32': 'Stone Edge', '33': 'Ice Punch', '34': 'Heart Stamp', '35': 'Discharge', '36': 'Flash Cannon', '37': 'Peck', '38': 'Drill Peck', '39': 'Ice Beam', '40': 'Blizzard', '41': 'Air Slash', '42': 'Heat Wave', '43': 'Twineedle', '44': 'Poison Jab', '45': 'Aerial Ace', '46': 'Drill Run', '47': 'Petal Blizzard', '48': 'Mega Drain', '49': 'Bug Buzz', '50': 'Poison Fang', '51': 'Night Slash', '52': 'Slash', '53': 'Bubble Beam', '54': 'Submission', '55': 'Karate Chop', '56': 'Low Sweep', '57': 'Aqua Jet', '58': 'Aqua Tail', '59': 'Seed Bomb', '60': 'Psyshock', '61': 'Rock Throw', '62': 'Ancient Power', '63': 'Rock Tomb', '64': 'Rock Slide', '65': 'Power Gem', '66': 'Shadow Sneak', '67': 'Shadow Punch', '68': 'Shadow Claw', '69': 'Ominous Wind', '70': 'Shadow Ball', '71': 'Bullet Punch', '72': 'Magnet Bomb', '73': 'Steel Wing', '74': 'Iron Head', '75': 'Parabolic Charge', '76': 'Spark', '77': 'Thunder Punch', '78': 'Thunder', '79': 'Thunderbolt', '80': 'Twister', '81': 'Dragon Breath', '82': 'Dragon Pulse', '83': 'Dragon Claw', '84': 'Disarming Voice', '85': 'Draining Kiss', '86': 'Dazzling Gleam', '87': 'Moonblast', '88': 'Play Rough', '89': 'Cross Poison', '90': 'Sludge Bomb', '91': 'Sludge Wave', '92': 'Gunk Shot', '93': 'Mud Shot', '94': 'Bone Club', '95': 'Bulldoze', '96': 'Mud Bomb', '97': 'Fury Cutter', '98': 'Bug Bite', '99': 'Signal Beam', '100': 'X Scissor', '101': 'Flame Charge', '102': 'Flame Burst', '103': 'Fire Blast', '104': 'Brine', '105': 'Water Pulse', '106': 'Scald', '107': 'Hydro Pump', '108': 'Psychic', '109': 'Psystrike', '110': 'Ice Shard', '111': 'Icy Wind', '112': 'Frost Breath', '113': 'Absorb', '114': 'Giga Drain', '115': 'Fire Punch', '116': 'Solar Beam', '117': 'Leaf Blade', '118': 'Power Whip', '119': 'Splash', '120': 'Acid', '121': 'Air Cutter', '122': 'Hurricane', '123': 'Brick Break', '124': 'Cut', '125': 'Swift', '126': 'Horn Attack', '127': 'Stomp', '128': 'Headbutt', '129': 'Hyper Fang', '130': 'Slam', '131': 'Body Slam', '132': 'Rest', '133': 'Struggle', '134': 'Scald Blastoise', '135': 'Hydro Pump Blastoise', '136': 'Wrap Green', '137': 'Wrap Pink', '200': 'Fury Cutter Fast', '201': 'Bug Bite Fast', '202': 'Bite Fast', '203': 'Sucker Punch Fast', '204': 'Dragon Breath Fast', '205': 'Thunder Shock Fast', '206': 'Spark Fast', '207': 'Low Kick Fast', '208': 'Karate Chop Fast', '209': 'Ember Fast', '210': 'Wing Attack Fast', '211': 'Peck Fast', '212': 'Lick Fast', '213': 'Shadow Claw Fast', '214': 'Vine Whip Fast', '215': 'Razor Leaf Fast', '216': 'Mud Shot Fast', '217': 'Ice Shard Fast', '218': 'Frost Breath Fast', '219': 'Quick Attack Fast', '220': 'Scratch Fast', '221': 'Tackle Fast', '222': 'Pound Fast', '223': 'Cut Fast', '224': 'Poison Jab Fast', '225': 'Acid Fast', '226': 'Psycho Cut Fast', '227': 'Rock Throw Fast', '228': 'Metal Claw Fast', '229': 'Bullet Punch Fast', '230': 'Water Gun Fast', '231': 'Splash Fast', '232': 'Water Gun Fast Blastoise', '233': 'Mud Slap Fast', '234': 'Zen Headbutt Fast', '235': 'Confusion Fast', '236': 'Poison Sting Fast', '237': 'Bubble Fast', '238': 'Feint Attack Fast', '239': 'Steel Wing Fast', '240': 'Fire Fang Fast', '241': 'Rock Smash Fast', }
item_list = {'0': 'Unknown', '1': 'Pokeball', '2': 'Greatball', '3': 'Ultraball', '4': 'Masterball', '101': 'Potion', '102': 'Super Potion', '103': 'Hyper Potion', '104': 'Max Potion', '201': 'Revive', '301': 'Lucky Egg', '401': 'Incense Ordinary', '402': 'Incense Spicy', '403': 'Incense Cool', '404': 'Incense Floral', '501': 'Troy Disk', '602': 'X Attack', '603': 'X Defense', '604': 'X Miracle', '701': 'Razz Berry', '702': 'Bluk Berry', '703': 'Nanab Berry', '704': 'Wepar Berry', '705': 'Pinap Berry', '801': 'Special Camera', '901': 'Incubator Basic', '902': 'Incubator x3', '1001': 'Pokemon Storage Upgrade', '1002': 'Item Storage Upgrade'}

current_logfile = datetime.now().strftime('%y%m%d-%H%M%S')


# --- initial config function ---
def init_config():
    parser = argparse.ArgumentParser()
    config_file = 'config.json'
    
    load = {}
    if os.path.isfile(config_file):
        with open(config_file) as data:
            try:
                load.update(json.load(data))
            except Exception as e:
                print('Error in config.json file. {}'.format(e))
                sys.exit(1)
    
    required = lambda x: not x in load
    parser.add_argument(
        '-a',
        '--auth_service',
        help="Auth Service ('ptc' or 'google')",
        required=required("auth_service"))
    parser.add_argument(
        '-u',
        '--username',
        help="Username",
        required=required("username"))
    parser.add_argument(
        '-p',
        '--password',
        help="Password",
        required=required("password"))
    parser.add_argument(
        '-rd',
        '--rawdata',
        help="Password",
        default=0)
    config = parser.parse_args()
    
    for key in config.__dict__:
        if key in load and config.__dict__[key] == None:
            config.__dict__[key] = str(load[key])
    
    if config.auth_service not in ['ptc', 'google']:
        print("invalid auth service specified! ('ptc' or 'google')")
        sys.exit(1)
    
    return config


# --- player information function ---
def player_infomation(stats, data, pokemon_count, item_count):
    content = '\nPlayer Stats\n\n'
    content += 'Name: ' + str(data.get('username', 0)) + '\n'
    content += 'Level: ' + str(stats.get('level', 0)) + '\n'
    current_xp = stats.get('experience', 0)
    level_xp = stats.get('next_level_xp', 0)
    content += 'Experience: ' + str(current_xp) + '/' + str(level_xp) + ' XP  |  ' + str(level_xp - current_xp) + ' XP to Level Up!\n'
    content += 'Pokecoin: ' + str(data['currencies'][0].get('amount', 0)) + '\n'
    content += 'Stardust: ' + str(data['currencies'][1].get('amount', 0)) + '\n'
    content += 'Pokemon Storage: {}/{}\n'.format(pokemon_count, data.get('max_pokemon_storage', 0))
    content += 'Bag Storage: {}/{}\n'.format(item_count, data.get('max_item_storage', 0))
    content += 'Walk Distance: {0:.2f} km\n'.format(stats.get('km_walked', 0))
    content += 'Egg Hatched: ' + str(stats.get('eggs_hatched', 0)) + '\n'
    content += 'Pokestops Visited: ' + str(stats.get('poke_stop_visits', 0)) + '\n'
    content += 'Pokemons Captured: ' + str(stats.get('pokemons_captured', 0)) + '\n'
    content += 'Pokemons Encountered: ' + str(stats.get('pokemons_encountered', 0)) + '\n'
    content += 'Pokeballs Thrown: ' + str(stats.get('pokeballs_thrown', 0)) + '\n'
    content += 'Pokedex: ' + str(stats.get('unique_pokedex_entries', 0)) + '\n'
    return content
    

# --- pokemon candies function ---
def pokemon_candies(candies):
    content = '\nCandies\n\n'
    content += '# Species: Amount\n' + '-'*17 + '\n'
    for candy in candies:
        family_id = candy.get('family_id', 0)
        species = pokemon_list[int(family_id) - 1]
        candy_count = candy.get('candy', 0)
        content += '{} {}: {}\n'.format(family_id, species, candy_count)
    return content


# --- pokemon stats function ---
def pokemon_stats(data):
    writer = csv.writer(open('pokemon_stats_{}.csv'.format(current_logfile), 'w'))
    writer.writerow(['#', 'Nickname', 'Species', 'CP', 'HP', 'Kg', 'M', 'Attack', 'Defense', 'Stamina', 'IV', '%', 'Fast Move', 'Charge Move'])
    
    for pkmn in data:
        if 'is_egg' in pkmn:
            continue
        
        id = int(pkmn.get('pokemon_id', 0))
        species = pokemon_list[id - 1]
        nickname = pkmn.get('nickname', '')
        
        attack = pkmn.get('individual_attack', 0)
        defense = pkmn.get('individual_defense', 0)
        stamina = pkmn.get('individual_stamina', 0)
        iv = attack + defense + stamina
        potential = round(float(iv) / 45.0 * 100.0, 2)
        
        cp = pkmn.get('cp', 0)
        hp = pkmn.get('stamina_max', 0)
        
        weight = round(float(pkmn.get('weight_kg', 0)), 2)
        height = round(float(pkmn.get('height_m', 0)), 2)
        
        fast_move = move_list[str(pkmn.get('move_1', 0))].replace(' Fast', '')
        charge_move = move_list[str(pkmn.get('move_2', 0))]

        writer.writerow([id, nickname, species, cp, hp, weight, height, attack, defense, stamina, iv, potential, fast_move, charge_move])


# --- player itemlist function ---
def player_item_list(items):
    content = '\nItems\n\n'
    content += 'Item: Amount\n' + '-'*12 + '\n'
    for item in items:
        item_id = item.get('item_id', 0)
        item_name = item_list[str(item_id)]
        item_count = item.get('count', 0)
        content += item_name + ': ' + str(item_count) + '\n'
    return content


# --- pokedex function ---
def pokedex(data, stats):
    content = '\nPokedex\n\n'
    content += '# Species: Captured/Encountered => Storage\n' + '-'*42 + '\n'
    pokemons_count = {}
    for pokemon in stats:
        species_id = pokemon.get('pokemon_id', 0)
        pokemons_count[species_id] = pokemons_count.get(species_id, 0) + 1
    for pokemon in data:
        species_id = pokemon.get('pokemon_id', 0)
        captured = pokemon.get('times_captured', 0)
        encountered = pokemon.get('times_encountered', 0)
        species = pokemon_list[int(species_id) - 1]
        count = pokemons_count.get(species_id, 0)
        if count > 0:
            content += '{} {}: {}/{} => {}\n'.format(species_id, species, captured, encountered, count)
    return content


# --- main function ---
def main():
    config = init_config()
    location = Location(33.74168493949062,-118.10637474060057)
    api = pgoapi.PGoApi()
    
    try:
        if not api.login(
            config.auth_service,
            config.username,
            config.password,
            location.latitude,
            location.longitude,
            location.altitude):
            raise exceptions.AuthException('Login failed')
        
        request = api.create_request()
        request.get_player()
        request.get_inventory()
        response = request.call()
        
        enable_rawdata = False
        try:
            if int(config.rawdata) > 0:
                enable_rawdata = True
        except ValueError as e:
            pass        
        if enable_rawdata:
            with open('raw_data_{}.json'.format(current_logfile), 'w') as fileout:
                fileout.write(pprint.PrettyPrinter(indent = 4).pformat(response))
        
        inventory_items = response['responses']['GET_INVENTORY']['inventory_delta']['inventory_items']
        player_data = response['responses']['GET_PLAYER']['player_data']
        player_stats = None
        
        pokemons = []
        stats = []
        egg_incubators = []
        items = []
        candies = []
        others = []
        
        item_count = 1
        
        for item in inventory_items:
            if 'pokedex_entry' in item['inventory_item_data']:
                pokemons.append(item['inventory_item_data']['pokedex_entry'])
            elif 'pokemon_data' in item['inventory_item_data']:
                stats.append(item['inventory_item_data']['pokemon_data'])
            elif 'egg_incubators' in item['inventory_item_data']:
                egg_incubators.append(item['inventory_item_data']['egg_incubators'])
            elif 'item' in item['inventory_item_data']:
                items.append(item['inventory_item_data']['item'])
                item_count += item['inventory_item_data']['item'].get('count', 0)
            elif 'candy' in item['inventory_item_data']:
                candies.append(item['inventory_item_data']['candy'])
            elif 'player_stats' in item['inventory_item_data']:
                player_stats = item['inventory_item_data']['player_stats']
            else:
                others.append(item['inventory_item_data'])
        
        content = 'Data from Your Pokemon Go Account\n\n'
        content += player_infomation(player_stats, player_data, len(stats), item_count)
        content += pokemon_candies(candies)
        content += player_item_list(items)
        content += pokedex(pokemons, stats)
        
        with open('player_stats_{}.txt'.format(current_logfile), 'w') as fileout:
            fileout.write(content)
                
        
        pokemon_stats(stats)
        
        print('             Done! :)\n \
            Check all the extracted data in the PogoExtractor directory.\n{} \
            * player_stats_{}.txt\n \
            * pokemon_stats_{}.csv\n'.format(
                '             * raw_data_{}.txt\n'.format(current_logfile) if enable_rawdata else '',
                current_logfile,
                current_logfile))
                
    except exceptions.AuthException as e:
        print(e.args[0])
    except exceptions.NoPlayerPositionSetException as e:
        print('latitude, longitude, and altitude are required')
    except exceptions.NotLoggedInException as e:
        print('not logged in')
    except exceptions.EmptySubrequestChainException as e:
        print('empty request list')
        

# --- the first ---
if __name__ == '__main__':
    main()
