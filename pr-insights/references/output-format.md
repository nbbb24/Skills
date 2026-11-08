# Output format

Use the headings, fields, and state labels below. Replace placeholders with evidence-backed facts; use `未能确认` when a required field cannot be established. Keep all timestamps in ISO 8601 with offsets. The report is written in Chinese unless the user requests another language.

## `report.md`

```markdown
# <owner/repo> PR 洞悉｜<start>—<end>

> 仓库：<repository URL>
> 生成时间：<ISO 8601 timestamp>
> 统计口径：窗口 `[start, end)` 内创建、更新、关闭或合并的 PR；按仓库和 PR 编号去重。
> 目标分支：全部 / <user-specified branch filter>

## 1. 总览

| 指标 | 数量 |
| --- | ---: |
| PR 总数（去重） | <integer> |
| 已合并 | <integer> |
| 开放（其中草稿 <integer>） | <integer> |
| 关闭未合并 | <integer> |
| 已合并能力项 | <integer> |
| 进行中能力项 | <integer> |

本期主要变化：<2–4 句；区分窗口内的活动和 PR 整体工作。>

## 2. 已合并的特性与能力

| ID | 模块 | 能力 | 具体支持内容 | 交付状态 | 关联 PR 与依据 |
| --- | --- | --- | --- | --- | --- |
| C1 | <module> | <short name> | <observable behavior> | 已合并至 `<base>` / 已发布 `<version>` | [#123](<PR URL>)、[变更依据](<evidence URL>) |

没有符合条件的能力时写“本窗口没有可确认的已合并能力”。不要把合并等同于发布。

## 3. 进行中的能力

| ID | 模块 | 计划支持内容 | 阶段 | 关联 PR 与依据 |
| --- | --- | --- | --- | --- |
| C2 | <module> | <expected behavior> | 开放 / 草稿 | [#124](<PR URL>)、[变更依据](<evidence URL>) |

只列有足够证据的开放或草稿 PR。不能确认预期能力的 PR 仍列在第 5 节。

## 4. 分类统计

| 工作类型 | PR 数 | 已合并 | 开放 | 关闭未合并 |
| --- | ---: | ---: | ---: | ---: |
| feature | <n> | <n> | <n> | <n> |

| 模块 | PR 数 | 主要工作 | 关联 PR |
| --- | ---: | --- | --- |
| <repository-derived module> | <n> | <brief summary> | [#123](<PR URL>) |

工作类型按每条 PR 的唯一主要类型计数，合计应等于 PR 总数。模块允许多选，因此模块计数之和可以大于 PR 总数。

## 5. 逐条 PR

### [#123 <PR title>](<PR URL>)

- 状态：已合并 / 开放 / 草稿 / 关闭未合并；目标分支：`<base>`
- 本期活动：<创建、更新、关闭、合并的事件及时间；只写窗口内事件>
- 分类：`<primary type>`；模块：`<module 1>`、`<module 2>`
- 解决的问题：<problem or 未能确认>
- 完成的工作：<specific changes, not a title restatement>
- 结果或预期结果：<observable behavior or quality improvement; label planned outcomes for open PRs>
- 关联能力：C1 / 无
- 依据：[PR 描述](<URL>)、[关键变更](<URL>)、[测试或文档](<URL>)
- 待确认：<unverified claims or 无>

<!-- 每个纳入统计的 PR 恰好一节。按最近窗口内活动时间倒序，编号相同时按 PR 号排序。 -->

## 6. 数据完整性与限制

- 数据来源与抓取时间：<provider, timestamp>
- 抓取页数、去重前记录数、去重后 PR 数：<numbers>
- 筛选及核对方式：<event queries, count reconciliation>
- 无法读取或分析完整的 PR：<numbers and reasons, or 无>
- 未确认的能力、发布状态及原因：<items, or 无>
```

## `prs.json`

Use UTF-8 JSON. Preserve the following shape; additional source-specific fields may be added under `source_metadata`. IDs such as `C1` are unique within the report. The `prs` array contains every included PR exactly once. Every ID in `capability_ids` must exist in `capabilities`, and every capability's `pr_numbers` must refer to included PRs.

```json
{
  "schema_version": "1.0",
  "repository": {
    "provider": "github | gitlab | gitcode | other",
    "full_name": "owner/repo",
    "url": "https://example.com/owner/repo"
  },
  "window": {
    "start": "2026-01-01T00:00:00+08:00",
    "end": "2026-01-31T00:00:00+08:00",
    "timezone": "Asia/Shanghai",
    "mode": "activity"
  },
  "collection": {
    "fetched_at": "2026-01-31T00:00:00+08:00",
    "pages_fetched": 0,
    "records_before_deduplication": 0,
    "prs_after_deduplication": 0,
    "complete": true,
    "limitations": []
  },
  "prs": [
    {
      "number": 123,
      "title": "Example title",
      "url": "https://example.com/owner/repo/pull/123",
      "state": "open | merged | closed_unmerged",
      "draft": false,
      "base_branch": "main",
      "created_at": "2026-01-02T00:00:00+08:00",
      "updated_at": "2026-01-03T00:00:00+08:00",
      "closed_at": null,
      "merged_at": null,
      "activity_in_window": ["created", "updated"],
      "primary_type": "feature",
      "modules": ["module-name"],
      "work": {
        "problem": "What prompted the change",
        "changes": "What the PR changed",
        "result": "Observed result or planned result"
      },
      "capability_ids": ["C1"],
      "evidence": [{"label": "PR diff", "url": "https://example.com/owner/repo/pull/123/files"}],
      "unverified": []
    }
  ],
  "capabilities": [
    {
      "id": "C1",
      "name": "Capability name",
      "module": "module-name",
      "description": "Specific supported or planned behavior",
      "status": "in_progress | merged_to_branch | released",
      "target_branch": "main",
      "release": null,
      "pr_numbers": [123],
      "evidence": [{"label": "PR diff", "url": "https://example.com/owner/repo/pull/123/files"}]
    }
  ]
}
```

The strings containing `|` above show allowed values; emit one value, not the whole string. Use `null` for missing timestamps or release identifiers and an explanation in `unverified` or `collection.limitations` when the gap matters. Never serialize credentials or full API responses.
