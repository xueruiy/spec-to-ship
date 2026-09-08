# 来源、许可证与复用记录

核对日期：2026-09-08。状态：研究已完成，流程及模板为待审阅初稿，Skills 适配尚未实施。

通过 GitHub 页面与临时目录内只读浅克隆核对默认分支 HEAD、跟踪文件和正文；没有运行上游脚本、安装依赖或加载其 Skills 执行流程。以下版本是本次取得的快照，不保证未来 HEAD 不变。

## 上游快照与许可证

| 上游 | 默认分支与固定 commit | 提交时间 | 许可证核对 | 本次处理 |
| --- | --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | main · `3cca18b368ae95cdbdebbff572ccafa662551015` | 2026-09-04T09:43:27+01:00 | 根目录 [LICENSE](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/LICENSE)：MIT，Copyright (c) 2026 Matt Pocock | 阅读与概念参考；没有复制或修改上游 Skill 文件 |
| [RR9-cn/agentic-delivery](https://github.com/RR9-cn/agentic-delivery) | main · `9573a3758e19c82925a580010d4d9d54a023a70a` | 2026-09-03T22:48:58+08:00 | 当前跟踪文件中未发现 LICENSE／LICENCE／COPYING／NOTICE；[README 的 Status](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/README.md#status) 将最终许可证列为待定 | 复用权限未明确；不复制其代码、模板、schema 或 Skill 正文，按本次用户需求独立写作 |

Matt 的 MIT 文本要求复制其软件或实质内容时保留版权和许可声明。后续若引入上游内容，应随文件保留完整声明、固定来源版本与改动说明；本次没有导入上游文件。agentic-delivery 的设计文档提及未来 LICENSE 文件不代表当前已有授权，后续复用前应重新核查或取得明确授权。

本仓库尚未选择自身许可证，本次不擅自添加 LICENSE，也不把上游 MIT 声明当成本仓库整体许可。

## 实际阅读的参考文件与差异

以下是研究映射，不表示这些 Skills 已可在本仓库运行。链接固定到上表 commit。

| 来源文件 | 核对内容与本仓库处理 |
| --- | --- |
| [Matt · README.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/README.md) | Matt 的可组合 Skills 定位；作为后续能力组合基础。 |
| [Matt · skills/productivity/grilling/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling/SKILL.md) | 澄清方式参考；本仓库只要求关键决定确认，低风险细节可记录假设，不照搬穷尽询问及委派指令。 |
| [Matt · skills/engineering/grill-with-docs/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/grill-with-docs/SKILL.md) | 实际转调 grilling 与 domain-modeling；本次仅阅读，没有调用。 |
| [Matt · skills/engineering/domain-modeling/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md) | 术语和重要决定参考；模块知识沿用业务项目权威文档，不强制新建词汇表或每任务 ADR。 |
| [Matt · skills/engineering/to-spec/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-spec/SKILL.md) | 其 spec 同含产品与实现决定且会发布工单；本仓库分离 PRD 与技术方案，技术事实保留核查版本和入口，不沿用发布动作。 |
| [Matt · skills/engineering/to-tickets/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-tickets/SKILL.md) | 独立验证与依赖拆分的概念适配；任务单增加实施证据，初始草稿，索引仅导航。 |
| [Matt · skills/engineering/implement/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/implement/SKILL.md) | 含测试、评审及提交动作；未来适配需对齐用户授权、项目检查范围及任务记录，当前未执行。 |
| [Matt · skills/engineering/tdd/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/tdd/SKILL.md) | 行为验证思路参考；单元测试不能替代产品所需的真实验收证据。 |
| [Matt · skills/productivity/handoff/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/handoff/SKILL.md) | 引用产物与去敏思路参考；存放位置由业务项目约定，不固定系统临时目录。 |
| [agentic-delivery · README.md](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/README.md) | 核对现有 CLI／lifecycle／插件定位；本仓库不引入其运行系统。 |
| [agentic-delivery · plugins/agentic-delivery/skills/delivery-workflow/references/artifact-contract.md](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/plugins/agentic-delivery/skills/delivery-workflow/references/artifact-contract.md) | 研究阶段产物及证据关系；本仓库仅形成手工交接约定，无 hash 门禁或状态机。 |
| [agentic-delivery · plugins/agentic-delivery/skills/delivery-test/SKILL.md](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/plugins/agentic-delivery/skills/delivery-test/SKILL.md) | 研究证据限制与重测方向；没有采用其命令、门禁及额外逐步授权规则。 |
| [agentic-delivery · plugins/agentic-delivery/templates/test-plan.md](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/plugins/agentic-delivery/templates/test-plan.md) | 仅研究，不复制模板；测试字段依据用户明确需求独立编写。 |
| [agentic-delivery · plugins/agentic-delivery/templates/review.md](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/plugins/agentic-delivery/templates/review.md) | 仅研究，不引入额外必需评审报告；相关发现可记任务或测试文档。 |
| [agentic-delivery · plugins/agentic-delivery/skills/delivery-archive/SKILL.md](https://github.com/RR9-cn/agentic-delivery/blob/9573a3758e19c82925a580010d4d9d54a023a70a/plugins/agentic-delivery/skills/delivery-archive/SKILL.md) | 研究当前知识与历史证据的区别；本仓库使用权威模块文档同步，不引入 Ontology／Design Library 或多重发布机制。 |

## 本次产物归属

| 分类 | 本次内容 |
| --- | --- |
| 上游原样复用 | 无。未导入 Skill、代码、模板或 schema |
| 概念适配，中文独立表述 | Matt 的澄清、任务拆分、行为验证、轻量交接思路；agentic-delivery 仅作阶段证据与收尾知识的研究对照，未复制表达或结构 |
| 按用户需求新增 | 七阶段流程；独立 PRD／方案；R／AC／T／TC 引用；产品验收；任务兼实施记录；小修改合并规则；版本与未提交改动证据；当前模块知识同步；八类模板及维护、使用说明 |

具体归属：[README.md](README.md)、[AGENTS.md](AGENTS.md)、本文件均为仓库专用新文档；[workflow.md](workflow.md) 及 [templates/](templates/README.md) 为按本次需求独立编写的初稿。所谓概念适配不代表已经完成可执行 Skill 适配。

## 后续 Skills 适配建议（未实施）

1. 先选少量 Matt 能力：澄清、spec 综合、任务拆分、实施／行为测试、会话交接；核对其传递调用、许可证和当前版本，不整套安装产生重名或冲突。
2. 优先解决边界差异：to-spec 输出拆为 PRD 与方案；to-tickets 对接业务项目任务位置及草稿状态；implement 对齐项目检查、提交授权和实施记录；handoff 对接既有路径。
3. 测试执行记录、逐 AC 产品验收、知识同步先用本仓库模板人工试跑；真实功能暴露重复操作后，再决定是否补成薄层 Skill。避免另建一套与 Matt 重叠的设计、开发、测试技能。
4. 不直接复用 agentic-delivery 内容；若后续希望引入，先解决许可问题。继续保持模板约定与运行能力分开描述。

仍需决定：本仓库自身许可证；首批适配范围与部署位置；Farvis 的具体试跑功能及产物位置。这些属于后续选择，本次未修改 Farvis，也未推送或发布。
