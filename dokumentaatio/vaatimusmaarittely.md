# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla pystyy pelaamaan miinaharava -peliä eri vaikeusasteilla, luomaan käyttäjätunnuksen sekä tarkastelemaan parhaat tulokset -listaa. 

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri päänäkymästä

Sovellus aukeaa kirjautumisnäkymään, jossa on mahdollista rekisteröityä käyttäjäksi, kirjautua jo aiemmin luodulla tunnuksella tai sulkea sovellus erillisestä lopetusnapista. Tämän jälkeen 
sovellus avautuu näkymään josta on valittavissa kolmen eri vaikeusasteen peliä, avata parhaat tulokset -sivu, kirjautua ulos, ja sulkea sovellus

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen. 
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 1 merkki.
- Käyttäjä voi kirjautua järjestelmään.
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle.
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä.
- Käyttäjä voi sulkea sovelluksen erillisestä sovelluksen napista.

### Kirjautumisen jälkeen

- Sovellus avautuu näkymään josta on valittavissa aloitettavan pelin vaikeusasteen määritys, parhaat tulokset -sivu, 
uloskirjautuminen, tai sovelluksen sulkeminen.

### Pelitila

- Vaikeusasteen valittuaan käyttäjälle avautuu miinaharava-pelin pelinäkymä, jossa miinojen määrä ja alueen koko määrittyvät vaikeusasteen mukaan.
- Käyttäjä voi avata pelialueen ruutuja, jonka seurauksena käyttäjä voi osua miinaan, tai avata ruudun, joka paljastaa viereisissä ruuduissa olevien miinojen määrän.
- Käyttäjä voi myös merkata avaamattomia ruutuja miinojen sijaintien muistamisen helpottamiseksi.

### Pelin jääkeinen loppunäkymä

- Pelaaja näkee saavuttamansa tuloksen, ja voi valita uuden pelin tai palata alkuvalikkoon.

### Parhaat tulokset -näkymä

- Käyttäjä näkee 10 parasta tulosta kaikilta käyttäjiltä. Jokaisella vaikeusasteella on oma tulosnäkymänsä.

## Jatkokehitysideoita

Perusversion jälkeen sovellusta voi täydentää ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Miellyttävämpi graafinen toteutus
- Mahdollisuus valita miinojen määrä ennen peliä ja/tai aikaraja jonka puitteissa peli on voitettava. 
- Äänet pelin eri tapahtumille
- Tila pelialueen yläpuolelle, josta näkee pelikellon sekä merkattujen miinojen määrän.
- Paremmin toteutettu rakenne pelille, jotta koodia olisi helpompaa testata/muokata
