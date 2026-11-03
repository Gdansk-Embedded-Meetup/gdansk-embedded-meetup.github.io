---
template: presentation.html
title: "Embedded is dead? Long live embedded. How AI agents transformed firmware development at Amazon Ring and how we ship code to 130 million devices streaming video every day."
tags:
    - AI
    - programming
---

## Opis
Ring makes video doorbells and security cameras. More than 100 million of them stream and record video every day, and each one runs firmware: the low-level software that makes the hardware work. We'll show how we use AI to write and deliver that firmware faster.

We regularly bring up new device platforms on new chips, often before the chip's documentation is complete. Each time, a lot of parts must work together from scratch: the image sensor, the image processing, video compression, Wi-Fi, and the connection to our cloud. That work used to take months from a large group of engineers. On our latest platform, a team of AI agents did it, working with three engineers. We had live video in the Ring app 29 days after the first firmware work on the board. Our previous comparable project took 3x as long.

We'll show how this works day to day. The agents tune image quality by capturing frames, scoring them, and adjusting settings, first in a simulator and then on the real chip. They load firmware onto real devices, read the logs, and debug the hardware directly when video stutters. We'll also show where they get it wrong. We'll finish with what the engineer's job looks like now that much of the code is written by agents, and how that role has changed in the last few months.

## O sobie
- Piotr Kaminski — Software Development Manager, Amazon RING
- Jakub Rewieński — Embedded Senior Development Engineer, Amazon RING
