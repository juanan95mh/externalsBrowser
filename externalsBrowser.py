import subprocess

def get_svn_externals(path):
	cmd = ['svn', 'propget', 'svn:externals', '-R', path]
	result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if result.returncode != 0:
		print(f"Error: {result.stderr.decode()}")
		return []
	externals = result.stdout.decode().splitlines()
	return externals

def open_in_rabbitvcs(path):
	cmd = ['rabbitvcs', 'browser', path]
	subprocess.run(cmd)

def main():
	path = "/home/vcs/00_REPO_SVN/B65"
	externals = get_svn_externals(path)
	for i, external in enumerate(externals, start=1):
		print(f"{i}. {external}")
	choice = int(input("Pick an external: ")) - 1
	if 0 <= choice < len(externals):
		open_in_rabbitvcs(externals[choice])
	else:
		print("Invalid choice")

if __name__ == "__main__":
	main()