# Ohjelmistotekniikka, harjoitustyö

## Miinaharava-peli

### Dokumentaatio

- [Vaatimusmaarittely](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Tyoaikakirjanpito](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/hakkajoe/ot-harjoitusty-/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Release](https://github.com/hakkajoe/ot-harjoitusty-/releases/tag/viikko5)

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
