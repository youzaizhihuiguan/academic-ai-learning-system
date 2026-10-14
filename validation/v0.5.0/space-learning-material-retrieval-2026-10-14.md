# Space Learning Material Retrieval — 2026-10-14

## Objective

Add a minimal cross-course source-discovery convention without introducing a new Skill or duplicating long-term learning materials into multiple Projects.

User convention:

`Space / 学习资料 / <课程或主题>`

Examples include traditional courses (数学分析、常微分方程、概率论) and nontraditional learning tracks (AI 全栈、Python、系统工程).

## Product boundary verified

Current OpenAI Space documentation states that Space is the home for pages, uploaded files and related work; for accounts with Space, Space replaces Library. Projects remain separate and continue to organize project chats, files and instructions.

Authoritative references:
- https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt
- https://help.openai.com/zh-hans-cn/articles/20001549-getting-started-with-space-in-chatgpt

Therefore this implementation does **not** assume that a Project automatically inherits every Space file. Direct Space retrieval is capability-dependent: if the current environment can access the relevant Space content, the Tutor may retrieve it; otherwise it asks the user to reference/add the existing Space file rather than uploading another copy.

## Architecture

### Space

Long-lived, cross-course reusable learning sources:
- textbooks;
- lecture notes;
- transcripts;
- README / course originals;
- examples and supporting source material;
- other durable learning references.

Default user organization:

`学习资料/<课程或主题>`

This is a convention, not a claim that every account must use the same directory name.

### Project

Course/workstream runtime context:
- chats;
- current assignments;
- current-stage files;
- course-specific instructions;
- temporary artifacts;
- current learning state / pointers.

Do not duplicate the same long-term source into several Projects just to make it visible.

### Course Learning Profile / 课程学习配置

Keep only a lightweight source-location record:
- current course/topic long-term source location;
- important primary sources by name;
- prerequisite course/topic source pools only when they are genuinely useful.

Do **not** create an exhaustive per-file Reference Registry.

### Domain Tutor retrieval behavior

1. Prefer current conversation / Project context when sufficient.
2. If source text or course material is needed, consult the current course learning configuration for the long-term source location.
3. If Space is accessible, search `学习资料/<当前课程或主题>` first.
4. Search a prerequisite course/topic directory only after a real dependency has been identified.
5. Read only the chapter/fragment needed for the current problem.
6. Return to the current course mainline after filling the dependency.
7. Do not scan all of Space without a reason.
8. Do not ask the user to re-upload a duplicate merely because the current Project lacks the file.
9. If Space cannot be accessed in the current environment, state the limitation and ask the user to reference/add the existing Space file.

## Modified Skills

Only four existing Skills are modified:

1. `course-tutor-builder`
2. `rigorous-math-tutor`
3. `statistics-quant-lab`
4. `computer-ai-tutor`

Not modified:
- `interactive-learning-designer`
- `learning-progress-coordinator`
- `obsidian-academic-kb`

No Skill descriptions / trigger metadata were changed, avoiding new auto-routing behavior.

## Source blobs

- `skills/course-tutor-builder/SKILL.md`
  - `1c9067b112eb09a7b03d356538e0d41f8dc8ff05`
- `skills/course-tutor-builder/references/profile-schema.md`
  - `0dd2f3881149e3426b4262bf6b9d700493da51c1`
- `skills/rigorous-math-tutor/SKILL.md`
  - `547ca6b200a2a8ce1ed62999b87f2923418973d1`
- `skills/statistics-quant-lab/SKILL.md`
  - `24094ce7fd8899f56b527b01ad158ea3914dcf1b`
- `skills/computer-ai-tutor/SKILL.md`
  - `ca11d597899460fa01dce7d15797b003bf8a556c`

Base for this stacked branch:
- PR #2 installed/evidenced head:
  `6039784d7f6ac210f97c172e236e05d743e5b3ba`

## Skill Creator validation

Official scripts used:
- `quick_validate.py`
- `package_skill.py`
- `unzip -t` archive integrity check

All four Skills: **PASS**.

### Packages

| Skill | ZIP bytes | SHA-256 |
| --- | ---: | --- |
| course-tutor-builder | 16,839 | `4b4395aec8687feb53db6d44f477c2f4d211e62ae0eeffae9cd78fbce5590fd2` |
| rigorous-math-tutor | 4,803 | `5a4ba355f3cc78a59ac29d5c0c434c2f2c8f297ecdb73c214ea6023eedea37b4` |
| statistics-quant-lab | 5,213 | `4778da8faf7de0446a5fc3bcf2fd0397292c955ca83f3826db7da499a23ec47a` |
| computer-ai-tutor | 5,320 | `6acf3eff61013337229d0e054813591a05053a67be417268cfbe40dec6888bbe` |

## Acceptance matrix

| ID | Scenario | Expected behavior |
| --- | --- | --- |
| S01 | ODE question is fully answerable from current Project context | Math Tutor answers directly; no Space search. |
| S02 | ODE needs exact wording from current ODE textbook | Search `学习资料/常微分方程` if Space is accessible; retrieve only relevant section. |
| S03 | ODE genuinely needs a linear algebra prerequisite | After identifying the dependency, search `学习资料/高等代数`; fill only the needed prerequisite, then return to ODE. |
| S04 | Probability question needs a mathematical-analysis prerequisite | Stats Tutor searches the prerequisite source pool only after the dependency is established. |
| S05 | AI 全栈 lesson needs Python async/event-loop background | Computer Tutor may search `学习资料/Python` only after identifying the prerequisite, then return to the AI 全栈 task. |
| S06 | Current Project lacks a textbook that exists in Space, but Space access is unavailable in this chat | Tutor asks the user to reference/add the existing Space file; it does not request a fresh duplicate upload by default. |
| N01 | Simple question answerable from known definitions | No Space search. |
| N02 | Tutor merely suspects another course may be related | No prerequisite Space search until the dependency is actually relevant. |
| N03 | User has many unrelated files in Space | No broad Space scan. |
| N04 | User explicitly supplied a file in the current conversation | Use that file; do not go searching for a second copy in Space. |

## Deployment boundary

This branch changes repository source only. Account-installed Skills remain unchanged until formal Skills Git sync updates the four existing identities.

Installation must preserve existing Skill IDs and follow the previously observed backend restriction: one Skill per push, with rollback and canonical readback after each update.

Do not create duplicate Skills.

Do not merge PR #2 or this stacked PR merely because source validation passed. Runtime/account acceptance remains a separate gate.
