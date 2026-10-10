# R03 — Ordinary Chat interactive-math user acceptance

- Date: 2026-10-10 (Asia/Tokyo).
- System: Academic AI Learning System v0.5.0, complex native teaching interaction.
- Environment: user's **ordinary Chat**; a live DIL stateful interface was rendered in the conversation.
- Source authority at test entry: `feat/v0.5.0-learning-fusion@cb2ee1a6f19292d1962f2cc86f7ed5178caa0e40`.
- **Verdict: R03 PASS as user-observed functional acceptance.** The earlier `PARTIAL` status in `g4-independent-ordinary-chat-acceptance-2026-10-10.md` remains accurate *as of that previous checkpoint*, but is now superseded for R03 by this new observation.
- Scope restriction: evidence is one user's submitted state plus explicit visual confirmation, **not independent browser telemetry**, recording of each event, or a cross-platform compatibility result.

## Actual user interaction

The rendered interface implemented `A(t)=[[1,t],[t,1]]` with preset parameter buttons, an editable numeric input, rendered transformed unit square, determinant/area outputs, invalid-input feedback and reset. Its submit control was authored as disabled until all five client flags (tested `t=1`, `t=-1`, `t=2`, invalid input and reset) and the explicit `visualOK` checkbox were true.

The user submitted this message via the interaction:

> G4 实际交互验收结果：已依次测试 t=1、t=-1、t=2，触发非法输入并重置；界面提交的状态为 t=0、det=1、面积倍数=1。我已勾选确认图形、数字、错误提示和重置正常显示。请判断 R03 是否验收通过，说明证明范围；不要写入长期学习 Evidence。

A previously submitted separate R03 case reported `t=-2, det=-3, abs_area=3`. Neither submission records hidden client event history; the visual outcome is supported by **the user's explicit confirmation**.

## Independent mathematical oracle

Using `T_t(x,y)=(x+t*y,t*x+y)`, `det A(t)=1-t^2`, and the independent transformed-polygon area oracle already calculated in the prior engineering report:

| State | determinant | unsigned area factor | geometric expectation |
| --- | ---: | ---: | --- |
| t=1 | 0 | 0 | rank-1 degeneracy (segment) |
| t=-1 | 0 | 0 | rank-1 degeneracy (segment) |
| t=2 | -3 | 3 | orientation reversed; area factor 3 |
| reset t=0 | 1 | 1 | identity, unit square restored |
| previously submitted t=-2 | -3 | 3 | orientation reversed; area factor 3 |

No discrepancy in the submitted final `(t,det,area)=(0,1,1)`.

## Acceptance scope

**PASS in current ordinary Chat:** preset transitions were operated, an invalid input was triggered, reset returned to identity, displayed picture/numbers/error feedback were confirmed by the user, and the submitted state propagated into this conversation. The input-handler model and independent formula/polygon checks were also previously executed and passed.

**NOT PROVED:** exhaustive real browser trace of each UI event, pixel/geometry accuracy under all viewports, cross-browser consistency, every possible numeric input, actual installed-Skill **implicit auto-selection** in a brand-new chat, other subjects' R04/R05 interactions, Coordinator persistence, or learner mastery.

This is a **technical UI acceptance record only**, not a long-term Learning Evidence, Review Queue entry or personal Progress update. No real user learning data or Obsidian Vault write was performed.

**Release gate:** R03 is closed as PASS; G4 overall remains PARTIAL because fresh-chat routing and other runtime scenarios are not yet completed. PR #1 remains Draft; do not merge main or create v0.5.0 tag.
