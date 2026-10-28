from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def read(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

pub = read("S2_publication_register.csv")
app = read("S4_design_specific_appraisal_register.csv")
strategy = read("S5_strategy_membership_and_annotations.csv")
decisions = read("S11_indicator_decisions.csv")
expected = read("S11_indicator_counts.csv")
identities = {x["reference_id"]: x["doi"].lower() for x in pub}
assert len(pub) == len(identities) == len(set(identities.values())) == 189
assert len(app) == 189 and {x["reference_id"] for x in app} == set(identities)
assert len(strategy) == len({x["reference_id"] for x in strategy}) == 143
assert len(decisions) == len({(x["reference_id"], x["indicator"]) for x in decisions}) == 1701
for rows in [app, strategy, decisions]:
    assert all(x["doi"].lower() == identities[x["reference_id"]] for x in rows)
assert "source_excerpt" not in decisions[0]
indicators = list(dict.fromkeys(x["indicator"] for x in decisions))
assert len(indicators) == len(expected) == 9
by_indicator = {x["indicator"]: x for x in expected}
for key in indicators:
    rows = [x for x in decisions if x["indicator"] == key]
    counts = Counter(x["decision"] for x in rows)
    assert len(rows) == 189
    assert set(counts) <= {"CONFIRMED", "NOT_IDENTIFIED", "UNCERTAIN", "NOT_APPLICABLE"}
    target = by_indicator[key]
    for field, state in [("confirmed", "CONFIRMED"), ("not_identified", "NOT_IDENTIFIED"), ("uncertain", "UNCERTAIN"), ("not_applicable", "NOT_APPLICABLE")]:
        assert int(target[field]) == counts[state]
    assert int(target["denominator"]) == 189
    share = f"{100 * counts['CONFIRMED'] / 189:.1f}"
    assert target["confirmed_coverage_percent"] == share
    assert all(int(x["numerator_contribution"]) == int(x["decision"] == "CONFIRMED") for x in rows)
    print(f"{key}: {counts['CONFIRMED']}/189 ({share}%), uncertain={counts['UNCERTAIN']}")
print("PASS: publication identities, joins, row counts, decision contributions and coverage summaries agree.")
