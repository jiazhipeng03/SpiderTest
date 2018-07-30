from lxml import html
from lxml import etree
import csv

def saveCSV(dict, file = 'new.csv'):
    with open(file, 'w', newline='') as f:
        f_csv = csv.writer(f)
        row = ['英雄']
        row +=['克制']
        row += [' '] * 4
        row += ['被克制']
        row += [' '] * 4
        row += ['配合']
        f_csv.writerow(row)
        for hero in dict:
            row = [hero] + dict[hero][0] + dict[hero][1] + dict[hero][2]
            f_csv.writerow(row)

def saveXML(dict, file = 'new.xml'):
    root = etree.Element('Root')
    for heroName in dict:
        heroNode = etree.SubElement(root, 'HeroName')
        heroNode.text = heroName
        #Hero.text = heroName
        for bestversus in dict[heroName][0]:
            etree.SubElement(heroNode, 'BestVersus').text = bestversus
        for worstversus in dict[heroName][1]:
            etree.SubElement(heroNode, 'WorstVersus').text = worstversus
        for bestteammate in dict[heroName][2]:
            etree.SubElement(heroNode, 'BestTeammate').text = bestteammate
    tree = etree.ElementTree(root)
    tree.write(file, pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == '__main__':
    dic = dict()
    dic['a'] = [[1,2,3],[1,2,3],[1,2,3]]
    dic['b'] = [[4,5,6],[4,5,6],[4,5,6]]
    #saveXML(dic)
    saveCSV(dic)