from pokedex import PokemonDexCrawler, PokemonDexWriter
from utils import GetPokemonUrl
import time

pokedex_url = "https://www.pokemon.cn/play/pokedex/"
headers = {
       "Referer": "http://localhost:8888/",
       "Upgrade-Insecure-Requests": "1",
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
   }


def main():
    index = 1
    flag = True
    pokedex = []
    print("Starting to get pokemon...")
    while flag:
        pokemon_url = GetPokemonUrl(pokedex_url, index)
        pokemon = PokemonDexCrawler(pokemon_url, headers)
        if pokemon is None:
            flag=False
        else:
            pokedex.append(pokemon)
            sub_index = 1
            while pokemon is not None:
                pokemon_url = GetPokemonUrl(pokedex_url, index, str(sub_index))
                pokemon = PokemonDexCrawler(pokemon_url, headers, str(sub_index))
                if pokemon is not None:
                    pokedex.append(pokemon)
                    sub_index += 1
            index += 1
        if index % 10 == 0:
            print("Get %d Pokemons at %s!" % (len(pokedex), time.strftime('%H:%M:%S')))
        if index % 100 == 0:
            PokemonDexWriter(pokedex)
    PokemonDexWriter(pokedex)


if __name__ == "__main__":
    main()
