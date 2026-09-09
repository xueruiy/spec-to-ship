# spec-to-ship

面向个人与小团队的 AI 辅助研发工具包。**原生 Matt Skills 负责澄清、规格、任务、实施与验证；spec-to-ship 补充入口选择、产品验收和知识同步。**

包含固定版本的 **12 个 Matt Skills + 3 个自定义 Skills，共 15 个**。原生文件不改写，不要求每个任务走完整流程，也不要求把已有 PRD／技术文档重写成 spec。来源和逐文件校验见 [SOURCES.md](SOURCES.md) 与 [manifest](upstream-manifest.json)。

## 1. 安装到业务项目

保留本仓库的固定本地位置，用 Python 3.10+ 建立项目级链接：

```bash
python3 /绝对路径/spec-to-ship/scripts/link-project-skills.py /绝对路径/业务项目 --check
python3 /绝对路径/spec-to-ship/scripts/link-project-skills.py /绝对路径/业务项目
```

脚本只链接 `.agents/skills/`，不安装全局、不修改业务规范。已安装旧版的项目重新运行即可增加 `sts-workflow`，已有冲突不会覆盖。进入下一轮会话后核对 15 个入口及实际路径；文件存在不等于宿主发现成功。同名全局版本和配置细节见 [项目接入](docs/project-setup.md)。

## 2. 首次初始化

在业务项目明确调用原生 setup：

```text
请使用 /绝对路径/业务项目/.agents/skills/setup-matt-pocock-skills/SKILL.md，
检查已有 AGENTS、CLAUDE 和文档约定，配置 Local Markdown tracker 与知识读取入口。
保留已有权威规范，不复制第二套规则。
```

初始化与安装分开，已有配置不必每个任务重跑。原生 setup 根据项目现状展示并确认配置，无需先手写模板。

文件放在哪里、哪些需要人审阅或提交 Git，见 [接入后的目录与维护方式](docs/project-setup.md#接入后的目录与维护方式)。目录按需生成，模块知识更新项目已有文档。

## 3. 开始一个任务

不确定入口时，用 `sts-workflow` 说明目标、已有材料和本次范围：

```text
$sts-workflow 我想改善客户资料的重复录入，现有说明在 docs/customer.md。
请先判断还缺哪些产品决定，这轮只澄清，不改代码。
```

已有清楚任务可以直接继续：

```text
$sts-workflow 按 docs/import-prd.md 和 docs/import-design.md 继续未完成的导入功能。
复用已有材料，不重写 spec；先核对当前代码与证据，暂不提交。
```

`sts-workflow` 负责选择下一步：明确小改动可直接处理；原生调用条件与宿主能力允许时衔接所选 Skill，需要显式触发时给你下一条具体调用指令。**它不会无条件自动跑完所有原生 Skills。** 熟悉入口后仍可直接调用 `implement`、`diagnosing-bugs`、`code-review` 等。

短名只在路径已确认时使用；有歧义请改为 `请使用 /绝对路径/业务项目/.agents/skills/sts-workflow/SKILL.md ……`，依赖也绑定同一项目目录。

## 从哪里进入

![根据目标、已有材料与授权选择入口](docs/diagrams/workflow-overview.svg)

完整的可复制开场、Agent 行为、用户参与点和完成产物见 **[场景使用指南](docs/usage-guide.md)**；范围、证据与原生调用规则以 [workflow.md](workflow.md) 为准。[HTML 源图](docs/diagrams/workflow-overview.html) 可下载后离线查看，GitHub 页面展示的是源码。

想先看协作方式，读 [完整功能协作图](docs/usage-guide.md#一次完整功能如何协作)；想知道文档如何关联、知识如何保留，读 [产物与知识关系图](workflow.md#产物与知识关系)。

## 范围与目录

- [skills/](skills/)：12 个原生 Skills，`sts-workflow`、`sts-acceptance`、`sts-closeout`；验收与收尾模板按需使用。
- [项目接入](docs/project-setup.md) · [场景指南](docs/usage-guide.md) · [流程合同](workflow.md)。
- [来源](SOURCES.md) · [逐文件 manifest](upstream-manifest.json) · [许可证](licenses/) · [维护要求](AGENTS.md)。

业务知识和真实产物留在业务项目。本仓库不建立流程 CLI、看板、状态机或全局控制器。原生 `implement` 含提交动作，`code-review` 仅覆盖已提交差异，均需遵守 [版本与权限合同](workflow.md#版本证据与权限)。工具链检查及隔离场景试用不能替代目标宿主发现、真实业务验证或用户验收。
