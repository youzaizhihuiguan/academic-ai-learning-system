# v0.5.0 Work Skill sync HTTP 422 — resolved

Date: 2026-10-10 (UTC). Repository: `youzaizhihuiguan/academic-ai-learning-system`; construction branch: `feat/v0.5.0-learning-fusion`; PR #1 remains Draft.

This report supersedes only the **new-two-Skill installation blocker** in [the earlier Work report](g4-work-installation-report.md). Earlier observations remain historical evidence. Full G4/G5 acceptance and v0.5.0 release remain pending.

## Actual failure and diagnosis

- Official workspace: `/root/.codex/skills/remote-skills`.
- Fetch and push remote: `https://chatgpt.com/backend-api/git-authed/skills`; no separate push URL. Local `master` tracks `origin/master`; remote HEAD advertises `refs/heads/master`.
- At recovery, local and remote were `025e2b96035bdf28902add17f0abe030f48d8fee`. Existing candidate commit `03a249a6a22e8de254790e2d2c84195888c22ff1` was still in local Git objects and restored by fast-forward. It was one commit ahead, zero behind, and changed two Skill bundles. No candidates were regenerated or duplicated.
- Reproduced with `git push --verbose origin HEAD:refs/heads/master`. Receive-pack and upload-pack advertisements returned HTTP 200. The **POST git-receive-pack** (14055 bytes) returned HTTP/2 422, `text/plain; charset=utf-8`, 76-byte body, request ID `e7da3617-9452-4062-916e-bb2b5fec6565`.

Exact service response:

```text
invalid push content: aggregate skills Arcade push may modify only one skill
```

Git exited 1 with RPC/curl 22, unexpected sideband disconnect and remote hangup. Its trailing `Everything up-to-date` was not an installation receipt; the remote remained at the baseline after the rejected aggregate push.

The service explicitly rejected the **number of Skills changed in one push**. This is not a diagnosis inferred from status 422. No metadata, credential, permission, branch-name or Skill-text change was needed to make the same official route succeed.

Diagnostics captured curl response headers/body into a private temporary trace. Only received status, content type/length, request IDs and sanitized response bodies were retained. Outbound authorization headers, cookies, request payloads and credential configuration values were excluded; the raw trace was deleted. The machine-readable evidence includes the sanitized Git error and response.

## Minimal repair and sequential official sync

The original aggregate commit was retained locally at `recovery/v050-original-candidate-03a249a`. A mixed reset to the baseline preserved the two existing candidate folders. Only `interactive-learning-designer` was staged for the first commit. After successful push, the platform's actual canonical account snapshot was fetched and used as the base for the second Skill. The untracked coordinator folder survived that alignment. No force push was used.

| Step | Client commit | Push result | Fresh canonical remote HEAD |
| --- | --- | --- | --- |
| First: interactive-learning-designer only | `9c187f8af1519663190525daddc5388966d13847` | exit 0; `025e2b9..9c187f8 master -> master` | `f8f5fcaeabc9ada13a06b8d129449b3dbba459d6` |
| Second: learning-progress-coordinator only | `8c064973c9daf51cb6fc3bfbb7d226e207f79076` | exit 0; `f8f5fca..8c06497 master -> master` | `2efafac6e339a8bac38974d3f5d3cf2a7e18ac3f` |

The service materializes a canonical aggregate snapshot with assigned Skill ID directories. Its exported HEAD differs from the client push commit. Fresh `git ls-remote`, `git fetch` and content verification were therefore used instead of assuming that client and canonical commit IDs must be identical. Local `master` was finally aligned to the latest canonical remote HEAD and was clean.

## Account inventory and authoritative content

The freshly fetched account export contains each new internal name exactly once:

| Internal name | Assigned account Skill directory | Persistent account state |
| --- | --- | --- |
| interactive-learning-designer | `skill-6aca39ab0c8c81919be8fdb11a892483` | Present, complete five-file bundle |
| learning-progress-coordinator | `skill-6aca3a1602908191a5fe5c8484f8d28d` | Present, complete five-file bundle |

The authoritative GitHub tree at `8fd428e3d432be37967e2deaed3bd8301bc2ad82` was independently re-read. For both Skills:

- `SKILL.md` and both `references/*.md` match the authoritative Git blob hashes exactly.
- The five-file inventory matches. YAML parsing of `agents/openai.yaml` is semantically equal, although remote serialization changes its byte hash.
- `assets/icon.svg` differs after the service round trip. Designer's returned icon matches the existing CS tutor icon; coordinator's returned icon is a heart. The source icons were not changed to hide this difference. **The full bundle is not byte-identical**; icon fidelity remains a documented presentation discrepancy.
- All original five complete Skill subtree hashes are unchanged from `025e2b9`; the existing WebCodex driver is also unchanged. Their rollback baseline is preserved by Git history.

The JSON evidence records every source/remote file hash and every original bundle tree hash. Installation persistence is established by successful writes plus fresh account-export reads. This is stronger evidence than a local candidate or an unverified push receipt, but does not establish implicit runtime invocation.

## Session loading limitation and remaining acceptance

The current executor Skill catalog was read after each push, including all pages. It still lists the six pre-existing user Skills and omits both new IDs. Explicit `skills.read` against each newly assigned package returned `skill package is not available`. The observed session catalog has not refreshed; the mechanism or refresh timing is not established. Do not count this as a Skill invocation or claim automatic triggering passed.

Next runtime check: start a fresh **ordinary Chat**, check both existing installed identities in its Skill selector/manager, then execute the unchanged [runtime acceptance protocol](runtime-acceptance-protocol.md). Record actual routing, loading and UI operations. Do not create duplicate Skills or use a Work teaching demonstration as ordinary Chat Intelligent UI acceptance. If a fresh conversation also cannot load the installed identities, investigate that separate catalog/runtime boundary using the canonical IDs and remote snapshot above.

| Gate | Current result |
| --- | --- |
| Official sync of the two existing candidates | PASS |
| Persistent account inventory / core content readback | PASS, with YAML serialization and icon differences above |
| Current Work host loading | BLOCKED: catalog omits new packages; explicit package reads unavailable |
| Automatic routing, ordinary Chat Intelligent UI, cross-chat private Progress restore | PENDING; no new live case credited |
| Original four Skill updates | Deferred; original five installations unchanged |
| G4 / G5 / v0.5.0 | Partial acceptance / not started / not released |

No real learning Progress or Obsidian Vault was accessed or modified in this investigation. No PR metadata was edited, no merge was performed, no `main` write or release tag was created. Main remained `b40363416a3c153d903612eb1ec70573e44b31f9`.
