name: Trigger DAG

on:
  push:
    branches:
      - master

jobs:
  trigger_dag:
    runs-on: ubuntu-latest

    steps:
      - name: Set up Google Cloud SDK
        uses: google-github-actions/setup-gcloud@v0
        with:
          project_id: ${{ secrets.GCP_PROJECT_ID }}
          service_account_key: ${{ secrets.GCP_SA_KEY }}
          
      - name: Trigger DAG
        run: |
          gcloud composer environments run ENVIRONMENT_NAME \
            --location LOCATION_NAME \
            trigger_dag -- DAG_NAME
