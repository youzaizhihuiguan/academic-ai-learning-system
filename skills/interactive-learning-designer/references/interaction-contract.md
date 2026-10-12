# Intelligent UI Handoff Contract

本参考只在当前学习回答需要**有状态交互、多个联动视图或可回传操作结果**时读取。它定义的是内容层与 UI 层的边界，不代表存在跨 Skill RPC。

## 1. Learning Intent / Tutor Content

领域 Tutor 或当前上下文提供：

- `learning_goal`：用户现在要理解或完成什么。
- `domain_content`：定义、公式、题目、步骤、数据、结论或代码语义。
- `ground_truth_constraints`：关键条件、答案标准、模型假设、运行边界。
- `response_preference`：是否要直接答案、练习、比较、探索、纯文本等。

这些字段决定**内容**，不是 UI Skill 自己发明的教学计划。

## 2. Intelligent UI Layer

本 Skill 负责把上述内容映射成当前 Chat 实际支持的界面：

- `inputs`：用户可修改/提交的值或选择。
- `visible_state`：当前可见状态与派生结果。
- `state_transition`：操作如何改变状态。
- `layout_and_views`：文字、公式、图、表、控件之间如何组合。
- `feedback`：仅展示已有判据能够支持的反馈；开放答案保留领域 Tutor / 工具核验。

不要求输出 JSON；这些是内部设计检查项。

## 3. Interactive Observation

只有真正回传到模型或可信工具的内容才能交给后续判断，例如：

- `input_or_action`
- `observed_result`
- `feedback_basis`
- `provenance`
- `evidence_limit`

客户端局部点击若没有进入上下文，不能猜测或补写。

## 4. Evidence / Progress

UI 只是表达与操作层。是否构成 Evidence 由领域 Tutor 根据学科标准判断；是否写入长期 Progress 由 `learning-progress-coordinator` 在真实来源、授权和存储条件满足时处理。
