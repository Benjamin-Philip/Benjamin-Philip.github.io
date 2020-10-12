---
layout: post
title: Package Management on Windows with Chocolately
subtitle: A life saver for all the Windows users out there
tags: [Windows Chocolately]
---

Have you ever felt the anger and distress of having to install
an application on a Windows Machine? How do you install, update,
remove or, in short, manage packages in Windows?

# Introducing Chocolately

> Chocolately is software management automation for windows that wraps installers, executables, zips and scripts into compiled packages -- Chocolately Website

For this cause, I found [chocolately](https://chocolately.org)
to be the best. Sure there is the new
[winget](https://docs.microsoft.com/en/windows/package-manager/winget)
, but it requires a windows 10 system and is still in
Preview(beta). Chocolately in short words, is a community maintained
project which hosts servers for windows packages. Much like [homebrew](https://brew.sh)
This makes it just the thing for installing our packages with.

# Requirements

To install chocolatey, you will need:

- A windows 7+ machine
- Powershell v2+
- .Net Framework 4+

## Checking your Powershell Version

Paste the following test into your Powershell(Not Command Prompt):

```
Get-Host | Select-Object Version
```

You should get something like the following:

```
PS C:\Users\Ben> Get-Host | Select-Object Version

Version
-------
5.1.19041.1
```

{: .note-box}
**Note: **Powershell comes bundled with your windows installation. There is no need to install it.

## Checking your .Net Framework version

Again in Powershell, Paste the following command :

```
(Get-ItemProperty "HKLM:SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full").Release -ge 394802
```

This command will return `True` if your .Net is `v4.6` and above or `False` if your .Net is too low.
You should get something like the following:

```
PS C:\Users\Ben> (Get-ItemProperty "HKLM:SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full").Release -ge 394802
True
```

# Download the script

Chocolately has a Powershell script which it depends on to install files.
You must download it in your home directory(or wherever) to use Chocolately (that is if you want to inspect it for security)

Here is the [link](https://chocolatey.org/install.ps1])

# Give the shell script execution permissions

We now must give our install script (which will be pulled from the web) execute permission i.e we need
to configure Powershell to execute this unknown script (without compromising security of course)

Let us get the `ExectutionPolicy`:

```
Get-ExecutionPolicy
```

If the returned Value is `Restricted`, You will have to paste the following:

```
Set-ExecutionPolicy AllSigned
```

Or this:

```
Set-ExecutionPolicy Bypass -Scope Process
```

I personally suggest the first.

Here are the points regarding the two:

### AllSigned

- Scripts can run
- Requires that all scripts and configuration files be signed by a trusted publisher, including scripts that you write on the local computer.
- Prompts you before running scripts from publishers that you haven't yet classified as trusted or untrusted.
- Risks running signed, but malicious, scripts.

### Bypass

- Nothing is blocked and there are no warnings or prompts.
- This execution policy is designed for configurations in which a PowerShell script is built in to a larger application or for configurations in which PowerShell is the foundation for a program that has its own security model.

# Install Chocolately

Now run the following command:

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Wait a few moments for the script to run et Voilà! You have installed chocolately!

# Using Chocolately

Now that we have chocolately installed, let's figure out how to use it.

{: .note-box}
**Note:** I will be using `openjdk` for this example.

## Help

This is one of the most important things to using a cli: you must know how to get the documentation.

You can get a list of commands with `choco --help`

For a command, you use `choco <command> --help`
```
PS C:\Users\Ben> choco search --help
Chocolatey v0.10.15
List/Search Command

Chocolatey will perform a search for a package local or remote. Some
may prefer to use `clist` as a shortcut for `choco list`.

NOTE: 100% compatible with older Chocolatey client (0.9.8.x and below)
with options and switches. In most cases you can still pass options
and switches  with one dash (`-`). For more details, see
the command reference (`choco -?`).

Usage

choco search <filter> [<options/switches>]
choco list <filter> [<options/switches>]
clist <filter> [<options/switches>]
```

## Searching for packages

You can search with `choco search <package>`
Let's search for openjdk:

```
PS C:\Users\Ben> choco search openjdk14
Chocolatey v0.10.15
openjdk14 14.0.2 [Approved] Downloads cached for licensed users
adoptopenjdk14 14.0.2.1200 [Approved]
adoptopenjdk14openj9 14.0.2.1200 [Approved] Downloads cached for licensed users
adoptopenjdk14openj9jre 14.0.2.1200 [Approved] Downloads cached for licensed users
adoptopenjdk14jre 14.0.2.1200 [Approved]
5 packages found.
```

# Installing a package

Now once we have found a package(its name), we can install it.

{: .box-warning}
You will need root(admin) permissions for this. If you install without root, you will create a local version
accessible only to you, which then causes lots of complications like duplicate installs.

```
choco install openjdk14
```

Chocolately will then install your package and will ask you permission to run the install script.
You then should type `A` or `Y` if yes, or `N` or `P` if no. Once the process is over, close the terminal and start it again to reload PATH
That's it! Let's check if jdk is installed?

```
PS C:\Users\Ben> java --version
openjdk 15 2020-09-15
OpenJDK Runtime Environment (build 15+36-1562)
OpenJDK 64-Bit Server VM (build 15+36-1562, mixed mode, sharing)
```

# Updating a package 

When time passes, we will need to install the updates of all your packages. We can achieve this using:

```
choco upgrade all
```

Or for just a single package:

```
choco upgrade <package>
```

# Uninstalling a package

We can remove a package with the following:
```
choco uninstall <package>
```


That's It! You know how to use chocolately! Please tell us about your relief in the comments below!
