### Using Logitech K830 with Barrier #
If you're like me, you juggle computers, frequently using more than one
computer at-a-time.

And you control those computers with a single keyboard and touchpad, which
brings us to the subject of software KVM - the ability to control multiple
physical GUI computers with a single keyboard and mouse shared over the
network.

I've been running this way for so long that it's hard to imagine a more optimal
way to work on more than one GUI machine that is not virtual, rather physical.
Which brings me to barrier. Barrier is what synergy used to be: awesome and
free, enabling me to run in exactly the three laptop setup that I did when I
ran synergy years ago: Windows, MacOS, and Linux with a single shared keyboard
and touchpad.

But there's only one problem.

The K830 for all of it's design brilliance has one near-fatal flaw: it cannot
be configured for natural scroll out of the box in any easy way, like a
preferences or settings GUI until very recently. Literally, you could not
configure this touchpad to do natural scorlling on Windows prior to 2020
without resorting to a registry edit. And not just any registry edit - one that
is so complex it may win an award for configuration complexity.

The good news is that there is a fix: Logitech Options got this capability in
2020 but there is a bug to note relative to Logitech Options use with Barrier.
That is, if you turn on Content tracks fingers under Point&Scroll in Logitech
Options the touchpad will cease to function over Barrier on the client
computers. I run barrier server on Windows so in my setup this was Mac and
Linux that got a dead touchpad. However, this is easily solved by simply
disabling Smooth Scrolling in Logitech Options and restarting.