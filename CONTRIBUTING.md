# Contributing to Semantic SerDes

Thank you for your interest in contributing to **Semantic SerDes**! We value every contribution — whether it's a bug report, schema improvement, new example, or documentation update.

---

## Getting Started

1. **Fork the repository** by clicking the "Fork" button at the top right of the [main repository page](https://github.com/SocioProphet/semantic-serdes).

2. **Clone your fork** locally:

   ```bash
   git clone https://github.com/your-username/semantic-serdes.git
   cd semantic-serdes
   ```

3. **Set the upstream remote** so you can keep your fork in sync:

   ```bash
   git remote add upstream https://github.com/SocioProphet/semantic-serdes.git
   ```

---

## Making Changes

1. **Create a feature branch** for your work:

   ```bash
   git checkout -b my-new-feature
   ```

2. **Make your changes** — see [What to Contribute](#what-to-contribute) below for guidance.

3. **Validate your changes** (requires Python 3.8+ and `jsonschema`):

   ```bash
   pip install jsonschema
   python tools/validate_semantic_serdes.py
   ```

4. **Commit your changes** with a clear, descriptive message:

   ```bash
   git commit -am 'Add context_merge_policy example for CONDITIONAL_FALLBACK'
   ```

5. **Keep your branch up to date** with the upstream `main` branch:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

6. **Push your branch** to your fork:

   ```bash
   git push origin my-new-feature
   ```

7. **Open a pull request** against the `main` branch of [SocioProphet/semantic-serdes](https://github.com/SocioProphet/semantic-serdes). Include a clear title and description explaining what your change does and why.

---

## What to Contribute

| Area | Description |
|------|-------------|
| **Schemas** | Improve or extend JSON Schema definitions in `schemas/`. Ensure backward compatibility. |
| **Examples** | Add or improve YAML examples in `examples/`. Examples should be valid against their corresponding schema. |
| **Canonical enums** | Propose new enum values in `canonical_enums.yaml` with a rationale in the PR description. |
| **Validation tooling** | Improve `tools/validate_semantic_serdes.py`. |
| **Documentation** | Update `README.md`, `docs/`, or add new architecture decision records. |
| **Bug fixes** | Fix incorrect schema constraints, wrong enum references, or broken examples. |

---

## Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming environment for everyone.

---

## Questions?

Open an [issue](https://github.com/SocioProphet/semantic-serdes/issues) and we'll be happy to help.
