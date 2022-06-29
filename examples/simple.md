<h1 align="center">Downloading 1 singular file</h1>

<p align="center">
	<b>See other<a href="https://github.com/adenviney/worldwideupdater/blob/main/examples"> examples.</a></b>
</p>

```py
import wwu

base = "https://mysite.com/downloads"
Cli = wwu.client("downloads", version_url=f"{base}/version.txt", current_version="0.0.1", f"{base}/file.py") # Make sure to change current_version in your new program!

if Cli.check():
  print("Updating!")
  Cli.download()
  print("Updated!")
  
 # Code...```
