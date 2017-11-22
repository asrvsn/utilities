from github import Github
import argparse

parser = argparse.ArgumentParser(description='Spit out milestone issues into a CSV')
parser.add_argument('-u', dest='username', help='github username')
parser.add_argument('-p', dest='password', help='github password')
parser.add_argument('--repo', dest='repo_name', help='repository name (formated as \{owner\}/\{repo\})')
parser.add_argument('--milestone', dest='milestone_name', help='milestone title')
parser.add_argument('-o', dest='output', help='output file')

args = parser.parse_args()

g = Github(args.username, args.password)
repo = g.get_repo(args.repo_name)
milestone = None
for m in repo.get_milestones():
	if m.title == args.milestone_name:
		milestone = m
issues = repo.get_issues(milestone=milestone)

with open(args.output, 'w+') as f:
	for issue in issues:
		f.write("%s,%s\n" % (issue.title, issue.html_url))