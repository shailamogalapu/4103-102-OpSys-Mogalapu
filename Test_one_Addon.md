##Multi*
##Define the following and give examples of each.
###1.MULTI-TASKING:
A mode of operation that provides for the concurrent performance or interleaved execution of two or more computer tasks.
General definition: An Operating System is said to have Multi-tasking capability if it allows the user to perform one or more tasks at a time. Where task can be defined as an operation of an application program.

Example: when we are able to work on the internet(open some pages) and also do some work on the system like word/excel/programming and so on, it can be called as Multi-tasking.

###2.MULTI-PROGRAMMING:
Multiprogramming is a mode of operation that provides for the interleaved execution of two or more computer programs by a single processor.
General definition: for utilizing/maximize the usage of CPU time, it will make sure that the programs that are in the waiting state and are ready to execute can be given CPU time. That is, several programs can run on the processor at the same time.

Example: if we are editing a file, listening to the music, downloading some files and running some tests all these programs appear to be done simultaneously, but in the background the OS is providing different times for the program to run.

###3.MULTI-PROCESSING:
A mode of operation that provides for parallel processing by two or more processors of a multiprocessor.
It can be referred to as the system’s ability to support/perform more than one process at a time.
Or the management of multiple processes within multiprocessor.

Example: if we are using word, listening music, downloading files and running an anti-virus program, all these will be divided between different processors and will be performed as process at a time simultaneously on different CPU’s.

###4.MULTI-THREADED:
Multithreading  is a technique in which a process, executing an application, is divided into threads that can run concurrently, where thread is the dispatchable unit of work which Is created by a process/ a lightweight process.
Multithreading is the ability of a program or an operating system process to manage its use by more than one user at a time and to even manage multiple requests by the same user without having to have multiple copies of the programming running in the computer.

Example: database server that listens for and processes numerous client requests.

##Review Questions From Chapters 3
##1.What is an instruction trace?
An instruction trace can be defined as the continuous recorded data which is related to the CPU instruction execution, having the OS code and the context switches.
##2.What common events lead to the creation of a process?
Four common events lead to the process creation. They are as follows:
1.New batch Job: 
	the OS is provided with a batch job control stream.
2.Interactive log-on:
	a user at a terminal logs on to the system
3.created by the OS to provide a service
4.spawned by existing process

##3.What does it mean to preempt a process?
    To preempt a process means to reclaim a resources(processor) from a process before 
    the process has finished using it. 
    The process is executing and could continue to execute, but is preempted 
    so that another process can be executed.
    
##4.What is swapping and what is its purpose?
    Swapping involves moving part or all of a process from main memory to disk. 
    Its purpose is to maximize the number of processes in the system, we swap a process
    from the ready state to the ready suspend state.
    
##5.Why does Figure 3.9b have two blocked states?
If a process in the running state requires more memory, then at least one blocked process can be swapped out of memory onto disk. 
The transition can also be made for the blocked process if there are ready processes available, and the OS determines that the ready process requires more main memory to maintain adequate performance.
A blocked process that is suspended becomes blocked suspend. To obtain more memory we have two blocked states so that memory can be obtained by using secondary memory like disks. When the process is in blocked state we can simply place that onto the disk
if we require more space for bring in more blocked processes and later they can be brought back whenever possible.

##6.List four characteristics of a suspended process.
  1. The process is not immediately available for execution. 
  2. The process may or may not be waiting on an event. If it is, this blocked condition is
  independent of the suspend condition, and occurrence of the blocking event does not enable the process
  to be executed immediately. 
  3. The process was placed in a suspended state by an agent: either itself, a parent process, or the OS,
  for the purpose of preventing its execution.   
4.The process may not be removed from this state until the agent explicitly orders the removal.  

##7.List three general categories of information in a process control block.
	Process identification: id of this process, id of the parent process and user id. \\
	Processor state information: program counter, status registers, and general-purpose registers. 
	Process control information: 
    a. Scheduling & state information: process state, priority, scheduling-related information 
    (amount of time waiting and time being executed), event (identity of event the process is awaiting before can be resumed) 
    b. Data structuring: a process may be linked to other process in a queue. 
    c. Memory management: include pointers to page tables that describe the virtual memory assigned
    d. Resource ownership and utilization
    e. Process privileges: e.g. the memory that may be accessed, types of instructions that may be executed and
    the use of system utilities and services 
    f. Interprocess communication

##8.Why are two modes (user and kernel) needed?
	Processes in kernel mode can access both: kernel and user addresses.
	Processes in user mode can access their own instructions and data but not kernel instructions
	and data (or those of other processes).
User mode avoids direct access to the hardware and ensures isolated execution of each process, 
a system call from the user program leads to a switch to kernel mode. Various privileged instructions
can be run only when in kernel mode. So we require two modes.

##9.What is the difference between an interrupt and a trap?
A trap is an exception in a user process. It's caused by division by zero or invalid memory access.
It's also the usual way to invoke a kernel routine (a system call) because those run with a higher 
priority than user code. Handling is synchronous. In a sense they are active most of the time, 
the code expects the trap to happen and relies on this fact.
An interrupt is something generated by the hardware. These are asynchronous or passive 
since the interrupt handler has to wait for them to happen eventually.

##10.Give three examples of an interrupt
Generally there are three types of Interrupts 

1) clock Interrupt
2) I/O Interrupt.
3) memory fault.

##11.What is the difference between a mode switch and a process switch?
  process switch may occur any time that the OS has gained control from the currently running process where as a mode switch may occur without changing the state of the process that is currently in the Running state.


















