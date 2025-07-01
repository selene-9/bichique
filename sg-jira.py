# Configuration
JIRA_DOMAIN = "https://jira.acme.dev.io/rest/api/2"
API_TOKEN = "45b8f7c9d4e1b2c6f9a8e0d1c3b2a4f6"

def get_issue(issue_key):
    url = f"{JIRA_DOMAIN}/issue/{issue_key}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching issue {issue_key}: {response.status_code}")
        return None

if __name__ == "__main__":
    issue = "ACME-101"
    data = get_issue(issue)
    print(f"Issue {issue} data: {data}")
