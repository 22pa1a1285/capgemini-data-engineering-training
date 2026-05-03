# Uploading the Capstone Project to Databricks

The Databricks CLI is not installed in the current local environment. To upload this project from the command line, either install the Databricks CLI or use Databricks Repos from the workspace UI.

## Option 1 - Databricks Repos

1. Open Databricks.
2. Go to **Workspace** or **Repos**.
3. Select **Add Repo**.
4. Use this GitHub repository URL:

   ```text
   https://github.com/22pa1a1285/capgemini-data-engineering-training
   ```

5. Open `Projects/Capstone Project`.
6. Configure the DLT pipeline using the files in `notebooks/dlt_pipeline`.

## Option 2 - Databricks CLI

Set credentials locally using environment variables:

```powershell
$env:DATABRICKS_HOST = "https://your-databricks-workspace"
$env:DATABRICKS_TOKEN = "your-token"
```

Then import files into a Databricks workspace folder.

Never commit the token to GitHub.
