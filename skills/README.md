# Shared skills

This catalog is part of the single public website repository. No skill is
published yet. Prepare candidates in private staging before adding them here.

A skill is an instruction package; it may also contain scripts or templates.
Describe required tools, allowed actions, setup, examples and limitations. Do
not present a script-bearing skill as something that cannot execute code.

Before a public commit, the owner must confirm personal ownership and permission
to share, use of general examples, review of every packaged file, the license,
and publication approval. A generic rewrite alone is not proof of ownership.
Employer-specific skills and skills derived from company-owned kits stay private.

For each reviewed skill, create `skills/<id>/SKILL.md`, `LICENSE`, and supporting
files. Register it in `catalog.json` with:

- `id`, `title`, `description`, `license`, `provenance`;
- `files`: every file included, including `SKILL.md` and `LICENSE`;
- `ownershipConfirmed`, `generalizationReviewed`, `syntheticExamplesOnly`,
  `publicationApproved`: all explicitly true;
- `companyDerived`: explicitly false.

Run `python3 scripts/test_public_catalog.py` and `npm run build` before publishing.
The site creates `/skills/<id>/`, `/skills/<id>.md`, and `/skills/<id>.zip`.
The package includes its license. A skill-specific license governs that skill;
the site's default content terms do not automatically permit skill reuse.

The nightly automation skill is only a possible future candidate. Its public
version, provenance review, and publication approval have not been established.
