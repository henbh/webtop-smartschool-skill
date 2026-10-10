# Webtop MCP server (experimental)

A local, read-only MCP server for the Israeli Webtop student portal. It currently provides `get_dashboard` and `get_homework` tools. Homework data is returned as the original JSON so an assistant can preserve the teacher's full wording and format the requested date range.

**Ministry of Education SSO is not supported.** This server cannot reuse a signed-in Chrome session. If you normally log in through the Ministry of Education, use the [Chrome workflow](../README.md) instead; do not enter Ministry credentials into this server.

This integration uses [`pywebtop`](https://github.com/t0mer/pywebtop), an unofficial client for Webtop's private API. It is not endorsed by Smartschool/Webtop, and the API or its login flow may change. Only direct Webtop username/password login is implemented; SSO, CAPTCHA, and two-factor authentication are unsupported. The regular `$webtop` skill remains usable without this MCP server.

Validation so far: local MCP startup, tool discovery, and missing-credential handling passed. Successful live homework retrieval has not been verified. The server does not expose child-switching tools; if the dashboard is for a different child, use Chrome rather than assuming class codes will switch the student.

## Requirements

- Python 3.10 or newer and [`uv`](https://docs.astral.sh/uv/).
- A Webtop account you are authorized to use with direct Webtop username/password login.
- MCP client that supports local stdio servers.
- The Webtop `class_code` and `class_number` for homework requests. These are school-specific; the MCP does not guess them.

## Install and configure

Clone this repository. Store direct Webtop credentials in your MCP client's local environment configuration outside the repository. Do not put passwords in chat, command history, or Git. The current server reads environment variables; it does not automatically load a `.env` file.

### Codex

Add the following to your personal `~/.codex/config.toml` (not a project configuration). Replace the path and placeholders on your own computer. `uv` must be available to the app; use its absolute executable path if needed. See the [official MCP configuration guide](https://developers.openai.com/codex/mcp/).

```toml
[mcp_servers.webtop]
command = "uv"
args = ["--directory", "/absolute/path/to/webtop-smartschool-skill/mcp-server", "run", "webtop-mcp"]

[mcp_servers.webtop.env]
WEBTOP_USERNAME = 'your-direct-webtop-username'
WEBTOP_PASSWORD = 'your-direct-webtop-password'
```

Restart the app after saving. These values are stored as plain text in your personal configuration; keep that file private. If you previously added Ministry credentials, remove them.

### Clients using JSON MCP configuration

Add a local stdio server entry to the client's personal configuration, replacing the path with the absolute path to this repository:

```json
{
  "mcpServers": {
    "webtop": {
      "command": "uv",
      "args": ["--directory", "/absolute/path/to/webtop-smartschool-skill/mcp-server", "run", "webtop-mcp"],
      "env": {
        "WEBTOP_USERNAME": "your-username",
        "WEBTOP_PASSWORD": "your-password"
      }
    }
  }
}
```

`WEBTOP_DATA` may also be added in the `env` table/object if your school needs a custom login value; see [pywebtop's authentication documentation](https://github.com/t0mer/pywebtop#authentication-details). This setting does not add SSO support. Keep the MCP server local; do not expose its stdio bridge over a public network.

## Tools

- `get_dashboard`: checks API login and returns the dashboard/student data.
- `get_homework(class_code, class_number)`: returns homework data for the specified class.

Example request: “Use Webtop to list homework from 4–10 October 2026 in a Hebrew table, preserving every detail.” First use `get_dashboard` to confirm that login works and inspect the account context; then call `get_homework` with the class values configured for that student's school. The returned homework structure is school-specific, so verify its fields and date coverage before claiming the report is complete.

## Troubleshooting and limits

- Missing environment variables produce a setup message; invalid login or API errors return a generic failure without printing server response bodies or tokens.
- If login requires an unsupported flow, use the connected-Chrome workflow in `$webtop`.
- A successful API response does not guarantee it includes every historical assignment. Check the returned date coverage and use Chrome to fill gaps.
- Do not store credentials, access tokens, or raw login data in skill history or source control.

## License and dependencies

Copyright 2026 Hen Ben-Hemo. The MCP code is licensed under [Apache License 2.0](LICENSE), the same license as the parent project. Dependencies are separately licensed and are not relicensed by this project.

`pywebtop` currently has conflicting upstream declarations: its package metadata declares MIT, while its repository's `LICENSE` is Apache 2.0. See [the upstream license note](https://github.com/t0mer/pywebtop#license). Preserve the license files supplied with the exact dependency versions you redistribute; this repository does not vendor their source code.
