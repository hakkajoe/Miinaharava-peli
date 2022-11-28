# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla pystyy pelaamaan miinaharava -peliä eri vaikeusasteilla, luomaan käyttäjätunnuksen sekä tarkastelemaan parhaat tulokset -listaa. 

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri päänäkymästä

Sovellus aukeaa kirjautumisnäkymään, jossa on mahdollista rekisteröityä käyttäjäksi, kirjautua jo aiemmin luodulla tunnuksella tai sulkea sovellus erillisestä lopetusnapista. Tämän jälkeen 
sovellus avautuu näkymään josta on valittavissa kolmen eri vaikeusasteen peliä, avata parhaat tulokset -sivu, kirjautua ulos, ja sulkea sovellus

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen /tehty
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 1 merkki /tehty
- Käyttäjä voi kirjautua järjestelmään /tehty
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle /tehty
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä /tehty
- Käyttäjä voi sulkea sovelluksen erillisestä sovelluksen napista. /tehty

### Kirjautumisen jälkeen

- Sovellus avautuu näkymään josta on valittavissa aloitettavan pelin vaikeusasteen määritys, parhaat tulokset -sivu, 
uloskirjautuminen, tai sovelluksen sulkeminen. /tehty

### Pelitila

- Vaikeusasteen valittuaan käyttäjälle avautuu miinaharava-pelin pelinäkymä, jossa miinojen määrä ja alueen koko määrittyvät vaikeusasteen mukaan. 
Näkymässä on myös pelikello, sekä merkkaamattomien miinojen määrä. 
- Käyttäjä voi avata pelialueen ruutuja, jonka seurauksena käyttäjä voi osua miinaan, tai avata ruudun, joka paljastaa viereisissä ruuduissa olevien miinojen määrän /tehty
- Käyttäjä voi myös merkata avaamattomia ruutuja miinojen sijaintien muistamisen helpottamiseksi. /tehty

### Pelin jääkeinen loppunäkymä

- Pelaaja näkee saavuttamansa tuloksen, ja voi valita uuden pelin tai palata alkuvalikkoon.

### Parhaat tulokset -näkymä

- Käyttäjä näkee 10 parasta tulosta kaikilta käyttäjiltä. Jokaisella vaikeusasteella on oma tulosnäkymänsä.  

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Miellyttävämpi graafinen toteutus
- Mahdollisuus valita miinojen määrä ennen peliä ja/tai aikaraja jonka puitteissa peli on voitettava. 
