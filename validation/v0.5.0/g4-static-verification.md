# v0.5.0 G1–G4 Source Verification & Runtime Gate

- Date: 2026-10-10 (Asia/Tokyo)
- Branch: `feat/v0.5.0-learning-fusion`
- Status: **G1/G2 source packages built, G3 minimal source integration done, G4 PARTIAL — live ChatGPT validation PENDING**
- No existing ChatGPT installed Skill was replaced; no user Progress/Vault was edited; no release tag issued.

## Executed checks (not hypothetical)

1. Installed five original `SKILL.md` files were compared against GitHub baseline using `git hash-object`; all five matched G0 recorded Git blob SHAs.
2. New `interactive-learning-designer`: complete `SKILL.md`, UI metadata, icon, two linked references. `quick_validate.py` PASS, official `package_skill.py` PASS, ZIP open/CRC/inventory PASS.
3. New `learning-progress-coordinator`: complete `SKILL.md`, UI metadata, icon, two linked references. Same validator/packaging/ZIP checks PASS.
4. Four legacy Skill entries (`course-tutor-builder`, `rigorous-math-tutor`, `statistics-quant-lab`, `computer-ai-tutor`) each received **one short conditional integration section**; `obsidian-academic-kb` unchanged at SHA-1 `a16e7e2839e82e70b2db1595fe6a17edd1b6bd5e`.
5. Full seven Skill folders passed `validation/v0.5.0/check_skills.py`: metadata identity and uniqueness, references, icons, no template placeholders, domain safeguards and expected contract anchors. Result: `CHECKED 7 skills; PASS`. All seven individually passed `quick_validate.py`.
6. All seven complete Skill packages were built with `package_skill.py`, ZIP contents checked against local source bytes, `testzip()` returned no CRC errors.
7. GitHub files for both new Skills and all four edited `SKILL.md` were re-fetched, SHA-1 checked against packaged local source files; all matched.
8. Collision identified and fixed: removed broadly triggering phrase about merely 'continuing an existing course' from Progress Coordinator description. Progress Coordinator now focuses on stored state and review requests, not default lesson continuation.

**What these tests do not establish:** platform-level implicit routing, automatic multi-Skill composition, live Intelligent UI operation in the target account, cross-chat durable writes, actual delayed retention, or user-specific academic mastery.

## M01–M20 regression ledger

Legend: `S` = source contract inspected/static integrity passed; `L` = requires live use after installation; `X` = needs authorized persistent storage. `S` is **not** a substitute for `L`.

| Case | Expected behavior | Current evidence / pending |
| --- | --- | --- |
| M01 | Ordinary math explanation routes to math, not complex UI design | S; L |
| M02 | Full proof request answered directly without mandatory quiz | S; L |
| M03 | Interactive math parameter/explanation agreement and proof separation | S; L |
| M04 | State reset, invalid input and boundaries work in actual components | S; L |
| M05 | Statistical UI distinguishes theory, simulation and observed data | S; L |
| M06 | Animated code state never masquerades as real tool execution | S; L |
| M07 | Targeted prerequisite diagnosis distinguishes slip/isolated gap/misconception | S; L |
| M08 | No mandatory all-course Probe, DAG, repeated quiz or plan approval | S; L |
| M09 | Optional predict→observe→explain after AI coding, no project interruption | S; L |
| M10 | Hinted vs independent vs delayed Evidence explicitly distinguished | S; L |
| M11 | Unreported UI clicks cannot be stored as learner mastery | S; L |
| M12 | Retrieval/spacing/interleaving plan respects prerequisites and observations | S; L |
| M13 | Learning Debt distinct from Review Queue in real change management | S; L; X |
| M14 | Exam task identifies real materials/answers vs generated supplements | S; L |
| M15 | Cross-chat reads an authoritative actual prior Progress state | S; L; X |
| M16 | Cannot read/write: honest unknown state, no fake save | S; L; X |
| M17 | Historical 12 scenarios re-executed without routing regressions | Historical G0 scenarios preserved; L pending |
| M18 | New Skills unavailable/misaligned: Tutor continues useful work | S; L |
| M19 | Real personal evidence not automatically written to public repository | S; X (isolated authorized write tests pending) |
| M20 | Obsidian explicit-only and no original Skill regression | Original SHA unchanged; L |

## Known platform / environment boundaries

- The original five Skill configurations remain installed; the two new ones are source artifacts only. This session cannot certify implicit invocation behavior without installing and running both new Skills in a ChatGPT account.
- No authorized **private** Progress store was selected for personal learning data; hence no real Progress write/read test or delayed follow-up was attempted.
- Complex Intelligent UI must use real supported components and test direct callbacks and state. A Skill's text cannot itself guarantee that the host will render a requested widget or persist it across chats.
- Original System Audit reported 12/12 **scenario checks**, not platform-level invocation telemetry. This G4 source check does not count them as freshly re-run live tests.

## Gates

- **G0:** PASS, GitHub evidence in `g0-baseline.md`.
- **G1:** Source/packaging PASS; live interaction behavior to G4.
- **G2:** Source/packaging PASS; actual persistence scenarios to G4.
- **G3:** Minimal GitHub source integration done; original Obsidian unchanged; full routing regression to G4.
- **G4:** **PARTIAL / BLOCKED** on installation+live UI, implicit routing, private Progress write/read permission, and real task tests.
- **G5:** **NOT AUTHORIZED TO CLAIM RELEASED**; no merge, installed Skill replacement, or `v0.5.0` tag until outstanding gates close.

## Recovery / next action

From branch `feat/v0.5.0-learning-fusion`, compare to `main`, re-run `python validation/v0.5.0/check_skills.py` and Skill creator validators; install Skills into a controlled ChatGPT Skill environment when possible, execute live M01–M20 and historical 12, then record `reports/v0.5.0-validation-verdict.md` with actual outcomes. Keep main and real Progress untouched if blockers persist.
