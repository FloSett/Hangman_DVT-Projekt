from hangman_spieler import eingabe_Spieler, wort_erzeugen, farbe, konfetti                      # Funktionen aus Teil 1 importieren
from hangman_anzeige import hangman_zeichnen, wort_darstellen, trennlinie                        # Funktionen aus Teil 2 importieren


# ───────────────────────────────────
#  TEIL 3: Spiellogik & Hauptprogramm
# ───────────────────────────────────

def buchstaben_raten(geratene_buchstaben, spieler_name):
    # Lässt den aktuellen Spieler einen Buchstaben oder ein ganzes Wort eingeben
    # Eingabe ist robust: nur Buchstaben erlaubt, Warnung bei bereits genutzten Buchstaben

    while True:                                                                                   # Schleife läuft bis eine gültige Eingabe gemacht wurde
        eingabe = input("Welchen Buchstaben möchtest du? ").strip().upper()                       # Eingabe lesen, Leerzeichen entfernen und in Grossbuchstaben umwandeln

        if not eingabe:                                                                           # Prüfen ob die Eingabe leer ist
            print("  Fehler: Eingabe darf nicht leer sein.")                                      # Fehlermeldung bei leerer Eingabe
            continue                                                                              # Zurück zum Anfang der Schleife

        if not eingabe.isalpha():                                                                 # Prüfen ob die Eingabe nur Buchstaben enthält
            print("  Fehler: Nur Buchstaben erlaubt (keine Zahlen oder Sonderzeichen).")
            continue                                                                              # Zurück zum Anfang der Schleife

        if len(eingabe) == 1 and eingabe in geratene_buchstaben:                                  # Prüfen ob ein einzelner Buchstabe bereits benutzt wurde
            print(f"  Hinweis: Den Buchstaben '{eingabe}' hast du bereits benutzt!")              # Hinweis ausgeben
            continue                                                                              # Zurück zum Anfang der Schleife

        return eingabe                                                                            # Gültige Eingabe zurückgeben (einzelner Buchstabe oder ganzes Wort)


def spielrunde(spieler):
    # Führt eine komplette Spielrunde durch
    # Spieler raten abwechselnd - bei richtigem Buchstaben darf der gleiche Spieler nochmal
    # Runde endet wenn das Wort erraten wurde oder der Galgen vollständig ist

    wort = wort_erzeugen()                                                                        # Zufälliges Wort aus der Liste auswählen
    geratene_buchstaben = set()                                                                   # Leere Menge für alle bereits genutzten Buchstaben
    fehler = 0                                                                                    # Fehlerzähler auf 0 setzen
    max_fehler = 8                                                                                # Maximale Anzahl an Fehlern bevor das Spiel verloren ist
    spieler_index = 0                                                                             # Index des aktuellen Spielers (wird bei Fehler erhöht)

    print("\n" + "=" * 45)                                                                        # Obere Trennlinie für neue Runde
    print("           NEUE RUNDE STARTET!")                                                       # Ueberschrift neue Runde
    print(f"       Das Wort hat {len(wort)} Buchstaben.")                                         # Länge des gesuchten Wortes anzeigen
    print("=" * 45)                                                                               # Untere Trennlinie

    while fehler < max_fehler:                                                                    # Hauptschleife - läuft solange noch Versuche übrig sind

        sp = spieler[spieler_index % len(spieler)]                                                # Aktuellen Spieler holen (% sorgt für Rundlauf)

        print(f"\n{farbe('Hallo ' + sp['name'] + ', du bist dran:', sp['farbe'])}\n")             # Spieler in seiner Farbe begrüssen
        hangman_zeichnen(fehler)                                                                  # Aktuellen Galgenstand zeichnen
        print()                                                                                   # Leerzeile nach dem Galgen
        gewonnen = wort_darstellen(wort, geratene_buchstaben)                                     # Wortanzeige ausgeben und prüfen ob fertig
        print()                                                                                   # Leerzeile nach der Wortanzeige

        if gewonnen:                                                                              # Prüfen ob das Wort vollständig erraten wurde (Buchstabe für Buchstabe)
            konfetti()                                                                            # Konfetti-Regen anzeigen
            print("\033[32m" + "-" * 45 + "\033[0m")                                              # Grüne Trennlinie oben
            print(f"\033[32mGEWONNEN! Das Team hat das Wort erraten!\033[0m")                     # Gewonnen-Nachricht in Grün
            print(f"\033[32mDas Wort war: {wort}\033[0m")                                         # Gelöstes Wort in Grün anzeigen
            print("\033[32m" + "-" * 45 + "\033[0m")                                              # Grüne Trennlinie unten
            return True                                                                           # True zurückgeben = Runde gewonnen

        trennlinie()                                                                              # Trennlinie vor der Eingabe
        eingabe = buchstaben_raten(geratene_buchstaben, sp["name"])                               # Buchstaben- oder Worteingabe vom Spieler holen

        if len(eingabe) > 1:                                                                      # Prüfen ob ein ganzes Wort eingegeben wurde (mehr als 1 Buchstabe)
            if eingabe == wort:                                                                   # Prüfen ob das eingegebene Wort dem gesuchten Wort entspricht
                print(f"\n  Richtig! '{eingabe}' ist das gesuchte Wort!")                         # Erfolgsmeldung ausgeben
                print()                                                                           # Leerzeile
                hangman_zeichnen(fehler)                                                          # Aktuellen Galgenstand nochmal zeigen
                print()                                                                           # Leerzeile
                wort_darstellen(wort, set(wort))                                                  # Vollständiges Wort anzeigen
                konfetti()                                                                        # Konfetti-Regen anzeigen
                print("\033[32m" + "-" * 45 + "\033[0m")                                          # Grüne Trennlinie oben
                print(f"\033[32mGEWONNEN! {sp['name']} hat das Wort erraten!\033[0m")             # Gewonnen mit Spielername in Grün
                print(f"\033[32mDas Wort war: {wort}\033[0m")                                     # Gelöstes Wort in Grün anzeigen
                print("\033[32m" + "-" * 45 + "\033[0m")                                          # Grüne Trennlinie unten
                return True                                                                       # True zurückgeben = Runde gewonnen
            else:
                print(f"\n  Falsch! '{eingabe}' ist nicht das gesuchte Wort.")                    # Fehlermeldung bei falschem Wort
                fehler += 1                                                                       # Fehlerzähler um 1 erhöhen
                spieler_index += 1                                                                # Nächster Spieler ist dran

        else:                                                                                     # Einzelner Buchstabe wurde eingegeben
            geratene_buchstaben.add(eingabe)                                                      # Buchstaben zur Menge der genutzten Buchstaben hinzufügen

            if eingabe in wort:                                                                   # Prüfen ob der Buchstabe im gesuchten Wort vorkommt
                vorkommen = wort.count(eingabe)                                                   # Anzahl der Vorkommen zählen
                print(f"\n  Richtig! '{eingabe}' ist {vorkommen}x im Wort!")                      # Erfolgsmeldung mit Anzahl
                # spieler_index bleibt gleich - richtiger Buchstabe = nochmal raten
            else:
                print(f"\n  Falsch! '{eingabe}' ist nicht im Wort.")                              # Fehlermeldung wenn Buchstabe nicht im Wort
                fehler += 1                                                                       # Fehlerzähler um 1 erhöhen
                spieler_index += 1                                                                # Nächster Spieler ist dran

    # Hierher wird nur gelangt wenn alle 8 Fehler aufgebraucht sind = Verloren
    print()                                                                                       # Leerzeile
    hangman_zeichnen(fehler)                                                                      # Vollständigen Galgen zeichnen
    print()                                                                                       # Leerzeile
    wort_darstellen(wort, set(wort))                                                              # Gesuchtes Wort aufdecken und vollständig anzeigen
    print("\033[31m" + "-" * 45 + "\033[0m")                                                      # Rote Trennlinie oben
    print("\033[31mVERLOREN! Der Hangman ist vollständig.\033[0m")                                # Verloren-Nachricht in Rot
    print(f"\033[31mDas gesuchte Wort war: {wort}\033[0m")                                        # Gesuchtes Wort in Rot anzeigen
    print("\033[31m" + "-" * 45 + "\033[0m")                                                      # Rote Trennlinie unten
    return False                                                                                  # False zurückgeben = Runde verloren


def nochmal_spielen():
    # Fragt das Team ob sie noch eine weitere Runde spielen möchten
    # Gibt True zurück bei "ja", False bei "nein"

    while True:                                                                                   # Schleife läuft bis eine gültige Antwort eingegeben wurde
        antwort = input("\nMoechtet ihr noch einmal spielen? (ja/nein): ").strip().lower()        # Antwort einlesen und in Kleinbuchstaben umwandeln
        if antwort in ["ja", "j"]:                                                                # Prüfen ob Antwort "ja" oder "j" ist
            return True                                                                           # True zurückgeben = nochmal spielen
        elif antwort in ["nein", "n"]:                                                            # Prüfen ob Antwort "nein" oder "n" ist
            return False                                                                          # False zurückgeben = aufhören
        else:
            print("  Bitte 'ja' oder 'nein' eingeben.")                                           # Fehlermeldung bei ungültiger Antwort


def main():
    # Hauptfunktion - steuert den gesamten Programmablauf
    # Startet die Spielerverwaltung und die Spielschleife

    spieler = eingabe_Spieler()                                                                   # Spieler registrieren (Namen und Farben abfragen)

    siege = 0                                                                                     # Siegzähler auf 0 setzen
    niederlagen = 0                                                                               # Niederlagenzähler auf 0 setzen

    while True:                                                                                   # Spielschleife - läuft bis das Team nicht mehr spielen möchte
        gewonnen = spielrunde(spieler)                                                            # Eine Spielrunde starten und Ergebnis speichern

        if gewonnen:                                                                              # Prüfen ob die Runde gewonnen wurde
            siege += 1                                                                            # Siegzähler erhöhen
        else:
            niederlagen += 1                                                                      # Niederlagenzähler erhöhen

        print(f"\nErgebnis: {siege} Sieg(e) / {niederlagen} Niederlage(n)")                       # Aktuellen Spielstand anzeigen

        if not nochmal_spielen():                                                                 # Fragen ob nochmal gespielt werden soll
            break                                                                                 # Schleife verlassen wenn das Team aufhören möchte

    print("\n" + "=" * 45)                                                                        # Obere Abschluss-Trennlinie
    print("     DANKE FÜRS SPIELEN! AUF WIEDERSEHEN!")                                            # Abschiedsnachricht
    print(f"  Endstand: {siege} Sieg(e) - {niederlagen} Niederlage(n)")                           # Endstand anzeigen
    print("=" * 45)                                                                               # Untere Abschluss-Trennlinie


# ── Programmstart ─────────────────────────────────────────────────────
# Dieser Block wird nur ausgefuehrt wenn die Datei direkt gestartet wird
# (nicht wenn sie als Modul in eine andere Datei importiert wird)
if __name__ == "__main__":
    main()                                                                                        # Hauptfunktion aufrufen und das Spiel starten
