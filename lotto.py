"""
Module solves an assignment about a lottery 
to demonstrate set and dict behaviour
"""

from random import sample


def ziehung_durchfuehren(datum, ziehungen):
    """
    Führe eine Lottoziehung durch. Die Menge der gezogenen Kugeln wird zurückgegeben
    und die detaillierte Ausgabe in eine logdatei geschrieben.

    Parameter:
    ----------
    datum : str
        Das Datum der Ziehung

    Returns:
    --------
    set[int]
        Die gezogenen Lottazahlen
    """
    spielkugeln = frozenset(range(1, 50))
    kugeln_in_trommel = set(spielkugeln)
    # Since sample() only works with sequences from Python 3.11
    # on we first convert our set to a list using sorted
    kugeln_in_ablage = set(sample(sorted(spielkugeln), k=6))
    kugeln_in_trommel -= kugeln_in_ablage
    ziehungen[datum] = kugeln_in_ablage
    log = f"Ziehung vom {datum}:\n"
    log += f"\tgezogene Zahlen: {kugeln_in_ablage}\n"
    log += f"\tverbleibende Kugeln in der Trommel: {kugeln_in_trommel}\n"
    log += f"\tGewinnzahlen: {sorted(kugeln_in_ablage)}\n\n"
    with open("log_file.txt", "a", encoding="utf8") as log_file:
        log_file.write(log)
    return kugeln_in_ablage


def main():
    ziehungsdaten = ("2017-08-05", "2017-08-12", "2017-08-19", "2017-08-26")
    ziehungen = {}
    # Ziehungen durchführen
    for datum in ziehungsdaten:
        kugeln_in_ablage = ziehung_durchfuehren(datum, ziehungen)
        print(f"Zahlen der Ziehung {datum}: {kugeln_in_ablage}")

    # Dictionary ausgeben
    print(f"\nDictionary der Ziehungen: {ziehungen}\n")

    # Alle gezogenen Zahlen als Vereinigung der in ziehungen gespeicherten Mengen
    # Stern-Operator zur Expansion benutzen!
    alle_gezogenen_zahlen = sorted(set().union(*ziehungen.values()))
    print(f"Alle gezogenen Zahlen: {alle_gezogenen_zahlen}\n")

    zahlen_statistik = {}
    for datum, ziehung in ziehungen.items():
        for zahl in ziehung:
            zahlen_statistik.setdefault(zahl, []).append(datum)

    print("Zahl | Ziehung(en)")
    print("------------------")
    for zahl in sorted(zahlen_statistik.keys()):
        print(f"{zahl:4d} | {', '.join(zahlen_statistik[zahl])}")


if __name__ == "__main__":
    main()
