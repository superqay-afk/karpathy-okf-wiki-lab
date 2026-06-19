# Tool Interface Map

Principle: use CLI/API/MCP first, browser second, computer-use last.

## Systems

| system | preferred | fallback | human_gate |
| --- | --- | --- | --- |
| GitHub | gh CLI or GitHub connector | browser only for visual review | push/create_pr/merge |
| 满帮 Wiki | wiki skill + Wiki MCP | browser only if MCP cannot access the page | publish/update official docs |
| FTAPI/API 文档 | ftapi skill + FTAPI MCP | local exported docs | none for read-only queries |
| 钉钉/群通知 | mid-dingtalk-mcp | manual copy | send_external_message |
| Google/Office documents | Google Drive connector or documents/spreadsheets/presentations skills | local file editing | share externally or overwrite important files |
| Web products and internal tools | CLI/API/MCP first; browser/chrome for UI verification | computer-use for no-interface apps | submit approval, irreversible action, spend money |

## Human Confirmation Gates

- `send_external_message`
- `publish_social_post`
- `delete_or_overwrite_user_files`
- `submit_approval`
- `push_to_remote`
- `create_pull_request`
- `merge_pull_request`
- `deploy_production`
- `spend_money`

