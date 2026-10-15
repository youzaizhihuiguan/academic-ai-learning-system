# Google Drive learning-material retrieval — source validation

Date: 2026-10-15

## Authority

- Repository: `youzaizhihuiguan/academic-ai-learning-system`
- Base PR: #3 `feat(skills): retrieve cross-course learning sources from Space`
- Base authoritative HEAD: `eefb78afd0d0e668790406eaefde3a31e85bde9f`
- Construction branch: `feat/google-drive-learning-material-retrieval`

## Objective

Replace the PR #3 Space-specific long-term learning-source coupling with the user's current Google Drive learning-material library, without redesigning the learning system.

The fixed long-term material convention is:

`Google Drive / 学习资料 / <课程或主题>`

This change does not make cloud storage metadata part of a Course Learning Profile. Profiles retain source identity, authority, role, route, teaching depth, Evidence and other course-level rules; Google Drive is infrastructure.

## Scope

Modified existing Skills only:

1. `course-tutor-builder`
2. `rigorous-math-tutor`
3. `statistics-quant-lab`
4. `computer-ai-tutor`

Modified source files:

- `skills/course-tutor-builder/SKILL.md`
- `skills/course-tutor-builder/references/profile-schema.md`
- `skills/rigorous-math-tutor/SKILL.md`
- `skills/statistics-quant-lab/SKILL.md`
- `skills/computer-ai-tutor/SKILL.md`

Explicitly unmodified:

- Skill names and trigger descriptions
- `interactive-learning-designer`
- `learning-progress-coordinator`
- `obsidian-academic-kb`
- existing Evidence / Stage / Round / Learning Debt rules
- existing native Intelligent UI architecture
- existing domain boundaries

No new Skill was created.

## Retrieval contract

For the three domain Tutors and course handoff behavior:

1. If the current message, attachment or Project already contains sufficient material, answer directly and do not query the long-term library.
2. If course source text is actually required and Google Drive is accessible, query only `学习资料/<当前课程或主题>`.
3. Query `学习资料/<前置课程或主题>` only after a real prerequisite dependency has been established.
4. Retrieve only the files/sections needed for the current problem; do not scan the full learning library.
5. After filling a prerequisite gap, return immediately to the current course mainline.
6. If the relevant Drive is not connected or the current account lacks access, say so and prefer connecting the Drive or referencing/adding the existing Drive file rather than requesting a duplicate upload.

For `course-tutor-builder`:

- keep primary-source identity, role and authority in the Course Learning Profile;
- do not store Google Drive provider/path as course metadata;
- do not create a per-file Reference Registry;
- do not duplicate reusable long-term source files into multiple Projects.

## Source blobs

- `skills/course-tutor-builder/SKILL.md`: `e2acce5a8639273163e26defae8d43ca5c600503`
- `skills/course-tutor-builder/references/profile-schema.md`: `5013f71430779b48bdd32c18668363cbcb6ba19a`
- `skills/rigorous-math-tutor/SKILL.md`: `5007be92b6f1ea77d807278c873825af8641d920`
- `skills/statistics-quant-lab/SKILL.md`: `c4790246f4cf2174cb670293626d0dbe40c4eb26`
- `skills/computer-ai-tutor/SKILL.md`: `b0b39df64e448db824c334800042c8ae0cfb5081`

Local `git hash-object` values matched the GitHub content blobs for all five files.

## Skill Creator validation

Official Skill Creator workflow:

- `quick_validate.py`: PASS x4
- `package_skill.py`: PASS x4
- `unzip -t`: PASS x4

Packages:

- `course-tutor-builder`: 16,979 bytes; SHA256 `1c69ee23a209437ee2f3ef27884f70867202c00216044be4802f4bcabd9cb815`
- `rigorous-math-tutor`: 4,839 bytes; SHA256 `a85f898afa3011814865a3200e681ef42ec094b898cc25ed52db0e19519e352e`
- `statistics-quant-lab`: 5,249 bytes; SHA256 `a7a89e22d11b09ce9120fa6a1c7f3877f8d949ef52236b7e70b0ff002652d4de`
- `computer-ai-tutor`: 5,360 bytes; SHA256 `aa12fdfc2f89c13235f5f4efe17dfc5a5e20b8ea7729b8d8d7db14ae96d379f7`

## Acceptance matrix

| ID | Scenario | Expected behavior |
|---|---|---|
| G01 | ODE question answerable from current context | Do not query Drive |
| G02 | ODE requires exact current textbook source | Query only `学习资料/常微分方程` |
| G03 | ODE genuinely needs Advanced Algebra prerequisite | Then query `学习资料/高等代数`, retrieve minimum material, return to ODE |
| G04 | Probability/statistics genuinely needs math prerequisite | Query prerequisite folder only after dependency is established |
| G05 | AI full-stack task genuinely needs Python async/event-loop prerequisite | Query `学习资料/Python`, retrieve minimum material, return to AI full-stack task |
| G06 | Relevant Drive is not connected / current account has no access | State access limitation; prefer connect/reference/add existing Drive file; no duplicate-upload default |
| N01 | Simple definition/explanation | No Drive query |
| N02 | Merely related prerequisite course exists | Do not search prerequisite folder without a real dependency |
| N03 | Learning library contains many unrelated files | No full-library scan |

## Deployment boundary

Repository source only in this phase. Account-installed Skills remain on the PR #3 account-sync version until a separate formal account update is explicitly executed.
