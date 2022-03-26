<!-- markdownlint-disable -->
## Project Status
<table class="no-border">
  <tr>
    <td><img src="https://img.shields.io/badge/Python-3.10-blue.svg"/></td>
    <td><img src="https://img.shields.io/badge/CPU-x86%20%7C%20x86__64%20%7C%20arm%20%7C%20aarch64-blue?style=flat&logo=amd&logoColor=b0c0c0&labelColor=363D44" alt="CPU Architect"/></td>
    <td><img src="https://img.shields.io/badge/License-GPLv3-blue.svg"</td>
    <td><img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white"/></td>
  </tr>
</table>



## Table of contents[![](./Images/pin.svg)](#table-of-contents)
We'd love for you to take a look at our project!
1. [Motivation](#motivation)
2. [How It Works](#how-it-works)
   - [CPU](#CPU)
   - [Clock](#Clock)
   - [Console](#Console)
   - [Memory](#Memory)
   - [Power](#Power)
3. [Installation and Dependencies](#installation-and-dependencies)
4. [License](#License)



## Motivation[![](./Images/pin.svg)](#motivation)

  In an increasingly software-driven world, it can be easy to forget the fundamental hardware that makes what we do on computers possible. This project aims to introduce the basics of how a computer runs using friendly building blocks that can be connected to produce interactive hardware. Introduced in a manner that a younger audience can appreciate, this project intends to guide the user through building a simulated computer and then run a program on it using very basic assembly commands.\
  \
  It is our hope that this will give young students a fun way to learn how computers work in an online format. Since students today may have trouble accessing actual electronic equipment, this is a clear and low cost approach to teaching this vital concept without the restrictive barriers of physical tools. We hope that students enjoy playing this game as much as we enjoyed making it and we look forward to our first batch of users!

## How it works[![](./Images/pin.svg)](#how-it-works)
- #### [CPU](#CPU)
  Greetings! I am the CPU of your computer, which stands for Central Processing Unit. Think of me as the brain of your computer, figuring out what the computer should do every time I get a clock pulse. 
  
  <img src="https://github.com/Zelknite/HooHacks2022_TeamJAR/blob/main/Images/CPU.png?raw=true" alt="CPU.png">
  
  In order to figure out what to do, I read a ‘program’, which is kind of like a blueprint of how to do something like display an Instagram page or do your taxes. But how do I run each instruction?

  Every instruction in your program includes a piece of data and an address. The address tells the CPU where the instruction is stored so that the CPU can find it! It's like knowing the address of your friend's house so you can find it. The data is the actual action to perform, like adding two numbers. So if I know where my friends house is located, I can get directions from where I am to get there!


  
- #### [Clock](#Clock)
  Hello, I’m a clock! I act as the ‘heart’ of your computer by pulsing high and low signals to the rest of my system like a heart beats in your body.
  
  <img src="https://github.com/Zelknite/HooHacks2022_TeamJAR/blob/main/Images/Clock_with_heart.png?raw=true" alt="Clock_with_heart.png">

  Each time I pulse, I output a high pulse that tells the computer to perform one instruction. The more times I pulse per second, the faster the computer can do cool things like run video games or play a YouTube video. The clock in your computer pulses over 3 billion times a second! 


- #### [Memory](#Memory)
Hi there! I’m your computer’s memory. Think of me as the library of your computer that holds your program and all the data that it needs to work. 
Remember how we talked about data and addresses? I hold both of these pieces to create a program that I send to the CPU. 

  <img src="https://github.com/Zelknite/HooHacks2022_TeamJAR/blob/main/Images/Memory.png?raw=true" alt="Memory.png">
  Think of a program like a very tall shelf with cubbies for each address that holds a piece of data. Every time the CPU needs some data, it just goes to the cubby or address where that data is, grabs it, and then does something with it!

- #### [Console](#Console)
  <!-- Need to add pictures **J** -->
  H E L L O … T H E R E! I’m the console in charge of writing what the computer is thinking. Translating it to human terms, I am like the mouth for humans. I’m in charge of telling you and other computers what the CPU should do to show you things like websites, emails, texts and even games! I LOOOVE games. You can rely on me to help you make games to play on the computer!

  
- #### [Power](#Power)
  Watts up! I’m food that goes into the belly of the computer! The CPU, Clock, Memory, and the Console all rely on me to keep them working in tip top shape! Just like you need food to fill your stomach, computer’s need electricity to live!

  <img src="https://github.com/Zelknite/HooHacks2022_TeamJAR/blob/main/Images/BetterPower.gif?raw=true" alt="power.png">


## Installation:[![](./Images/pin.svg)](#installation-and-dependencies)
> pip install pygame_gui

>attrs==21.4.0

>flake8==4.0.1

>iniconfig==1.1.1

>mccabe==0.6.1

>packaging==21.3

>pluggy==1.0.0

>py==1.11.0

>pycodestyle==2.8.0

>pyflakes==2.4.0

>pygame==2.1.2

>pyparsing==3.0.7

>pytest==7.1.1

>tomli==2.0.1
<br>

## License:[![](./Images/pin.svg)](#License)
GPL3
