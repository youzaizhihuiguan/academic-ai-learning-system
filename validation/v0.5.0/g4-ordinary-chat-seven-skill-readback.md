# v0.5.0 — Ordinary Chat seven-Skill readback

- Date: 2026-10-10 (Asia/Tokyo).
- Runtime: the user's existing ordinary Chat, not Work's stale Skill catalog.
- Authority: `feat/v0.5.0-learning-fusion@94143028f9b3573d57b147eca3fc23c742054568`.
- Verdict: **PASS installed identity discovery and core-instruction exact match (7/7)**. No automatic routing or live UI pass implied.

## Actual test

Loaded Skill catalog, read each installed Skill entry through the platform reader, and fetched the matching `skills/<name>/SKILL.md` from the authoritative construction branch. For comparison only, excluded GitHub YAML frontmatter and the platform reader's generated reference-list footer; matched the complete trimmed instruction body exactly for each entry.

| Logical identity | GitHub SKILL.md blob | Ordinary Chat result |
| --- | --- | --- |
| `course-tutor-builder` | `2961a0ca7c8c2a2acac707a712bd9ce472c5e7b2` | **EXACT** (enhanced) |
| `rigorous-math-tutor` | `407af7bec7eca89a7ed7e2ba152b0ff7f2ec972b` | **EXACT** (enhanced) |
| `statistics-quant-lab` | `6d59e6030071301e111d0766a8ffaa4ea4189602` | **EXACT** (enhanced) |
| `computer-ai-tutor` | `2a9ad170ba312a240f7e067bb00a705c30bd05df` | **EXACT** (enhanced) |
| `obsidian-academic-kb` | `a16e7e2839e82e70b2db1595fe6a17edd1b6bd5e` | **EXACT** (original) |
| `interactive-learning-designer` | `d7df19586c7354053913c43f2b1c026786583c6d` | **EXACT** (new) |
| `learning-progress-coordinator` | `de9a5851591eb7ffd8804a221bbc23d0e7c8bfdb` | **EXACT** (new) |

- Four previously installed domain/builder entries now contain the v0.5.0 enhancement and match GitHub source.
- Obsidian remains byte-equivalent at `SKILL.md` level and unenhanced as intended.
- Two new entries appear and load. Their four references were separately verified from ordinary Chat earlier; see `g4-ordinary-chat-load-check.md`.
- Work independently checked existing identity preservation, full rollback bundles and 422 one-Skill-per-push sync resolution; see `four-skill-update-report.md`.
- The installed platform has normalized some YAML/icon bytes; this test does **not** claim all bundle bytes or icons are identical.

## Remaining gate

No fresh-chat implicit Skill routing or genuine interactive math UI state callbacks were tested by this **explicit Skill-read** check. The synthetic private Progress fixture has not been independently restored in a second ordinary Chat. Do not infer learner mastery from these technical validations.

PR #1 remains Draft, main unchanged, no `v0.5.0` release/tag until the runtime acceptance protocol is complete.
