# Utera: A Period Piece

## Overview

Utera is an interactive educational tool designed to reduce stigma around the topic of menstruation and instruct viewers on the menstrual cycle. In the United States, the age of menarche (when girls first get their period) is about 12.5 years, but many of the resources for teaching this topic are heavily medical, and not designed for younger people. Since menstruation can be so present in the lives of female bodied individuals, I wanted to design a system that communicated the most important parts of the menstrual cycle in a more entertaining, approachable way. Also, by forcing viewers to pick up Utera and physically trigger the next state, she forces viewers to interact with this often shunned topic, and confront any reactions of discomfort, aversion, or disgust.


## Hardware

- 17 x LEDs (11 red, 6 white)
- 2 Push Buttons
- 1 x ESP32
- 1 x 5V Portable Charger

## Software

- Arduino

## How to Run

1. Upload the [`Uterus`](https://github.com/devitos-yale/cpsc334/blob/main/Final/Uterus/Uterus.ino) code to the ESP that is installed inside Utera.
2. Connect the ESP to the 5V portable charger, and close the zipper.

## Usage

To interact with Utera, simply pick her up and turn her on by holding down the power button. To advance to the next phase of the cycle, represented by different patterns of LEDs, hold down the play button until the LEDs change. There are four different parts of the menstrual cycle represented: (1) the development of an ovarian follicle; (2) ovulation, where the egg is released from the ovary and travels down the fallopian tube; (3) the thickening of the endometrium (uterine lining); and (4) menstruation, the shedding of this lining.
