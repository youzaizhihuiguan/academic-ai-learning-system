# Intelligent UI native-use architecture — Account installation evidence

Date: 2026-10-12. Verdict: **ACCOUNT INSTALLATION AND CANONICAL READBACK PASSED**. Ordinary Chat runtime acceptance remains **NOT RUN**.

## Authority and scope

- Repository: `youzaizhihuiguan/academic-ai-learning-system`.
- Source branch: `fix/interactive-learning-autotrigger`, PR #2.
- Immutable installation authority: `802c5d5fd7337d04ee68e112324161faa531924a`.
- PR #2 was independently read before and after installation: open, Draft, unmerged.
- Only four existing account identities were updated, in the required order. No Skill source files were edited, regenerated, or redesigned. The GitHub commits in this run add validation evidence only.

## Phase 0 — Canonical export and rollback

The existing authenticated account Skills Git origin (`https://chatgpt.com/backend-api/git-authed/skills`) was fetched before any mutation. Its canonical baseline was `ad4d1eaa334325c1386d82ba2a233361661dbbc8`. The local workspace was clean and exactly at this remote ref.

The session's executor Skill discovery cache omitted Designer and Progress Coordinator. Both were present in the freshly fetched canonical account Git export. Identity and duplicate checks therefore used the authoritative live Git export, not the stale session cache. This does not assert that an ordinary Chat runtime has refreshed its discovery state.

Complete rollback export: [account-before.json](rollback/intelligent-ui-account-sync-2026-10-12-ad4d1eaa/account-before.json).

- Durable pre-install evidence commit: `9c075806dd4a9abef532a9711954ffc94d2225c1`.
- Export SHA-256: `89d03b6975bf9a1e444abf0c34193ea9510a03b95497c85d4223253681c4a014`.
- Contains the complete canonical account file export: every SKILL.md, agents/openai.yaml, reference and asset actually present, with original identity, modes, Git blob hashes, SHA-256 hashes, directory tree hashes, and available account revision.
- The four target snapshots are identified by the export's `targets` map and their existing ID prefixes in `entries`. Absent optional references/assets are not invented.
- Export was committed and then fetched back byte-for-byte before the first Skill push. Previous rollback evidence was not overwritten.
- Rollback: reconstruct one target's files from its ID-prefixed entries, remove files absent from that snapshot inside that same ID only, and perform a single-Skill commit/push followed by canonical readback. Preserve the original ID and name; never delete/recreate the Skill. Repeat only for the identities being rolled back. Platform icon/YAML canonicalization may occur again; the original canonical bytes remain preserved in this export.

## Single-Skill push sequence

| Order | Skill | Existing ID, unchanged after update | Account push commit | Canonical readback ref | Result |
| --- | --- | --- | --- | --- | --- |
| 1 | interactive-learning-designer | `skill-6aca39ab0c8c81919be8fdb11a892483` | `d37cd47e0139d30bfcc9a65d9aba779e6c533dfc` | `68b096092e488fa5600babc244a98a955186daf5` | Push PASS; identity PASS; content PASS |
| 2 | rigorous-math-tutor | `skill-6ab8d7746f0c81919625f7a2e38672d2` | `e1126ec5a57363dea4906740d5a9f976a6974a02` | `0537a4be4b1bfd6d1b514ced2a81311676876d1a` | Push PASS; identity PASS; content PASS |
| 3 | statistics-quant-lab | `skill-6ab8e0879ddc8191a31bd0fc1f91da77` | `c273ed3724bfd27160fe207ff986bccfad32dad9` | `c273ed3724bfd27160fe207ff986bccfad32dad9` | Push PASS; identity PASS; content PASS |
| 4 | computer-ai-tutor | `skill-6ab8e8f26b24819190f3b1210fb803c1` | `329eabfc4607a3f8b0c88f266427c60e96af5b63` | `329eabfc4607a3f8b0c88f266427c60e96af5b63` | Push PASS; identity PASS; content PASS |

Each push modified only one existing ID directory. Every step completed remote read → push success → fresh fetch → canonical content/identity checks → durable evidence save before proceeding to the next Skill. No aggregate Skills push was attempted.

Raw push output, full per-Skill canonical files, hashes and checks:
- [interactive-learning-designer.json](intelligent-ui-account-sync-2026-10-12/interactive-learning-designer.json)
- [rigorous-math-tutor.json](intelligent-ui-account-sync-2026-10-12/rigorous-math-tutor.json)
- [statistics-quant-lab.json](intelligent-ui-account-sync-2026-10-12/statistics-quant-lab.json)
- [computer-ai-tutor.json](intelligent-ui-account-sync-2026-10-12/computer-ai-tutor.json)

## Canonicalization

All four installed SKILL.md files match the GitHub authority **byte-for-byte**, including frontmatter and body. Designer's three intended references also match byte-for-byte. The final file sets exactly match the authority's intended directory sets; no superseded experience-design.md or practice-design.md is present.

Observed platform changes, permitted by the installation request:

- skill-6aca39ab0c8c81919be8fdb11a892483/agents/openai.yaml YAML formatting canonicalization.
- skill-6aca39ab0c8c81919be8fdb11a892483/assets/icon.svg platform replaced source SVG 4b96fd7df071003784fca4ca12e23a9bdfe37f58 with canonical platform icon f387e96b74b4a2a407760075db8859a99fdf91f1.
- skill-6ab8d7746f0c81919625f7a2e38672d2/assets/icon.svg platform replaced source SVG f0ec0fb4fb305880342dc69ee33cec099fb4dd24 with canonical platform icon 16cc917601dd1e26eec844321d180f0b1a669759.

Statistics and Computer/AI had no content canonicalization. YAML semantic values remained unchanged; all four `allow_implicit_invocation` values are `true`. Icon changes are actual platform asset substitutions, not byte-identical copies or merely whitespace changes. No identity was recreated to correct metadata.

## Core content checks

- Math: exact active-use instruction retained: “主动直接使用，即使用户没有点名 UI，也不要等待 `interactive-learning-designer`”. Strict-proof boundary retained.
- Statistics: same active-use instruction; theory/simulation/empirical-data distinction, post-hoc power rules, and inference/data-leakage boundaries remain present.
- Computer/AI: same active-use instruction; UI simulation is not execution in the user's environment, and actual execution requires real tool evidence.
- Designer: ordinary UI belongs directly to the domain Tutors; Designer is not a prerequisite. Only complex state, linked views, shared input, branches, back/reset, feedback and QA belong here. The domain Tutor owns definitions, questions, content, proofs and answer criteria.

## Final seven-Skill inventory

| Skill | Account ID | Canonical SKILL.md blob | Result |
| --- | --- | --- | --- |
| course-tutor-builder | `skill-6ab7def0ccf48191baf6dd3758b30516` | `2961a0ca7c8c2a2acac707a712bd9ce472c5e7b2` | Unchanged (whole directory tree hash) |
| rigorous-math-tutor | `skill-6ab8d7746f0c81919625f7a2e38672d2` | `8194fe508447bc7393cb66d29a2617fce0cc5fbc` | Updated, exact authority SKILL.md |
| statistics-quant-lab | `skill-6ab8e0879ddc8191a31bd0fc1f91da77` | `a79584a443075b255b1f3d140dac955fd23ff082` | Updated, exact authority SKILL.md |
| computer-ai-tutor | `skill-6ab8e8f26b24819190f3b1210fb803c1` | `8c50876c48cb02b083780653aae823b79669c00a` | Updated, exact authority SKILL.md |
| obsidian-academic-kb | `skill-6ab8f11863448191ba3dadde8037d515` | `a16e7e2839e82e70b2db1595fe6a17edd1b6bd5e` | Unchanged (whole directory tree hash) |
| interactive-learning-designer | `skill-6aca39ab0c8c81919be8fdb11a892483` | `7b3dc12827470faaf5e8f358bec13145932d2ce4` | Updated, exact authority SKILL.md |
| learning-progress-coordinator | `skill-6aca3a1602908191a5fe5c8484f8d28d` | `de9a5851591eb7ffd8804a221bbc23d0e7c8bfdb` | Unchanged (whole directory tree hash) |

All seven are present; no duplicate names or IDs. The account also has the unrelated webcodex-project-driver, which remained unchanged. Course Tutor Builder, Learning Progress Coordinator and Obsidian were verified unchanged by full directory tree hashes and all file blobs against the baseline, both after each push and in the final fresh account export.

Final canonical account ref: `329eabfc4607a3f8b0c88f266427c60e96af5b63`.

Machine-readable final inventory, before/after references, per-file hashes and preservation checks: [final-verification.json](intelligent-ui-account-sync-2026-10-12/final-verification.json).

## Stop boundary

The four account updates are complete and ready to enter a separate ordinary Chat Intelligent UI runtime acceptance. No runtime invocation/interaction claim is made by this report. No real learning Progress or Obsidian Vault was changed. PR #2 remains Draft; no merge, release or tag was performed.
