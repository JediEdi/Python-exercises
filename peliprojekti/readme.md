# Ohjelmisto 1 - Peliprojekti

**Edi Pajanen**

## Tietoa

**Rakenne**
Peliprojekti
    |- esineet (mahtuu pelaajan tavaraluetteloon tai huoneeseen, voi lukea ja käyttää)
        |- __init__.py (rehellisesti en tiedä, mitä tämä tekee)
        |_ esine.py (sisältää esine-luokan ja kartoille, kirjoille ym. käytettävän luettava-alaluokan)
    |- huoneet (sisältää esineitä, mekanismeja ja pelaajan, huoneita voi kiinnittää toisiinsa neljässä ilmansuunnassa)
        |- __init__.py (rehellisesti en tiedä, mitä tämä tekee)
        |_ huone.py (sisältää huone-luokan ja kartan rajana toimivan tyhjä-alaluokan)
    |- mekanismit (eivät mahdu pelajaan tavaraluetteloon, mutta mahtuvat huoneeseen, voivat vaatia esineen toimiakseen)
        |- __init__.py (rehellisesti en tiedä, mitä tämä tekee)
        |_ mekanismi.py (sisältää mekanismi-luokan. tarkemmat toiminnot selvitän projektin edetessä tarpeen mukaan)
    |- main.py (päävalikko ja itse peli)
    |_ pelaaja.py (nimi, tavaraluettelo ja sijainti, voi liikkua huoneesta toiseen sekä käyttää esineitä, ja mekanismeja)