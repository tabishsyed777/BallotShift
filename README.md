# BallotShift

Measure how a ranked-choice result changes when a single ballot is removed.

Use one ordered list per voter. Exhausted ballots leave the active denominator. Ties for elimination remove the alphabetically first tied candidate. This is a sensitivity simulation with a fixed tie rule.

## Run locally

From this folder with Python 3.8 or newer, run the included synthetic example and tests. Only the standard library is required.

```bash
python3 app.py
python3 -m unittest -v
```

Copy sample.json and edit its values, then run `python3 app.py your-input.json`.

## Sample output

```json
{
  "winner": "C",
  "rounds": [
    {
      "A": 2,
      "B": 1,
      "C": 2
    },
    {
      "A": 2,
      "C": 3
    }
  ],
  "sensitive_ballots": []
}
```
