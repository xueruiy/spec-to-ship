# 来源、版本与复用边界

核对日期：2026-09-09。当前实现采用固定版本原生 Matt Skills，辅以项目链接、产品验收及知识同步。没有第二套 PRD／技术方案／tickets 流程；旧 `templates/` 已删除，历史记录仅保留在 Git 历史。

## Matt Skills：原生导入

- 来源：[mattpocock/skills](https://github.com/mattpocock/skills)，固定 commit `3cca18b368ae95cdbdebbff572ccafa662551015`（2026-09-04T09:43:27+01:00）。本次固定此版本，不宣称它是未来最新版本。
- 使用系统 skill-installer 的 `install-skill-from-github.py --repo mattpocock/skills --ref 3cca18b368ae95cdbdebbff572ccafa662551015 --dest /绝对路径/spec-to-ship/skills --path ...` 导入下表完整目录，保留正文、agents 元数据、references、模板与脚本，不改写原生文件。
- [完整 MIT 许可证](licenses/mattpocock-skills.LICENSE)：Copyright (c) 2026 Matt Pocock，适用于导入内容。所有原生来源路径、本地路径、逐文件 SHA-256、选入原因和依赖见 [upstream-manifest.json](upstream-manifest.json)。复制这些原生目录时应同时保留该许可，不将其视为本仓库全部自有内容的许可证。
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

原生的显式触发标记和 `agents/openai.yaml` 原样保留；安装后需在宿主确认发现与路径，不能把文件存在当调用成功。本仓库不增加全局强制编排器。全局同名版本不覆盖，明确路径调用见 [项目接入](docs/project-setup.md)。

接入初始化复用原生 setup，安装脚本只链接、不代写项目规范。业务项目的 tracker／domain 配置可以按其 AGENTS 和已有文档布局调整；这是原生允许的项目配置，不是对原生 Skill 做补丁。spec 产品与技术决定合并，tickets 使用原生结构；原生提交、发布、确认步骤都受用户当前有效授权约束。

原生 implement 的 review 在 commit 之前，code-review 又只读取已提交差异。这一版本的覆盖限制通过最终交付 HEAD 再审查来显式处理，未提交范围保留未覆盖状态，不改原生正文。详见 [流程](workflow.md#版本证据与权限)。

## 本仓库新增

- `skills/sts-acceptance`：按已确认 spec 标准与当前证据验收，记录用户最终结论；按需使用其自包含模板。
- `skills/sts-closeout`：整理实际交付与遗留，将确认知识同步到唯一权威模块文档；按需使用其自包含模板。
- README、workflow、AGENTS、接入说明及透明项目链接／校验脚本为本仓库自有内容。未强制 R／AC 编号，未重建原生规格或任务模板。

自定义 Skills 使用系统 skill-creator 指导编写，并运行其 quick_validate。原生导入使用系统 skill-installer helper；这两项开发辅助工具未复制进项目，也不是业务研发链的运行依赖。使用已有 Python、Playwright、Chrome 进行验证，没有安装第三方依赖。

## agentic-delivery：仅历史研究参考

来源：[RR9-cn/agentic-delivery](https://github.com/RR9-cn/agentic-delivery)，曾核对 commit `9573a3758e19c82925a580010d4d9d54a023a70a`。当时跟踪文件未发现 LICENSE／LICENCE／COPYING／NOTICE，[README](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/README.md#status) 将最终许可证列为待定。

曾阅读 README、`plugins/agentic-delivery/skills/delivery-workflow/references/artifact-contract.md`、delivery-test／delivery-archive 的 SKILL.md、templates/test-plan.md 与 review.md，用于理解阶段证据和当前知识。未复制其代码、模板、schema 或 Skill 正文，当前不是运行依赖；验收与知识补充依据用户需求独立编写。

## diagram-design：图表制作与模板复用

- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)，本地插件 manifest **2.6.17**，commit `2724fd2efd8c6737f6fa704fbf5da52d67375497`；Skill metadata 标为 2.6。
- 本地 LICENSE 为 MIT，Copyright (c) 2025 Cathryn Lavery。完整版权和许可保留在 [HTML](docs/diagrams/workflow-overview.html) 与 [SVG](docs/diagrams/workflow-overview.svg) 顶部注释。
- HTML／CSS 源自 `skills/diagram-design/assets/template.html`，其 SHA-256 为 `78097811877b253fdf755867fd66efdb30ac93498f058c9b2c852a0fe333272a`；修改内容、布局与系统字体，SVG 从 HTML 导出。图表达当前原生路线，无外部字体或图标文件依赖。
- 采用 SKILL、flowchart、semantic-patterns、style-guide、output-spec、export 指导并执行 self_check；绘图 Skill 不作为业务研发 Skills 导入。

本仓库自有内容的整体许可证仍待所有者选择。工具链安装及静态验证不等于真实业务测试、用户验收或 Farvis 接入完成。
