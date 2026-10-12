# v0.5.0 — Open-ended Intelligent UI learning designer revision

Date: 2026-10-12 (Asia/Tokyo). Status: **source revision and CI PASS; account sync / fresh-chat automatic routing not yet accepted**. PR #2 supersedes its earlier one-file trigger-only proposal.

## Feedback and diagnosis

Real-user feedback identifies two different deficiencies:

1. **Activation**: the initially installed description required the user to explicitly request a complex interactive UI, missing many high-value learning situations.
2. **Creative scope**: even the first trigger-only patch emphasized sliders, dynamic graphs, matrices, sampling and recursion too strongly. The operative skill text lacked a strong design process for choosing and composing unbounded native Intelligent UI experiences, and its "complex interactions only" criterion could discourage simple but high-value explorations.

OpenAI's current Intelligent UI guidance describes compositional text/visual/interactive responses chosen for the question, not a fixed component/gallery checklist: https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt and https://openai.com/index/gpt-6-for-everyone/.

## Revision implemented on existing PR #2

**Only `skills/interactive-learning-designer/` was edited; original Skill identity preserved.** The files changed from `main` are:

- `SKILL.md`: new activation description (does not require "UI/交互" nor repeat failure), and a concise open-ended design workflow: learning intent → meaningful learner intervention → observation → explanation → optional evidence.
- `references/experience-design.md` (new): axes for objects, intervention, representation and discovery, plus non-exhaustive cognitive action primitives and cross-subject inspiration; explicitly not a closed list, template or mandatory checklist.
- `references/interaction-qa.md`: adds design quality tests for teaching value, composition, explanatory change, learner control, runtime capability and linked-view consistency.
- `references/interaction-contract.md`: broadens state/evidence handoff wording beyond only "complex continuous interactions".
- `agents/openai.yaml`: improves visible description and default prompt to reflect free composition. `policy.allow_implicit_invocation: true` remains unchanged.
- `assets/icon.svg`: not changed.

The four domain/builder Skills, coordinator, Obsidian, real Progress and Vault were not edited.

## Acceptance design: positive cases

The expected signal is **task-fit and meaningful interaction**, NOT one mandatory widget family. Run each case in a new ordinary Chat, without explicit Skill selection; record the actually invoked Skill if observable, the rendered UI, controls and correct domain explanation. A well-designed simple Tutor-generated UI may also solve a trivial case without the designer, but high-value interactive scenarios should discover and use the specialist more reliably.

| ID | Prompt (no mandatory "UI" vocabulary) | Quality oracle |
| --- | --- | --- |
| C01 | 为什么连续函数会在某处逼近一个极限？改变容许误差会怎样？ | Show ε-δ relation, test constraints and quantifiers; do not replace proof with plot |
| C02 | 我总搞混线性变换本身和换基后的矩阵；想看哪些东西真的变了。 | Linked object/coordinate representations; maintain invariant transformation |
| C03 | 初值不同，常微分方程的解曲线为何不同？我想观察稳定点。 | Direction field/solution trajectories with correct ODE assumptions |
| C04 | 抽样分布和原始数据分布到底区别在哪？样本量增大会怎样？ | Distinguish sampling distribution, theory, simulated draws and finite-sample uncertainty |
| C05 | 供需曲线平移时，均衡量、价格和福利为什么不一定同方向变？ | Different scenario interventions with correct curves and explanations |
| C06 | 递归返回的时候，变量和调用栈究竟怎么恢复？ | Runnable-state model steps/backtracking; no claim of actual execution |
| C07 | 我觉得贪心算法每一步选局部最优就行了；在哪些图上会失败？ | Interactive counterexample builder / decision trace and conditions |
| C08 | 为什么贝叶斯先验会改变后验？希望能从证据变化理解。 | Formula/visual linked updates with explicit model assumptions |
| C09 | 量词换顺序真的会改变真假吗？想自己试一个反例。 | Learner construction of counterexamples and immediate qualified feedback |
| C10 | 梯度下降会怎样穿过不同损失地形？为什么有时不收敛？ | Trajectory/step comparison and step-size trade-offs; label simplified model |
| C11 | 给我一个能自己操作的二分法过程，能回退和比较两条路径。 | State graph and next-step validation; not necessarily a slider or quiz |
| C12 | 我已懂公式，但还是看不出图和表、符号之间对应的是同一个对象。 | User-selected linked representations, focus/annotation, minimal clutter |

## Negative regression cases

| ID | Prompt | Expected |
| --- | --- | --- |
| N01 | 伯努利微分方程是什么？用两句话说。 | Domain Tutor concise text; no forced UI |
| N02 | 请直接完整证明介值定理，不要练习。 | Domain Tutor full proof, not interaction gate |
| N03 | 直接计算 2×2 矩阵的行列式。 | Calculation only |
| N04 | Python 的 ImportError 为什么发生？帮我定位错误。 | CS Tutor debugging, not visualization-first |
| N05 | 给我的 SaaS 网站设计注册页。 | Product UI out of this teaching Skill scope |
| N06 | 我只要一张静态坐标示意图。 | Simple native display by domain Tutor; no complex specialist requirement |
| N07 | 现在不想做练习，直接给正确答案。 | Respect answer preference, no coercive quiz |
| N08 | 我在界面点了按钮，请记为高代独立掌握。 | Reject unsupported evidence write |

## Verification and limits

- GitHub Actions validated all seven Skill source trees after the final `Learning Intent` contract anchor was restored. A previous intermediate attempt failed on that missing anchor and was **not** counted as passing; the later successful run is authoritative.
- GitHub branch diff should contain changes to this Skill only and validation evidence; no unrelated Skill files or real personal data.
- **Not yet established:** complete official Skill Creator ZIP packaging for this final revision, update of the account's original Skill ID, new-chat automatic invocation rates, actual rich interface behavior and state/feedback consistency on the target UI.
- The previously distributed ZIP for the narrow trigger-only patch is now **obsolete**; do not upload/install it. Use this PR's source after a full updated bundle validation instead.
- Correct installation path remains official Work account Skills Git backend, one modified Skill per push, existing ID `skill-6aca39ab0c8c81919be8fdb11a892483`, canonical readback and rollback. PR merge alone is not an installation.

## Decision

**Ready for review of design/content. Not yet approved for automatic installation, merge or runtime effectiveness claim.** We must test new Chat positive/negative routing against actual installed version first. Keep PR #2 Draft and main unchanged.
