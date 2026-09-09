# spec-to-ship

面向个人与小团队的 AI 辅助研发接入仓库：**原生 Matt Skills 负责澄清、spec、tickets、实施、测试和审查；本仓库补充项目接入、产品验收与知识同步。**

已收录固定版本的 12 个 Matt Skills 和 2 个自定义 Skills，原生文件不改写。工具链文件与项目链接方式已做本地检查，尚不能据此宣称真实业务交付已验证。来源、许可证和逐文件校验见 [SOURCES.md](SOURCES.md) 与 [upstream-manifest.json](upstream-manifest.json)。

## 流程总览

![原生 Matt Skills 到产品验收与知识同步](docs/diagrams/workflow-overview.svg)

图中为用户按需显式调用的顺序与反馈，不是自动编排或程序化门禁。详细约定见 [workflow.md](workflow.md)。[可编辑 HTML 源图](docs/diagrams/workflow-overview.html) 可下载后离线打开；GitHub 展示的是源码。图表沿用 diagram-design 默认配色和系统字体。

## 快速开始

1. 将本仓库保留在固定本地位置，在业务项目创建链接。命令中的路径替换为实际绝对路径，不改全局 Skills：

   ```bash
   python3 /绝对路径/spec-to-ship/scripts/link-project-skills.py /绝对路径/业务项目 --check
   python3 /绝对路径/spec-to-ship/scripts/link-project-skills.py /绝对路径/业务项目
   ```

2. 在业务项目下一轮会话检查可用 Skills 与路径。存在全局同名版本时，使用明确路径：`请使用 /绝对路径/业务项目/.agents/skills/setup-matt-pocock-skills/SKILL.md 配置本地 Markdown tracker。` 初次接入按 [项目接入](docs/project-setup.md) 核对 tracker、产物路径和知识职责，保留已有 AGENTS／CLAUDE 内容。
3. 开始真实功能时依次按需调用：

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
