## Commit Message Style

- **First line**: action verb + concise description, no conventional-commit
  prefix (`feat:`, `fix:`, `perf:`, etc.).
  Example: `Implement single-dictionary lookup fast-path for PrefixMatch`
- **Body**: one or two sentences summarising motivation and scope, separated
  from the title by a blank line.
- **Multi-area changes**: add a `Detailed Changes:` section with bold headers
  and sub-bullets:
  ```
  Detailed Changes:
  - **Section Name**:
    - Sub-point one.
    - Sub-point two.
  ```
- **No** `Co-Authored-By` trailer lines.
