# v0.5.0 — Ordinary Chat installed-Skill load check

- Date: 2026-10-10 (Asia/Tokyo)
- Environment: existing **ordinary Chat**, not Work.
- Source authority: `feat/v0.5.0-learning-fusion@1ea4ba1fbf96721e854aa4d1f39a274d876695ae`.
- Scope: **installed Skill discovery and instruction-content readback**, not automatic invocation, rendered UI behavior or persistent Progress.
- Work install detail: [v0.5.0 Work recovery report](g4-work-installation-report.md). That report documents the push error "aggregate skills Arcade push may modify only one skill" and the subsequent one-Skill-per-push successful account sync.

## Executed in ordinary Chat

The account's available Skill catalog was read. Both new logical names were present exactly once among the listed Skills:

- `interactive-learning-designer`
- `learning-progress-coordinator`

For each Skill, read its installed `SKILL.md` through the platform Skill reader; compared the trimmed body (ignoring YAML frontmatter and the reader's generated reference-list footer) with the GitHub source under the same identity and branch. Both matched exactly. Then read both referenced Markdown files per Skill using the installed Skill reader and compared their full text with the GitHub source after trimming final whitespace.

| Identity / file | Ordinary Chat result |
| --- | --- |
| `interactive-learning-designer/SKILL.md` body | EXACT |
| `interactive-learning-designer/references/interaction-contract.md` | EXACT |
| `interactive-learning-designer/references/interaction-qa.md` | EXACT |
| `learning-progress-coordinator/SKILL.md` body | EXACT |
| `learning-progress-coordinator/references/progress-contract.md` | EXACT |
| `learning-progress-coordinator/references/review-policy.md` | EXACT |

Installed UI YAML and image bytes are not verified by this Chat test. Work's existing report notes semantic YAML normalization and replacement of custom icons, so do not claim full package byte identity.

## Verdict and remaining gates

- **PASS:** Both new Skill identities are discoverable in ordinary Chat; all installed core rules and four references are readable and text-identical to the reviewed GitHub source.
- **NOT TESTED:** Implicit automatic Skill routing when user prompts are submitted to fresh conversations. This existing chat performed an explicit instruction read; do not treat this as a trigger test.
- **NOT TESTED:** Native Intelligent UI components, actual interactive state/callback behaviors, mathematical/clinical/statistical correctness under interaction, and evidence transmission to the assistant.
- **NOT TESTED:** Installed Coordinator's private Progress read/write and restoration from a second ordinary Chat; no real user Progress was changed.
- **G4:** Remains PARTIAL. Continue the R01–R20 plus historic routing acceptance protocol in `runtime-acceptance-protocol.md`. Maintain Draft PR and do not merge/tag `v0.5.0`.

No source Skill file, personal study record or Obsidian Vault was modified by this Chat-side check.
