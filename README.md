Paravirtualizing OpenGL ES in Simics
======

Master's Thesis in Computer Science

Author: Eric Nilsson (EricNNilsson@gmail.com)
* Blekinge Institute of Technology
* Intel Corporation

Abstract
------

Full-system simulators provide benefits to developers in terms of a more rapid development cycle; since development may begin prior to that of next-generation hardware being available. However, there is a distinct lack of graphics virtualization in industry-grade virtual platforms, leading to performance issues that may obfuscate the benefits virtual platforms otherwise have over execution on actual hardware.
This dissertation concerns the implementation of graphics acceleration by the means of paravirtualizing OpenGL ES 2.0 in the Simics full-system simulator.
Furthermore, this study illustrates the benefits and drawbacks of paravirtualized methodology, in addition to performance analysis and comparison with the Android Emulator; which likewise utilize paravirtualization to accelerate simulated graphics.

In this study, we propose a solution for paravirtualized graphics using Magic Instructions; the implementation of which is subsequently described. Additionally, three benchmarks are devised to stress key points in the developed solution; comprising areas such as inter-system communication latency and bandwidth. Furthermore, the solution is evaluated based on computationally intensive applications.
For the purpose of this study, elapsed frame times for respective benchmarks are collected and compared with four platforms; i.e. the hardware accelerated Host machine, the paravirtualized Android emulator, the software rasterized Simics- and the paravirtualized Simics platforms.

This thesis establishes paravirtualization as a feasible method to achieve accelerated graphics in virtual platforms. The study shows graphics acceleration of up to 34 times of that of its software rasterized counterparts.
Furthermore, the study establishes magic instructions as the primary bottleneck of communication latency in the devised solution.
