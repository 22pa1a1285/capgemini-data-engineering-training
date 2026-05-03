# Databricks and GitHub Setup

This guide explains how to connect the training project with Databricks and GitHub without exposing access tokens.

## 1. Connect GitHub Repository in Databricks

1. Open the Databricks workspace.
2. Go to **Workspace** or **Repos**.
3. Select **Add Repo**.
4. Choose **GitHub** as the Git provider.
5. Enter the repository URL:

   ```text
   https://github.com/22pa1a1285/capgemini-data-engineering-training
   ```

6. Clone the repository into your Databricks workspace.

## 2. Work on Notebooks and Scripts

Recommended flow:

1. Open the required week/day/phase folder.
2. Attach the notebook to a running cluster.
3. Run the notebook or script in order.
4. Save meaningful outputs as screenshots in the matching `Outputs/` folder.
5. Commit only project files, notebooks, SQL scripts, Python scripts, documentation, and safe output images.

## 3. Commit Changes from Databricks

From Databricks Repos:

1. Open the Git panel.
2. Review changed files.
3. Add a clear commit message, for example:

   ```text
   Add Delta Lake day 8 notebooks and documentation
   ```

4. Commit the changes.
5. Push to GitHub.

## 4. Token Safety

Never commit Databricks personal access tokens.

Use tokens only in secure places:

- Databricks account settings
- Databricks secrets
- Local environment variables
- Secure CI/CD secret stores

Do not store tokens in:

- `README.md`
- notebooks
- `.py` files
- `.sql` files
- screenshots
- Git commit messages
- `.env` files that are tracked by Git

If a token is accidentally shared, revoke it immediately and generate a new token from Databricks.

## 5. Local Databricks CLI Configuration

If you use the Databricks CLI locally, configure credentials through environment variables.

Windows PowerShell:

```powershell
$env:DATABRICKS_HOST = "https://your-workspace-url"
$env:DATABRICKS_TOKEN = "your-token-value"
```

macOS/Linux:

```bash
export DATABRICKS_HOST="https://your-workspace-url"
export DATABRICKS_TOKEN="your-token-value"
```

After setting credentials, validate access with:

```bash
databricks current-user me
```

## 6. Recommended Git Hygiene

- Keep each assignment in its matching week/day/phase folder.
- Use short but clear commit messages.
- Keep generated temporary files out of Git.
- Add outputs only when they help show assignment completion.
- Pull latest changes before starting work in Databricks Repos.
- Push after each completed assignment or documentation update.
