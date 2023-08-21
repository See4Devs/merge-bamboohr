import merge
from merge.client import Merge
import csv

merge_client = Merge(
    api_key="YOUR_MERGE_API_KEY", 
    account_token="YOUR_MERGE_LINKED_ACCOUNT_TOKEN")

try:
    jobsOpenList = merge_client.ats.jobs.list(status="OPEN")
    # Define the CSV file name
    csv_file = "bamboohr_jobs_open_results.csv"

    # Write the API response to a CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(["Name", "Status", "Created At"])

        # Write data rows
        for job in jobsOpenList.results:
            name = job.name
            status = job.status
            created_at = job.remote_created_at

            writer.writerow([name, status, created_at])

    print(f"Results written to {csv_file}")
except Exception as e:
    print('Exception when getting open jobs list: %s' % e)
