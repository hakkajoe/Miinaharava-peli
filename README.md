# Ohjelmistotekniikka, harjoitustyö

## Miinaharava-peli

### Dokumentaatio

- [Käyttöohje]((https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/kayttohje.md)

- [Vaatimusmäärittely](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/testausdokumenttii.md)

- [Release](https://github.com/hakkajoe/ot-harjoitusty-/releases/tag/dec6)

### Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Lähteet

Miinaharava-pelssä käytettävät kuvat ovat lainattu Wikimedia Commons -sivustolta (https://commons.wikimedia.org/wiki/)
