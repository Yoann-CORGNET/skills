# skills

My personal skills for everyone to use. A public [Claude Code](https://claude.com/claude-code)
marketplace.

## Install

```
/plugin marketplace add Yoann-CORGNET/skills
/plugin install write-forge@yoann
```

Check `/plugin` to see it enabled.

## What's in it

### write-forge

A skill that builds _your_ writing skill.

Asking a model to "write like me" does not work, because the request has nowhere to land. This one
extracts the reusable components of how a person actually writes, from a corpus of their own texts
plus a structured interview, then generates a standalone plugin that holds them.

No texts to hand? An optional in-depth session produces the material instead: the person writes a
few short texts and one long one, then picks blind between variants of their own sentences. Traits
built that way stay tagged as session material, weaker evidence than real sent texts.

The model has four layers, in strict precedence:

| Layer        | What it supplies | What it is                                       |
| ------------ | ---------------- | ------------------------------------------------ |
| **Registre** | the form         | hard genre constraints                           |
| **Audience** | the inputs       | real knowledge, power and distance to the reader |
| **Posture**  | the dose         | the value played on each component               |
| **Voix**     | the direction    | the personal core, filling the space left free   |

The criterion that tells voice from register is from Biber & Conrad (2009): voice is what is _not_
functionally motivated by the situational context. The rest of the method follows from that, with a
decision procedure that files any given trait into its layer.

Three things it does differently from the usual "style guide" approach:

- **Counting refutes, it does not discover.** Stylometry is used as a filter that rules out traits
  you thought were personal but are really genre. The substance comes from reading discourse moves
  and from the interview.
- **A recurring habit is not automatically a style choice.** Telling a deliberate marker from a lazy
  tic cannot be settled from a corpus. The protocol instruments the question and then asks the
  person, because "tic" is a judgement, not an observation.
- **It ships a validator.** A writing skill maintained by hand drifts into dead pointers and
  unreachable postures. `valide-instance.py` checks a generated instance holds together.

Both scripts are standard-library Python, nothing to install:

```
# check a generated instance (dead pointers, unreachable postures, undeclared contradictions)
python3 plugins/write-forge/skills/write-forge/scripts/valide-instance.py <instance>

# refutation filter over a corpus
python3 plugins/write-forge/skills/write-forge/scripts/compte-traits.py --help
```

**Scope.** All four layers ship. Voix and Posture are personal, so the protocol extracts them from
you. Registre and Audience are universal and come complete in the instance template, like the
anti-slop floor: eight registers (`email`, `message-court`, `post-social`, `article-vulgarisation`,
`rapport`, `documentation-technique`, `papier-recherche`, `lettre-motivation`) and an `audience.md`
with its routing table and content-level rules. A generated instance runs as is. The protocol walks
you through the register catalogue with an explicit accept or decline on each entry, as it does for
postures, and the instance keeps only what you accepted.

The registers are written at a mechanical depth: situational characteristics, form constraints, a
span norm and declared overrides. They are not the product of genre-by-genre research, and the
library does not cover every genre. For a finer register, or one that is missing, add it by
following the interface contract in `references/contrats-interface.md`.

**Language.** The skill is written in French. The instances it produces are not: the protocol is
parameterised by the language of the corpus, and the markers that depend on a language are flagged
to be re-derived rather than translated.

Read `plugins/write-forge/skills/write-forge/references/limites.md` before trusting a result. The
sharpest limit: the comparison baseline is a neutral rewrite produced by the model, so any trait you
share with the model stays invisible to it.

## Layout

```
.
├── .claude-plugin/
│   └── marketplace.json          # Marketplace manifest
├── plugins/
│   └── write-forge/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── write-forge/
│               ├── SKILL.md      # The protocol, kept short
│               ├── references/   # Concept model, components, protocol, limits
│               ├── examples/     # Instance template (a standalone plugin, registers included)
│               └── scripts/      # Validator, trait counter
├── .github/workflows/            # release-please version automation
├── .prettierrc.json              # markdown formatting (100-char wrap)
└── CONTRIBUTING.md               # conventions: commits, formatting, releases
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Two rules are stricter here than in a private marketplace:
no personal content, and no dependency on a plugin outside this marketplace.

## License

[MIT](LICENSE).
