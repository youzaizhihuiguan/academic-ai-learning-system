# v0.5.0 — Independent Ordinary Chat Acceptance (2026-10-10)

- Test environment: authenticated ordinary Chat, separately from the prior Work window. Installed source files were checked in the local Skill runtime; GitHub repository via connected GitHub API; fictional Library file via authorized Files retrieval.
- Source/recovery HEAD before this report: `feat/v0.5.0-learning-fusion@6625cfce5bc0025a534f6812913f0046f1130b92`.
- Verdict: **G4 PARTIAL PASS — installed/packaged core and cross-conversation *read* passed; full R01–R20 live route/UI and autonomous persistence NOT accepted; G5 BLOCKED**.
- No real learning history, user's personal Progress, Obsidian vault, protected `main`, or Skill installation was changed in this Chat-side audit.

## 1. GitHub / installation state

- PR #1 remained `draft=true`, `merged=false`; `main` remained `b40363416a3c153d903612eb1ec70573e44b31f9`.
- Feature branch before this check was `6625cfce5bc0025a534f6812913f0046f1130b92`, ahead of main with no commits behind; 49 changed files comprised 10 new Skill source files, four original `SKILL.md` additive upgrades, 34 validation/evidence/rollback files, and one GitHub Actions workflow. No `progress/` or Obsidian changes.
- GitHub Actions passed on the exact previous feature HEAD for both PR and push triggers; the actual source-check step was successful.
- A fresh ordinary-Chat platform Skill catalog and independent local filesystem entry read found **seven distinct installed Skill identities**. Every `SKILL.md` Git blob hash was compared with the reviewed GitHub counterpart and matched: 7/7. Their parsed frontmatter named the expected identity, `name` and `description` keys only, and distinct descriptions.
- The official Skill Creator `quick_validate.py` was executed against each of the **seven currently installed** complete directories, not against temporary input templates: **7/7 PASS**.
- The four original enhancements were loaded; Obsidian remained on its original `SKILL.md`. Prior Work account export confirms original IDs retained, no duplicate names, with complete rollback bundles.
- The platform's canonical exports normalize selected YAML and replace a few custom icons; **do not claim the entire installed archive is byte-identical** or that the icon fidelity discrepancy has disappeared.

## 2. R03: interactive math correctness / observed handoff

The user previously submitted from an interactive math task `t=-2, det=-3, abs_area=3` into this ordinary Chat. We received that reported state and verified the numbers; we do not have independent telemetry of every client-side input or rendered SVG frame.

Independent executable reference checks used `A(t)=[[1,t],[t,1]]`, `T_t(x,y)=(x+ty,tx+y)`, and the *independent shoelace formula* on the transformed unit-square polygon:

| t | Expected determinant | Polygon oriented area | Absolute area | Verdict |
| --- | ---: | ---: | ---: | --- |
| 0 | 1 | 1 | 1 | PASS |
| 1 | 0 | 0 | 0 | PASS |
| -1 | 0 | 0 | 0 | PASS |
| 2 | -3 | -3 | 3 | PASS |
| -2 | -3 | -3 | 3 | PASS |

A standalone Node reproduction of the previously authored UI's input handler logic checked valid presets 0, 1, -1, 2 and -2, rejected letters/blank/out-of-range/Infinity while preserving the prior accepted state, accepted fractional input, and cleared error/draft on reset: **11/11 PASS**. This validates deterministic formulas and the reviewed handler model, **not actual browser slider rendering, actual reset clicks, CSS/SVG/layout, or hidden interaction history**.

**R03: PARTIAL PASS.** Math + reported state handoff supported; live rendering/reset/invalid-input interactions await observable browser/user evidence.

## 3. R13: independent cross-conversation synthetic Progress recovery

Without importing Work's state into chat history, performed an **ordinary-Chat Library search** for the file named `Academic_AI_v050_Private_Test_Progress.md` created by a separate Work session. Found the current authorized raw-file backing, read complete content via Files, and materialized the file *for independent SHA-256 verification*.

- Raw byte size: `1292`.
- SHA-256 from current ordinary Chat: `30e932207fa69f88a9b1f66704ad25c5c6f8fc3504cfab6adcf8e3d7f2b72ae4` — **identical to Work's final write receipt**.
- Contains `private-synthetic-case-001` and `private-synthetic-case-002` **exactly once each**.
- Preserves `KEEP_THIS_LINE` and `PRESERVE_CONCURRENT_NOTE`; stage remains `unknown`.
- The record is explicitly fictional; one numeric determinant and a synthetic transfer variation support only their **test-case arithmetic**, not real independent mastery.
- Review Queue contains a **synthetic transfer question**, explicitly **no reminder scheduled**; Learning Debt is **none verified**.
- Files API identified this materialized backing by its own `version_id=1`, whereas Work's internal save test labeled its final update `version=2`. We **do not assume these version counters have identical semantics**. Matching byte hash proves the recovered *content*, not equivalence of counter numbering.
- No private/real learning data was written, no user's actual Progress was changed.

**R13 cross-conversation content retrieval: PASS** for a separate Chat reading the exact Work-created authorized synthetic file. **Installed Coordinator automatic invocation, cross-conversation write, ACL audit and future autonomous restoration: untested**, so the complete G4 user-visible automation requirement remains open.

## 4. Negative claims and release blockers

| Gate | Result |
| --- | --- |
| 7/7 installed source/hash/format and CI | PASS |
| Existing identities and Obsidian unchanged / rollback | PASS (Work+GitHub evidence) |
| R03 formula/reference and reported message payload | PASS (subtests); R03 as a whole PARTIAL |
| Work → ordinary Chat synthetic file byte recovery / SHA | PASS |
| Synthetic GitHub/Library optimistic concurrency primitive | PASS (from Work evidence), not installed Coordinator invocation |
| Real implicit auto-selection in fresh user chats, including negative routes | **NOT TESTED** |
| Native interactive widget visual/functionality including reset/invalid input | **NOT OBSERVED in live browser** |
| R04 statistical sample UI, R05 recursion UI | **NOT TESTED** |
| R01–R02, R06–R12, R14–R20 live scenarios and historical 12 fresh-chat routes | **NOT TESTED as isolated live scenarios** |
| Private persisted learner Progress *end-to-end via installed Coordinator* | **NOT TESTED** |
| Actual user knowledge/independent mastery | **NOT ASSESSED** |
| Merge to main, release `v0.5.0`, delete rollback | **DO NOT DO** |

A skill being installed and readable proves availability; it does not prove that the model picked it automatically or that complex UI performed correctly at runtime. The user can already use installed Skills but the project’s **formal v0.5.0 release gate** requires recorded live evidence for those remaining risks.

## 5. Next minimum live acceptance packet

1. In **fresh ordinary Chat** (no explicit @ selection), run R01 and R16 to check simple questions are not hijacked by Designer/Coordinator; invocation telemetry unobservable must be recorded as `unobserved` rather than PASS.
2. Run R03 UI with real user observation of presets, invalid input, reset and geometry. The previous submitted `t=-2` number is not enough to declare full UI PASS.
3. Run R04/R05 as cross-domain complex UI smoke tests and audit the theory/simulation/runtime-execution boundary.
4. For the Coordinator, run R09 (reject fake mastery), R13 using the **same synthetic private fixture**, R14 (no access/no fabricated save), and an authorized synthetic write/readback if explicitly needed. Don't write real Progress or Vault.
5. R17 Obsidian remains explicit-only; run representative old routing regression as planned.
6. Record actual answers, UI actions, tool evidence, status and blockers in versioned G4 report before changing Draft PR or creating a release tag.

This report is intentionally an independent acceptance checkpoint, **not** a claim that G4 or G5 is COMPLETE.
