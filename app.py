import argparse
import json
from pathlib import Path


def solve(data):
    ballots = data["ballots"]
    candidates = set().union(*(set(ballot) for ballot in ballots))
    def elect(votes):
        remaining = candidates.copy()
        rounds = []
        while remaining:
            counts = dict.fromkeys(sorted(remaining), 0)
            for ballot in votes:
                first = next((c for c in ballot if c in remaining), None)
                if first is not None:
                    counts[first] += 1
            rounds.append(counts)
            total = sum(counts.values())
            if not total:
                break
            leader = max(counts, key=counts.get)
            if counts[leader] * 2 > total:
                return leader, rounds
            loser = min(counts, key=lambda c: (counts[c], c))
            remaining.remove(loser)
        return None, rounds
    winner, rounds = elect(ballots)
    flips = []
    for index in range(len(ballots)):
        alternate, _ = elect(ballots[:index] + ballots[index + 1:])
        if alternate != winner:
            flips.append({"removed_index": index, "winner": alternate})
    return {"winner": winner, "rounds": rounds, "sensitive_ballots": flips}

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Measure how a ranked-choice result changes when a single ballot is removed.')
    parser.add_argument("input", nargs="?", type=Path, default=Path(__file__).with_name("sample.json"))
    args = parser.parse_args()
    print(json.dumps(solve(json.loads(args.input.read_text())), indent=2))
