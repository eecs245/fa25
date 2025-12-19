---
layout: default
title: "⚙️ Tech Support"
nav_order: 4
description: Instructions on how to set up your programming environment and type up math problems.
---


# {{ page.title }}
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


---

<!-- ## Walkthrough Video

[This video](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699) walks through most of the steps here, but it’s not a substitute for reading this page carefully.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/b74ed3c77fe74ef4a4fa4fcc2b247699?sid=15db74ca-5f63-401a-bdac-a86ef00ecab5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

It's a long, but useful video. In addition to walking you through the setup stages, it gives you some command-line tips and tricks, and shows you the various Jupyter Notebook interfaces you can choose between (JupyterLab, Notebook, Notebook Classic, VSCode). Here are some relevant timestamps:

- [2:40](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699?t=160): Downloading and running the Miniforge3 installer, creating the `eecs245` conda environment
- [9:00](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699?t=540): Cloning the course GitHub repository
- [11:25](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699?t=685): Launching JupyterLab
- [12:28](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699?t=748): Jupyter Notebook basics and the autograder
- [22:09](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699?t=1329): Restarting the kernel and submitting to Gradescope
- [24:53](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699?t=1493): JupyterLab, Jupyter Notebook, Jupyter Notebook Classic, VSCode, and Bash Profiles
- [29:25](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699?t=1765): Verifying public tests pass on Gradescope

<!-- {: .green }
**You're encouraged to follow along by walking through and submitting the "Example Homework", which can be found in our public course GitHub repository. It is not a real assignment, but just exists to make sure you know how to access, run, and submit our assignments.** -->

## Where Will We Write Code?

In this class, we'll be writing Python code, specifically in the context of machine learning. Instead of using a more traditional IDE or text editor + Terminal setup, where you write your code in one window and run it in a separate command-line, we will be using [Jupyter](https://jupyter.org), which allows us to write and run code within a single document. Within a _Jupyter Notebook_, not only can you run code and see its results in-line (from the results of `print` statements to interactive visualizations), but you can also write text and include images, which will be useful when communicating the results of data analyses to others.

In this class, labs and homeworks will involve writing some code in Python, using the Jupyter Notebook interface and some very specific versions of Python packages. There are two ways you can write code in this class:

- **Option 1**: Using the **EECS 245 DataHub**, a web-based environment that allows you to access and run all necessary code directly in your browser by clicking a single link.
- **Option 2**: By setting up Jupyter Notebooks and the correct package versions on your computer, and using Git to pull the latest versions of assignments.

The choice of which option to follow is up to you, and you can switch between the two at any time.

The pro of Option 1 is that it's very easy to get started – you don't need to deal with your Terminal, or Python packages, or Git. We've already installed all of the correct versions of Python packages for you on the DataHub, and every time we release a new assignment, we'll give you a **magic link** on the course homepage that will automatically open the relevant code notebook on your DataHub, without you needing to use Git at all. The downside to Option 1 is that the servers we're using for the DataHub are experimental and not very powerful, and if too many students try and access them at once, they may become slow or unresponsive. There is a chance you may be required to use Option 2 later in the semester, if the Option 1 servers prove to be too unreliable.

At some point in a future course or in industry, you'll need to follow Option 2. The pro is that you can work on assignments on your own computer without needing to use the internet, and the performance of your computer will be better than the DataHub's. The downside is that the setup is slightly more complicated, and each time you need to access a new assignment you'll need to pull it from `Git`, but we'll do our best to walk you through it.

---

## Option 1: Using the EECS 245 DataHub

The EECS 245 DataHub can be found at [datahub.eecs245.org](https://datahub.eecs245.org). Only students enrolled in EECS 245 have access to the server.

The **first time** you access DataHub, your username will be your uniqname (without `@umich.edu`). The password you enter will become your password for accessing DataHub. If you ever forget or need to reset your password, email `rampure@umich.edu` and we'll trigger a password reset.

You'll never really need to go to [datahub.eecs245.org](https://datahub.eecs245.org) directly. Instead, for labs, homeworks, or lectures that have programming components, we'll give you a magic link that will automatically open the relevant code notebook on your DataHub. Clicking a magic link **does not** delete any of your work – all it does is pull the latest versions of our assignment skeletons onto your DataHub.

**The first time** you open a notebook on DataHub – likely in Lab 1 – you'll need to **click "Python 3 (ipykernel)"** in the top right corner of the notebook and select **"Python 3.10 for EECS 245"**. Make sure to click "Always start the preferred kernel". 

<center><img src="../assets/site-images/select-kernel.png" alt="Select Kernel" width="300"></center>

You should only need to do this step once, but if you ever see "Python 3 (ipykernel)" in the top right corner of the notebook, make sure to switch it to "Python 3.10 for EECS 245".

To submit your Jupyter Notebooks to Gradescope, you'll need to first download them to your computer, and then upload them to Gradescope.

{: .yellow }
> As mentioned above, Option 1 has the potential of being slow and unreliable, so if you're comfortable with the local steps, we recommend following Option 2.
>
> Another note: You should not store any sensitive information on DataHub, as the instructors have access to your files for debugging purposes. The server is limited in its storage capacity, so you should only use it to work on course materials for this class, nothing else.

---

## Option 2: Local Setup

Here, we'll detail how to:
1. Download Jupyter Notebooks and set up the correct Python packages on your computer, i.e. set up your "programming environment".
1. Access the latest versions of assignments from our course GitHub repository.

We'll use the command-line (Terminal on macOS and Linux, or WSL on Windows) here extensively. This tutorial contains all of the commands you'll need to follow, but if you'd like more details, you can check out the [EECS 280 Command-Line Tutorial](https://eecs280staff.github.io/tutorials/cli.html).

There is also a [**🎥 walkthrough video**](https://www.loom.com/share/b74ed3c77fe74ef4a4fa4fcc2b247699) we recorded for a different class that covers many of the same steps. Feel free to refer to it, but it's not a substitute for reading this page carefully.

### Step 0: If using Windows, install WSL
{:.no_toc}

If you're using macOS or Linux, you can skip to Step 1.

If you're using a Windows machine, you'll need to install the Windows Subsystem for Linux (WSL). This will run an Ubuntu Linux guest virtual machine on your Windows computer, giving you access to a Terminal that behaves the same way as on macOS and Linux. Follow the [EECS 280 tutorial on how to install and use it](https://eecs280staff.github.io/tutorials/setup_wsl.html) then come back here.

### Step 1: Install `mamba`
{:.no_toc}
    
1. Download the `mamba` installer. To do this, open your Terminal and run:

    ```
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    ```

    This will place a file named something like `Miniforge3-Darwin-arm64.sh` wherever you ran the command. If you get an error saying `command not found: curl`, replace `curl -L -O` with `wget` and rerun the same command.

2. Run the installer. To do this, immediately after the last command, run:

    ```
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

When you're asked `"Do you wish to update your shell profile..."`, **type `yes` and hit enter.** If you accidentally say `no`, run the command `bash Miniforge3-$(uname)-$(uname -m).sh` again.

Now, if you restart your Terminal, it should show `(base)` at the start of each line. This is telling you you're in the base, or default, `conda` environment.

{: .yellow }
Run into an error saying `ERROR: File or directory already exists: /Users/<username>/miniforge3`? Check out [the Troubleshooting section below](#issue-error-file-or-directory-already-exists-usersusernameminiforge3-when-setting-up-environment).

### Step 2: Download [`environment.yml`](https://github.com/eecs245/eecs245.github.io/blob/main/resources/environment.yml)
{:.no_toc}

[This file](https://github.com/eecs245/eecs245.github.io/blob/main/resources/environment.yml) contains the necessary details to configure your environment. If you take a look at it, you'll see that it contains a specific Python version (`python=3.10`) along with specific package versions (like `pandas==2.1.0` and `scikit-learn==1.5.1`, for example).

### Step 3: Create a new `conda` environment
{:.no_toc}

To create the environment, in your Terminal, run:

```
mamba env create -f environment.yml
```

Note that if you put `environment.yml` in your Downloads or Desktop folder, you should replace `environment.yml` with the path to the file, for example: `mamba env create -f /Users/yourusername/Desktop/environment.yml`. Otherwise, you might get an error saying `environment.yml` does not exist. Alternatively, you can `cd` to the directory on your computer in which `environment.yml` lives before running the above command.

This step may take several minutes, and that's fine!

### Step 4: Activate the environment
{:.no_toc}

To do so, run:

```
mamba activate eecs245
```

_Where did the name `eecs245` come from, you might ask? We defined it for you at the top of `environment.yml` with `name: eecs245`._

If you get an error saying `mamba` isn't defined, try closing and reopening your Terminal first and then rerunning the command.

{: .yellow }
**The four steps above only need to be run once!**


Now, every time you work on assignments for this class, all you need to do is run

```
mamba activate eecs245
```

in your Terminal. If you need to install any packages into your `eecs245` environment using `mamba install`, make sure to activate the environment first.

### Launching Jupyter Notebooks
{:.no_toc}

There are a few different-looking IDEs in the Jupyter universe, all built on JupyterLab, **all of which you run in your browser (e.g. Google Chrome)**. You can launch each one with a different command in your Terminal:

- JupyterLab is a full-fledged IDE that allows you to open multiple notebooks in a single browser window, along with a text editor and embedded Terminal. To launch it, use `jupyter lab`.
- Jupyter Notebook is a more simplistic-looking interface that shows you just one document at a time, without a file explorer on the side. To launch it, use `jupyter notebook`.
- Jupyter Notebook Classic is the older, more classic Jupyter Notebook interface from before the JupyterLab era. To launch it, use `jupyter nbclassic`.

{: .yellow }
In some cases, launching a Jupyter notebook from the integrated VSCode Terminal may lead to dependency issues, where `otter`, `numpy`, `pandas`, and other modules may not be able to be imported. To fix this, run commands like `jupyter notebook` from the Terminal app, not the VSCode integrated Terminal.

You can launch the other two interfaces from JupyterLab, by clicking "Open In" in the top right corner of the screen. Suraj personally uses Jupyter Notebook Classic out of habit, but you're encouraged to try out all three and decide which one works best for you.

You can also use [VSCode](https://code.visualstudio.com/) (not the same as Visual Studio) to access your Jupyter Notebooks. If you'd like to do this, then **you’ll need to make sure to activate your `eecs245` conda environment within your notebook in VSCode**. Here’s how to do that.
1. Open a Juypter Notebook in VSCode.
2. Click "Select Kernel" in the top right corner of the window.
3. Click "Python Environments" in the toolbar that appears in the middle.
4. Finally, click "eecs245 (Python 3.10.14)".

### Accessing assignments using Git
{:.no_toc}

All of our course materials, including your assignments, are hosted on
GitHub in [this Git repository](https://github.com/eecs245/fa25). If you follow Option 1 and use DataHub, the magic links we provide automatically pull from this repository.

If following Option 2, though, you'll need to pull from this repository any time we release a new assignment. This means that you'll need to download and use Git in order to work with the course
materials. You can do so [here](https://git-scm.com/).

Git is a *version control system*. In short, it is used to keep track of
the history of a project. With Git, you can go back in time to any
previous version of your project, or even work on two different versions
(or \"branches\") in parallel and \"merge\" them together at some point
in the future. We\'ll stick to using the basic features of Git in EECS 245.

There are Git GUIs, and you can use them for this class. You can also
use the command-line version of Git. To get started, you\'ll need to
\"clone\" the course repository. The command to do this is:

    git clone https://github.com/eecs245/fa25

This will copy the repository to a directory on your computer. You should only need to do this once. (If you're doing this before the first lab, the repository will be pretty empty, and that's fine.)

Moving forward, to bring in the latest version of the repository, in your local repository, run:

```
git pull
```

This will **not** overwrite your work. In fact, Git is designed to make it very difficult
to lose work (although it\'s still possible!).

<!-- **Merge Conflicts**

You might – but hopefully won't! – face issues when using `git pull` regarding merge issues and branches. This is caused by files being updated on your side while we are also changing the [Git repository](https://github.com/eecs245/fa25) by updating assignments on our side.

To minimize frustration, working with GitHub pulls, merges, etc., it's a good idea to save your important work locally so that if you accidentally overwrite your files you still have the work saved. **Save your work locally, in a separate, duplicated folder (e.g. duplicate `eecs398` to `eecs398-copy`, if your local folder is called `eecs398`) before following the steps below.**

1. `git status` shows the current state of your Git working directory and staging area. It's a good sanity check to start with. You will probably see your project and lab files that you have worked on.
1. `git add .`  will add all your files to be ready to commit.
1. `git commit -m "some message of your choice"`  will commit the files, with some description in the quotations. This can be whatever you want, it won't matter.

At this stage, if you `git pull`, it should work. You should double-check that you have new files, as well as that your old files are unchanged. If they are changed then you should be able to just copy-paste from your local backup.

If the above steps do **not** work and you actually have a **merge conflict**, then:

1. `git checkout --theirs [FILENAME]`  will tell git that whenever a conflict occurs in `[FILENAME]` to keep your version. Run this for each file with a conflict.
1. `git add [FILENAME]` to mark each file with a conflict as resolved. 
1. `git rebase --continue` or `git merge`, depending on the setup.

There's a lot more to using Git than we've outlined here. What's here should be sufficient for this class, but if you find yourself needing more help, take a look [here](https://www.w3schools.com/git/) or [here](https://dsc-capstone.org/2023-24/lessons/06/).
 -->

---

## FAQs: Local Setup

### Issue: `ERROR: File or directory already exists: /Users/<username>/miniforge3` when setting up environment
{:.no_toc}

In Step 1 of the setup instructions, after running `bash Miniforge3-$(uname)-$(uname -m).sh` in your Terminal, you may see:

```
ERROR: File or directory already exists: /Users/<username>/miniforge3
If you want to update an existing installation, use the -u option.
```

This may happen if you've installed conda in the past through a different technique.

The easiest solution is to open the folder `/Users/<username>/miniforge3` and rename it to something else, like `/Users/<username>/miniforge3-old`, and then rerun `bash Miniforge3-$(uname)-$(uname -m).sh` once again.

### Issue: Libraries not importing correctly in Jupyter Notebook after successful installation
{:.no_toc}

*Problem:*
A student completed the setup process but encountered issues with importing libraries in Jupyter Notebook. Although the `eecs245` environment was active, the versions of the libraries did not match those specified in `environment.yml`. The `environment.yml` was confirmed to be in the correct directory.

*Cause:*
The issue can arise for two reasons:
1. Jupyter was launched from the VSCode integrated Terminal. To resolve this, try opening Jupyter from the system Terminal, not the one in VSCode.
2. Jupyter was previously installed using `pip`, causing the system to use the Jupyter binary located in `~/.local/bin` instead of the one associated with the `eecs245` environment. This occurred due to `~/.local/bin` being prioritized in the system’s `$PATH`. (You can check this by running `echo $PATH`). The rest of this FAQ concerns this second issue.

*Resolution:*
1. Confirm the problem by running `import sys; print(sys.executable)` in a Jupyter Notebook, which revealed that the incorrect Python executable (`/usr/bin/python`) was being used instead of `miniforge3/envs/eecs245/bin/python` (which is the Python installed in the `eecs245` environment).
2. Uninstall the old versions of Jupyter with `pip uninstall notebook` and `pip uninstall jupyter`. This worked, but the binaries remained in `~/.local/bin`. These were manually removed by `cd`-ing to `~/.local/bin` and running `rm jupyter*`. WARNING: this is dangerous, so only run this if you're confident you're deleting the right files.
3. Reinstall Jupyter using `conda install jupyter` and `conda install notebook`, which corrected the issue.
4. [Not everyone will see this error] Finally, an error related to `matplotlib` and `pyparsing` was resolved by running `pip uninstall pyparsing` followed by `pip install pyparsing`.

*Takeaway*: If it looks like the wrong libraries/programs are running, confirm that by running commands like `which jupyter`, `sys.executable`, and `echo $PATH`. Use that information to what to remove or install.

### Issue: `(base)` not appearing in Terminal
{:.no_toc}

If it doesn't look like the `(base)` conda environment doesn't seem active, you may have installed `conda` in the past without updating your shell profile. The initial install probably didn't get to that step last time because conda was already installed. If that's the case,
- Open the user folder on your computer and rename the `miniforge3` folder to `miniforge3-old`.
- Try running the instructions again: `bash Miniforge3-$(uname)-$(uname -m).sh`, wherever you have the Miniforge3 installer downloaded.
- When you do it this time, it should ask you about updating your shell profile.

### Issue: "Operation not permitted" when accessing `environment.yml`
{:.no_toc}

Your Terminal may not be able to access files on, say `Desktop`, `Downloads`, or `Documents` where `environment.yml` is stored. Try moving `environment.yml` to another folder and trying again.

### Issue: Wanting to exit `(base)` on Terminal
{:.no_toc}

With `mamba` installed, your Terminal will permanently say `(base)`, at least for the rest of the semester. There's a command you can run to get rid of that, too, but when you do that you won't be able to `conda activate eecs245` anymore. You can still use your Terminal as normal even if it says `(base)`. Here's are [instructions](https://docs.anaconda.com/anaconda/install/uninstall/) to uninstall conda entirely.

### Issue: JupyterLab not automatically launching on Windows
{:.no_toc}

See [here](https://stackoverflow.com/questions/52691835/wsl-ubuntu-how-to-open-localhost-in-browser-from-bash-terminal/62275293#62275293) for the fix.

### Issue: Can't access the JupyterLab debugger
{:.no_toc}

A student on Ed once asked:

> Is there a way to do line by line debugging in Jupyter Notebooks? I want to be able to see the values of the code I'm running as it runs in each cell.

There's actually a debugger built into JupyterLab. You might be able to access it here, by clicking the bug:

<center>
<img src="../assets/site-images/debugger.png" width="50%">
</center>

Unfortunately, it is often greyed out by default. To enable it, go to this file on your computer, but replace `surajrampure` with your username:

```
/Users/surajrampure/miniforge3/envs/eecs245/share/jupyter/kernels/python3/kernel.json
```

Open it, and edit `"debugger": false` to be `"debugger": true`. Once you save and close the file, and restart JupyterLab, the debugger should work!

### Issue: Tests that should be passing are failing and displaying `np.True_`
{:.no_toc}

You may have the wrong version of `numpy` installed, likely because you ran `pip install numpy` in the past. In a notebook cell, run `!pip install numpy==1.26.0`, then restart your kernel and try again. From the Terminal, `pip install numpy==1.26.0` will suffice.

### Issue: Getting a `RecursionError` when running `grader.check`
{:.no_toc}

This is a convoluted issue. See [here](https://github.com/ucbds-infra/otter-grader/issues/480) for more details, but to fix it, open the following directory:

```
/Users/<username>/miniforge3/envs/eecs245/lib/python3.10/site-packages/
```

and delete the following file (it may not be named exactly this, but it will involve `pdb`, `hijack`, and `.pth`):

```
PDBPP_HIJACK_PDB.pth
```

Then, try restarting your kernel and running all of your cells again.

### Issue: Git merge conflict
{:.no_toc}

From time to time, you may see an error like this when you try to `git pull` our course repository:

```
error: Your local changes to the following files would be overwritten by merge:
        homeworks/hw01/hw01.ipynb
Please commit your changes or stash them before you merge.
Aborting
```

This happens when we've made changes to assignments after we've released them. We only do this in rare situations, since we want to avoid these merge conflicts. But, there are a few ways you can fix them.

- One solution: Rename the conflicting files. In the above example, you could rename `hw01.ipynb` to `hw01-old.ipynb`. Then, once you `git pull`, `hw01.ipynb` will contain the "new" version of Homework 1. You could either copy your work over to the new version, or check Ed/the course website for any clarifications on the differences.
- Another solution: If (and only if!) you don't have any important changes locally, and are okay with replacing the version of the conflicting file with our new version, run `git stash`, then `git pull`. 