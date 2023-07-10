import unittest
from duckduckgo_translate import Translator

long_text = """
There are varying accounts as to Valerian's fate following his capture at the hands of Shapur.

Some scholars claim Shapur sent Valerian and some of his army to the city of Bishapur, where they lived in relatively good conditions. Shapur used the remaining soldiers in engineering and development plans, as the Romans were skilled tradesmen and artisans. Band-e Kaisar (Caesar's dam) is one of the remnants of Roman engineering located near the ancient city of Shushtar.

According to another source (Lactantius), Shapur humiliated Valerian, using the former emperor as a human stepping-stool while mounting his horse. He was reportedly kept in a cage and was humiliated for the Persian emperor's pleasure, according to Aurelius Victor. Upon his death, Valerian's body was allegedly skinned and stuffed with, depending on which account, manure or straw, to produce a trophy of Roman submission preserved in a Persian temple.

However, there are also accounts that stipulate he was treated with respect, and that allegations of torture may have been fabricated by Christian historians of late antiquity to show the perils that befell persecutors of Christianity.

Following Valerian's capture, Shapur took the city of Caesarea and deported some 400,000 of its citizens to the southern provinces of the Sassanian Empire. He then raided Cilicia, but he was finally repulsed by a Roman force that was rallied by Macrianus, Callistus and Odenathus of Palmyra.

Valerian's defeat at Edessa became the catalyst for a series of revolts that would lead to the temporary fragmentation of the Roman Empire. In the East, Macrianus used his control of Valerian's treasury to proclaim his sons Macrianus Minor and Quietus as emperors. Along the Danubian frontier, Ingenuus and Regalianus were also proclaimed emperors. In the West, the Roman governor Postumus took advantage of Gallienus' distraction to murder the Imperial heir, Saloninus, and take control of what is now called the Gallic Empire"""

long_text_translated = """Il existe différents récits sur le sort de Valérian après sa capture par Shapur. Certains érudits affirment que Shapur a envoyé Valérian et une partie de son armée dans la ville de Bishapur, où ils ont vécu dans des conditions relativement bonnes. Shapur a utilisé les soldats restants dans les plans d'ingénierie et de développement, car les Romains étaient des artisans qualifiés. Band-e Kaisar (le barrage de César) est l'un des vestiges de l'ingénierie romaine situé près de l'ancienne ville de Shushtar. Selon une autre source (Lactance), Shapur a humilié Valérian, utilisant l'ancien empereur comme un tabouret humain tout en montant son cheval. Il aurait été gardé dans une cage et aurait été humilié pour le plaisir de l'empereur perse, selon Aurelius Victor. À sa mort, le corps de Valérian aurait été écorché et bourré, selon le compte, de fumier ou de paille, pour produire un trophée de soumission romaine conservé dans un temple persan."""

class TestStringMethods(unittest.TestCase):
    def test_english_to_azerbaijani(self):
        translator = Translator()

        translated = translator.translate('Say hello to my little friend', dest='az')
        text = translated.text
        self.assertEqual(text.lower(), 'balaca dostuma salam de')

    def test_upper(self):
        translator = Translator()

        translated = translator.translate('Hello World', dest='de')
        text = translated.text
        self.assertEqual(text.lower(), 'hallo welt')

    def test_unicode(self):
        translator = Translator()

        translated = translator.translate('안녕하세요', src='ko', dest='ja')
        self.assertEqual(translated.text, 'じゃない')

    def test_language_name(self):
        translator = Translator()

        translated = translator.translate('Hello World', src='ENGLISH', dest='HUNGaRiAn')
        self.assertEqual(translated.text.lower(), 'helló világ')

    def test_language_name_with_space(self):
        translator = Translator()

        translated = translator.translate('Hello', src='en', dest='chinese simplified')
        self.assertEqual(translated.dest, 'zh-Hans')
    
    def test_translate_without_src(self):
        translator = Translator()

        translated = translator.translate('Hello World', dest='danish')
        self.assertEqual(translated.text, 'Hej verden')

    def test_detected_src(self):
        translator = Translator()

        translated = translator.translate('Hola Mundo', dest='en')
        self.assertEqual(translated.detected, 'es')

    def test_change_vqt(self):
        translator = Translator()

        old_vqd = translator.vqd
        translator._change_vqd()
        self.assertNotEqual(old_vqd, translator.vqd)

    def test_change_useragent(self):
        translator = Translator()

        old_useragent= translator.headers['User-Agent']
        translator._change_useragent()
        self.assertNotEqual(old_useragent, translator.headers['User-Agent'])

    def test_long_text(self):
        translator = Translator()

        translated = translator.translate(long_text, src='en', dest='fr')
        self.assertEqual(translated.text, long_text_translated)

if __name__ == '__main__':
    unittest.main()
