"""Minimal NODE implementation extracted from the paper SI.

Source:
Levinson (2026), "Network Origin-Demand Estimation Using Percolation (NODE)",
Findings, DOI: 10.32866/001c.147387.

This file preserves the Python code listing found in the supplementary
information. It is a minimal allocation routine, not a complete reproduction
script for the paper figures or stochastic example.
"""


def node(W, J, C):
    # W: dict o->int, J: dict d->int, C: dict (o,d)->cost or inf
    from math import inf

    X = {(o, d): 0 for (o, d) in C if C[(o, d)] < inf}
    w = W.copy()
    j = J.copy()
    events = sorted([(C[(o, d)], o, d) for (o, d) in X.keys()])
    for _, o, d in events:
        m = min(w[o], j[d])
        if m > 0:
            X[(o, d)] += m
            w[o] -= m
            j[d] -= m
    return X, w, j
