# Four existing Skill updates — rollback baseline

Date: 2026-10-10. Source authority: feat/v0.5.0-learning-fusion@d325b7c6fba320331727fafc9cc3c9225c5e97b6.

User explicitly authorized updating the four existing identities using the validated source, superseding the older planning/PR installation deferral. No redesign is authorized.

Fresh account snapshot: 2efafac6e339a8bac38974d3f5d3cf2a7e18ac3f. Clean master tracks origin/master at https://chatgpt.com/backend-api/git-authed/skills. Local recovery branch: recovery/v050-pre-four-updates-2efafac.

The 16 files under rollback/pre-four-updates preserve complete pre-update bundles byte for byte. All four SKILL.md blobs match G0. Enhanced SKILL.md contains the original bytes as a prefix; only the reviewed additive v0.5.0 section follows. All 30 source blobs were independently read at the authority SHA and match existing local source bytes.

Update each skill-<ID> directory in place; never create a named duplicate. Stage and push exactly one Skill, fetch the service's canonical snapshot, check identity/content and untouched bundles before the next update. Rollback by restoring one backed-up bundle into the SAME identity, committing and pushing one at a time; do not push the local recovery branch or overwrite the aggregate account state.

Obsidian, both newly installed Skills and WebCodex driver are protected. Main, Draft PR and release state remain protected. Runtime acceptance remains pending.
