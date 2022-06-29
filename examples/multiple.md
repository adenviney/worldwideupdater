<h1 align="center">Downloading multiple files</h1>

<p align="center">
	<b>See other<a href="https://github.com/adenviney/worldwideupdater/blob/main/examples"> examples.</a></b>
</p>

```py
import wwu

base = "https://mysite.com/downloads"
Cli = wwu.client("downloads", version_url=f"{base}/version.txt", current_version="0.0.1", f"{base}/file.py", f"{base}/file2.py") # Make sure to change current_version in your new program!

if Cli.check():
  print("Updating!")
  Cli.download(folder="folder123") # Folder isn't required, but downloading multiple files can get messy!
  print("Updated!")
  
 # Code...
