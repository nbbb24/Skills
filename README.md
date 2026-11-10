# Skills

Reusable Codex skills.

- [pr-insights](pr-insights/SKILL.md): Analyze pull requests across repositories and produce an evidence-backed work and capability report.
- [readme-sync-from-prs](readme-sync-from-prs/SKILL.md): Keep repository READMEs aligned with verified PR outcomes.

## Install for automatic discovery

Keeping skills at the top of this repository does not register them with Codex.
Run the installer from this checkout:

```bash
python3 scripts/install_skills.py
python3 scripts/install_skills.py --check
```

It creates links in `~/.agents/skills/` pointing to the two skill folders, so
updates in this checkout are immediately available without copying generated
reports. Existing skills at either destination are left untouched. To use a
different discovery directory, pass `--skills-dir /path/to/skills`.

Codex supports [symlinked skill folders and implicit invocation](https://learn.chatgpt.com/docs/build-skills).
Both skills explicitly enable `allow_implicit_invocation`; their descriptions
identify the tasks that should activate them. For example:

- `https://gitcode.com/Ascend/memfabric_hybrid/ 看一下过去三周的 PR 情况`
  → `pr-insights`.
- `根据最近合入的 PR 更新 README` → `readme-sync-from-prs`.
- `帮我 review PR #123` → neither repository-wide workflow.

If a newly installed skill does not appear in the skill list, restart Codex.
The repository's [AGENTS.md](AGENTS.md) also routes matching tasks to the local
skill files when working in this checkout.
