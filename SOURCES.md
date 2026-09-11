# 来源、版本与复用边界

核对日期：2026-09-11。当前实现采用固定版本原生 Matt Skills，通过 Codex 插件整包分发，辅以项目接入、按任务选择入口、产品验收及知识同步。没有第二套 PRD／技术方案／tickets 流程；旧 `templates/` 已删除，历史记录仅保留在 Git 历史。

## Matt Skills：原生导入

- 来源：[mattpocock/skills](https://github.com/mattpocock/skills)，固定 commit `3cca18b368ae95cdbdebbff572ccafa662551015`（2026-09-04T09:43:27+01:00）。本次固定此版本，不宣称它是未来最新版本。
- 此前使用系统 skill-installer 的 `install-skill-from-github.py --repo mattpocock/skills --ref 3cca18b368ae95cdbdebbff572ccafa662551015 --dest /绝对路径/spec-to-ship/skills --path ...` 导入下表完整目录；现整体迁移到 `plugins/spec-to-ship/skills/`，保留正文、agents 元数据、references、模板与脚本，方法正文不变；调用字段适配见下文。
- [完整 MIT 许可证](plugins/spec-to-ship/licenses/mattpocock-skills.LICENSE)：Copyright (c) 2026 Matt Pocock，适用于导入内容。所有原生来源路径、本地路径、逐文件 SHA-256、选入原因和依赖见 [upstream-manifest.json](upstream-manifest.json)。复制这些原生目录时应同时保留该许可，不将其视为本仓库全部自有内容的许可证。
- [verify-upstream.py](scripts/verify-upstream.py) 校验 36 个原生文件及许可证的 hash、文件集合、依赖和资源链接。加 `--source /上游Git目录` 可直接用固定 commit 的 `git show` 字节对比，而非只信任本地 manifest。

| 原生 Skill | 固定提交内来源目录 | 选入原因／传递依赖 |
| --- | --- | --- |
| setup-matt-pocock-skills | skills/engineering/setup-matt-pocock-skills | 原生项目配置；完整保留 tracker 和 domain seed |
| grill-with-docs | skills/engineering/grill-with-docs | 澄清入口，调用 grilling、domain-modeling |
| grilling | skills/productivity/grilling | 澄清依赖；需要宿主子 Agent 能力 |
| domain-modeling | skills/engineering/domain-modeling | 词汇与按需 ADR；保留 CONTEXT／ADR 格式参考 |
| to-spec | skills/engineering/to-spec | 产品、实现和测试决定写入同一 spec；依赖 setup 配置 |
| to-tickets | skills/engineering/to-tickets | 可验证交付及阻塞关系；依赖 setup 配置 |
| implement | skills/engineering/implement | 原生调用 tdd、code-review；保留末尾提交动作，受任务授权约束 |
| tdd | skills/engineering/tdd | 行为测试循环；条件引用 codebase-design |
| codebase-design | skills/engineering/codebase-design | 模块接口与测试位置；保留两份设计参考 |
| code-review | skills/engineering/code-review | 双轴子 Agent 审查；依赖 setup 配置，只覆盖 base...HEAD |
| diagnosing-bugs | skills/engineering/diagnosing-bugs | 缺陷诊断补充；完整保留 scripts/hitl-loop.template.sh |
| handoff | skills/productivity/handoff | 按需会话交接，原生默认写系统临时目录 |

`triage` 是 setup 对宿主已有能力的条件检查，`wayfinder` 是 tracker seed 的可选章节，`improve-codebase-architecture` 是 domain seed 对其他调用方的描述，均不是这条执行链必须调用的依赖，因此不导入。完整原生 seed 保留这些提及，不把它们描述成已安装能力。Skill 内真实 Markdown 资源引用已核对，围栏中的业务路径示例不属于包资源。

## 原生行为与项目配置

六个入口的显式限定已按本次授权适配为自动选择，其他元数据和方法正文保留；安装后需在宿主确认发现与路径，不能把文件存在当调用成功。本仓库不增加全局强制编排器。全局同名版本不覆盖，明确路径调用见 [项目接入](docs/project-setup.md)。

接入初始化复用原生 setup，插件安装只准备能力、不代写项目规范。业务项目的 tracker／domain 配置可以按其 AGENTS 和已有文档布局调整；这是原生允许的项目配置，不是对原生 Skill 做补丁。需要新建 spec 时产品与技术决定合并，tickets 使用原生结构；已有足够的 PRD／技术文档不重复转写，继续引用实际权威依据。原生提交、发布、确认步骤都受用户当前有效授权约束。

原生 implement 的 review 在 commit 之前，code-review 又只读取已提交差异。自定义入口先核对范围，未提交内容采用明确标注的工作区人工审读；最终核对证据是否覆盖交付内容，内容及依据一致可复用，有变化则补审。不改原生正文，也不将人工审读冒称原生调用。详见 [流程](workflow.md#版本证据与权限)。

## 本仓库新增

当前包含 12 个原生 Skill 与 3 个自定义 Skill，共 15 个。manifest 保留上游原始 hash，并逐文件记录调用适配及分发 hash；自定义内容由 Git 跟踪。

- `plugins/spec-to-ship/skills/sts-workflow`：根据目标、已有材料、证据和授权选择最小足够入口，衔接原生或补充能力；实际执行所选同包方法，不要求逐阶段调用，也不强制运行完整链。

- `plugins/spec-to-ship/skills/sts-acceptance`：按已确认 spec 或等价材料标准与当前证据验收，记录用户最终结论；按需使用其自包含模板。
- `plugins/spec-to-ship/skills/sts-closeout`：整理实际交付与遗留，将确认知识同步到唯一权威模块文档；按需使用其自包含模板。
- README、workflow、AGENTS、接入说明、场景指南及插件元数据与校验脚本为本仓库自有内容。未强制 R／AC 编号，未重建原生规格或任务模板；小任务不强制验收和收尾文件。

自定义 Skills 使用系统 skill-creator 指导编写，并运行其 quick_validate。原生导入使用系统 skill-installer helper；这些开发辅助工具未复制进项目，也不是业务研发链的运行依赖。本轮使用临时 Python venv 中的 PyYAML 运行系统校验 helper，不改变项目依赖；此前图表验证使用 Python、Playwright、Chrome。

## Codex 插件打包

使用本地系统 plugin-creator 的 `create_basic_plugin.py` 创建 [插件清单](plugins/spec-to-ship/.codex-plugin/plugin.json) 与 [repo marketplace](.agents/plugins/marketplace.json)，沿用 helper 默认的 `personal` 名称。包根是 `plugins/spec-to-ship`，包含唯一一份 15 个 Skills 和 Matt MIT 许可；`upstream-manifest.json` 保留来源路径、固定 commit 与原始 SHA-256；调用适配另外记录，不覆盖原始 hash。

3 个 sts 的依赖解析适配为同一插件的相对资源与实际安装路径；业务规则、配置和产物继续留在业务项目。旧 `link-project-skills.py` 和对应安装测试移除，改为插件包校验测试，不保留第二套安装方式。不为插件添加 MCP、apps 或自动业务配置。

本次完整 helper 校验要求无错误通过，不再豁免旧版的六项显式标记拒绝。静态校验、隔离试用与目标宿主发现分别报告，见 [调用适配验证](docs/invocation-validation.md)。此前旧版曾在 Codex 发现 15 个入口，不能将该历史结果用作本次适配的运行证据。

### 调用适配与升级

为支持“一次进入、按需推进”，六个入口 `grill-with-docs`、`to-spec`、`to-tickets`、`implement`、`setup-matt-pocock-skills`、`handoff` 仅做两项适配：`disable-model-invocation: true → false`、`allow_implicit_invocation: false → true`。后两者仍只在任务确需且已授权时由入口选择，安装本身不初始化业务项目或生成交接。调用开放不改变方法正文中的实质确认、提交及依赖步骤。sts-workflow 另按宿主支持方式解释 Skill 加载动作：有工具用工具，Codex 文件加载型宿主读取同包指令并执行及递归处理依赖。此映射不改上游正文，不允许只读不执行或伪造工具调用。

清单每个适配文件的 `sha256` 始终是固定上游 hash，`invocation_adapter` 记录精确原值、新值和适配文件 hash。校验器只接受上述两个字段，先检查分发文件，再还原并验证上游 hash；使用 `--source` 时还会比较还原后的固定 Git 原文。测试覆盖正文被改后重算适配 hash、非法适配及资源缺失，不能以更新适配记录掩盖正文漂移。

升级时重新导入完整固定版本并核对许可证、依赖和原始 hash，再审查这六个入口是否仍需适配；重新计算分发 hash，执行完整包校验与宿主发现验证。禁止自动向已变化的上游字段套用旧补丁，禁止手改插件缓存。此包应称为“固定 Matt 方法与调用适配”，不能宣称所有分发字节完全原生。

## agentic-delivery：仅历史研究参考

来源：[RR9-cn/agentic-delivery](https://github.com/RR9-cn/agentic-delivery)，曾核对 commit `9573a3758e19c82925a580010d4d9d54a023a70a`。当时跟踪文件未发现 LICENSE／LICENCE／COPYING／NOTICE，[README](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/README.md#status) 将最终许可证列为待定。

曾阅读 README、`plugins/agentic-delivery/skills/delivery-workflow/references/artifact-contract.md`、delivery-test／delivery-archive 的 SKILL.md、templates/test-plan.md 与 review.md，用于理解阶段证据和当前知识。未复制其代码、模板、schema 或 Skill 正文，当前不是运行依赖；入口、验收与知识补充依据用户需求独立编写。

## diagram-design：图表制作与模板复用

- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)，本地插件 manifest **2.6.17**，commit `2724fd2efd8c6737f6fa704fbf5da52d67375497`；Skill metadata 标为 2.6。
- 本地 LICENSE 为 MIT，Copyright (c) 2025 Cathryn Lavery。完整版权和许可保留在 [HTML](docs/diagrams/workflow-overview.html) 与 [SVG](docs/diagrams/workflow-overview.svg) 顶部注释。
- HTML／CSS 源自 `skills/diagram-design/assets/template.html`，其 SHA-256 为 `78097811877b253fdf755867fd66efdb30ac93498f058c9b2c852a0fe333272a`；修改内容、布局与系统字体，SVG 从 HTML 导出。图表达按当前目标选择入口的使用方式，无外部字体或图标文件依赖。
- 采用 SKILL、flowchart、semantic-patterns、style-guide、output-spec、export 指导并执行 self_check；绘图 Skill 不作为业务研发 Skills 导入。

- 新增 [完整功能协作图](docs/diagrams/feature-collaboration.html)（swimlane）与 [产物与知识关系图](docs/diagrams/artifacts-and-knowledge.html)（architecture 关系布局）：依据本仓库已有约定独立编写图中文字与连线，沿用同一模板、配色和离线字体。HTML 与导出的 SVG 均保留上述 MIT 许可；同时参考相应图类型说明，不引入新的流程规则或运行能力。

本仓库自有内容的整体许可证仍待所有者选择。工具链安装及静态验证不等于真实业务测试、用户验收或 Farvis 接入完成。
