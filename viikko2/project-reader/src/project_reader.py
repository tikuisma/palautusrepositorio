from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        lista = []
        for item in data.values():
            for i in item.values():
                lista.append(i)
                
        toinen = []
        for index in range(len(lista)-2):
            for key in lista[index]:
                toinen.append(lista[index][key])
            index += 1

        name = toinen[0]
        des = toinen[2]
        toinen.pop(0)
        toinen.pop(0)
        toinen.pop(0)
        toinen.pop(0)
        uusi = []
        for inde in range(len(toinen)):
            for key in toinen:
                for k in key.keys():
                    uusi.append(k)
        
        del uusi[0:5]
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        # return Project("Test name", "Test description", [], [])
        return Project(name, des, uusi[0:2], uusi[2:])
