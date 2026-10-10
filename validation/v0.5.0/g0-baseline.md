# v0.5.0 G0 — Baseline verification

- Date: 2026-10-10 (Asia/Tokyo)
- Branch: `feat/v0.5.0-learning-fusion`
- Starting HEAD: `b40363416a3c153d903612eb1ec70573e44b31f9`
- Authority: `reports/v0.5.0-fusion-architecture.md` and `reports/v0.5.0-construction-readiness.md`
- Status: **G0 PASS — read-only evidence before subsequent Skill edits**.

## Existing installed Skill snapshots

The following SHA-1 Git blob IDs of the five installed local SKILL.md files match the connector-fetched corresponding paths at this branch byte for byte:

| Skill | SHA-1 Git blob |
| --- | --- |
| course-tutor-builder | `f304871efe46b4770720b336de79ec7c54d5773d` |
| rigorous-math-tutor | `5a8ed3badd16cff8e8250d9aa7efc586070cf1c0` |
| statistics-quant-lab | `270cc5fe606764c48dd34be4634c53268b669a58` |
| computer-ai-tutor | `a0b70beaa2694e381b971774ab99afa29ef69d3f` |
| obsidian-academic-kb | `a16e7e2839e82e70b2db1595fe6a17edd1b6bd5e` |

GitHub source currently includes README, old system/integration reports, Course Learning Profile, Progress and preserved five Skill directories. Original installation and GitHub snapshot agree at SKILL.md level; other bundled asset bytes have not yet been exhaustively compared. `progress/computer.md` still reports actual Pxx/Evidence as **unknown**, not unfinished. The repository is `public`; no personal Evidence is authorized for writes to this branch.

## Historical regression tasks to preserve

Derived from `reports/system-audit-2026-09-27.md` / `reports/integration-2026-09-27.md`, representative routing/behavior checks:

1. Independent mathematical existence/continuity proof → math Tutor.
2. Two-group A/B difference, estimate and uncertainty → statistics Tutor.
3. Group leakage in evaluation → statistics Tutor.
4. Deployment memory growth diagnosis → computer Tutor.
5. Python mutable default behavior → computer Tutor.
6. Simulated four-unit syllabus to CLP → Builder, retains original sequence.
7. Real computer long-term roadmap to CLP → Builder, retains native P00–P31 and conditions.
8. Explicit Obsidian export → Obsidian Skill only when requested; don't invent Vault write.
9. Ordinary Python explanation → computer Tutor; no default Obsidian export.
10. Executed Python behavior → distinguish actual code execution evidence from inference.
11. Mean unbiasedness and uncertainty → statistics Tutor, can handle short proof.
12. Mixed model performance and production pipeline problem → one owner based on judgment goal, coherent cross-domain response.

The historical 12/12 is a prior **scenario review**, not observed new Skill selection telemetry. This G0 records preserved old acceptance scenarios; fresh G3/G4 regression executions must be reported separately.

## Scope and gate

G1 is now authorized on an isolated feature branch only. No new Skill or old Skill edit occurred in this G0 checkpoint. G1 must not claim released functionality or automatic cross-Skill calls; real component runtime and installation acceptance are later gates.
