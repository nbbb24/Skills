---
name: readme-sync-from-prs
description: Update an existing repository README from evidence-backed PR insights. Use when asked to reflect recent merged PR capabilities, usage changes, or compatibility changes in README files. Do not use for release notes, changelogs, or creating a README from scratch.
---

# README Sync from PR Insights

Update repository README content to match capabilities that readers can actually use on the README's branch. Keep this workflow independent of repository, language, and hosting provider.

## Inputs

- Target repository and branch: use the user's choice; otherwise use the current checkout and branch, or the repository default branch when there is no checkout. Identify the README files and language variants maintained on that branch. Follow repository-specific instructions and existing README conventions.
- PR evidence: use the most recent `report.md` and `prs.json` from the companion `pr-insights` skill for the same repository and intended time window. If they are absent or stale, run `pr-insights` when available, or collect equivalent evidence before editing. Verify repository identity, time window, completeness, and PR links rather than trusting filenames.
- Scope: update only README files unless the user asks for other documentation. Commit or push README edits only when requested.

## Select changes

1. Inspect the existing README and current branch's code, examples, and documentation. Treat the PR insights as candidate changes, not final product claims. Confirm that each candidate still exists in the target branch; a PR merged into another branch is insufficient evidence.
2. Update content that changes how a reader evaluates, installs, configures, integrates, or uses the project: supported capabilities, important limitations, compatibility, examples, and links. A routine bugfix, refactor, test, or CI change usually needs no README edit unless it changes one of those facts.
3. Use merged PRs for supported capability claims. Say “released” only when a release or version artifact establishes it. Do not describe open or draft PRs as supported. Mention an in-progress capability only when the user requests roadmap content or the README already maintains a clearly labeled roadmap; keep it separate from supported features. Closed-unmerged PRs do not establish capability.
4. Map each accepted change to an existing section. Make focused edits that preserve the README's structure, voice, links, and useful older content. Add a new section only when no existing section fits. Avoid turning the README into a PR log; keep PR traceability in the execution summary unless the README convention calls for PR links.
5. If multiple language variants document the same area, update their equivalent claims consistently. Preserve each language's established terminology and link targets. If a variant cannot be updated reliably, report the exact gap instead of leaving contradictory claims unmentioned.

## Verify and report

- Re-read the edited sections against the current branch. Check relative links, named files, commands, configuration names, examples, and version claims. Run a relevant lightweight check when the repository provides one; follow any stronger repository documentation gate. Do not claim a build or runtime test that was not run.
- Give a concise change table in the final response with columns `README 文件/章节`, `更新内容`, `依据 PR`, and `核实方式`. List skipped candidate PRs only when the omission would be surprising, with a short reason. If no candidate warrants a README change, leave files untouched and report that result with the evaluated PRs.
- Mark any claim that remains unverified and do not add it to the README as fact. Report incomplete PR data or unavailable target-branch evidence as a limitation.
