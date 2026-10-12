# Intelligent UI Native-Use Architecture — 2026-10-12

## Correction

The previous PR #2 iterations over-specialized **Intelligent UI** as a learning-specific pedagogy. That framing is superseded.

OpenAI's current product documentation describes Intelligent UI as a general ChatGPT response capability that composes text, visuals and interactive elements around what the user is trying to understand or do. Learning complex topics is one important use case, not the ownership boundary of a separate teaching method.

Therefore the Academic AI Learning System should not rely on a dedicated Skill being selected before Intelligent UI can appear.

## Final responsibility model

### Domain Tutors use Intelligent UI directly

`rigorous-math-tutor`, `statistics-quant-lab`, and `computer-ai-tutor` remain the owners of definitions, question generation, examples/counterexamples, proofs, statistical inference, code semantics, hints and answer criteria.

Each is now instructed to **proactively use native Intelligent UI directly** when it materially improves understanding or operation, even if the user did not explicitly ask for UI, and **not to wait for** `interactive-learning-designer`.

Examples of normal direct Tutor UI:
- math: geometric/structural diagrams, parameter exploration, definition conditions, examples/counterexamples, proof-step highlighting;
- statistics: distribution/sampling/model views, sensitivity, uncertainty and experiment comparisons;
- CS/AI: call stacks, data structures, algorithm steps, memory/dataflow/model structure;
- any of the above: simple comparison layouts, one input/control, a small deterministic tool, simple exercise input/feedback.

Simple text remains preferred when text is clearer.

### Interactive Learning Designer becomes a complex-UI specialist

The existing identity `interactive-learning-designer` is retained, but its role is now narrow and technical:
- multi-step state;
- multiple linked views;
- shared inputs and derived state;
- branching;
- complex back/reset behavior;
- nontrivial feedback logic;
- interaction QA;
- reusable or unusually complex in-chat tools.

It does **not** own pedagogy, curriculum, definitions, question generation, proofs, inference or code semantics. It is not a prerequisite for Tutors to use Intelligent UI.

## Source changes on PR #2

Modified Skills:
1. `interactive-learning-designer` — refactored to complex Intelligent UI design/QA only; pedagogy-specific references removed and replaced by a generic composition reference.
2. `rigorous-math-tutor` — one additive v0.5 paragraph strengthened from "UI can be used" to proactive direct use.
3. `statistics-quant-lab` — same proactive direct-use rule with statistical evidence boundaries preserved.
4. `computer-ai-tutor` — same proactive direct-use rule with execution-vs-simulation boundary preserved.

Not modified:
- `course-tutor-builder`
- `learning-progress-coordinator`
- `obsidian-academic-kb`

No real Progress or Vault content changed.

## Package validation

Official Skill Creator validation/package checks were run after the architectural correction.

### interactive-learning-designer
- quick_validate: PASS
- package_skill: PASS
- ZIP integrity: PASS
- archive members: 6
- size: 7,356 bytes
- SHA-256: `7ef3f607d71fdebce6cc377ddb6d4179aca64ea13417abac400ff3a79db8d6c2`

### rigorous-math-tutor
- quick_validate: PASS
- package_skill: PASS
- ZIP integrity: PASS
- size: 4,489 bytes
- SHA-256: `79bf2efc5b2dc8e88453236bbdf6b64e6c33b4f19ebf4b82afe7a1f55bed1b6b`

### statistics-quant-lab
- quick_validate: PASS
- package_skill: PASS
- ZIP integrity: PASS
- size: 4,875 bytes
- SHA-256: `c7ba7f583e6bbdd11b8243cf002dcf4c16bb09d1aef99f753e1a94d1e5153874`

### computer-ai-tutor
- quick_validate: PASS
- package_skill: PASS
- ZIP integrity: PASS
- size: 4,974 bytes
- SHA-256: `fb5534a7eb39dd27d4f926826473a1feee83f091dbca28d884d216b0ce447730`

The three Tutor package SKILL.md blob hashes were checked against PR #2 and match exactly. The designer package is validated as a complete Skill bundle; GitHub CI remains the authority for branch source integrity.

## Runtime acceptance matrix

Run after official account sync, one modified Skill per push.

| ID | Prompt | Expected owner / UI behavior |
| --- | --- | --- |
| U01 | “为什么矩阵换基后数字变了但线性映射没变？” | Math Tutor; proactively choose a useful linked/visual UI if it helps. Designer need not trigger. |
| U02 | “给我解释 ε-δ 定义里两个量的先后关系。” | Math Tutor; may use a simple interactive/visual explanation directly. |
| U03 | “样本量增大时抽样分布为什么变窄？” | Stats Tutor; direct Intelligent UI if useful; theory vs simulation explicit. |
| U04 | “递归返回时调用栈怎么恢复？” | CS Tutor; direct state/stack UI if useful; no claim of real execution. |
| U05 | “给我两道定义辨析题。” | Domain Tutor owns question generation; may present via Intelligent UI, but designer is not required. |
| U06 | “比较三个估计方法的假设和不确定性。” | Stats Tutor; side-by-side Intelligent UI may be chosen directly. |
| C01 | “做一个有 4 个联动视图、共享参数、可回退历史和非法输入恢复的矩阵实验。” | Complex designer may trigger / lead UI engineering. |
| C02 | “这个交互有三个步骤和分支，切回上一步后图表没有同步，帮我修 UI 状态。” | Complex designer should be discoverable. |
| N01 | “伯努利微分方程是什么？两句话。” | Tutor concise text; no UI required. |
| N02 | “直接完整证明介值定理，不要互动。” | Math Tutor direct proof. |
| N03 | “修这个 ImportError。” | CS Tutor debugging; no UI unless genuinely useful. |

**Key acceptance metric:** ordinary learning UI should appear because the Tutor judges it useful, not because `interactive-learning-designer` happened to be routed. The designer's auto-invocation rate is only relevant for genuinely complex UI requests.

## Deployment boundary

The account still uses the previously installed versions until Work Skills Git sync updates the existing identities. Official sync must preserve IDs and perform **one Skill per push**:
1. `interactive-learning-designer`
2. `rigorous-math-tutor`
3. `statistics-quant-lab`
4. `computer-ai-tutor`

After each push: canonical remote readback, identity check, rollback evidence, then new-chat runtime tests.

Do not install duplicates. Do not claim runtime behavior fixed from CI alone.
