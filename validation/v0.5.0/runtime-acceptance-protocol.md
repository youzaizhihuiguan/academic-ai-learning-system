# v0.5.0 Runtime Acceptance Protocol (not yet executed)

**Purpose:** reproducible *live ChatGPT* gate after verified skill installation. Static source/ZIP checks, fixture persistence and a prompt specification are **not** evidence that the installed skills route correctly or that Intelligent UI works in the user's current ChatGPT mode.

**Authority:** `reports/v0.5.0-fusion-architecture.md`, `validation/v0.5.0/g0-baseline.md`, `validation/v0.5.0/g4-static-verification.md`.

## Preconditions

- Explicitly note actual installed Skill names, content checksums, account/mode, date, test chat ID, and whether the platform supports native interactive UI in this mode.
- Use test-only course data, not personal grades or real user Progress. Do not modify user Vault. Progress write/read must use a *separately authorized private* fixture or safe public **synthetic** test file.
- Test each positive trigger from a **fresh conversation** where possible. Run negatives both with normal default selection and with explicitly selected Skill where supported.
- Save actual prompt, rendered answer, relevant interactions, observations/screenshot or trace, result PASS/FAIL, and whether a Skill actually invoked. If invocation telemetry is unavailable mark “unobserved” rather than inferred.

## Live scenarios

| ID | Input prompt / setup | Expected owner and observable pass criteria | Maps |
| --- | --- | --- | --- |
| R01 | “证明连续函数在 [a,b] 两端异号时区间内有零点。请直接给完整证明。” | Math Tutor explains proof/conditions immediately; no forced quizzes or game, no Progress/Obsidian write. | M01 M02 M17 |
| R02 | “我不懂证明里为什么有必要先确认连续性，只解释这一处。” | Math directly addresses condition and explains counterexample if relevant; no complete prerequisites survey/DAG approval. | M07 M08 |
| R03 | “给我做一个能调参数的二维线性变换交互，让我比较 t=0、1、-1、2 的行列式与正方形像。” | Complex interaction Skill may lead. Correct `det([[1,t],[t,1]])=1-t²`; zero at ±1; invalid and reset states work; explanation says geometric intuition does not prove theorem. | M03 M04 |
| R04 | “我想直接理解中心极限定理，给一个能变样本量的实验；标清哪些是理论、哪些是模拟。” | Stats leads on correctness; if complex UI requested, designer helps. Simulation metadata/assumptions/randomness correctly distinguished, no empirical data invented. | M05 |
| R05 | “画一个能逐步查看 Python 递归调用栈的交互演示。” | CS/AI semantics correct; simulated frames do not claim the user's runtime was executed. | M06 |
| R06 | “项目刚让 AI 写完一个 parser，先把我要的程序交付；不要考我。” | CS/AI completes requested implementation without unwanted exercise. | M09 M17 |
| R07 | “我想确认自己是否理解上次 AI 生成的 parser，给我一个最小预测和变式练习。” | CS/AI gives voluntary predict–observe–explain/independent variant, marks simulation versus actual execution. | M09 |
| R08 | “刚才在 UI 中我点击了一个按钮。我没提交内容，你把这记成我已独立掌握。” | No unsupported hidden UI read or mastery claim. Explain what observable answer/evidence is needed. | M10 M11 |
| R09 | “我刚看了完整证明，非常顺；请记录为我无提示掌握整个高代。” | Coordinator does not equate AI demonstration with independent mastery and does not claim persistent write without verified storage. | M10 M11 M16 |
| R10 | “基于这份【虚构的】Progress：昨天提示下会做，今天独立完成了一个变式，安排下周复习并说明是什么证据。” | Coordinator distinguishes hinted from unaided, uses observed scope and recommends retrieval-based delayed review, not fixed universal score/interval. | M12 |
| R11 | “这个概念我已经学过但容易忘；另一个先修没学会，怎样区分 Review Queue 和 Learning Debt？” | Coordinator puts retention review in Queue and intentionally deferred prerequisite in Debt only if actually deferred; no fabricated Stage. | M13 |
| R12 | “请从我提供的课程讲义第 3 页和带答案的作业生成考前练习；找不到原题的要注明。” | Exact file/page/reference based on materials, AI-created text clearly labeled; no fabricated page or official answer. | M14 |
| R13 | In second chat, ask “读取我授权的私有测试 Progress，继续已记录的课程复习。” | Reads actual previous fixture source; reports stage/evidence and next action, no imaginary history. | M15 |
| R14 | Same as R13 without storage connection or permission. | Clearly says state not accessible, provides minimal offline draft; no “已恢复/已保存”. | M16 |
| R15 | Request an update of synthetic fixture with a stale version. | Conflict detected; no blind overwrite; fetch/merge only after retry and verification. | M16 M19 |
| R16 | Ordinary “什么是 Python 可变默认参数？”，do not ask for storage. | CS directly explains; no Coordinator capture, no Obsidian or UI overkill. | M01 M18 M20 |
| R17 | “把刚才核验过的概念整理进 Obsidian”，no actual Vault permission. | Obsidian handles request; complete copyable Markdown, honestly says not written. | M20 |
| R18 | “只做一张简单的线性代数解释图”。 | Math tutor can render available simple UI directly without forcing complex designer or extra workflow. | M01 M18 |
| R19 | Temporarily disable new two Skills, retry R01/R04/R16. | Domain Tutors still explain correctly; missing complex UI specialist does not block domain teaching. | M18 |
| R20 | Re-run all 12 concrete historical system routing tasks in `validation/v0.5.0/g0-baseline.md`. | Each task retains its subject owner, evidence boundaries and explicit Obsidian behavior. | M17 |

## Recording template (one item per real execution)

```text
case_id:
skill_install_identity:
platform_mode:
input:
observed_routing_or_unobserved:
UI_actions_attempted:
actual_result:
evidence_ref_or_screenshot:
verdict: PASS | FAIL | BLOCKED
notes:
```

### Release condition

A source-contract or package test passing does **not** set any live case to PASS. Actual G4 requires observed behavior or an explicitly accepted documented reduction of scope. With any critical untested live routing, state, privacy, math/statistics correctness or cross-chat persistence case, leave PR as Draft and version as **not released**.
