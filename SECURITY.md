# Security policy

`dropkit.contents` is a public site and research repository. The related
[`local-llm/agent-harness`](https://github.com/Hskim-droid/local-llm/tree/main/agent-harness)
lane is an experimental, draft-first fixture; it is not a production ERP, QMS,
mail, or desktop automation connector.

## Do not publish sensitive material

Do not put passwords, API keys, browser cookies, session files, customer or
employee data, ERP/QMS URLs, mail credentials, or screenshots from a real
work system in an issue, pull request, commit, or fixture. The public examples
must remain synthetic.

If sensitive data was committed, stop sharing the repository copy, revoke or
rotate the affected credential, and contact the maintainer through the
[GitHub profile](https://github.com/Hskim-droid) rather than opening a public
issue. Do not assume that deleting a later commit removes data from repository
history or existing clones.

## Reporting a code vulnerability

Use GitHub's private vulnerability reporting channel for this repository when it
is enabled. If it is unavailable, contact the maintainer privately through the
GitHub profile and include only the minimum reproducible details. Public issues
are appropriate for non-sensitive bugs and documentation corrections.

The project is experimental. A successful fixture test does not certify a
real-host UI permission, credential boundary, model privacy setting, or mail
delivery path.
