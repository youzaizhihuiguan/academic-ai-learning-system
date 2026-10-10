# v0.5.0 — Four existing Skill updates and seven-Skill readback

Date: 2026-10-10 (Asia/Tokyo). **Installation update PASS; live runtime acceptance remains PARTIAL/BLOCKED. Not released.**

Authority: `feat/v0.5.0-learning-fusion@d325b7c6fba320331727fafc9cc3c9225c5e97b6`. User explicitly authorized updating the four existing Skill identities. This supersedes the old planning/PR installation deferral; it does not authorize a merge, main write or release.

## Baseline and rollback

Before mutation, fresh Skills remote and local master were clean at `2efafac6e339a8bac38974d3f5d3cf2a7e18ac3f`. All four pre-update SKILL.md hashes match G0. The 16 files in [rollback/pre-four-updates](rollback/pre-four-updates/) preserve complete installed bundles. They were committed before updating at `2b24d9d7b276ecd7c2f86534e4d3f26d47db1eb2`, and the GitHub tree was independently read: **16/16 exact blob hashes**.

The local recovery ref `recovery/v050-pre-four-updates-2efafac` also retains the complete account snapshot. Roll back by copying one archived bundle into its original `skill-<ID>` directory and pushing one Skill at a time. Do not push the aggregate old snapshot: it would change other Skills.

All 30 source blobs were independently retrieved at the pinned GitHub authority and matched existing local files. No Skill was regenerated, redesigned or rewritten. Each enhanced SKILL.md contains the original version verbatim followed by the already validated additive section.

## Sequential official updates

The official remote remains `https://chatgpt.com/backend-api/git-authed/skills`, current branch `master`. Each accepted push modifies exactly one existing identity and exactly one file, SKILL.md. No named duplicate was created.

| Skill | Existing identity | Client update commit | Final SKILL.md blob |
| --- | --- | --- | --- |
| course-tutor-builder | skill-6ab7def0ccf48191baf6dd3758b30516 | 1a839167642b44f04a30b9d6f048f70424282567 | 2961a0ca7c8c2a2acac707a712bd9ce472c5e7b2 |
| rigorous-math-tutor | skill-6ab8d7746f0c81919625f7a2e38672d2 | 45cb42fbe5e0fb52fa40b1d6867b7c72316a5aa2 | 407af7bec7eca89a7ed7e2ba152b0ff7f2ec972b |
| statistics-quant-lab | skill-6ab8e0879ddc8191a31bd0fc1f91da77 | 9e30f82430323cfe7591c49cfcf56a8021f95896 | 6d59e6030071301e111d0766a8ffaa4ea4189602 |
| computer-ai-tutor | skill-6ab8e8f26b24819190f3b1210fb803c1 | 9534bd3a04a6e2304e3ebe6439e566a43e4ed9a1 | 2a9ad170ba312a240f7e067bb00a705c30bd05df |

Every push exited 0. The final fresh canonical account head is `ad4d1eaa334325c1386d82ba2a233361661dbbc8`. A later fetch and ls-remote again returned the same head; local/remote diff was empty.

### Delayed materialization observations

- After Math's initial successful readback, `e5fc2e9` replaced only its icon. Its enhanced core remained exact. The next update stopped before writing because the remote moved; after verifying the delta, local master was aligned.
- CS push `9534bd3` was followed by canonical snapshot `c77254c` containing CS's OLD SKILL.md. Verification correctly failed. A proposed retry stopped before writing when the remote changed again; **no second CS push occurred**.
- The subsequent canonical snapshot `ad4d1ea` contained the intended enhanced CS blob. Final full readback and the later independent ref read agree. The mechanism behind the transient stale content is **unestablished**. A push receipt alone is insufficient.
- Final differences from source: Math icon only; both new Skills retain previously documented YAML serialization/icon differences. All seven SKILL.md and reference files are byte-exact, YAML semantics match. Do not claim all seven complete bundles are byte-identical.

Per-Skill raw safe push receipts, prior/final trees and content hashes are in [installed-updates](installed-updates/); full final inventory is [four-update-final-readback.json](four-update-final-readback.json).

## Seven-Skill inventory and ownership review

All seven learning Skill logical names occur exactly once in the account export; the separate WebCodex driver also remains installed.

| Skill | Account content result | Primary owner / boundary |
| --- | --- | --- |
| course-tutor-builder | Enhanced source exact | Stable course CLP and source fidelity; live Progress belongs to Coordinator |
| rigorous-math-tutor | Enhanced core exact; platform icon differs | Conditions, proof and mathematics; simple UI optional, independent of Designer |
| statistics-quant-lab | Enhanced complete bundle exact | Inference, design and uncertainty; simulations do not replace assumptions; post-hoc power rule retained |
| computer-ai-tutor | Enhanced complete bundle exact | Code/system semantics and real execution evidence; voluntary checks do not interrupt delivery |
| interactive-learning-designer | Existing core exact; prior YAML/icon differences | Complex learning interaction state/feedback; domain correctness remains Tutor-owned |
| learning-progress-coordinator | Existing core exact; prior YAML/icon differences | Authorized persistent Progress/Evidence/Review Queue/Debt; does not invent observed answers |
| obsidian-academic-kb | Original complete subtree unchanged | Explicit Obsidian requests only |

Descriptions of the four updated Skills were unchanged. Reviewed additive sections preserve the original domain boundaries, CLP route, direct-answer behavior, proof/statistical rigor and explicit Obsidian export. No new ownership conflict was found in this **source-contract review**. It is not observed routing telemetry.

The existing G4 checker was executed against actual canonical ID directories through a name-to-ID path adapter: **7/7 PASS**. This checks structure, references, distinct descriptions and invariant anchors; it does not execute ordinary Chat routing or UI.

Protected complete subtrees—Obsidian, both newly installed Skills and the WebCodex driver—match the pre-update baseline exactly.

## Runtime acceptance boundary

The current Work executor catalog was read through all pages. It still lists six pre-existing user Skills. Its four old Skill readers return pre-update instruction bodies; reads of the two new packages return `skill package is not available`. This is a stale host-session view, not evidence that the freshly read account installation is absent.

The branch already contains [ordinary Chat load-check evidence](g4-ordinary-chat-load-check.md) at `d325b7c`: both new Skills' core files were accessible in ordinary Chat. That record does **not** cover the newly updated four, implicit routing or live UI.

A fresh direct browser check of https://chatgpt.com/ rendered Login/Sign up and no signed-in account. Thus this browser cannot test the installed account. No unauthenticated answer was counted as a Skill test. No credentials were read, copied or imported from the Skills Git channel.

The WebCodex fallback was capability-checked: Mac Runner online with browser read/control capability, Windows offline. The Mac Runner's registered Browser list was empty. Its Browser gateway does not support attaching the user's existing profile. No existing signed-in ordinary Chat surface was obtained. Native desktop actions were not performed.

**No ordinary Chat R01–R20 or historical 12 live routing scenario is credited in this Work run.** No UI demonstration in Work substitutes for ordinary Chat acceptance. No personal Progress or real Vault was accessed.

## Next allowed action

In the user's ordinary Chat environment:
1. Read the SAME four installed Skill identities and confirm their `v0.5.0` sections; load both existing new identities. Do not reinstall or create copies.
2. Follow [runtime-acceptance-protocol.md](runtime-acceptance-protocol.md) with fresh chats and record actual routing, prompts, outputs and UI actions. R03 must cover t=0, 1, -1, 2, invalid input and reset; R04/R05 need statistical/program semantic checks.
3. For R13/R15 use only the already authorized **synthetic private test Progress**, pinned/version-aware readback, and a second ordinary Chat. Storage primitive tests from the prior run are not cross-chat Coordinator acceptance.
4. Keep unobserved invocation marked unobserved and unexecuted cases PENDING/BLOCKED. Commit real evidence on this construction branch.

A direct logged-in test surface would permit automation. The current login boundary is an environment limitation, not a new permission requirement for installing Skills.

## Checkpoint integrity and protected state

The intermediate `e057679` statistics evidence file accidentally contained a missing-file diagnostic after the pre-write stop; `19aa9b8` replaces it with verified successful JSON. The CS checkpoint `38811d8` retained only the accepted push receipt while the local verifier failed (relative-path and helper-name errors); `b287ffc` replaces it with the completed canonical verification. These intermediate checkpoints are historical attempts, not PASS evidence. Final evidence uses parsed JSON and completed validation.

Main remains `b40363416a3c153d903612eb1ec70573e44b31f9`; PR #1 remains Draft/open/unmerged. No merge, release/tag, real learning record edit or real Vault operation was performed. The four installation updates are complete; **G4 remains partial and v0.5.0 remains unreleased**.
