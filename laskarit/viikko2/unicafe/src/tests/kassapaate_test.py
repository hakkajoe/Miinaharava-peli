import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.alku = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_tieto_on_olemassa(self):
        self.assertEqual(self.alku.kassassa_rahaa, 100000)
        self.assertEqual(self.alku.edulliset, 0)
        self.assertEqual(self.alku.maukkaat, 0)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_syo_edullisesti_kateisella(self):
        self.alku.syo_edullisesti_kateisella(250)

        self.assertEqual(str(self.alku.kassassa_rahaa), "100240")
        self.assertEqual(str(self.alku.edulliset), "1")

    def test_syo_edullisesti_kateisella_fail(self):
        self.alku.syo_edullisesti_kateisella(100)

        self.assertEqual(str(self.alku.kassassa_rahaa), "100000")
        self.assertEqual(str(self.alku.edulliset), "0")

    def test_syo_maukkaasti_kateisella(self):
        self.alku.syo_maukkaasti_kateisella(500)

        self.assertEqual(str(self.alku.kassassa_rahaa), "100400")
        self.assertEqual(str(self.alku.maukkaat), "1")

    def test_syo_maukkaasti_kateisella_fail(self):
        self.alku.syo_maukkaasti_kateisella(300)

        self.assertEqual(str(self.alku.kassassa_rahaa), "100000")
        self.assertEqual(str(self.alku.edulliset), "0")

    def test_syo_edullisesti_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        self.alku.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

        self.assertEqual(str(self.alku.kassassa_rahaa), "100000")
        self.assertEqual(str(self.alku.edulliset), "1")
        return True

    def test_syo_edullisesti_kortilla_fail(self):
        self.maksukortti = Maksukortti(100)
        self.alku.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

        self.assertEqual(str(self.alku.kassassa_rahaa), "100000")
        self.assertEqual(str(self.alku.edulliset), "0")
        return False

    def test_syo_maukkaasti_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        self.alku.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

        self.assertEqual(str(self.alku.kassassa_rahaa), "100000")
        self.assertEqual(str(self.alku.maukkaat), "1")
        return True

    def test_syo_maukkaasti_kortilla_fail(self):
        self.maksukortti = Maksukortti(100)
        self.alku.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")

        self.assertEqual(str(self.alku.kassassa_rahaa), "100000")
        self.assertEqual(str(self.alku.maukkaat), "0")
        return False

    def test_lataa_rahaa_kortille(self):
        self.alku.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
        self.assertEqual(str(self.alku.kassassa_rahaa), "100500")

    def test_lataa_rahaa_kortille_fail(self):
        self.alku.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(str(self.alku.kassassa_rahaa), "100000")