# parameter mellom bensin og el bil
KM_YEAR = 12_000

FORSIKRING_YEAR_BENSIN = 7_500
FORSIKRING_YEAR_EL = 5_000

TRAFIKKAVGIFT = 8.38

EL_PRIS_KWH = 2.0
EL_EFFIC_KWH = 0.2

KOSTNAD_EL_KM = EL_PRIS_KWH * EL_EFFIC_KWH
KOSTNAD_BENSIN_KM = 1

BOMAVGIFT_EL_KM = 0.1
BOMAVGIFT_BENSIN_KM = 0.3


def total(
    km_year: int,
    daglig_trafikkavgift: float,
    bensin_per_km: float,
    bomavgift: float,
    total_forsikring: int,
) -> float:
    """
    funksjon for å beregne pris
    """
    total_trafikkavgift = 365 * daglig_trafikkavgift
    total_bensin = km_year * bensin_per_km
    total_bomavgift = km_year * bomavgift
    return total_trafikkavgift + total_bensin + total_bomavgift + total_forsikring


total_el = total(
    KM_YEAR,
    TRAFIKKAVGIFT,
    KOSTNAD_EL_KM,
    BOMAVGIFT_EL_KM,
    FORSIKRING_YEAR_EL,
)
total_bensin = total(
    KM_YEAR,
    TRAFIKKAVGIFT,
    KOSTNAD_BENSIN_KM,
    BOMAVGIFT_BENSIN_KM,
    FORSIKRING_YEAR_BENSIN,
)
print(f"Total for elbil: {total_el} kr")
print(f"Total for bensin: {total_bensin} kr")

if total_el > total_bensin:
    print(f"Bensin er billigere med {total_el - total_bensin} kr")
else:
    print(f"Elbil er billigere med {total_bensin - total_el} kr")
