# 调用适配验证记录

2026-09-11，针对本仓库工作区的调用适配变更。流程规则以 [workflow.md](../workflow.md) 为准，适配范围与升级方式见 [SOURCES.md](../SOURCES.md#调用适配与升级)。本记录不是业务验收。

## 工程检查

- `python3 scripts/verify-upstream.py` 通过：12 个 Matt Skills、36 个来源文件及 MIT 许可证、17 个资源链接与依赖；适配文件还原后匹配固定上游原始 hash。本轮没有重新连接上游 Git。
- `tests/test_plugin_package.py` 的 8 项测试全部通过：整包异地复制与资源可移植性、原文变动拒绝、缺失资源拒绝、marketplace 解析、正文改动即使重算分发 hash 仍拒绝、非法适配拒绝、六入口双字段开放、完整插件 helper 无错误通过。
- 3 个自定义 Skills 通过系统 `quick_validate.py`。完整 plugin helper 不再豁免旧版的六项 `disable-model-invocation` 错误。
- helper 需要 PyYAML；默认 Python 与 bundled Python 均缺失该依赖，因此在临时 venv 安装 PyYAML 6.0.3 后运行，未改变项目依赖。
- 3 组 HTML/SVG 嵌入内容逐字一致且 XML 可解析；本次仅替换两张图的流程文字，未重新布局。文档本地链接与 Git diff 在交付前核查。

## 隔离行为试用

由独立 Agent 在临时空项目读取仓库最新入口及同包依赖，不安装插件、不修改业务项目、不提交。

第一轮发现：Matt 组合入口要求 Skill 工具，而当前 Codex 使用文件加载机制。随后在自定义入口明确宿主加载映射，保持 Matt 正文原文；再次试用实际通过文件加载执行 `sts-workflow → grill-with-docs → grilling + domain-modeling`，提出首轮独立产品问题并等待回答，没有要求重新调用 Skill。访谈仍在等待回答，不记为共同理解已确认。

场景里的旧计划只覆盖列表排序，新问题涉及客户导入与去重。试用未把新范围追加到旧计划，没有将未确认术语写入领域文档，也没有擅自生成 spec 或实施。

规格路径使用独立的已确认需求夹具，通过文件加载执行 setup、领域术语记录及 to-spec；在临时项目实际生成并回读 AGENTS.md、tracker/domain 配置、CONTEXT.md 和中文 spec，共 5 个文件。规格保留原生七段结构，覆盖匹配复用、编号不存在、重复导入、混合成败四类行为要求；明确无现成代码或测试先例，测试尚未编写或运行。没有要求补调用、拆票、实施或提交。

fixture 已明确选择 Local Markdown、配置位置与测试边界，并在 tracker 中实际记录 ready-for-agent 仅表示可实施，不代表实施授权；没有额外生成 triage 配置。不能将人工提供确认答案的隔离试用称为完整真实用户访谈。主 Agent 已回读规格核对上述结论；规格 SHA-256：`71643c875e254d6a98589379c7b49e11f76c5d93783f232e12580f74be27386b`。临时样例不作为业务产物收入插件。

## 尚未验证的边界

- 用户随后授权提交、推送并更新插件：实现提交 `e95332b` 已推送 main；安装版本为 `0.1.0+codex.20260911025611`。通过 `codex plugin add spec-to-ship@personal` 重装，缓存全部文件与源包逐字节一致。
- 已通过独立 Codex app-server 的 `skills/list`（Farvis cwd、forceReload）发现全部 15 个新版本入口，全部启用、来源正确、无发现错误。这不证明原有会话已刷新上下文；新任务才能可靠使用新版本。已安装包中的真实业务衔接仍未运行。
- 未执行真实业务的 tickets、implement、提交、导出或验收，不能宣称全部研发链端到端通过。
