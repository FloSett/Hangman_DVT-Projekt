# ============================================================
#                      HANGMAN - Komplett
# ============================================================

import random                                                                                     # Wird benötigt um ein zufälliges Wort aus der Liste auszuwählen
#import os                                                                                        # Wird benötigt für Betriebssystem-Funktionen


# ── ANSI Farbcodes ───────────────────────────────────────────
# Wörterbuch mit allen wählbaren Farben: Schlüssel = Zahl, Wert = (ANSI-Code, Farbname)
FARBEN = {
    "1": ("\033[31m", "Rot"),                                                                     # ANSI-Code für rote Schrift
    "2": ("\033[32m", "Grün"),                                                                    # ANSI-Code für grüne Schrift
    "3": ("\033[33m", "Gelb"),                                                                    # ANSI-Code für gelbe Schrift
    "4": ("\033[34m", "Blau"),                                                                    # ANSI-Code für blaue Schrift
    "5": ("\033[35m", "Lila"),                                                                    # ANSI-Code für lila Schrift
    "6": ("\033[36m", "Cyan"),                                                                    # ANSI-Code für cyanfarbene Schrift
    "7": ("\033[37m", "Weiß"),                                                                    # ANSI-Code für weiße Schrift
}
RESET = "\033[0m"                                                                                 # ANSI-Code um die Farbe zurückzusetzen (auf Standard)


def farbe(text, farbcode):
    # Gibt den übergebenen Text umhüllt mit dem Farbcode und Reset zurück
    return f"{farbcode}{text}{RESET}"




# ─────────────────────────────────────────────
#  TEIL 1: Spieler-Verwaltung & Wort-Erzeugung
# ─────────────────────────────────────────────

def eingabe_Spieler():
    # Fragt die Anzahl der Spieler (2-5), deren Namen und Lieblingsfarbe ab
    # Gibt eine Liste von Woerterbüchern zurück: 
    # [{"name": ..., "farbe": ..., "farbname": ...}, ...]

    print("\n" + "\033[31m" + "=" * 45 + "\033[0m")                                               # Obere Trennlinie in Rot ausgeben
    print("\033[31m" + "         WILLKOMMEN BEI HANGMAN!" + "\033[0m")                            # Ueberschrift in Rot ausgeben
    print("\033[31m" + "=" * 45 + "\033[0m")                                                      # Untere Trennlinie in Rot ausgeben

    while True:                                                                                   # Schleife läuft bis eine gültige Spieleranzahl eingegeben wurde
        try:
            anzahl = int(input("\nWie viele Spieler spielen? (2-5): ").strip())                   # Eingabe einlesen und in Zahl umwandeln
            if 2 <= anzahl <= 5:                                                                  # Prüfen ob die Zahl zwischen 2 und 5 liegt
                break                                                                             # Schleife verlassen wenn die Eingabe gültig ist
            else:
                print("  Fehler: Bitte eine Zahl zwischen 2 und 5 eingeben.")                     # Fehlermeldung bei ungültigem Bereich
        except ValueError:
            print("  Fehler: Ungültige Eingabe. Bitte eine Zahl eingeben.")                       # Fehlermeldung wenn keine Zahl eingegeben wurde

    spieler = []                                                                                  # Leere Liste für alle Spieler-Daten anlegen
    benutzte_farben = set() # Leere Menge um bereits gewählte Farben zu speichern
    print()                                                                                       # Leerzeile zur besseren Lesbarkeit

    for i in range(anzahl):                                                                       # Schleife für jeden Spieler

        # Name abfragen
        while True:                                                                               # Schleife läuft bis ein gültiger Name eingegeben wurde
            name = input(f"Name von Spieler {i + 1}: ").strip()                                   # Name einlesen und Leerzeichen entfernen
            if name == "":                                                                        # Prüfen ob der Name leer ist
                print("  Fehler: Name darf nicht leer sein.")                                     # Fehlermeldung bei leerem Namen
            elif not name.isalpha():                                                              # Prüfen ob der Name nur Buchstaben enthält
                print("  " \
                "Fehler: Nur Buchstaben erlaubt (keine Zahlen, Sonderzeichen oder Leerzeichen).")
            elif name.lower() in [s["name"].lower() for s in spieler]:                            # Prüfen ob der Name bereits vergeben ist
                print("  Fehler: Dieser Name wurde bereits verwendet.")                           # Fehlermeldung bei Dopplung
            else:
                break                                                                             # Schleife verlassen wenn der Name gültig ist

        # Farbe abfragen
        while True:                                                                               # Schleife läuft bis eine gültige Farbe gewählt wurde
            print(f"\n  Waehle eine Farbe für {name}:")                                           # Aufforderung zur Farbwahl ausgeben
            for key, (code, fname) in FARBEN.items():                                             # Alle Farben aus dem Woerterbuch durchlaufen
                belegt = " (bereits vergeben)" if key in benutzte_farben else ""                  # Hinweis wenn Farbe schon gewählt
                print(f"    [{key}] {code}{fname}{RESET}{belegt}")                                # Farboption farbig ausgeben
            wahl = input("  Deine Wahl (1-7): ").strip()                                          # Farbwahl einlesen
            if wahl not in FARBEN:                                                                # Prüfen ob die Eingabe eine gültige Farbnummer ist
                print("  Fehler: Bitte eine Zahl zwischen 1 und 7 eingeben.")                     # Fehlermeldung bei ungültiger Zahl
            elif wahl in benutzte_farben:                                                         # Prüfen ob die Farbe bereits von einem anderen Spieler gewählt wurde
                print("  Fehler: Diese Farbe wurde bereits gewählt.")                             # Fehlermeldung bei bereits belegter Farbe
            else:
                farbcode, farbname = FARBEN[wahl]                                                 # Farbcode und Farbname aus dem Woerterbuch holen
                benutzte_farben.add(wahl)                                                         # Farbe als belegt markieren
                spieler.append({"name": name, "farbe": farbcode, "farbname": farbname})           # Spieler in Liste speichern
                print(f"\n  {farbe(f'Hallo, {name}! Deine Farbe ist {farbname}.', farbcode)}")    # Begrüssung in gewählter Farbe
                break                                                                             # Schleife verlassen wenn eine gültige Farbe gewählt wurde

    namen = [farbe(s["name"], s["farbe"]) for s in spieler]                                       # Alle Spielernamen farbig formatieren
    print(f"\nTeam: {', '.join(namen)} - Viel Erfolg!")                                           # Team-Uebersicht mit farbigen Namen ausgeben
    return spieler                                                                                # Spielerliste zurückgeben


def wort_erzeugen():
    # Liest die Wortliste aus 'words.txt' und wählt zufällig ein Wort aus
    # Falls die Datei fehlt wird eine eingebaute Ersatzliste verwendet

    try:
        with open("words.txt", "r", encoding="utf-8") as f:                                       # Wortdatei zum Lesen öffnen
            woerter = [line.strip().upper() for line in f if line.strip()]                        # Alle Zeilen einlesen, Leerzeichen entfernen und in Grossbuchstaben umwandeln

        if not woerter:                                                                           # Prüfen ob die Liste leer ist
            raise ValueError("Wortliste ist leer.")                                               # Fehler auslösen wenn keine Woerter gefunden wurden

        return random.choice(woerter)                                                             # Zufälliges Wort aus der Liste zurückgeben

    except FileNotFoundError:                                                                     # Wird ausgefürt wenn die Datei words.txt nicht gefunden wurde
        print("  Hinweis: 'words.txt' nicht gefunden. Nutze eingebaute Ersatzliste.")
        ersatz = [                                                                                # Eingebaute Ersatzliste mit deutschen Woertern
            "HANGMAN", "PYTHON", "PROGRAMMIERUNG", "COMPUTER", "TASTATUR",
            "BILDSCHIRM", "MAUS", "DRUCKER", "NETZWERK", "DATENBANK",
            "ALGORITHMUS", "SCHLEIFE", "FUNKTION", "VARIABLE", "KLASSE"
        ]
        return random.choice(ersatz)                                                              # Zufälliges Wort aus der Ersatzliste zurückgeben
