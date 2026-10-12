> **SUPERSEDED.** Final architecture is [intelligent-ui-native-layer-2026-10-12.md](intelligent-ui-native-layer-2026-10-12.md): Intelligent UI is a native Tutor response capability; `interactive-learning-designer` is only the complex-UI specialist. This historical report is retained for traceability and must not drive installation.\n\n> **SUPERSEDED by the wider experience-design revision.** The original one-file trigger-only patch and its ZIP/checksums in this report are historical checkpoints, **not the current source to install**. The authoritative updated design, file list, CI and runtime acceptance scope are in [interactive-capability-architecture-2026-10-12.md](interactive-capability-architecture-2026-10-12.md). The new Skill includes a revised body, metadata and design/QA references. Do not install the earlier narrow-patch ZIP.

# Interactive Learning Designer: automatic-trigger remediation (2026-10-12)

## Report and scope

User reports that the installed `interactive-learning-designer` "often does not activate on its own" during real learning. This is a user observation, not verified event telemetry. Current production source at `main@4ee98174574c0a41c4aaf66be0c6bc795f6085a2` has `policy.allow_implicit_invocation: true`, so auto-invocation was **not** disabled.

The original `SKILL.md` description, however, begins with the narrow trigger "用户明确要求...复杂的交互式教学界面"; the main body also says it should be loaded "只有真正需要复杂输入...". Official documentation states that implicit selection is based primarily on the `description`, with the full body loaded only after the Skill has been selected. See: https://learn.chatgpt.com/docs/build-skills

**Likely avoidable cause:** prompts that imply a high-value dynamic exploration ("我看不懂递归栈为什么这么变化") without mentioning "交互/UI/滑块" have poor lexical alignment with the old description. This is not evidence of a platform bug or a promise that changing descriptions will guarantee invocation.

## Targeted change

- Adjust **only** `skills/interactive-learning-designer/SKILL.md`: broaden *when to consider* the Skill to genuinely dynamic learning bottlenecks and high-value complex operable explorations, **including without an explicit UI request**.
- Retain the separate domain tutors' ownership of proof, inference, program correctness and ordinary explanation. Do **not** require UI for every math/statistics/CS question; don't treat simple diagrams as a reason to invoke a specialist.
- Retain client state, simulation-vs-execution, Evidence and private Progress boundaries.
- Leave the other six Skills, `agents/openai.yaml`, references, icons, installed Skill IDs, actual Progress, and Vault unchanged.

## Fresh ordinary-Chat prompt packet (runtime **NOT YET EXECUTED**)

Each prompt belongs in a clean new ordinary Chat with no explicit `@` Skill selection; record actual invoked Skill if telemetry shows it, rendered output and UI state. "Should consider" does not force this Skill to win against a domain tutor; when the domain tutor creates a correct simple UI itself, that can be acceptable.

| ID | Prompt | Expected behavior |
| --- | --- | --- |
| A01 | 我还是不理解矩阵怎样把正方形变成线段。改变矩阵里的参数会发生什么？能让我亲自试不同情况吗？ | Positive: offer operable parameter-geometry exploration; designer should be discoverable without the word "交互" |
| A02 | 中心极限定理里样本量变大究竟改变了什么？我想亲眼看 n 变化后的抽样结果。 | Positive: dynamic statistical simulation; differentiate theoretical prediction and synthetic draws |
| A03 | Python 递归返回的时候调用栈怎么一层一层消失？我真的看不懂执行顺序。 | Positive if multi-step changing stack visualization adds value; label any UI simulation |
| A04 | 二分法里每一步区间怎么缩小？我能连续选中点并观察下一步吗？ | Positive: stepwise state transitions with wrong-input/reset handling |
| A05 | 我想拖动 t 看两个向量是否共线，以及行列式什么时候变成 0。 | Positive: explicit input-driven experiment |
| A06 | 在概率模型里改变 p 时，分布怎样变化？要一个可以反复试的实验。 | Positive: tunable distribution and clear source of results |
| N01 | 伯努利微分方程是什么？用两段话讲。 | Negative: domain tutor gives concise answer, no specialist UI |
| N02 | 请直接证明介值定理，完整给出步骤，不要练习。 | Negative: math tutor direct proof, no forced interaction |
| N03 | 请帮我计算这个 2×2 矩阵的行列式。 | Negative: straightforward calculation |
| N04 | 给线性代数概念画一张静态示意图即可。 | Negative: domain tutor can use basic native UI without designer |
| N05 | 给我的网站设计一个漂亮的登录界面。 | Negative: nonlearning product UI work |
| N06 | 修复这个 Python traceback 里的 ImportError。 | Negative: CS/AI tutor debugging, no UI specialist |

## Acceptance protocol

1. **Structural/source check:** original content preserved apart from the two intentional description-and-activation edits; validator and full package checks pass. GitHub CI passes on PR.
2. **Installed identity check:** update existing `interactive-learning-designer` account Skill ID `skill-6aca39ab0c8c81919be8fdb11a892483`; do not add a duplicate. Save pre-update rollback snapshot.
3. **Official sync:** the ChatGPT Skills Git backend accepts **one modified Skill per Git push**; this patch changes only that Skill, but GitHub branch push by itself does **not** update installed account state. Sync through authorized Work channel and verify exact remote SKILL.md content with a fresh account export; account exports may normalize YAML/icons.
4. **Actual routing:** run fresh ordinary Chat A01–A06 and N01–N06. Record invocation telemetry where available; otherwise distinguish observed output from unobserved router decision. Do not infer real invocation from a plausible interactive answer.
5. **Regression:** mathematical/statistical/CS correctness, no invented observed results, no fake Evidence writes or Obsidian export, no mandatory quiz, ordinary tutor remains independent.

**Status:** source patch prepared; deployment and fresh-chat effectiveness remain pending until actually executed. Do not label the routing bug fixed from source tests alone, and do not create a release tag.


## Actual source/package validation completed

- Target production source before patch: `d7df19586c7354053913c43f2b1c026786583c6d` (Git blob), `main@4ee98174574c0a41c4aaf66be0c6bc795f6085a2`.
- New patched `SKILL.md` Git blob: `4f94cfb53755f611804597317067bb1bf7884506`. Both intentional edits are within this single file: its primary trigger `description` and matching activation guidance. The `name` and identity remain `interactive-learning-designer`.
- The official `quick_validate.py` returned `Skill is valid!`; the official `package_skill.py` produced one complete `skill.zip` (7,308 bytes).
- New package SHA-256: `9fdbc0880e9371f6bfabf5b1a971cdfd8ed7672289c7abd887dd15b15602d583`. `unzip -t`: no errors.
- Compared original v0.5.0 packaged archive vs new archive: **the only changed path is `interactive-learning-designer/SKILL.md`**. The other four files (two references, UI metadata and icon) are byte-identical to the original distribution.
- YAML parsing confirms `name` unchanged and `policy.allow_implicit_invocation == true`. Description length is 278 characters (below max 1024).
- These results prove source integrity and intent clarification, **not actual automatic routing**. Ordinary Chat still reads the previously installed version until the existing Skill ID is updated through the official Work Skills Git channel.
