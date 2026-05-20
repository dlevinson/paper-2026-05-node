# SPDX-License-Identifier: CC-BY-SA-4.0
"""Run the deterministic NODE toy-network example from the paper text.

The example uses the event order reported in Table 2 of the paper:
    (O2, D1) = 4, (O1, D1) = 5, (O2, D2) = 6,
    (O1, D2) = 7, (O2, D3) = 8, (O1, D3) = 9.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from node_minimal_from_si import node  # noqa: E402


def main() -> int:
    workers = {"O1": 4, "O2": 5}
    jobs = {"D1": 4, "D2": 3, "D3": 2}
    costs = {
        ("O2", "D1"): 4,
        ("O1", "D1"): 5,
        ("O2", "D2"): 6,
        ("O1", "D2"): 7,
        ("O2", "D3"): 8,
        ("O1", "D3"): 9,
    }

    allocation, residual_workers, residual_jobs = node(workers, jobs, costs)

    expected = {
        ("O1", "D1"): 0,
        ("O1", "D2"): 2,
        ("O1", "D3"): 2,
        ("O2", "D1"): 4,
        ("O2", "D2"): 1,
        ("O2", "D3"): 0,
    }
    assert allocation == expected
    assert residual_workers == {"O1": 0, "O2": 0}
    assert residual_jobs == {"D1": 0, "D2": 0, "D3": 0}

    print("Deterministic NODE toy-network allocation")
    print("origin,D1,D2,D3,row_total")
    for origin in ("O1", "O2"):
        values = [allocation[(origin, dest)] for dest in ("D1", "D2", "D3")]
        print(f"{origin},{values[0]},{values[1]},{values[2]},{sum(values)}")
    print("total,4,3,2,9")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
