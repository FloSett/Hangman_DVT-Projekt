from hangman_spieler import farbe, RESET                                                          # Hilfsfunktion und Reset-Code aus Teil 1 importieren


# ─────────────────────────────────────────────
#  TEIL 2: Hangman-Darstellung & Wort-Darstellung 2
# ─────────────────────────────────────────────

def hangman_zeichnen(fehler):
    # Zeichnet den Galgen mit chr(9744)-Zeichen je nach Anzahl der bisherigen Fehler
    # Je mehr Fehler desto mehr vom Galgen wird sichtbar (8 Stufen)

    if fehler == 0:                                                                               # 0 Fehler: Noch nichts zeichnen
        pass

    elif fehler == 1:  # 1 Fehler: Halber Berg als Basis
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Obere Reihe des halben Berges
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Untere Reihe des halben Berges

    elif fehler == 2:  # 2 Fehler: Ganzer Berg
        print("   ",chr(9744),chr(9744),chr(9744))                                                # Bergspitze
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))                                       # Zweite Bergreihe
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Dritte Bergreihe
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Bergbasis

    elif fehler == 3:  # 3 Fehler: Senkrechter Mast kommt dazu
        print("     ",chr(9744))                                                                  # Mast Zeile 1
        print("     ",chr(9744))                                                                  # Mast Zeile 2
        print("     ",chr(9744))                                                                  # Mast Zeile 3
        print("     ",chr(9744))                                                                  # Mast Zeile 4
        print("     ",chr(9744))                                                                  # Mast Zeile 5 (unterster Teil)
        print("   ",chr(9744),chr(9744),chr(9744))                                                # Bergspitze
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))                                       # Zweite Bergreihe
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Dritte Bergreihe
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Bergbasis

    elif fehler == 4:  # 4 Fehler: Waagerechter Querbalken oben kommt dazu
        print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),                # Querbalken oben
              chr(9744),chr(9744),chr(9744))                                                      # Querbalken oben
        print("     ",chr(9744))                                                                  # Mast Zeile 1
        print("     ",chr(9744))                                                                  # Mast Zeile 2
        print("     ",chr(9744))                                                                  # Mast Zeile 3
        print("     ",chr(9744))                                                                  # Mast Zeile 4 (unterster Teil)
        print("   ",chr(9744),chr(9744),chr(9744))                                                # Bergspitze
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))                                       # Zweite Bergreihe
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Dritte Bergreihe
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Bergbasis

    elif fehler == 5:  # 5 Fehler: Seil hängt vom Querbalken herunter
        print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),                # Querbalken
              chr(9744),chr(9744),chr(9744))                                                      # Querbalken
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil Zeile 1
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil Zeile 2
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil Zeile 3
        print("     ",chr(9744))                                                                  # Mast allein Zeile 1
        print("     ",chr(9744))                                                                  # Mast allein Zeile 2
        print("   ",chr(9744),chr(9744),chr(9744))                                                # Bergspitze
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))                                       # Zweite Bergreihe
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Dritte Bergreihe
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Bergbasis

    elif fehler == 6:  # 6 Fehler: Kopf der Figur erscheint
        print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),                # Querbalken
              chr(9744),chr(9744),chr(9744))                                                      # Querbalken
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil
        print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))                            # Kopf obere Reihe
        print("     ",chr(9744),"    ",chr(9744),"   ",chr(9744))                                 # Kopf mittlere Reihe (Augen)
        print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))                            # Kopf untere Reihe
        print("     ",chr(9744))                                                                  # Mast allein Zeile 1
        print("     ",chr(9744))                                                                  # Mast allein Zeile 2
        print("   ",chr(9744),chr(9744),chr(9744))                                                # Bergspitze
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))                                       # Zweite Bergreihe
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Dritte Bergreihe
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Bergbasis

    elif fehler == 7:  # 7 Fehler: Körper mit Armen kommt dazu
        print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),                # Querbalken
              chr(9744),chr(9744),chr(9744))                                                      # Querbalken
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil
        print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))                            # Kopf obere Reihe
        print("     ",chr(9744),"    ",chr(9744),"   ",chr(9744))                                 # Kopf mittlere Reihe (Augen)
        print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))                            # Kopf untere Reihe
        print("     ",chr(9744),"       ",chr(9744))                                              # Körper obere Reihe
        print("     ",chr(9744),"   ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))          # Körper mit Armen
        print("     ",chr(9744),"       ",chr(9744))                                              # Körper untere Reihe
        print("     ",chr(9744))                                                                  # Mast allein
        print("   ",chr(9744),chr(9744),chr(9744))                                                # Bergspitze
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))                                       # Zweite Bergreihe
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Dritte Bergreihe
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Bergbasis

    elif fehler >= 8:  # 8 Fehler: Vollständiger Hangman mit Beinen - Spiel verloren
        print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),                # Querbalken
              chr(9744),chr(9744),chr(9744))                                                      # Querbalken
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil Zeile 1
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil Zeile 2
        print("     ",chr(9744),"       ",chr(9744))                                              # Mast + Seil Zeile 3
        print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))                            # Kopf obere Reihe
        print("     ",chr(9744),"    ",chr(9744),"   ",chr(9744))                                 # Kopf mittlere Reihe (Augen)
        print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))                            # Kopf untere Reihe
        print("     ",chr(9744),"       ",chr(9744))                                              # Körper obere Reihe
        print("     ",chr(9744),"   ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))          # Körper mit Armen
        print("     ",chr(9744),"       ",chr(9744))                                              # Körper untere Reihe
        print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))                            # Beine obere Reihe
        print("     ",chr(9744),"     ",chr(9744)," ",chr(9744))                                  # Beine untere Reihe (Füsse)
        print("     ",chr(9744))                                                                  # Mast allein
        print("   ",chr(9744),chr(9744),chr(9744))                                                # Bergspitze
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))                                       # Zweite Bergreihe
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))                              # Dritte Bergreihe
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))              # Bergbasis


def wort_darstellen(wort, geratene_buchstaben):
    # Zeigt das gesuchte Wort an – erratene Buchstaben werden sichtbar, der Rest als Unterstrich
    # Gibt True zurück wenn alle Buchstaben erraten wurden, sonst False

    anzeige_teile = []                                                                            # Leere Liste für die Buchstaben/Striche der Anzeige
    vollstaendig = True                                                                           # Annahme: Wort ist vollständig - wird auf False gesetzt wenn ein Strich vorkommt

    for buchstabe in wort:                                                                        # Jeden Buchstaben des gesuchten Wortes durchlaufen
        if buchstabe in geratene_buchstaben:                                                      # Prüfen ob der Buchstabe bereits erraten wurde
            anzeige_teile.append(buchstabe)                                                       # Erratenen Buchstaben sichtbar hinzufügen
        else:
            anzeige_teile.append("_")                                                             # Noch nicht erratenen Buchstaben als Unterstrich anzeigen
            vollstaendig = False                                                                  # Wort ist noch nicht vollständig erraten

    anzeige = "  ".join(anzeige_teile)                                                            # Buchstaben/Striche mit Leerzeichen verbinden
    print(f"Errate folgendes Wort:")                                                              # Ueberschrift ausgeben
    print(f"  {anzeige}")                                                                         # Wortanzeige mit Einrückung ausgeben
    return vollstaendig                                                                           # True wenn fertig, False wenn noch Buchstaben fehlen


def trennlinie():
    # Gibt eine einfache Trennlinie aus 45 Bindestrichen aus
    print("-" * 45)
