---
title: Memory
image: binary.jpg
filename: '_data/system_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"

     - To explain that the primary purpose of main memory
     - To distinguish between volatile and non-volatile memory
     - To understand the Role of RAM in a Computer System
     - To assess the impact of RAM capacity on a computer's performance
     - To kow the difference between RAm and ROM
     - To understand the concept of virtual memory
     - To know the purpose of cache memory, its hierarchical organization (L1, L2, L3)

The purpose of **main memory** is to store the instructions from the programs currently running on a computer system and to hold the data needed by those programs allowing quick access by the processor.

Memory is the computer’s facility to store data such as documents, music, pictures and any other files and data. It is either **volatile** or **non-volatile**

**Volatile memory** - When there is no power to the computer’s storage of the content is lost. 

**Non-volatile memory** - Even when there is no power, the data and files can be accessed again once power has been restored.

## Random Access Memory (RAM)

**Random Access Memory** (RAM) is the working memory of the computer system.  Each time computer software is run, the instructions for that software is first copied into RAM.  Each time a file is opened, the contents of that file are copied into RAM.  When a user makes changes to a document those changes will be stored in RAM

RAM is volatile, which means that it loses its data when the computer is powered off.  To ensure those changes are retained it is necessary to save the document to secondary storage.

Other important aspects of RAM include:

- **Multi-tasking**: RAM enables a computer to handle multiple tasks simultaneously. When you switch between applications or open multiple programs, the data for each of these tasks is stored in RAM, so they can be quickly accessed by the CPU without waiting for data to be retrieved from slower storage devices.

- **Capacity**: The amount of RAM in a computer can vary. Computers typically have several gigabytes (GB) of RAM, but more powerful systems used for tasks like gaming, video editing, or scientific simulations may have 16 GB or more. The amount of RAM you need depends on your specific use case.

- **Types of RAM**: There are different types of RAM, including DDR (Double Data Rate) RAM, DDR2, DDR3, DDR4, and DDR5, with each generation offering increased performance and efficiency. The type of RAM used in a computer depends on the motherboard and CPU compatibility.

- **Upgradability**: In many desktop computers, you can upgrade or add more RAM to improve performance, as long as your motherboard supports it. This is a common and relatively cost-effective way to enhance your computer's speed and multitasking capabilities.

## Read Only Memory (ROM)

ROM, which stands for Read-Only Memory, is a type of computer memory that stores data permanently, and this data cannot be easily modified or overwritten. Unlike RAM (Random Access Memory), which is volatile and loses its data when the computer is powered off, ROM retains its data even when the computer's power is turned off. Here are some key characteristics and uses of ROM:

- **Permanent Data Storage**: ROM is used to store data that needs to be preserved for the long term. This data is typically in the form of firmware or software that is essential for the operation of a device or computer. Once data is written to ROM, it cannot be easily changed, which is why it's called "read-only."

- **Firmware**: Many electronic devices, such as smartphones, tablets, game consoles, and computer motherboards, have firmware stored in ROM. Firmware is a type of software that provides low-level control and functionality for the hardware. For example, the BIOS (Basic Input/Output System) in a computer's motherboard is often stored in ROM.

- **Boot-up Instructions**: In a computer, the initial instructions that start the boot-up process are often stored in ROM. This is necessary because the computer needs these instructions to begin loading the operating system from other storage devices like hard drives or SSDs.

- **Software Protection**: Some software or data stored in ROM may be copy-protected or locked to prevent unauthorized modifications. This is common in gaming consoles to prevent piracy.

### Types of Read Only Memory

There are various types of ROM, including:

- **Mask ROM (MROM)**: The data is permanently programmed during manufacturing and cannot be changed.
- **Programmable Read-Only Memory (PROM)**: Users or manufacturers can program the data once using a special device. Once programmed, the data is fixed and cannot be altered.
- **Erasable Programmable Read-Only Memory (EPROM)**: Data can be erased and reprogrammed multiple times using ultraviolet light.
- **Electrically Erasable Programmable Read-Only Memory (EEPROM)**: Data can be electrically erased and rewritten, making it more flexible for certain applications.

## Virtual Memory

Computers have a limited amount of physical RAM, which is used to store actively running programs and data. However, the available RAM may not always be sufficient for all the tasks a computer needs to perform. **Virtual memory** extends the available memory by using a portion of the computer's storage devices (typically the hard drive or SSD) as if it were additional RAM. This creates a virtual address space that appears larger than the actual physical RAM.

![Virtual Memory](../../assets/images/system/virtual-memory.png)

The part of the storage device used for virtual memory is often referred to as the "page file" (in Windows) or "swap space" (in Linux). When the physical RAM is fully utilized, less frequently used data and program code are temporarily transferred to the page file.

The operating system manages the transfer of data between the physical RAM and the page file based on the program's needs. Portions of programs or data not actively in use may be swapped in and out of the physical RAM as needed.

While virtual memory provides flexibility, it comes with a performance cost. Accessing data from the physical RAM is much faster than accessing it from the storage device. Therefore, excessive use of virtual memory can lead to slower performance because of the time required to transfer data between RAM and the storage device.

## Cache Memory

In a computer system, there is a hierarchy of memory types, ranging from high-speed, low-capacity memory to slower, higher-capacity memory. This hierarchy includes cache memory, RAM, and secondary storage like hard drives or SSDs.

Cache memory is located closer to the CPU (Central Processing Unit) than RAM. There are typically multiple levels of cache (L1, L2, L3) with L1 being the smallest and fastest, and L3 being larger but slower.

The primary role of cache memory is to store copies of frequently accessed data and instructions from the main memory. Since it is faster than RAM, accessing data from the cache speeds up the overall performance of the computer.

When the CPU needs to access data or instructions, it first checks if the required information is in the cache memory. If it is, this is known as a **cache hit**, and the data can be quickly retrieved. If the data is not in the cache, it results in a **cache miss**, and the CPU needs to fetch the data from the slower main memory.

The cache memory is organized into different levels to balance speed and capacity. L1 cache is the smallest but fastest, residing directly on the CPU. L2 cache is larger but slightly slower, and L3 cache, if present, is larger still but slower compared to L1 and L2.

The size of the cache memory affects its effectiveness. A larger cache can store more data, reducing the likelihood of cache misses. However, larger caches also tend to have longer access times.

Cache management is dynamic, with the system determining which data to keep in the cache based on usage patterns. Frequently accessed data is retained, while less frequently accessed data may be replaced.

The use of cache memory is a key strategy for improving CPU performance. By storing frequently used data closer to the CPU, the processor spends less time waiting for data to be fetched from slower main memory.

## Memory Hierarchy

Each of the different layers or memory work together and form a hierarchy as summarised in the following diagram:

![Hierarchy of Memory](../../assets/images/system/memory-hierarchy.jpg)

## Questions

{{ show_questions(page.title, page.meta.filename) }}
