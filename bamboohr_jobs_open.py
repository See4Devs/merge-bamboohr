import MergeATSClient
from MergeATSClient.api import jobs_api
import csv

configuration = MergeATSClient.Configuration(
    host="https://api.merge.dev/api/ats/v1"
)

configuration.api_key['tokenAuth'] = 'YOUR_MERGE_API_KEY'
configuration.api_key_prefix['tokenAuth'] = 'Bearer'

with MergeATSClient.ApiClient(configuration) as api_client:
    api_instance = jobs_api.JobsApi(api_client)
    x_account_token = 'YOUR_MERGE_LINKED_ACCOUNT_KEY'
    
    try:
        api_response = api_instance.jobs_list(x_account_token, status="OPEN")

        # Define the CSV file name
        csv_file = "bamboohr_jobs_open_results.csv"

        # Write the API response to a CSV file
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write header row
            writer.writerow(["Name", "Status", "Created At"])

            # Write data rows
            for job in api_response["results"]:
                name = job["name"]
                status = job["status"]
                created_at = job["remote_created_at"]

                writer.writerow([name, status, created_at])

        print(f"Results written to {csv_file}")
    except MergeATSClient.ApiException as e:
        print('Exception when calling JobsApi->jobs_list: %s' % e)
