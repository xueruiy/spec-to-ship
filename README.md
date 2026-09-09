# spec-to-ship

面向个人与小团队的 AI 辅助研发接入仓库：**原生 Matt Skills 负责澄清、spec、tickets、实施、测试和审查；本仓库补充项目接入、产品验收与知识同步。**

已收录固定版本的 12 个 Matt Skills 和 2 个自定义 Skills，原生文件不改写。工具链文件与项目链接方式已做本地检查，尚不能据此宣称真实业务交付已验证。来源、许可证和逐文件校验见 [SOURCES.md](SOURCES.md) 与 [upstream-manifest.json](upstream-manifest.json)。

## 如何使用

![原生 Matt Skills 到产品验收与知识同步](docs/diagrams/workflow-overview.svg)

**一次接入，按任务进入研发循环，按证据完成验收与知识同步。** 这是一组可组合的研发能力，不是每个需求都必须依次执行的七步流程。

- **首次接入**：安装只建立 Skills 入口；再调用原生 setup，按项目现状配置 tracker 与知识读取约定。
- **日常研发**：从当前缺少的信息开始，复用已确认的讨论、spec 和 tickets。开发、测试和审查可以反复进行，发现规格变化就同步相关产物。
- **交付收尾**：对照既定标准验收当前实现，记录用户决定，再将值得维护的知识更新到已有模块文档。未完成的任务也可以如实收尾。

| 你手头已有的内容 | 从哪里开始 |
| --- | --- |
| 一个尚不清楚的新需求 | `grill-with-docs` 澄清，再用 `to-spec` 固化决定 |
| 已确认且适用于当前代码的 spec | 需要分工或多个交付结果时用 `to-tickets`；简单工作不人为拆多份 |
| 清楚、可实施的 ticket | `implement`，复用关联 spec；执行测试和规定的最终回归、审查 |
| 一个已观察到的缺陷 | `diagnosing-bugs` 先复现定位，再修复并验证 |
| 已实现、准备交付的功能 | 核对验证与审查证据，再用 `sts-acceptance` 和 `sts-closeout` |

选择后面的入口意味着前面的信息已经足够，不意味着可以跳过缺失的标准、必要测试或产品验收。详细合同见 [workflow.md](workflow.md)。[可编辑 HTML 源图](docs/diagrams/workflow-overview.html) 可下载后离线打开；图表使用现有配色与系统字体。

## 快速开始

1. 将本仓库保留在固定本地位置，在业务项目创建链接。命令中的路径替换为实际绝对路径，不改全局 Skills：

   ```bash
   python3 /绝对路径/spec-to-ship/scripts/link-project-skills.py /绝对路径/业务项目 --check
   python3 /绝对路径/spec-to-ship/scripts/link-project-skills.py /绝对路径/业务项目
   ```

2. 在业务项目下一轮会话检查可用 Skills 与路径。存在全局同名版本时，使用明确路径：`请使用 /绝对路径/业务项目/.agents/skills/setup-matt-pocock-skills/SKILL.md 配置本地 Markdown tracker。` 初次接入按 [项目接入](docs/project-setup.md) 核对 tracker、产物路径和知识职责，保留已有 AGENTS／CLAUDE 内容。
3. 根据任务选择入口；下表用于查找能力，不是必须逐行执行的清单：

   | 目的 | 用户入口 | 产物／结果 |
   | --- | --- | --- |
   | 澄清目标与决定 | `$grill-with-docs` | 已澄清讨论，按需更新词汇／重要决定 |
   | 整理统一规格 | `$to-spec` | `.scratch/<feature>/spec.md`，含产品、实现、测试决定 |
   | 拆分交付结果 | `$to-tickets` | `.scratch/<feature>/issues/<NN>-<slug>.md` |
   | 实施与测试循环 | `$implement`；缺陷按需 `$diagnosing-bugs` | 代码、测试结果；原生调用 tdd 与 code-review |
   | 最终回归与审查 | 执行项目约定回归，再 `$code-review` 并给出基线和 spec 路径 | 对应当前版本的检查结果和审查意见 |
   | 产品验收 | `$sts-acceptance` | 引用 spec 标准及当前证据的验收记录 |
   | 收尾知识同步 | `$sts-closeout` | 交付入口、遗留事项、当前模块知识更新 |

短名仅在会话已确认对应本项目路径时使用；否则将入口写成上面的绝对 `SKILL.md` 路径，依赖也选同目录固定版本。无需每个目的换会话；不要让导航器强制逐一调用所有 Skills。简单工作不强制拆多张 tickets。换会话时才用 `$handoff`。

原生 `implement` 包含提交动作；先沿用或明确该任务的提交授权。原生 `code-review` 用 `base...HEAD` 审查已提交差异：最终验收前，审查必须覆盖交付 HEAD，未提交变更不能假称已覆盖。细节见 [流程中的版本与权限](workflow.md#版本证据与权限)。

## 范围与目录

- [skills/](skills/)：12 个原生目录及 `sts-acceptance`、`sts-closeout`；补充模板各自在 Skill 内自包含。
- [docs/project-setup.md](docs/project-setup.md)：业务项目接入、最小配置、同名冲突与知识分工。
- [workflow.md](workflow.md)：当前单一路线、反馈和证据约定。
- [SOURCES.md](SOURCES.md)、[upstream-manifest.json](upstream-manifest.json)、[licenses/](licenses/)：来源和许可。
- [AGENTS.md](AGENTS.md)：只规定本仓库维护要求。

业务项目保留真实任务、代码证据和模块知识。本仓库不提供第二套 PRD／技术方案／任务模板，不强制 R／AC 编号，不建设流程 CLI、看板、状态机、复杂知识库或 OpenSpec。原生 Skills 是否成功发现及真实业务执行结果需在目标宿主验证。
