# PogoExtractor

Use PogoExtractor to extract all data such as **IVs**, **candies** and **items** from your Pokemon Go account

This is a simple tool for you, Pokémon trainer/master, to know some useful information from your Pokémon Go such as your Pokémons' IV (individual value). Stardust is difficult to get, keep it for your best Pokémons.

## Features

* Pokemon Stats

  * ID
  * Nickname
  * Species Name
  * CP (Combat Power)
  * HP
  * Weight
  * Height
  * IV (attack, defense, stamina, total, potential)
  * Moves (fast and charge)

* Player Stats

  * Name
  * Level
  * Experience (and ??? XP to Level Up)
  * Pokecoin
  * Stardust
  * Pokemon Storage
  * Bag Storage
  * Walk Distance
  * Hatched Eggs
  * Visited Pokestops
  * Captured and Encountered Pokemons
  * Thrown Pokeballs
  * Pokedex

* Candies, Items, and Pokedex

* Despite all this, you can also obtain raw data to study!

## Usage

```
python pogoextractor.py -a <ptc,google> -u "<username>" -p "<password>" -rd <0,1>
```

#### Method 1

Run this command in your Terminal.

```
python pogoextractor.py -a ptc -u "pokemongo" -p "p@55w0rd"
```

#### Method 2

Or, you can simply edit the provided `config.json` file with the *auth serivce*, your *username* and *password* before running command below:

```
python pogoextractor.py
```

### Raw Data

`-rd` argument is used to extract the *raw data* in `JSON` format. For example,

```
python pogoextractor.py -a ptc -u "pokemongo" -p "p@55w0rd" -rd 1
```

### Output

After executing the command, you will obtain 2 or 3 files as shown in the screenshot.

* `player_stats.txt`
* `pokemon_stats.csv`
* `raw_data.json`

![alt "Output Files"](https://raw.githubusercontent.com/joaodragao/PogoExtractor/master/screenshot.png)

## Requirements

* Python 2 or 3
* and `pip install --upgrade -r requirements.txt`

## Installation

Simply, download or clone the repository.

```
git clone https://github.com/joaodragao/PogoExtractor
cd PogoExtractor
```

Don't forget to edit the `config.json` file before run the last command.

```
python pogoextractor.py
```


## Credits

* [tejado](https://github.com/tejado) for the API
* [Mila432](https://github.com/Mila432/Pokemon_Go_API) for the login secrets
* [elliottcarlson](https://github.com/elliottcarlson) for the Google Auth PR
* [AeonLucid](https://github.com/AeonLucid/POGOProtos) for improved protos
* [AHAAAAAAA](https://github.com/AHAAAAAAA/PokemonGo-Map) for parts of the s2sphere stuff

## License

The MIT License (MIT)

Copyright (c) 2016 joaodragao

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.