import re

def RemoveBrackets(sentence, mark="<>"):
    pattern = re.compile(r'%s.*?%s' % (mark[0], mark[1]))
    result = re.sub(pattern, "", sentence).strip()
    return result

def GetPokemonUrl(url:str, index:int, sub_index:str = ""):
    pokemon_id = str(index).zfill(3)
    if sub_index!="":
        return url + pokemon_id + "_" + sub_index
    else:
        return url + pokemon_id
