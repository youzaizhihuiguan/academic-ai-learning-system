# Academic AI Learning System

本仓库保存一套可恢复的长期学习接口。每一层只回答一个问题：

| 层 | 回答的问题 | 唯一的主要记录位置 |
| --- | --- | --- |
| Source / Curriculum | 学什么，原路线、术语和阶段是什么？ | [`sources/`](sources/) 与[来源清单](sources/manifest.md) |
| Course Learning Profile | 这门课沿什么路线、用什么深度和证据标准学习？ | [`profiles/`](profiles/) |
| Progress / Evidence / Learning Debt | 现在到哪里，哪些真实证据、缺口与下一步？ | [`progress/computer.md`](progress/computer.md)；产物本体在项目仓库 |
| Domain Tutors | 如何理解、证明、建模、练习和定位问题？ | 用户当前问题 + Profile / Progress；五个安装 Skill 的快照见 [`skills/`](skills/) |
| WebCodex / Secure Tunnel | 怎样在**当前可访问**的环境实际运行、测试、模拟和调试？ | 项目仓库中的代码 / 测试 / 运行记录；本仓库只保留必要链接 |
| Obsidian | 明确提出沉淀时，什么知识值得长期保存？ | 用户的 Vault；未授权访问时只交付 Markdown 草稿 |
| GitHub | 怎样备份、看版本和跨环境恢复？ | 此仓库是系统文档基线；软件项目可独立建仓库 |

## 先从哪儿开始

1. 长期计算机路线：读 [`profiles/long-term-computer-science.md`](profiles/long-term-computer-science.md)；需要核查原 stage 时再看 [`sources/`](sources/)。
2. 本次真正的学习状态：读 [`progress/computer.md`](progress/computer.md)。目前未取得用户当前 Pxx 或实际 Evidence，不能把集成测试的案例写成你的学习进度。
3. 带着“当前问题 + 已知 Pxx + 最近证据或项目路径”找对应 Tutor；不必每次加载整条 70 KB 路线，也不必每次生成新课程协议。
4. 涉及本地代码或模型结果，需要真实执行时，先给可区分的假设，再运行最小检查，记录观察和回归结果。没有本机访问就说清尚未在你的环境验证。
5. 只有明确要求导入 Obsidian / 保存知识库时才整理笔记。概念和实验结论可以进入 Vault；完整代码、路线正文和聊天记录不搬进去。

`course-tutor-builder` 在输入或更新具体课程资料时生成 Profile；`rigorous-math-tutor` 处理独立严格证明；`statistics-quant-lab` 处理推断、模型评价及不确定性；`computer-ai-tutor` 处理代码和工程机制；`obsidian-academic-kb` 处理显式要求的沉淀。混合问题按当前问题的判断目标选一个主导者，形成一条回答；必要时吸收另一个领域的判断。

## 维护边界

- P00–P31 是随附计算机路线的原生编号，不是任何新课程的模板。Stage 可跨多轮；没有真实阶段需要时不制造 Round。
- Profile 仅在源资料、路线或教学协议实质变化时修订；当前阶段和新证据只改 Progress。一个 Evidence 只保留**位置与能支持的结论**，不在 Profile、Progress、Vault 各抄一份。
- [`skills/`](skills/) 是五个已安装 Skill 的恢复快照，**不是**这个仓库另起的平行安装版本；日常使用现有网页端 Skill。科研 / LaTeX Skill 暂缓，不在此添加。
- [`reports/`](reports/) 记录审计与本次真实链路测试；测试样例不自动提升为个人学习成就。

本次整体优化和稳定基线的证据见 [`reports/integration-2026-09-27.md`](reports/integration-2026-09-27.md)。
