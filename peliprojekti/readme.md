# Ohjelmisto 1 - Peliprojekti

**Edi Pajanen**

## Tietoa

Pelin ohjeet ja tavoitteet ovat Python Exercises -kansion intro.txt ja ohjeet.txt -tiedostoissa.

Pelissä otetaan erityisesti kaksi kestävän kehityksen tavoitetta huomioon:

6: Puhdas vesi ja sanitaatio

Pelissä aiheena on Suomen "janovuodet" noin 2600-luvulla.


13: Ilmastotekoja

...ei pelin maailmassa juurikaan tehty menneisyydessä. Tämän vuoksi miljöö kuvaa ilmastonmuutoksen aiheuttamaa katastrofia


**Rakenne**

    Peliprojekti

    |- esineet (mahtuu pelaajan tavaraluetteloon tai huoneeseen, voi lukea ja käyttää)

        |- __init__.py (ei ilmeisesti pakollinen, mutta varmuuden vuoksi täällä)

        |_ esine.py (sisältää esine-luokan ja kartoille, kirjoille ym. käytettävän luettava-alaluokan. jokaisella on tunnusluku, id, jota käytetään tallentamiseen)

    |- huoneet (sisältää esineitä, mekanismeja ja pelaajan, huoneita voi kiinnittää toisiinsa neljässä ilmansuunnassa ja niiden neljässä ilmansuunnassa voi olla este)

        |- __init__.py (ei ilmeisesti pakollinen, mutta varmuuden vuoksi täällä)

        |_ huone.py (sisältää huone-luokan, kartan rajana toimivan tyhjä-alaluokan ja korjaa huoneet -metodin, joka varmistaa, ettei huoneiden yhteydet riko fysiikan lakeja. jokaisella on tunnusluku, id, jota käytetään tallentamiseen)

    |- mekanismit (eivät mahdu pelajaan tavaraluetteloon, mutta mahtuvat huoneeseen, voivat vaatia esineen toimiakseen)

        |- __init__.py (ei ilmeisesti pakollinen, mutta varmuuden vuoksi täällä)

        |_ mekanismi.py (sisältää mekanismi-luokan ja este-alaluokan, jolla tukitaan huoneiden ilmansuuntia)

    |- main.py (päävalikko, tallentaminen, lataaminen ja itse peli)

    |_ pelaaja.py (nimi, tavaraluettelo ja sijainti, voi liikkua huoneesta toiseen sekä käyttää esineitä, ja mekanismeja)
    