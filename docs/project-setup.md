# 业务项目接入

本仓库统一维护原生 Skill 副本；安装链接与项目初始化是两件事。链接脚本仅准备项目技能入口，不初始化配置；用户随后显式调用原生 setup 探索与配置，真实产物留在业务项目。入口是用户选择的 Skill，不是全局控制器。安装需要 Python 3.10+，无第三方依赖。当前共 15 个 Skills：12 个原生和 3 个 sts 补充入口。

## 链接与版本选择

在业务项目已存在、没有其他同名项目 Skill 的前提下执行 README 的链接命令。[link-project-skills.py](../scripts/link-project-skills.py) 将本仓库每个 Skill 目录链接到目标项目 `.agents/skills/<name>`；`--check` 不写入。所有冲突在写入前检查，已指向同一源的链接可重复运行，不覆盖其他文件或软链接，也不跟随重定向的 `.agents` 目录。

本地源目录必须持续存在。链接依赖本机绝对路径，不应作为可移植安装包提交到其他机器；每位成员检出相同仓库版本后在自己的项目运行命令。若要忽略本地链接，可按项目已有 Git 约定管理，脚本不会改 `.gitignore` 或 Git 配置。移动源仓库后先人工核对旧链接再重建，不用强制覆盖。

脚本会只读提示 `~/.codex/skills` 与 `~/.agents/skills` 中的同名入口，但这不是宿主全部插件源的完整清单。全局同名 Skill 可能仍被发现；**不假定项目版本必然覆盖全局版本**。下一轮会话核对可用 Skill 的实际路径。若短名歧义，显式给出：

```text
请使用 /绝对路径/业务项目/.agents/skills/grill-with-docs/SKILL.md 澄清本功能。
其 grilling、domain-modeling 及后续所有 Matt 依赖均从这个项目的 .agents/skills 目录读取，
不要选择同名全局旧版本；实际执行仍遵从本项目 AGENTS 和本次授权。
```

这是明确路径调用，不声称宿主已注册成功。宿主无法发现或读取路径、不能执行原生依赖调用／子 Agent 时报告具体限制，不把工具链存在当执行成功。重新运行链接脚本会为已有 14 个入口的项目增加 sts-workflow；已有链接保留，下一轮会话仍需核对发现与路径。不自动改原生文件绕过该限制。

## 首次配置

用户调用项目路径下的 setup-matt-pocock-skills，明确选择 **Local Markdown**。原生 Skill 探索项目后展示配置，按其确认步骤及本次已有授权写入；原生默认优先编辑已有 CLAUDE.md，否则 AGENTS.md。若项目规定 CLAUDE.md 只是指向 AGENTS.md 的引用入口，先遵守该项目规则与已有授权，在唯一权威入口维护配置，保留引用，不把新规则复制到两个文件；不为这一项目差异改写原生 Skill。

下面是原生 setup 应生成或更新的最小配置说明，不要求用户安装前手写，也不另提供第二套初始化模板：

- `docs/agents/issue-tracker.md`：从原生 [本地 tracker 模板](../skills/setup-matt-pocock-skills/issue-tracker-local.md) 起步，说明 spec 为 `.scratch/<feature>/spec.md`，tickets 为 `issues/<NN>-<slug>.md`，publish 表示写本地文件。
- `docs/agents/domain.md`：从原生 [领域配置](../skills/setup-matt-pocock-skills/domain.md) 起步，指向当前已有知识位置，文件不存在时不为凑目录提前生成 CONTEXT／ADR。
- 现有 Agent skills 配置块：链接上述配置，并明确项目固定版本目录与业务规则入口，不覆盖其他规则。

这些是业务项目配置，可以按项目调整；`skills/` 中的原生 seed 文件仍保持不变。本批不包含 triage；当宿主也未发现额外的 triage 时，原生 setup 跳过 triage-labels 文件；若宿主另有 triage，则按 setup 的条件分支确认并生成标签配置。原生 to-spec／to-tickets 仍用 `ready-for-agent`，在 tracker 配置中明确此词表示“可实施”，不表示批准或验收；若项目需要其他状态也在这里集中定义，不要求新建标签管理机制。本地 tracker seed 的 wayfinder 段只是其他流程的可选约定，本批没有安装或调用 wayfinder。

Agent skills 配置块应说明：读取 tracker、domain；CONTEXT 与相关 ADR 按原生约定使用，同时读取项目当前模块知识；同名依赖绑定项目目录。用户已经确认的配置可直接作为 setup 的输入，缺失的重要项目事实先探索，不问泛化方案选择。

## 初始化后如何开始

日常可调用 `sts-workflow` 描述目标、已有材料和本轮范围，也可直接选择原生能力。统一入口在原生调用条件与宿主能力允许时衔接；需要显式触发时给出下一条具体调用，不自动跑完整链。

```text
$sts-workflow 阅读已有 docs/requirements.md 与 docs/design.md，核对当前进度，继续已授权的部分。
```

两个文件已足够表达本次需求时，继续引用它们，无需重写 spec；实现不强制先拆票。仅测试、仅审查、诊断、恢复和暂停的开场见 [场景指南](usage-guide.md)。

原生 implement 自带 tdd／code-review；最终审查仍须满足 [版本覆盖要求](../workflow.md#版本证据与权限)。如果本次只要工作区审查，可以进行清楚标注范围的人工审读，不能声称原生 `base...HEAD` 已覆盖它，也不能为审查自行提交。

## 知识职责

| 位置 | 职责 |
| --- | --- |
| AGENTS／CLAUDE | 执行要求、权限与配置导航，遵从现有适用范围 |
| CONTEXT／CONTEXT-MAP | 领域术语、上下文入口，不保存实现细节或任务流水 |
| 现有模块文档 | 当前有效业务行为、约束、接口与实现入口；唯一权威知识 |
| 现有 ADR | 重要取舍的追溯，按需新增，不每任务生成 |
| 代码／知识图谱 | 检索和导航；重新核实代码，不把推断直接升格为规则 |
| .scratch 功能目录 | spec、tickets、证据、验收和收尾，历史追溯 |

项目级链接实测只能证明路径和文件可用；完整 Skill 调用、测试环境、用户验收及知识写回须在真实业务任务里验证。
