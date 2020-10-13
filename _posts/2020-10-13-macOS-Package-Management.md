---
title: macOS package management
subtitle: A Linux like experience in macOS
tags: [macOS, homebrew]
---

Installing Applications in your mac can be as tedious as it is in Windows.
Like Windows, you have the App store which is filled with the usual junk
of games, WYISWG Editors etc . This perfectly fine until... You want to develop
stuff. It becomes difficult to install, update and manage compilers interpreters.

# Introducing homebrew

Now homebrew is a package management written entirely in bash(at least the install script)
so you can use it on a Linux system (Any Unix to be frank) but I strongly discourage you
from using it if you have an inbuilt package manager. You can read more about homebrew [here](https://brew.sh)
It is very similar to Windows' [Chocolately](https://benjamin-philip.github.io/2020-10-12-Windows-Package-Management)
But much better (because Unix makes it all simpler)

{: .note-box}
***Note:*** I am using a Linux box, and hence the dependencies installed
may be different.

# Login as an admin

Now installing homebrew is very simple. But use root access.
So if you are not not an admin, Login as an Admin in the terminal:

```
su - <admin code name>
```

And then type in the password

For eg:

```
su - ben
```

### Finding an admin and his/her codename

You can find all the users with root access with the following:

```
grep '^sudo:.*$' /etc/group
```

eg: 

```
ben@frodo:/mnt/c/Users/Ben$  grep '^sudo:.*$' /etc/group
sudo:x:27:ben
```


# Install homebrew

Now do the following:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Now brew may or may not ask you for sudo access(root). If it asks for it, please enter the admin's passwd.

# Using homebrew

{: .box-note}
**Note:** I will be using `openjdk` as an example. openjdk is a opensource java compiler, which in
my opinion better than regular jdk.


## Help

You can use the `--help` flag for this.
homebrew will give help on a command if specified (`brew <command> --help`)

eg:

```
ben@frodo:~$ brew install --help
Usage: brew install [options] formula|cask

Install a formula or cask. Additional options specific to a formula may be
appended to the command.

Unless HOMEBREW_NO_INSTALL_CLEANUP is set, brew cleanup will then be run for
the installed formulae or, every 30 days, for all formulae.
```

## Searching for a package

You can search for a package with `brew search`
Let's search for `openjdk`:

```
ben@frodo:~$ brew search openjdk
==> Formulae
adoptopenjdk                           adoptopenjdk@11                        openjdk                                openjdk@11
```

Let's find some more info on it:

```
ben@frodo:~$ brew info openjdk
openjdk: stable 14.0.1 (bottled) [keg-only]
Development kit for the Java programming language
https://openjdk.java.net/
Not installed
From: https://github.com/Homebrew/linuxbrew-core/blob/HEAD/Formula/openjdk.rb
==> Dependencies
Build: autoconf ✘, pkg-config ✘
Required: cups ✘, fontconfig ✘, libx11 ✘, libxext ✘, libxrandr ✘, libxrender ✘, libxt ✘, libxtst ✘, unzip ✘, zip ✘, alsa-lib ✘
==> Caveats
For the system Java wrappers to find this JDK, symlink it with
sudo ln -sfn /home/linuxbrew/.linuxbrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk is keg-only, which means it was not symlinked into /home/linuxbrew/.linuxbrew,
because it shadows the macOS `java` wrapper.

==> Analytics
install: 2,381 (30 days), 6,378 (90 days), 15,140 (365 days)
install-on-request: 505 (30 days), 1,334 (90 days), 3,038 (365 days)
build-error: 0 (30 days)
```


## Installing a package

Now, this is a process where you ***must*** use root access (If you care about installing everything properly).
So, Log into the admin, and do the following:

```
sudo brew install openjdk
```

Let the program run and that's it! You have installed your first package!
Let's check openjdk's version!:

```
java --version
```

I got:

```
ben@frodo:~$ java --version
openjdk 14.0.1 2020-04-14
OpenJDK Runtime Environment (build 14.0.1+7-Ubuntu-1ubuntu1)
OpenJDK 64-Bit Server VM (build 14.0.1+7-Ubuntu-1ubuntu1, mixed mode, sharing)
```

Now isn't this much better than installing it manually? You use a script for it.
That's the way things are done in Unix! (and GNU systems) Please don't do it the Windows way!

## Uninstalling a package

If at all you need to uninstall a package, you use the following:

```
sudo brew remove <package>
```

So, for openjdk it will be:

```
sudo brew remove openjdk
```

# Conclusion

Installing packages are a pain. That's why you use a package manager. Install your
all your packages with brew! Don't be a simpleton!

