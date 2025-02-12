import requests
from bs4 import BeautifulSoup
#S&P 500
#extraction du site web et sa structure
url = "https://en.wikipedia.org/wiki/S%26P_500"
response = requests.get(url)
structure = BeautifulSoup(response.text, 'html.parser')

#trouver le tableau contenant les données et définir l'image parmi toutes
table = structure.find('table', {'class': 'wikitable'})
images = structure.findAll('img')
if len(images) > 9:
    img_url = "https:" + images[9]['src']

#définir chaque variable comme une liste pour y stocker les valeurs
years = []
annual_returns = []
change_in_index = []
value_one_dollar = []

#définir toutes les lignes du tableau
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
#définition des cellules et de variables dans le tableau
    if len(cells) >= 4:
        year = cells[0].get_text(strip=True)
        annual_return = cells[1].get_text(strip=True)
        change_index = cells[2].get_text(strip=True)
        value_dollar = cells[3].get_text(strip=True)

    #vérifier que l'année est un nombre et est entre 2007 et 2023
        if year.isdigit() and 2007 <= int(year) <= 2023:
            years.append(year)
            annual_returns.append(annual_return)
            change_in_index.append(change_index)
            value_one_dollar.append(value_dollar)

#générer le fichier HTML
contenu_html = """<!DOCTYPE html>
<html lang='fr'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<header class="page-header"> <h1>S&P 500 (2007 - 2023)</h1> </header>
<style>
body { font-family: Arial, sans-serif; margin: 20px; }
header {background-color: #04AA6D; padding: 20px 0; text-align: center; color: white; font-size: 1.8em; font-weight: bold;}
h1 { text-align: center; }
table { width: 50%; border-collapse: collapse; margin: 50px 25%; }
th, td { padding: 10px; text-align: center; border: 1px solid #ddd; }
th { background-color: #04AA6D; color: white; }
tr:nth-child(even) { background-color: #f2f2f2; }
tr:hover {background-color: #e0e0e0;}
button { margin: 20px; margin-left: 33%; padding: 20px 200px; font-size: 25px;transition-duration: 0.4s; cursor: pointer;}
button:hover {background-color: #913042; color: white;}

</style>
</head>
<body>
"""

#image
image = f"<img src='{img_url}' alt='rendements annuels du S&P 500' style='display:block; margin:auto; margin-top: 25px; width:60%;'/>\n"

#construction du tableau
tableau = """<table>
<tr><th>Année</th><th>Rendement Annuel </th><th>Changement de l'Index</th><th>Valeur d'un dollar investi en 1970</th></tr>
"""

for year, annual_return, change, value_dollar in zip(years, annual_returns, change_in_index, value_one_dollar):
    tableau += f"<tr><td>{year}</td><td>{annual_return}</td><td>{change}</td><td>{value_dollar}</td></tr>\n"

tableau += "</table>\n"

bouton = """<button onclick="window.location.href='cac40.html'">CAC 40 (France)</button>\n"""
bouton_accueil = """<button style="margin: 20px; margin-left: 15px; padding: 20px 100px; font-size: 15px; transition-duration: 0.4s; cursor: pointer; background-color: #D3D3D3" onclick="window.location.href='index.html'"><span>Accueil</span></button>\n"""


#write et enregistrement du fichier
#s'assurer de mettre le bon chemin d'accés pour l'enregistrement du fichier
with open("/Users/kaledgoatache/Desktop/kaled_sacha_opw/sp500.html", "w") as fichier:
    fichier.write(contenu_html + bouton_accueil + image + tableau + bouton)

    fichier.write("</body>\n")
    fichier.write("</html>\n")


print("Le fichier sp500.html a été créé.")

#CAC40

#extraction du site web et sa structure
url1 = "https://en.wikipedia.org/wiki/CAC_40"
response1 = requests.get(url1)
structure1 = BeautifulSoup(response1.text, 'html.parser')

#trouver le tableau contenant les données et définir l'image parmi toutes
tables1 = structure1.findAll('table', {'class': 'wikitable'})
table1 = tables1[2]

#chercher image dans autre page image
url2 = "https://fr.wikipedia.org/wiki/CAC_40"
response2 = requests.get(url2)
structure2 = BeautifulSoup(response2.text, 'html.parser')
images1 = structure2.findAll('img')
if len(images1) > 2:
    img_url1 = "https:" + images1[8]['src']
#définir chaque variable comme une liste pour y stocker les valeurs
years1 = []
valeur = []
change_in_index1 = []

#définir toutes les lignes du tableau
for row1 in table1.find_all('tr')[1:]:
    cells1 = row1.find_all('td')
#définition des cellules et de variables dans le tableau
    if len(cells1) >= 4:
        year1 = cells1[0].get_text(strip=True)
        valeur_1 = cells1[1].get_text(strip=True)
        change_index1 = cells1[3].get_text(strip=True)

    #vérifier que l'année est un nombre et est entre 2007 et 2023
        if year1.isdigit() and 2007 <= int(year1) <= 2023:
            years1.append(year1)
            valeur.append(valeur_1)
            change_in_index1.append(change_index1)


#générer le fichier HTML
contenu_html1 = """<!DOCTYPE html>
<html lang='fr'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<header class="page-header"> <h1>CAC 40 (2007 - 2023)</h1> </header>
<style>
body { font-family: Arial, sans-serif; margin: 20px; }
header {background-color: #913042; padding: 20px 0; text-align: center; color: white; font-size: 1.8em; font-weight: bold;}
h1 { text-align: center; }
table { width: 50%; border-collapse: collapse; margin: 50px 25%; }
th, td { padding: 10px; text-align: center; border: 1px solid #ddd; }
th { background-color: #913042; color: white; }
tr:nth-child(even) { background-color: #f2f2f2; }
tr:hover {background-color: #e0e0e0;}
button { margin: 20px; margin-left: 33%; padding: 20px 200px; font-size: 25px;transition-duration: 0.4s; cursor: pointer;}
button:hover {background-color: #04AA6D;color: white;}


</style>
</head>
<body>
"""

#image
image1 = f"<img src='{img_url1}' alt='image cac40' style='display:block; margin:auto; width:30%;'/>\n"

#construction du tableau
tableau1 = """<table>
<tr><th>Année</th><th>Valeur en €</th><th>Changement de l'Index (%)</th></tr>
"""

for year1, valeur_1, change_index1 in zip(years1, valeur, change_in_index1):
    tableau1 += f"<tr><td>{year1}</td><td>{valeur_1}</td><td>{change_index1}</td></tr>\n"

tableau1 += "</table>\n"

bouton1 = """<button onclick="window.location.href='sp500.html'">S&P 500 (USA)</button>\n"""



#write et enregistrement du fichier
#s'assurer de mettre le bon chemin d'accés pour l'enregistrement du fichier'
with open("/Users/kaledgoatache/Desktop/kaled_sacha_opw/cac40.html", "w") as fichier:
    fichier.write(contenu_html1 + bouton_accueil +  image1 + tableau1 + bouton1)

    fichier.write("</body>\n")
    fichier.write("</html>\n")


print("Le fichier cac40.html a été créé.")

#design accueil


contenu_html3 = """<!DOCTYPE html>
<html lang="fr">
<head>
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 2;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 40px 0;
    font-size: 30px;
}

.container {
    display: flex;
    height: 100vh;
}

.left-column {
    width: 33%;
    padding: 20px;
    background-color: #2c3e50;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.left-column button {
    width: 80%;
    padding: 50px;
    margin-bottom: 10px;
    background-color: #34495e;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 30px;
}

.left-column button:hover {
    background-color: #2980b9;
}

.right-column {
    width: 67%;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100vh;
}

.right-column p {
    font-size: 18px;
    margin-bottom: 20px;
    text-align: center;
}

.right-column .image {
    width: 100%;
    height: auto;
    display: block;
    margin-top: 20px;
    margin-left: auto;
    margin-right: auto;
}

</style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trader Workstation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- En-tête avec le titre du site -->
    <header>
        <h1>Trader Workstation</h1>
    </header>

    <!-- Conteneur principal divisé en deux colonnes -->
    <div class="container">

        <!-- Colonne de gauche avec les boutons de navigation -->
        <div class="left-column">
            <button onclick="window.location.href='cac40.html'">CAC 40 (FRA)</button>
            <button onclick="window.location.href='sp500.html'">S&P 500 (USA)</button>
            <button onclick="window.location.href='https://en.wikipedia.org/wiki/Nikkei_225'">NIKKEI 225 (JAP)</button>
            <button onclick="window.location.href='https://en.wikipedia.org/wiki/DAX'">DAX 40 (GER)</button>
            <button onclick="window.location.href='https://en.wikipedia.org/wiki/FTSE_100_Index'">FTSE 100 (UK)</button>
            <button onclick="window.location.href='https://en.wikipedia.org/wiki/Índice_Bursátil_de_Capitalización'">IBVC (VEN)</button>
        </div>

        <div class="right-column">
    <section>
        <p>Bienvenue sur Trader Workstation, la plateforme idéale pour améliorer votre expérience de trading. Accédez à une gamme complète d'outils de trading, d'analyses en temps réel et de ressources éducatives adaptées à tous les niveaux.</p>

        <p>Grâce à nos graphiques personnalisables, indicateurs techniques avancés et alertes de marché, vous pouvez suivre les tendances et gérer vos investissements avec précision. Profitez également de nos formations, webinaires et ressources pour approfondir vos connaissances en trading.</p>

        <p>Notre plateforme vous offre aussi des outils de gestion des risques et une automatisation avancée pour optimiser vos stratégies. De plus, notre support client est disponible 24/7 pour vous assister à chaque étape de votre parcours.</p>
    </section>

            <img src="INDICESB.jpeg" class="image">
        </div>
    </div>

    <!-- Script pour gérer la transition automatique du diaporama -->
    <script src="slideshow.js"></script>

</body>
</html>
"""
with open("/Users/kaledgoatache/Desktop/kaled_sacha_opw/index.html", "w") as fichier:
    fichier.write(contenu_html3)
print("Le fichier index.html a été créé.")