<h1 align="center">Downloading multiple files with logging and launch_after</h1>

<p align="center">
	<b>See other<a href="https://github.com/adenviney/worldwideupdater/blob/main/examples"> examples.</a></b>
</p>

```py
import wwu

base = "https://mysite.com/downloads"
Cli = wwu.client("downloads", f"{base}/version.txt", "0.0.1", f"{base}/file1.py", f"{base}/modules/module.py", f"{base}/file2.py")

if Cli.check():
    print("Updating...")
    Cli.download(folder="updated", log=True, launch_after="file1.py") #Automatically puts you in new folder, log=True is for logging, can be disabled.
    print("Updated!")

# Code...
