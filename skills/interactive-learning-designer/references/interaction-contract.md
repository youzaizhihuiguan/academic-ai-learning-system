# Interactive Learning Handoff Contract

本参考只在需要**复杂的连续学习交互**或打算将结果转成 Evidence 时读取。概念契约不等于实际存在的跨 Skill RPC、外部服务或跨聊天自动同步。

## 1. Learning Intent（学科导师或用户输入）

最低字段，仅收集当前真正需要的信息：

- `course_topic`：当前课程/知识点；未知课程进度不自作主张。
- `learning_goal`：希望通过本次交互认识/解释/训练/比较什么。
- `learner_task`：用户实际需要执行什么操作或回答什么。
- `ground_truth_constraints`：关键定理条件、模拟假设、程序语义、边界与已知答案；由领域 Tutor 或可靠来源负责核实。
- `prior_knowledge`、`assistance_mode`：若已知，区分探索、提示练习、无提示验证、直接答案。

不要为了使用 UI 必须先提问收集完整表单；信息足够就继续。

## 2. Interactive Experience（当前会话/界面层）

用户看到并操作的对象应具有可追踪的状态边界：

- `inputs`：可选参数/答案/操作，与合法取值、无效输入处理。
- `visible_state`：当前可观察状态；重置/切换后行为可预期。
- `state_transition`：每个操作如何改变状态（客户端内即时逻辑或需要新模型推理的两类应区分）。
- `feedback`：何种确定性判断能实时展示；开放答案应保留人工/模型/工具核验路径。
- `explanation`：变化与正确性依据相连，不把视觉现象宣称为数学证明。

不要求输出机械 JSON；上述字段是内部设计检查项。

## 3. Interactive Observation（面向领域 Tutor）

只有可真正观察并回传的项目才可供审查：

- `task_and_context`、`input_or_action`、`observed_result`、`feedback_basis`。
- `assistance_used`：示范、提示、无提示，若未知必须写“未确认”。
- `provenance`：工具结果/用户主动提交/可见对话/仅 UI 本地。
- `evidence_limit`：支持“观察了什么”，不自动支持“理解定理/长期掌握”。

本地 UI 值若没有进入模型上下文，不能把推测的动作历史当已提交的答卷。未验证的得分也不应进入 Progress。

## 4. Evidence Assessment（领域 Tutor）

领域 Tutor 根据学科判据独立判断：数学是否满足证明与量词，统计是否满足模型与数据假设，代码是否在真实环境运行。可以给 
`claim / basis / assistance / confidence_boundary / source_ref`；回答错误或不可核实时不得包装为“通过”。

## 5. Progress / Review（协调器）

只有具备来源证据、实际可读取的 Progress、被授权的可用存储位置时，才写入最小变化。写后回读确认；否则生成待保存建议，不声称跨聊天已保存。Progress 的职责不归此 Skill。
