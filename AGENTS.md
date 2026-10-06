# AGENTS.md

This repo is a **public Claude Code marketplace**. It holds plugins and skills meant to be installed
by anyone, not an application.

## Structure

```
.claude-plugin/marketplace.json   # Marketplace manifest, lists every plugin
plugins/<plugin>/                  # One directory per plugin
  .claude-plugin/plugin.json       # Plugin manifest
  commands/*.md                    # Slash commands (auto-discovered)
  agents/*.md                      # Subagents (auto-discovered)
  skills/<skill>/SKILL.md          # Skills (auto-discovered)
```

## Conventions

- **kebab-case** for all directory and file names.
- Components **auto-discover**, so adding a skill/command/agent needs no manifest edit. Only adding
  a whole new _plugin_ requires an entry in `marketplace.json`.
- A skill's `description` frontmatter is what Claude matches to decide when to activate it. Keep it
  specific: name the tasks, tools, and keywords involved.
- Use `${CLAUDE_PLUGIN_ROOT}` for any intra-plugin path (hooks, scripts, MCP). Never hardcode
  absolute paths.
- Keep `SKILL.md` bodies focused; put detail in `references/`, executables in `scripts/`, templates
  in `examples/` (progressive disclosure).

## Public repo: two extra rules

Everything here is installed by people who have none of the author's context.

- **No personal content.** No employer, sector, client, stack, or private path. A worked example
  drawn from a real case stays, but it is described, not linked to something unreadable.
- **No dependency on a plugin outside this marketplace.** A skill here must work on its own. If
  another skill improves the experience, say so as an option and make the fallback explicit.

## Adding things

- **Skill**: `plugins/<plugin>/skills/<name>/SKILL.md`
- **Command**: `plugins/<plugin>/commands/<name>.md`
- **Agent**: `plugins/<plugin>/agents/<name>.md`
- **New plugin**: create `plugins/<name>/.claude-plugin/plugin.json`, then add an entry to the
  `plugins` array in `.claude-plugin/marketplace.json`, and a matching `extra-files` entry in
  `release-please-config.json` for its `version` field.

## Validating changes

```
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json'))"
python3 plugins/write-forge/skills/write-forge/scripts/valide-instance.py --help
```

After editing, refresh in a running session with `/plugin marketplace update yoann`.

## Contributing

@CONTRIBUTING.md
