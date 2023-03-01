from utils import RemoveBrackets

def NameInfoParser(soup):
    name_info = soup.find_all("div", attrs={"class": "pokemon-slider__main"})
    info = RemoveBrackets(str(name_info))
    info = info.split()
    number, name, subname = info[1], info[2], info[3]
    if subname == "]":
        subname = ""
    return number, name, subname

def TypeParser(soup):
    type_info = soup.find_all("div", attrs={"class": "pokemon-main__upper-left"})
    info = RemoveBrackets(str(type_info))
    info = info.split()
    type1, type2 = info[2], info[3]
    if type2 == "]":
        type2 = ""
    return type1, type2


def HeightParser(soup):
    height_info = soup.find_all("div", attrs={"class": "pokemon-info__height"})
    info = RemoveBrackets(str(height_info))
    info = info.split()
    height = info[2] + "m"
    return height


def WeightParser(soup):
    weight_info = soup.find_all("div", attrs={"class": "pokemon-info__weight"})
    info = RemoveBrackets(str(weight_info))
    info = info.split()
    weight = info[2] + "kg"
    return weight


def PokemonParser(soup):
    number, name, subname = NameInfoParser(soup)
    type1, type2 = TypeParser(soup)
    height = HeightParser(soup)
    weight = WeightParser(soup)
    pokemon = {
        "编号": number,
        "名称": name,
        "子名称": subname,
        "属性1": type1,
        "属性2": type2,
        "身高": height,
        "体重": weight,
    }
    return pokemon
