
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pokemon import PokemonParser

def PokemonDexCrawler(url, headers, sub_id=''):
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    info = soup.find("div", attrs={"class": "pokemon-detail"})
    pokemon = None
    if info is not None:
        pokemon = PokemonParser(info)
        pokemon["子编号"]=sub_id
        pokemon["url"]=url
    return pokemon


def PokemonDexWriter(pokedex):
    result = []
    for p in pokedex:
        result.append(
            [
                p["编号"],p["子编号"],
                p["名称"],p["子名称"],
                p["属性1"],p["属性2"],
                p["身高"],p["体重"],
                p["url"]
                ]
            )
    title = "data.xlsx"
    df = pd.DataFrame(result)
    df.to_excel(
        title,
        sheet_name="pokemon",
        index=False,
        header=[
            "编号", "子编号",
            "名称", "子名称",
            "属性1", "属性2",
            "身高", "体重",
            "url"]
        )
    print("Saving %d pokemons to PokemonDex..." % len(pokedex))
