---
layout: post
title: Installing ArchLinux
subtitle: The Initial Installation from a Live Arch Env
tags: [Linux, ArchLinux]
---

This is not a task for the light hearted. If you
want to use a Linux system and have an easy guided
setup (and use), check these out: [Ubuntu](https://ubuntu.com/).
If you want something Arch-based, use this: [Manjaro](https://manjaro.org/)
and for the people who want something like RHEL: [Fedora](https://getfedora.org/)
And those who want something Suse based: [OpenSUSE](https://www.opensuse.org/)
These Distros will hold your hand through out your journey.

Now if you want to know why I have been so discouraging about
using Arch, It's because it is a Linux Distro for people
who want their own personalised computer. Sure it is not as
extreme as [LFS](http://www.linuxfromscratch.org/lfs/), or
[Gentoo](https://www.gentoo.org/) But it is not easy to maintain and
use. It takes a lot effort not to foil up the setup and not have your
computer break when you update. (Which is every week/day, because Arch is
Rolling Release)

![An accurate description of Arch's behaviour](/assets/post-assets/2020-09-28-installing-arch/Fly-Bitch.jpg)

So here is tutorial (more accurate is my experience) for the folks
out there who want to use arch but want a little help during the
installation.

{:. box-warning}
**Warning:** The Author himself agrees he is not perfect. 
There are tons who are better.

{:. box-note}
**Note:** To all the Arch users who do know what they are
doing, if you find a mistake, please write a comment.
Along with an link to an explanation.

{:. box-warning}
 **Warning:** Now the most important note is that this article is just the installation.
We are just installing arch on the disk. We are not completely configuring arch.
The max we'll do is just add a Desktop Environment. You will have to configure arch to 
your needs overtime.

Few links before we start: 
1. [Installation Guide](https://wiki.archlinux.org/index.php/Installation_guide)
2. [General Recommendations](https://wiki.archlinux.org/index.php/General_recommendations)

# Downloading the ISO and verifying it

So now we need to install the latest disk image. So go to the [Downloads
Page](https://www.archlinux.org/download/) and click on the link for
the mirror your country on the downloads page.

## Download the ISO

Now once you have accessed your mirror, download the `.iso` and `.sig`
file.  The `.sig` file is to sign and verify Arch Disk image using PGP
signatures. Now, PGP (or GPG as its now called) is used by your Linux
package manager to verify if it has downloaded correct software and not
some malware. This required when we install arch into your disk when using
`pacstrap`.  This should take a while.

While the iso is downloading, you will have to install `gpg` the verify 
the iso. Otherwise there is a higher chance of the installation failing.
If you use Linux, you will already have gpg installed, but if you use 
Windows or macOS(if you haven't installed homebrew earlier) you will 
have to [install](https://www.gnupg.org/download/) it.

## Verify the ISO

Once you have got everything installed, you can now verify the iso.
Go to your terminal and change directory to the folder where the `.iso` and `.sig`
files are located. Now you can paste the following:

```bash
gpg --keyserver-options auto-key-retrieve --verify archlinux-year.month.date-x86_64.iso.sig 
```

Replace `year.month.date` with the actual file name.

Now if you something like this: 

```bash
gpg: assuming signed data in 'archlinux-2020.09.01-x86_64.iso'
gpg: Signature made Tue 01 Sep 2020 23:11:04 IST
gpg:                using RSA key 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC
gpg: key 7F2D434B9741E8AC: new key but contains no user ID - skipped
gpg: Total number processed: 1
gpg:           w/o user IDs: 1
gpg: Can't check signature: No public key
```

It means the keyserver returning the key did not include the user ID
so it could not be used to verify the signature.  You could change the
keyserver or alternately use WKD:

```bash
gpg --locate-keys pierre@archlinux.de
```

Here I am using Pierre Schmitz's public key to sign my iso.

When you try to verify again, you should get:

```bash
$ gpg --keyserver-options auto-key-retrieve --verify archlinux-2020.09.01-x86_64.iso.sig 
gpg: assuming signed data in 'archlinux-2020.09.01-x86_64.iso'
gpg: Signature made Tue 01 Sep 2020 23:11:04 IST
gpg:                using RSA key 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC
gpg: Good signature from "Pierre Schmitz <pierre@archlinux.de>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 4AA4 767B BC9C 4B1D 18AE  28B7 7F2D 434B 9741 E8AC
```

You can now burn the image.

# Burning the image

I am going to use KVM, so I won't be burning the image,
but if you are going to actually boot it now, you can use 
`xfburn`, `balena etcher`, `k3b` or even `dd` if you are on Linux. 
For the Windows or Mac user I suggest using [Fedora Media Writer](https://getfedora.org/en/workstation/download/).
Though it is used for creating live Fedora environments, it also has the
option to use a custom image.  So you have the added benefit of being
able to install Fedora without much fuss later on. You can use `rufus`,
as an alternative.

# Boot the live environment and connect to the internet.

## Set keyboard

When you boot you will be brought to the terminal.
You will first have to set the keyboard mapping according to your keyboard.
You can view all the key-mappings with:

```
ls /usr/share/kbd/keymaps/**/*.map.gz
```

The default keymap is US.

When loading the keymap, you need to use `loadkeys` and append a
filename omitting path or file extension. For example to load the french azerty 
keyboard:

```
loadkeys fr-latin1
```

## Connect to the internet

We can now connect to the internet. If you are using Ethernet,
All you need to do is connect the cable to the port. Or in my case,
using a VM, it will be automatically connected. 

### Wifi

However if you are using wifi, you will have to connect to your
modem using `iwctl`. Iwctl is a wireless daemon for Linux written by Intel. 
you can launch it by typing iwctl. 

Once you are in the shell you can type `help`. In short, you will have to: 

1. `list devices` choose the correct device, for example `wlan0` 
2. `station <device> scan`(station wlan0 scan)
3. `station device get-networks` (station wlan0 get-networks) and choose your network. eg `foobar-network`
4. `station device connect SSID` (station wlan0 connect foobar-network)

You can verify your connection with `ping`:

```
ping -c 5 archlinux.org
```

![Archlinux ping](/assets/post-assets/2020-09-28-installing-arch/ping.png)

# Update the system clock

We need to use `timedatectl` to ensure our clock is correct.
We will need to get `timedatectl` to use network time to correct our clock.
This can be acheived by switching on network time synchronization:

```
timedatectl set-ntp True
```

If you want, you can temporarily set the timezone. To list the timezones,
type:

```
timedateclt list-timezones
```

This would give you a long list of timezones. Once you have found your
timezone, press q to quit. You then can set then the timezone (In my
case Europe/Paris)with the following:

```
timedatectl set-timezone Europe/Paris
```
Check the status :

```
timedatectl status
```

![timedatectl pic](/assets/post-assets/2020-09-28-installing-arch/timedatectl.png)

# Check for UEFI mode

If you have UEFI, the booting and partitioning process is different.
To check if you UEFI, run:

```
ls /sys/firmware/efi/efivars
```

If this directory exists, you have a UEFI enabled system. You should
follow the steps for UEFI system. The steps that differ are clearly
mentioned.

# Partition and format disks

{.: box-warning}
**Warning:** Be very careful in this section of the installation. If
you were planning to dual-boot, be sure not to erase previous partitions.

For more information on partitioning click [here](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-partitions)

If you want to know about dual-booting, read the RHEL guide I attached above. You may have to shrink partitions.

We now need to list out all the disks. We can use `lsblk` or `fdisk -l`
for that. Usually a disk would be reffered to as sda1 or sda2. 

![List Disks picture](/assets/post-assets/2020-09-28-installing-arch/disks.png)

## Partition disks

### BIOS

We can now use fdisk to create partitions.

In Arch(At least in the wiki) we have the swap designated to the first partition
and the Linux partition in the second. But this is just a matter of personal preference.

You use `n` for creating a new partitions. The last bit where I specify `+1G` is actually
specifies a partition of 1 GB.

![Create partitions](/assets/post-assets/2020-09-28-installing-arch/Add-Partitions.gif)

After you have created the partitions, you will have to specify type and write them.

You can use `t` for this. You use `l` to list partition types.

![Declare /dev/sda1 as swap](/assets/post-assets/2020-09-28-installing-arch/Specify-Swap.gif)

Once you have finished partitioning, you can use `w` to write to disks.

### UEFI

For UEFI, the steps are almost same except the first partition is a EFI partition.
the second swap and the third the Linux partition. So :

|Partition type| Partition Number | Size|
| :------------| :----------------|:----|
| EFI system | 1 | 512MB|
| Swap | 2 | 1 - 4 GB (your choice) |
| Linux Filesystem | 3 | rest (your choice)| 

## Format Disks

{.: box-note}
**Note:** You can omit making a swap partition if you think
you have enough RAM. However you won't be able to hibernate.

### BIOS

We now can format the disk to the required filesystem. I will be using `ext4`, but if you 
want more information on filesystems, here is the [documentation](https://wiki.archlinux.org/index.php/File_systems)

We now will format the Linux partition:

```
mkfs.ext4 /dev/vda2
```

Then the Swap:

```
mkswap /dev/vda1
```

{.: box-note}
**Note:** Remember to replace `vda1` and `vda2` with the appropriate names 

And then mount the partitions:

```
mount /dev/vda2 /mnt
swapon /dev/vda1
```

![Format Disks](/assets/post-assets/2020-09-28-installing-arch/Format-Disks.gif)

### UEFI

So, you have two disk partitions and the first one is EFI type. Create
a FAT32 file system on it using the mkfs command:

```
mkfs.fat -F32 /dev/sda1
```

Now create an ext4 filesystem on the linux partition:

```
mkfs.ext4 /dev/sda3
```

And format the swap:

```
mkswap /dev/sda2
```

And finally mount the partitions:

```
mount /dev/sda3 /mnt
swapon /dev/sda2
```

# Install Arch

Now we install Arch on the Linux partition. The command used is pacstrap for this.
We then choose which programs we first install on Arch. 

{.: box-note}
**Note:** `base` refers to the arch base and `linux` to the linux kernel itself.

So what you would do is: 

```
pacstrap /mnt base linux linux-firmware
```

If you get an error, that the databases are corrupt, it may be 
because the databases are not getting downloaded properly. You will have 
to update your mirrolist with [reflector](https://wiki.archlinux.org/index.php/Reflector)
You then will have to delete the var/lib/pacman/sync directory.

```
mv etc/pacman.d/mirrorlist etc/pacman.d/mirrorlist.bak
reflector -c "your-country" > /etc/pacman.d/mirrorlist
rm -r /var/lib/pacman/sync
```

You then can try `pacstrap`

![Pacstrap in action](/assets/post-assets/2020-09-28-installing-arch/pacstrap.gif)

Congratulations! You have installed Arch Linux!

# Configuring your System

Now before we boot it, we need to have grub, Network, and Time-zone configured.
To do all of that we need to have to change root to the new system.

So generate a fstab file:

```
genfstab -U /mnt >> /mnt/etc/fstab
```

## Chroot 

change root into the new system

```
arch-chroot /mnt
```

## Timezone

set the timezone:

```
ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
```

Run hwclock to generate `/etc/adjtime`

```
hwclock --systohc
```

## Install Vim

I cannot think of something more important than this.
You can install Vim with :

```
pacman -S vim
```

Now you can export vim as the default editor

```
export EDITOR=vim
```

You can search for your preferred commandline editor using
`pacman -Ss`. For example:

```
pacman -Ss emacs
```

Just be sure your editor uses ncurces

## Localization

Edit /etc/locale.gen and uncomment en_US.UTF-8 UTF-8 and other needed locales. Generate the locales by running: 

```
locale-gen
```

Create the `/etc/locale.conf` file, and set the LANG variable accordingly: 

```
# Language File

LANG=en.GB.UTF-8
```

If you set the keyboard layout, make the changes persistent in `/etc/vconsole`: 

```
# Keyboard Config file

KEYMAP=fr-latin1
```

## Network Configuration

Create the /etc/hostname file:


```
# Hostname file

arch-vm
```

{.: box-note}
**Note:** Replace `arch-vm` with your preferred hostname

Add matching entries to `/etc/hosts`:

```
# Static table look up for hostnames

127.0.0.1	localhost
::1		localhost
127.0.1.1	arch-vm.localdomain	arch-vm
```

If the system has a permanent IP address, it should be used instead of `127.0.1.1`. 

### Install a Network Management software

We now install a Network Management software. You use a Network Manager
to remember wifi passwords and things like that. In this example we are
going install [NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager).

Here is a list of [Network Managers](https://wiki.archlinux.org/index.php/Network_configuration#Network_management)

So to install NetworkManager, run:

```
pacman -S networkmanager
```

Enable the daemon:

```
systemctl enable NetworkManager.service
```

When you boot you can connect to internet using [nmcli](https://wiki.archlinux.org/index.php/NetworkManager#nmcli_examples)

## Initramfs 

Creating a new initramfs is usually not required, because mkinitcpio was run on installation of the kernel package with pacstrap.
For LVM, system encryption or RAID, modify mkinitcpio.conf(5) and recreate the initramfs image: 

```
mkinitcpio -P
```

## Configuring Grub

### For BIOS

First install Grub:

```
pacman -S grub
```

And then install grub like this (don’t put the disk number sda1, just the disk name sda):

```
grub-install /dev/sda
```

And finally:

```
grub-mkconfig -o /boot/grub/grub.cfg
```

### For UEFI

Install required packages:

```
pacman -S grub efibootmgr
```

Create the directory where EFI partition will be mounted:

```
mkdir /dev/sda1 /boot/efi
```

Install grub like this:

```
grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/boot/efi
```

Finally:

```
grub-mkconfig -o /boot/grub/grub.cfg
```

## Root passwd

You can set the root password:

```
passwd
```

{.: box-warming}
NEVER EVER FORGET THIS PASSWORD. THIS PASSWORD CAN BE VITAL TO FIX YOUR COMPUTER
IF SUDO OR A CORE PACKAGE BREAKS. WRITE IT DOWN SOMEWHERE IF NEED BE.

## Create a user

We can create a user using [useradd](https://wiki.archlinux.org/index.php/Users_and_groups#Example_adding_a_user)

Here is an example:

```
useradd -m ben
```

We can then set a password for ben:

```
passwd ben
```

Let's add `ben` to the wheel group. The wheel group is the group
traditionally used for administrators with full root control:

```
usermod -aG wheel ben
```

Click [here](https://wiki.archlinux.org/index.php/Users_and_groups) for more info.

## Configure sudo

Let us first install sudo:

{.: note-box}
**Note:** It is not obligatory to use wheel as the administrator.
However it is better to stick to common standard in all things so that
it is easier to understand documentation, forums and so that it easier
for somebody else to use.

```
pacman -S sudo
```
{.: box-warning}
To configure sudo, we use visudo . Visudo is used to check 
for syntax errors is your /etc/sudoers file. NEVER EVER 
EDIT /etc/sudoers WITHOUT VISUDO. FAILURE TO DO SAW MAY RESULT
IN PERMISSION ERRORS THAT PREVENT SUDO FROM RUNNING PROPERLY.

visudo will use whatever is the value of `$EDITOR`

Configure sudo to give root permissions to all wheel members:
```
visudo
```

Now add the following after "#User Alias		ADMINS="

```
%wheel		ALL=(ALL) ALL
```

You can write and exit.

![/etc/sudoers file](/assets/post-assets/2020-09-28-installing-arch/sudo.png)

# Install a Desktop Environment

You can find tutorials with explanations for GNOME or KDE, but I am 
going to try and do a general explanation. 


## Install a display server

The first step to install a desktop environment is to have a display server
that would return display. You can install `xorg` with the following:

```
pacman -S xorg
```

## Install Desktop Environments

In this article, I am going to install XFCE, KDE and LXQT
This just for proof of concept on how to manage multiple environments.

You can install the above with:

```
pacman -S xfce4 xfce4-goodies plasma lxqt
```

You can install gnome with:

```
pacman -S gnome
```

{.: note-box}
**Note:** gnome, xfce4, plasma, lxqt are actually "groups" i.e a list of 
packages which can be installed by using the group name.


## Managing multiple Desktop environments


## Using a Desktop manager

Though uneccasary, you can use desktop mangers like GDM, SSDM, KDM etc.
You can use them by enabling the correct daemon, or appending the required
script to your xinitrc. 


You can enable GDM using the following:

```
systemctl start gdm.service
systemctl enable gdm.service
```

Or SSDM:

```
systemctl enable sddm.service
```

## Writing a script

Maybe when I have some time, I might write a script to replace display mangers, and
post it here. For more info on avoiding a Display manger, click [here](https://bbs.archlinux.org/viewtopic.php?id=123803)

# Conclusion

Installing Arch is easy. To be Frank, most distros are rather simple to install.
What is truly difficult is using Linux to its true potential and not messing up.
You must be prepared to read a lot of documentations and replace lot of scripts.
