# checkout-font: which text-size setting owns the label?

Two contrasting, natively qualified contracts. They come from the one content gap in the [rc.1 result](../../rc1-comparison/RESULT.md#native-grading). These are **development cases** built from a known incident, not fresh holdouts.

| Contract | Who owns the setting | Must pass | Must fail |
|---|---|---|---|
| `font-supplied-setting` | The caller passes a trait collection; the label shows exactly that size | Explicit `scaledFont(for:compatibleWith:)`; the same thing written as a tuple assignment | Explicit scaling **plus** `adjustsFontForContentSizeCategory = true`; system font in place of the design font; the **two observed rc.1 failing answers** (exact bytes, when the private return is present) |
| `font-live-environment` | The label's own environment, including later changes | `scaledFont(for:)` with automatic adjustment; a `registerForTraitChanges` handler that rescales; the observed rc.1 mechanism (scale for the current traits plus automatic adjustment) | One-time scaling with no tracking; system font with automatic adjustment |

**What the pair shows:** the mechanism both rc.1 versions produced fails the first contract and passes the second. So the guidance to write is "decide which setting owns the label", not "avoid automatic adjustment".

**Scope:**
- The contracts check font name, point size, wrapping and shrink settings on the iOS 26.5 simulator, deployment target 26.0, for a label outside any window.
- The live contract changes the environment through `traitOverrides` and `updateTraitsIfNeeded()`.
- They do not check rendering, layout fit or assistive-technology output.

**Qualify:**

```bash
python3 -B evals/headroom/checkout-font/qualify.py
```

- The script warms the simulator with the trusted rc.1 fixture first.
- It boots and shuts down the unit simulator only if it started it.
- [scorecard.json](scorecard.json) records the accepted run: 5 pass and 6 contract failures, all as expected.
- To record a new scorecard, run with `--record`. It refuses if a scorecard already exists.

**Next:** add an unaided baseline on both contracts before using them as decision tasks. That needs a separately authorized run.
