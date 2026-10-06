# Contributing

This is a public Claude Code marketplace. These are the conventions for changing it.

## Git workflow

Never commit or push to `main`. Every change lands through a pull request.

1. Branch off the latest `main`:
   ```
   git checkout main && git pull
   git checkout -b <type>/<short-description>
   ```
2. Commit your work on the branch.
3. Push and open a PR:
   ```
   git push -u origin <type>/<short-description>
   gh pr create --fill
   ```
4. Merge once reviewed, then delete the branch.

### Branch names

Follow [Conventional Branch](https://conventional-branch.github.io/): `<type>/<description>`,
kebab-case. Types:

- `feature/` new plugin, skill, command, or agent
- `bugfix/` correcting a broken component
- `hotfix/` urgent fix
- `chore/` housekeeping, config, tooling, docs

Example: `feature/pdf-summary-skill`.

### Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
`<type>[optional scope]: <description>`. The description is a short imperative subject, lowercase,
no trailing period. Types: `feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `build`, `ci`,
`perf`, `revert`. An optional body explains _why_, not _what_.

```
feat(write-forge): add posture catalogue with seven entries
```

## Adding components

Components auto-discover, so most changes need no manifest edit.

- **Skill**: `plugins/<plugin>/skills/<name>/SKILL.md`
- **Command**: `plugins/<plugin>/commands/<name>.md`
- **Agent**: `plugins/<plugin>/agents/<name>.md`
- **New plugin**: create `plugins/<name>/.claude-plugin/plugin.json`, add an entry to the `plugins`
  array in `.claude-plugin/marketplace.json`, and add a matching `extra-files` entry in
  `release-please-config.json` so its `version` field stays in sync.

Use kebab-case for all directory and file names. A skill's `description` frontmatter is what Claude
matches to decide when to activate it, so keep it specific about the tasks, tools, and keywords
involved.

### Inside a skill

Keep `SKILL.md` short and push the detail down, so Claude loads only what a task needs:

- `references/` — prose a skill reads on demand.
- `scripts/` — executables. Python 3 standard library only, no dependency to install: these run on
  other people's machines. Prettier does not touch them.
- `examples/` — templates and fixtures.

Use `${CLAUDE_PLUGIN_ROOT}` for any intra-plugin path, never an absolute one, and check that
relative paths resolve from the file that holds them.

### What public costs you

Anyone installing this has none of your context, so two rules are stricter here than in a private
repo:

- **No personal content.** No employer, sector, client, stack, or private path, including inside a
  worked example. An example drawn from a real case is described rather than linked.
- **No dependency on a plugin outside this marketplace.** A skill must work on its own. Where
  another skill would help, state it as an option and spell out the fallback.

### Generated plugins

`write-forge` writes a standalone plugin under `plugins/<name>/`, `plugins/write/` by default, the
person choosing the name. A generated instance is someone's personal content, not a component of
this marketplace: keep it out of `marketplace.json` and out of commits here.

## Formatting

Markdown is wrapped at 100 characters via Prettier (`proseWrap: always`, `printWidth: 100`, see
`.prettierrc.json`). Frontmatter descriptions and code fences are left intact, only body prose is
reflowed.

A committed `pre-commit` hook formats staged `*.md` automatically. It runs through `core.hooksPath`
(no husky, no `package.json`), so enable it once per clone:

```
git config core.hooksPath .githooks
```

To format the whole repo by hand: `npx prettier@3 --write "**/*.md"`.

## Before opening a PR

Validate the manifest and smoke-test the scripts:

```
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json'))"
python3 plugins/write-forge/skills/write-forge/scripts/valide-instance.py --help
python3 plugins/write-forge/skills/write-forge/scripts/compte-traits.py --help
```

Keep the docs in sync. Any change that touches structure, components, install or usage, or the
conventions themselves must land with the matching updates to `README.md`, `CONTRIBUTING.md`, and
any affected `SKILL.md` in the **same** PR. Documentation has to reflect the change before it is
merged, not in a follow-up.

## Releases & versioning

Do not bump version numbers by hand. [release-please](https://github.com/googleapis/release-please)
does it from the Conventional Commits on `main`. This is why commit types matter: `fix:` drives a
patch bump, `feat:` a minor bump, and a `!` or `BREAKING CHANGE:` footer a major bump. Other types
(`chore`, `docs`, `ci`, …) don't trigger a release on their own.

The flow:

1. Land your change through a normal PR with well-typed commits.
2. On merge to `main`, the `release-please` workflow opens (or updates) a **release PR** that bumps
   `version.txt`, the two `version` fields in `.claude-plugin/marketplace.json` and the one in
   `plugins/write-forge/.claude-plugin/plugin.json`, and refreshes `CHANGELOG.md`.
3. When you want to cut the release, merge that release PR. It tags `vX.Y.Z` and creates the GitHub
   release. Nothing releases on its own, the release PR is the gate.

Those `version` fields are kept in sync by the `extra-files` entries in
`release-please-config.json`; add a matching entry there if a new plugin introduces another
`version` field to track.

## Writing style

Keep prose plain and direct. Avoid the flattened, uniform register that AI text drifts toward,
including reflexive em-dashes.
