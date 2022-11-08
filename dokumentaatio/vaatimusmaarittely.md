# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla pystyy pelaamaan miinaharava -peliä eri vaikeusasteilla, luomaan käyttäjätunnuksen ja tarkkastelemaan parhaat tulokset listauksia. 

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri päänäkymästä

Sovellus aukeaa kirjautumisnäkymään, jossa on mahdollista rekisteröityä käyttäjäksi tai kirjautua jo aiemmin luodulla tunnuksella. Tämän jälkeen 
sovellus avautuu näkymään josta on valittavissa kolmen eri vaikeusasteen peliä, avata parhaat tulokset -sivu, kirjautua ulos, ja sulkea sovellus

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 5 merkkiä
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen

- Sovellus avautuu näkymään josta on valittavissa kolmen eri vaikeusasteen peliä, parhaat tulokset -sivu, 
uloskirjautuminen, tai sovelluksen sulkeminen. 

#### Pelitila

- Vaikeusasteen valittuaan käyttäjälle avautuu miinaharava-pelin pelinäkymä, jossa miinojen määrä ja alueen koko määrittyvät vaikeusasteen mukaan. 
Näkymässä on myös pelikello, sekä merkkaamattomien miinojen määrä. 
- Käyttäjä voi avata pelialueen ruutuja, jonka seurauksena käyttäjä voi osua miinaan, tai avata ruudun, joka paljastaa viereisissä ruuduissa olevien miinojen määrän
- Käyttäjä voi myös merkata avaamattomia ruutuja miinojen sijaintien muistamisen helpottamiseksi. 

#### Parhaat tulokset -näkymä

- Käyttäjälle avautuu pelin loputtua tai alkuvalikosta valittaessa parhaat tulokset listaus, jossa on näkyvillä 10 parasta tulosta kaikilta käyttäjiltä, sekä
parhaat 10 tulosta vain kirjautuneelta käyttäjältä. 

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Miellyttävämpi graafinen toteutus
- Mahdollisuus valita miinojen määrä ennen peliä ja/tai aikaraja jonka puitteissa peli on voitettava. 
