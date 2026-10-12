---
name: interactive-learning-designer
description: 复杂原生 Intelligent UI 的设计与验证。在学习/教学对话中，领域 Tutor 已经决定要讲什么、出什么题或如何判断正确性，但回答需要多步骤状态、多个联动视图、连续输入反馈、复杂回退/重置、交互逻辑审查或可复用的小工具时使用；也适用于用户明确要求创建或检查复杂交互体验。普通图示、图表、对照、单个控件、简单练习或其他日常 Intelligent UI 应由领域 Tutor 直接使用，不必等待本 Skill。非学习用途的网站或软件产品 UI 不属于本 Skill。
---

# Intelligent UI 复杂交互设计器

Intelligent UI 是 ChatGPT 的通用回答能力，不是本 Skill 的专属教学法。本 Skill 只负责**复杂交互结构与实现质量**：当普通 Tutor 已经知道内容和判据，但需要更复杂的界面状态、联动和验证时提供帮助。

## 职责边界

- **领域 Tutor 管内容。** 定义、出题、例/反例、证明、统计结论、代码语义、提示策略和答案判据均由相应 Tutor 或可靠来源决定。
- **领域 Tutor 也直接使用 Intelligent UI。** 普通学习问题只要图示、图表、并排比较、一个参数控件、简单输入反馈或小工具有帮助，就应直接生成，不需要调用本 Skill。
- **本 Skill 管复杂交互工程。** 多步骤状态、多视图联动、共享输入、分支、回退/重置、复杂反馈、交互 QA 或复用性较高的工具才值得加载。
- 不因为“学习”二字就触发，也不为了触发 Skill 强行把简单答案做复杂。
- 本 Skill 可以单独被选中，但不能假设会自动调用其他 Skill；学科内容不确定时先核实或明确边界。

## 工作方式

1. **读取 Learning Intent 与 Tutor Content。** 接收当前学习目标、领域内容、答案标准和用户偏好，不另建课程路线或教学法。
2. **判断复杂度是否值得专门设计。** 若领域 Tutor 用普通 Intelligent UI 就能完成，退回领域 Tutor；只有复杂状态、联动或交互正确性需要专门处理时继续。
3. **设计状态与视图。** 根据当前问题自由组合可用的文本、公式、图形、图表、按钮、选择、输入、表单和交互状态；不套固定模板。按需参考 `references/intelligent-ui-composition.md`。
4. **保证交互真实工作。** 控件必须改变对应状态或视图；共享派生数据同步；错误输入、边界、分支、返回和重置都要有实际行为。按需执行 `references/interaction-qa.md`。
5. **保持内容与界面分层。** UI 可以展示定义、练习、证明步骤、模拟或代码状态，但不能改写 Tutor 的学科判据，也不能把视觉现象冒充证明、把动画冒充真实执行、把模拟冒充实测。
6. **只报告真实可见状态。** 客户端本地点击不一定进入模型上下文。只有用户提交、支持的回调或可信工具结果才能形成可核查的 Interactive Observation；复杂交接参见 `references/interaction-contract.md`。

## 系统边界

- `rigorous-math-tutor`、`statistics-quant-lab`、`computer-ai-tutor` 等应直接使用普通 Intelligent UI；本 Skill 不是它们使用 UI 的前置条件。
- `course-tutor-builder` 决定课程级 CLP；本 Skill 不改变课程路线。
- UI 操作本身不是 Evidence。若领域 Tutor 已形成可核验 Evidence，且用户确有持久化诉求，再由 `learning-progress-coordinator` 按其规则处理。
- 只有用户明确要求 Obsidian 时才进入知识库流程。

## 降级

当前模式不支持所需交互，或复杂 UI 没有实际收益时，退回领域 Tutor 的普通 Intelligent UI 或纯文本回答。核心学科任务不得因本 Skill 不可用而中断。
