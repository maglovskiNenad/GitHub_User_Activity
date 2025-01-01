# GitHub User Activity Fetcher

A simple command-line tool that uses the GitHub API to fetch and display a user's recent activity directly in the terminal.

## Features
- Fetches recent activity (commits, issues, pull requests, etc.) for a given GitHub user.
- Displays the activity in a clean, human-readable format.
- Lightweight and easy to set up.

## Prerequisites
Before you can use this tool, ensure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- A GitHub Personal Access Token (if accessing private repositories or avoiding rate limits).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/github-user-activity-fetcher.git
   cd github-user-activity-fetcher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python main.py <github-username>
   ```

2. (Optional) Provide a GitHub Personal Access Token:
   - Create a token at [GitHub Developer Settings](https://github.com/settings/tokens) with the required scopes.
   - Set the token as an environment variable:
     ```bash
     export GITHUB_TOKEN=your_personal_access_token
     ```

## Example
Fetch recent activity for the user `octocat`:

```bash
python main.py octocat
```

Output:
```
Recent activity for user: octocat
- [Commit] Updated README in repository `octocat/Hello-World` (2025-01-01)
- [Issue] Created issue: "Bug in API response" in `octocat/API-Repo` (2024-12-31)
- [Pull Request] Merged PR: "Fix typos" in `octocat/Docs` (2024-12-30)
```

## Configuration

You can customize the script by modifying the following settings in the `config.py` file:
- API endpoint
- Number of activities to fetch
- Formatting options for terminal output

## Dependencies
This project uses the following Python libraries:
- `requests`: For making HTTP requests to the GitHub API
- `argparse`: For parsing command-line arguments
- `python-dotenv` (optional): For managing environment variables

## Contributing
Contributions are welcome! If you'd like to add features, fix bugs, or improve documentation, feel free to submit a pull request.

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy using GitHub User Activity Fetcher! 🚀
