### Top 3 Linux Distributions in 2022

Let's suppose that you're a Linux user, or somenoe who is Linux-curious, but looking to take a weekend and free your mind from the orthodoxy that has become the traditional linux environment, where you have multiple competing dichotomies such as desktop and server, Gnome and KDE, Debian and Redhat, where what you really wanted was Linux optimized for a particular purpose - custom linux, if you will, but perhaps less bespoke.

If that sounds like you, you might be immutability-curious, ephemerality-curious, or tiling-curious, but haven't quite taken the leap that Neo does in the matrix. 

Regardless, the 3 systems listed here are leading the charge into modern operating systems and while those systems are emergent, moving targets, they are approaching a tipping point of stability while the benefits of using one of them, or all of them, can be felt viscerally, as if by magic.

While the 3 linux distros listed below are wildly different in terms of what problem they are solving, what they share is an emergent conceptual and philosophical basis that is ephemeral and immutable.

File systems like zfs and btr have been on a collision course with distributed SCM for years, and these systems all prove that by taking the idea of a journalled or revisioned file system, and using that to enable system stability by combining immutability via ephemerality - meaning that the container is the fundamental _data _currency_ of the underlying operating system, where the system itself is polymorphic - the state of the running is changed simply by switching the current container state.

When something breaks, much like continuous deployment systems, system stability is always just a rollback away.

The leading edge of containers and virtualization are all at play here in some form though the specific implementations differe somewhat.


Imagine a future where the last mile of humans-in-the-loop system management is replaced by autonomous system operators (agents) and you have a rough idea where this is going. The real game is instrumenting the OS with sensors that enable the system to be managed autonomously and securely at scale. 

And now for something completely different...

#### Talos Linux

[Talos Linux](https://www.talos.dev/) takes many things we learned about cluster computing, and Kubernetes, or cloud native in particular, and visits some of those requirements back on the design of linux itself, such that the linux distribution is "all system management is done via an API. No SSH, shell or console". 

Let that sink in for a moment. If you'r an experience linux user, that statement may trigger abject terror. Yes, you can survive linux without the bane of every security person's existence: a root shell. 

Just like Kubernetes: the rise of API-driven systems infrastructure finally reaches the operating system (OS). The implications are vast and profound, particularly for those who may come from a systems management perspective, where being able to manage thousands of machines via Management Information Blocks (MIBs) was the way to scale access to thousands of machines running in a large organization. 

Last time I checked, public or private cloud was a large organization, of computers, not people. If cloud scaled 1:1 between computers and people it wouldn't have survived much beyond its early days twenty-some years ago. Allowing compute instances to grow essentially unbounded with regard to humans is what gives cloud its reason for existence.


#### Fedora Silverblue

Like Talos, [Fedora Silverblue](https://silverblue.fedoraproject.org/) has at its core, the idea of immutabile infrastructure, but whereas Talos is focused on cluster computing in the form of a Kubernetes cluster, Silverblue is focused on Developer Experience (DX) - the desktop development experience that has become the achilles heel on the year of the Linux desktop asymptote. 

Jam all of these tools together onto a single Linux desktop and the previous stability of the linux machine that you had come to rely on starts to resemble a version of Windows when Steve Ballmer was still calling the shots at Microsoft.

So Silverblue takes a small list of things that are uncommon and difficult to configure right now and makes them turnkey to the extent that they are installed in a complete product from an ISO USB stick that _just works_.

This article is kept intentionally short, but the things that make fedora silverblue unique include but are not limited to podman, gnome boxes, rpm-ostree, and so on.


#### Garuda Sway

[Garuda Sway]() may be the least promoted of these futuristic alternatives as it has nothing but the traditional open source organization behind it.

Like me, you may arrive at Garuda Linux, having dabbled in arch for years, realizing that there are alternatives to Ubuntu and Redhat, that you may not have heard much about since they get drown out by the respective marketing machines from Canonical and IBM.

Garuda is one of those distros that tries to be everything to everyone on the desktop, as is the tradition in most linux distros, by providing versions based on window managers everyone has heard of, like Gnome or KDE. Unfortunately, both Gnome and KDE have suffered a popularity tipping point much like Ubuntu where they became the thing they set out to disrupt, like agile.

Enter Garuda Sway. Arch Linux base? Check. Tiling i3 window manager and keybindings? Check. Wayland speed? Check. Deprecate X11? Check.

Garuda Sway runs better on a $649 commodity laptop with 8 GB RAM than most of the aforementioned bloated desktop systems run on 16 GB.

Garuda Sway is probably the most tractable way to deprecate your mouse, as long as people old enough to remember OS/2 and CUA have been complaining about mouse dependence and how it slows GUI vs CLI.

No matter. Garuda is the path to indescribable speed, power, and simplicity that comes from being able to manage a large number of windows on a large display without your brain running out of stack space or reaching for a mouse or touchpad. 

Put simply, Garuda Sway scales window management on the dektop to enable humans to master desktop information in a way that few have since the [200 points of light demo](https://www.youtube.com/watch?v=H5-T_S50Sr4) and [successive desktop research](https://dl.acm.org/doi/pdf/10.1145/191666.191676?casa_token=aYR2BhoLpPoAAAAA:yHrKxnjyqz9Oms335i-5OPLk5EPlXxBSGzCLkCui9ScA-kE5pepdY3Y2AhTPIn9kIoKcFFaf0wuKdw) thirty years ago.