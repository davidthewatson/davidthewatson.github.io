### Digital Diabetes Technology

#### Kudos

I owe a debt of gratitude to Keith Runyan. His book has been helpful, though
more on diet and exercise than pumps or CGMs.

I've also found Ian Lake's website and Zero Five 100 to be helpful.

Finally, Matt Vande Vegte has incredible content and led me to much of the
advice and conclusions that I mention here.

#### Room for improvement ####

Digital diabetes is a complex ecosystem owing to the integration of sensors and
mobile devices via bluetooth plus mobile devices and cloud systems via the 4G
LTE and the internet. The devices are complex even without wireless
connectivity but those things have only magnified the complexity and point to
the need for human-centered design, and a non-existent last mile geek squad of
technical support that is overwhelming doctors, diabetes educators, and
patients.

Design problems show up despite manufacturer's best efforts to solve them and I
believe this is a result of the aforementioned complexity. I have the benefit
of having worked in medical devices and digital health and so I can generally
intuit what's wrong when the system fails but there are at least a few cases
that were difficult to debug even for someone with a shared mental model,
technical depth and experience.

There are several incidents that are worth mentioning that demonstrate the
challenge that these companies face in overcoming the ecosystem complexity.
First, Dexcom and Tandem are not operating at NASA levels of technology
delivery maturity. They are doing well enough to survive and perhaps thrive in
the market, but there are cracks in the safety armor.

Almost a year ago, not long after I got the Dexcom G6, the blood glucose
readouts and notifications that would typically show up on my watch or phone
suddenly stopped and didn't start working for several days. This was widely
reported on the internet and reached major news sites such as the Wall Street
Journal.

This situation raises the need for vigilance on the part of patients,
caregivers, and everyone in the technology support system to be aware that the
publish-subscribe system employed by Dexcom to publish bluetooth data
originating from the sensor to it's subscribers (which may be everything from
the patient's watch to a parent's smart phone or other app) was dependent on a
single point of failure in the cloud.

I believe Dexcom learned its lesson with crisis PR, as the company now has
better status mechanisms in place, but there were a tense few days, not so much
for people like me - I can live without my watch displaying blood glucose - but
for parents with diabetic children or the like.
Second, Tandem's software quality problems have played out slightly
differently. The company was slow to market with a mobile app that interfaced
with the t:slim X2, but once delivered, the app seemed polished and
professional.

Unfortunately, that polish was a facade. The app worked well most of the time
but as I spent more time with it, I realized that there were serious latency
and queuing problems plaguing the app. This latency and queuing plague is so
serious that I've considered uninstalling the Tandem app from my phone.
In short, what happens is that notifications from the pump are queued and not
displayed on the phone until hours after the events that triggered them.
This may seem like a minor annoyance until you consider that those events are
important, like insulin delivery stopped and inherently timely, like receiving
the insulin delivery stopped notification when insulin delivery is not actually
stopped hours later or vice versa.

The implication of this is that the state machine that has to be managed by the
mobile app is out-of-synch with the insulin pump itself. The worse implication
would be that there is no state machine in the design.
This is a huge safety hole, one that I hope doesn't wind up causing injury or
harm because it could be easily misread and lead to bad dosing decisions on the
part of the patient or caregivers.

At a minimum, the app designers need to consider the cognitive dissonance that
occurs when the patient receives a notification that they know is out of synch
with the pump.This kind of latency may be fine in text messaging, but the
design consideration in medical devices should be a serious safety concern.
Third, the challenge of producing a system that is a collaborative venture
between two companies such as Dexcom and Tandem, and the G6 and t:slim X2,
respectively, is that the customer experience should not be concerned with
crossing the chasm between Dexcom and Tandem, either legally, technically, or
in terms of supply chain and support.

The past year has been challenging for everyone providing remote technical
support, as many systems were not up to the challenge of scaling to support so
many simultaneous connections, both human and machine.

However, where this shows up with Dexcom and Tandem is when a device or a
disposable component malfunctions, it can be confusing to navigate help lines,
web sites, and email addresses without a single, unified entry point into such
systems. Patients deserve better. I believe Tandem and Dexcom are working hard
to improve the disconnects, but it has been challenging when support needs to
transit a complex ecosystem of email, web, and phone. That said, I've had a
positive experience with both Tandem and Dexcom support and they've always
followed through when the products and services malfunctioned. Most commonly,
this has been with Dexcom's G6 transmitter batteries. They frequently failed
before their 90 day expiry and this has been resolved every time with a
warranty replacement, and a sensor to account for the wasted sensor owing to
the transmitter change.
