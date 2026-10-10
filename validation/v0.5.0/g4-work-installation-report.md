# v0.5.0 Work installation and acceptance checkpoint

- Date: 2026-10-10 (Asia/Tokyo).
- Authoritative source: `feat/v0.5.0-learning-fusion@267069a3d2c10e5728c787d1d63d7c66ac0011f4`.
- Verdict: **G4 PARTIAL / BLOCKED. v0.5.0 NOT RELEASED.**
- This is a real installation attempt and synthetic storage test report, not a live teaching acceptance result.
- Current user instruction authorizes candidate installation/management tests; it supersedes the earlier design checkpoint's no-install wording. It does not authorize merge, main writes, release tags, real Progress edits, or Vault access.

## 1. Recovery and source checks

Re-read PR #1, fusion architecture, construction readiness plan, G4 verification and runtime acceptance protocol at the exact source HEAD. PR remained open, Draft and unmerged. Main was re-read at `b40363416a3c153d903612eb1ec70573e44b31f9`.

Re-fetched 30 source blobs (29 files in the seven complete Skill trees plus the existing source checker), computed each Git blob SHA from its UTF-8 bytes and verified equality with the remote tree. No Skill content was rewritten or regenerated. The existing checker returned:

```text
CHECKED 7 skills (expected 7)
PASS - source integrity and expected contract anchors
```

The earlier pull-request source CI at `b266cabc3ed17fcc7931ff28dfe8f5d2d67181a8` was independently fetched: run 38052985663 completed with conclusion success. No live routing result follows from this.

## 2. Actual Skills management and installation attempt

| Check | Observation | Verdict |
| --- | --- | --- |
| Formal browser entry | The agent-controlled cloud browser opened ChatGPT and showed the logged-out page, login buttons and no authenticated Skills management controls. This is not a statement about the user's own signed-in browser. | BLOCKED |
| Existing install inventory | Platform Skill catalog contained the five original learning Skills and WebCodex Project Driver; neither new Skill was listed. Original five SKILL.md hashes matched G0. | PASS (baseline only) |
| Existing full archives | No ZIP is tracked in the source tree. Two targeted title searches and a broader v0.5.0 title search did not resolve an existing archive in accessible Library. This does not prove earlier conversation attachments are unavailable to the user. | Unresolved |
| Work candidate preparation | Reused the existing two complete source folders unchanged. Each has SKILL.md, agents/openai.yaml, icon and two references; both passed the official quick_validate.py. | PASS (candidate files only) |
| Official Work save attempt | Skill Creator instructs committing and pushing the Skills workspace. Local commit `03a249a6a22e8de254790e2d2c84195888c22ff1` contains only these ten new files. Push failed with HTTP 422 and exit 1. | FAIL (save operation) |
| Post-attempt reconciliation | Independent ls-remote still returned `025e2b96035bdf28902add17f0abe030f48d8fee`. Platform catalog still lacked the two new Skills. Local commit alone is not installation. | BLOCKED (installation) |
| Original four update / rollback | No original Skill was changed. A diff against the complete baseline commit for all existing Skill paths was empty. Full original bundles remain in the remote Skills baseline and in main's source snapshots. | PASS (preservation); updates DEFERRED |

Push output retained verbatim, with no credential or account session data:

```text
error: RPC failed; HTTP 422 curl 22 The requested URL returned error: 422
send-pack: unexpected disconnect while reading sideband packet
fatal: the remote end hung up unexpectedly
Everything up-to-date
exit_code: 1
```

The final “Everything up-to-date” line is contradicted by the nonzero exit and unchanged remote ref; it must not be treated as success. The precise 422 cause was not established. No policy bypass, metadata alteration, duplicate Skill creation or force push was attempted. Local candidates were preserved as instructed by Skill Creator.

The reused upstream contract file has a pre-existing trailing space on line 42. git diff --check reported it; it was deliberately not removed because this task preserves the exact reviewed source bytes. This cosmetic warning is unrelated to any established installation rejection cause.

Observed AX state: title “ChatGPT: Chat, Work, Create & Code with AI”; URL https://chatgpt.com/; sidebar heading “获取为你量身定制的回复”; text “登录以获取基于已保存聊天的回答，并可创建图片和上传文件。”; login buttons in the sidebar and header. No authenticated Skills controls were available. The matching screenshot was inspected during the observation.

Official documentation consulted: [Build skills](https://learn.chatgpt.com/docs/build-skills?translationFallback=pt-BR). It describes explicit @ selection, implicit description-based matching and Work's @skill-creator. It does not explain this 422, establish this account's management UI availability, or certify installation.

## 3. Work-compatible synthetic Progress storage tests

Created one clearly fictional test-only Markdown Progress in the account's Library, separate from actual course state. It contains no personal grades, answers or real learner Evidence. No sharing operation, public write of private fixture identifiers, or user Vault operation occurred. This session did not independently audit storage ACLs; do not interpret it as a broad privacy certification.

| Test | Actual execution | Result |
| --- | --- | --- |
| Create and restore version 0 | Created fixture; read its saved bytes via the same stable file identity. Source and restored content matched. | PASS |
| Guarded annotation update | Updated with expected version 0; returned version 1. Readback preserved KEEP_THIS_LINE and added PRESERVE_CONCURRENT_NOTE. | PASS |
| Duplicate-event check | Event 001 already existed once; no duplicate update was dispatched. This is a controller-side check, not Coordinator telemetry. | PASS (controller check only) |
| Stale overwrite prevention | Submitted old bytes with expected version 0 after version 1 existed. Returned CONFLICT at version_check, expected 0/observed 1; readback confirmed no overwrite. | PASS |
| Re-read and merge | Materialized latest version 1, preserved annotations, merged a second fictional numeric variation, wrote with expected version 1; returned version 2. | PASS |
| Immediate unqualified readback | First unqualified read after the version-2 write returned version_id 1 and 938-byte old content. The missing event was detected; no save-success claim was made from this read. | Stale-read observation |
| Version-aware verification | Read with version_id 2 and materialized latest version 2. Final 1292 bytes exactly matched the merged file. Both event IDs occur once; original annotations and unknown stage remain. | PASS |

Final fixture SHA-256: `30e932207fa69f88a9b1f66704ad25c5c6f8fc3504cfab6adcf8e3d7f2b72ae4`.

The stale-read observation has an undetermined cause (e.g. caching/indexing cannot be asserted). During acceptance, compare returned version/content with the write receipt; use a version-qualified read or latest authorized byte retrieval before certifying the write. Preserve version guards.

These results establish storage primitives and version-aware recovery within this Work session. They **do not** establish installed Coordinator invocation, automatic mastery assessment, a second ordinary Chat's restore behavior, delayed retention or implicit Skill routing. The user has not selected this fixture as their real long-term Progress destination.

## 4. Pending ordinary Chat acceptance

No teaching UI was generated in Work and counted as Intelligent UI acceptance. Runtime cases R01–R20 and historical 12 remain live-pending as defined by [the unchanged acceptance protocol](runtime-acceptance-protocol.md).

- R03: ordinary Chat matrix transformation, determinant 1-t², t=0/1/-1/2, invalid input, reset, geometry/proof boundary.
- R04: ordinary Chat CLT experiment with theory/simulation distinction, assumptions and actual sampling.
- R05: ordinary Chat recursive stack interaction with correct states and explicit simulation boundary.
- R08/R09: no hidden-click read, no unassisted-mastery claim from AI demonstrations.
- R13: a separate ordinary Chat reads the authorized synthetic private fixture and restores only its actual recorded state.
- R15 storage conflict primitive has been exercised, but its installed Skill end-to-end scenario remains pending.
- All automatic routing observations must be recorded as actual invocation or unobserved, not inferred from a plausible answer.

## 5. Minimal continuation and rollback

1. In the user's already-authenticated ChatGPT account, open its actual Skills management entry and check the two new internal names before adding anything. If web does not expose this entry, use the desktop Skills entry or report the actual UI limitation; do not invent a menu.
2. If neither is present, import the **existing complete archives from the earlier construction chat**, interactive-learning-designer first and learning-progress-coordinator second. If those archives cannot be located, recover the complete reviewed source trees from this branch; do not regenerate the Skill text or create duplicates. Do not upload SKILL.md alone when a full bundle is supported.
3. Re-open each installed item; verify its internal name, description, references and icon against the recorded source hashes. Confirm both are available through a fresh @ selector where supported. A listing alone is not an automatic-trigger PASS.
4. Original four updates remain deferred until the new installation path is real and reviewable. Before each update, export/retain its complete old version or select its actual version-history rollback path, keyed to main and the recorded baseline hashes. Update the existing identity; do not create a second copy.
5. Run the protocol's teaching scenarios in **ordinary Chat**, starting positive automatic-trigger tests without explicitly selecting a Skill, then use explicit @ selection for separate invocation checks. Retain prompt, answer, operations, reset/invalid-input observations and any real Skill telemetry.
6. For R13, select the synthetic file named `Academic_AI_v050_Private_Test_Progress.md` in a new ordinary Chat and ask to restore that **test fixture only**. Do not substitute real personal Progress or a Vault. Store only non-private verdicts/hashes on this public branch; keep file identities and learner details private.

## 6. Gate and protected state

- G0–G3 source work retained; no redesign or Skill source edits.
- G4: source/static PASS; synthetic public and account-storage primitives PASS with limits; installation, implicit routing, ordinary Chat Intelligent UI and cross-chat private restore still BLOCKED/PENDING.
- G5: not started; no release claim.
- No PR merge, no main mutation, no release-tag creation, no real Progress modification and no Vault operation in this session.
- Recovery starts with this report and its evidence manifest, then actual installation—not a rerun of G0–G3.
