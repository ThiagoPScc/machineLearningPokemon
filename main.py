import requests
#teste de conexão
url = "https://pokeapi.co/api/v2/pokemon/252"
resp = requests.get(url)
print(resp.status_code)
print(resp)

#função para poder coletar os pokemons
def addPok(dicionarioPokemons, pokemonAtual):
  status = {}
  tipos = {}
  nomePokemon = pokemonAtual["name"]
  try:
    for stat in pokemonAtual["stats"]:
      status.update({stat["stat"]["name"]: stat["base_stat"]})
    if possuiUmTipo(pokemonAtual):
      tipos.update({"tipo1":pokemonAtual["types"][0]["type"]["name"], "tipo2":None})
    else:
        tipos.update({"tipo1":pokemonAtual["types"][0]["type"]["name"], "tipo2":pokemonAtual["types"][1]["type"]["name"]})
    dicionarioPokemons[nomePokemon] = {"status":status, "tipos":tipos}
  except Exception as erro:
    print("Um erro ocorreu durante a inserção de dados")
    print(erro)

def possuiUmTipo(pokemonAtual):
  tamanho = len(pokemonAtual["types"])
  if tamanho == 1:
    return True
  else:
    return False

def coletarDadosApi():
  dicionarioPokemons = {}
  for id in range (1,387):
    try:
      respostaCompleta = requests.get( f"https://pokeapi.co/api/v2/pokemon/{id}")
      respostaCompleta.raise_for_status()
      pokemonAtual = respostaCompleta.json()
      addPok(dicionarioPokemons,pokemonAtual)
    except Exception as erro:
      print("erro: ",erro)
  print(dicionarioPokemons)
  return(dicionarioPokemons)

  #código:

  dicionarioFinal = coletarDadosApi()
  print(dicionarioFinal)