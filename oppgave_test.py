import pytest

from notebook_loader import last_notebook

oppgave = last_notebook("oppgave")

TEKST1 = 'Det var en kald morgen i februar da klassen samlet seg i matematikkrommet for første gang etter ferien. Læreren hadde skrevet en lang rekke tall på tavla, og ingen forsto helt hva de betydde. Etter en stund rakte en av elevene opp hånda og sa at det kanskje var en hemmelig melding. Det viste seg at hun hadde rett. Hver bokstav var byttet ut med en annen bokstav som lå et fast antall plasser lenger fram i alfabetet. For å finne nøkkelen telte elevene hvor ofte hver bokstav forekom i meldingen, og de sammenliknet med hvor vanlige bokstavene er i vanlig norsk tekst. Den bokstaven som dukket opp oftest, var nesten helt sikkert en e.'
TEKST2 = 'Programmering handler om å dele et stort problem opp i mange små problemer som datamaskinen kan løse ett etter ett. Det er lurt å teste koden ofte, og å lese feilmeldingene nøye før man endrer noe. Når programmet endelig virker, er det en god følelse som gjør det verdt alle feilene underveis.'

def krypter(tekst, skift):
    """Krypterer tekst med Cæsarchifferet. Bare a–z og A–Z flyttes, alt annet beholdes."""
    resultat = ""
    for tegn in tekst:
        if "a" <= tegn <= "z":
            resultat += chr((ord(tegn) - ord("a") + skift) % 26 + ord("a"))
        elif "A" <= tegn <= "Z":
            resultat += chr((ord(tegn) - ord("A") + skift) % 26 + ord("A"))
        else:
            resultat += tegn
    return resultat


@pytest.mark.parametrize("tekst", [TEKST1, TEKST2], ids=["tekst1", "tekst2"])
@pytest.mark.parametrize("skift", [0, 1, 3, 7, 13, 20, 25])
def test_knekk(tekst, skift):
    assert oppgave.knekk(krypter(tekst, skift)) == skift
