# spec-to-ship

面向个人与小团队的 AI 辅助研发流程，以可组合的 Skills 和阶段产物连接需求、实现与验收。

当前交付是**流程文档与模板初稿，待审阅**。以 Matt Skills 的可组合能力为后续适配基础，参考 agentic-delivery 的阶段产物与证据思路；Matt 与 agentic-delivery 的研发 Skills 尚未安装、适配或执行；README 流程图使用已安装的 diagram-design 绘图 Skill 制作。来源、固定版本、许可证和差异见 [SOURCES.md](SOURCES.md)。

## 适用范围

适用于需要把需求、技术实现和验收依据串起来的功能开发与小型修改。完整功能默认保留各阶段必要产物；小型修改允许合并文件，但需求、方案、验证、验收仍有独立段落与引用。PRD 定义产品行为，技术方案定义实现方式，不互相复制。

本仓库保存通用流程、模板及未来经过审阅的 Skills；业务规则、模块知识和实际任务产物留在业务项目。当前未提供 CLI、看板、自动状态机、程序化门禁或复杂知识库，不引入 OpenSpec。Farvis 真实功能试跑属于后续工作，本次未修改 Farvis。

## 流程总览

![七阶段研发流程、核心产物与反馈路径](docs/diagrams/workflow-overview.svg)

图中的顺序表示满足完成条件后的正常交接；失败、阻塞或未运行不能作为阶段通过的依据。具体输入、完成条件与反馈规则以 [workflow.md](workflow.md) 为准。[可编辑 HTML 源文件](docs/diagrams/workflow-overview.html) 可下载后用浏览器打开；GitHub 页面展示的是源码。HTML 与 SVG 均使用系统字体，无外部字体请求，可离线查看。

## 目录

- [AGENTS.md](AGENTS.md)：仅约束本仓库维护。
- [workflow.md](workflow.md)：阶段、交接、反馈、状态与知识同步的权威约定。
- [SOURCES.md](SOURCES.md)：来源核对与后续复用建议。
- [templates/README.md](templates/README.md)：模板选用、占位符和产物存放约定。
- `templates/`：PRD、技术方案、任务、测试、产品验收、收尾、模块知识、可选会话交接模板。

没有创建 `skills/` 空目录；后续确认适配范围后再加入实际能力。

## 快速开始

当前可直接使用的是文档模板，无需安装 Skills 或运行工具。

1. 阅读 [流程约定](workflow.md) 和 [模板索引](templates/README.md)，检查业务项目已有 AGENTS.md 与模块文档，沿用其权威位置。
2. 在业务项目建立任务目录，例如 `docs/changes/<功能名>/`。完整功能复制 `prd.md`、`technical-design.md`、`test.md`、`acceptance.md`、`closeout.md`；将 `task.md` 按任务复制为 `tasks/T-001.md` 等。小型修改可按流程合并文件，但保留需求、方案、验证、验收及收尾信息。
3. 替换 `{{说明}}` 占位符并修正链接。先在 PRD 中确定 R 需求与 AC 验收标准，再写技术方案、拆 T 任务；低风险假设记录下来，关键决定按已有授权确认。
4. 开发记录写回任务单；测试按 TC 记录版本、环境、实际结果与证据，产品验收逐项对照 AC。收尾时更新已有模块知识，或明确写“无需更新”；模块模板与会话交接模板仅按需使用。

同一个人、会话或 Agent 可以承担多个阶段。文档分离不要求更换会话，也不要求逐阶段重复确认。流程由人和 Agent 遵循，当前没有自动检查状态或阻止交接的程序。

审阅本初稿时重点确认文档体量是否合适；本仓库自身许可证、首批 Skills 适配范围以及 Farvis 试跑功能仍待决定，不影响本次初稿审阅。
