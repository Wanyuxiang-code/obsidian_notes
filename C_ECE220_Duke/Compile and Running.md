---
title: Compile and Running
date created: 星期一, 五月 27日 2024, 11:46:53 中午
date modified: 星期一, 六月 3日 2024, 10:56:45 晚上
categories: C_ECE220_Duke
---

****## Compile

### Overview：

   Translate the programming language into a machine-executable format. The complier will take your source code as input and writes out the executable file.

### Compilation Process:

   Apply `man` for manual page to see the basic information, and you can apply `man man` to see the details of manual command  
   Notice: `man -k` for keyword searching              
   ![compile](https://s2.loli.net/2024/06/01/l63dyF8eaQ4MocG.png)

   1. Process:  
     Combine the source code with any header files it includes  
     **Header file format**:  
     `#include< >` for the standard C header files  
     `#include "myHeader.h"` for own header files  
     It generally contains: function prototypes, macro definitions and type declaration  
     - Function prototypes:  
       Declare the name, return type, and parameter types of a function.  
     - Macros:  
       `#define pi 3.14` `#define Success 0`  
       Macro definition will tell the processor to change the label you have defined to the set value.  
       It boasts the advantages of better readability, better portability and convenience for constants.  
       **Notice : macro can also take arguments, nut it is different with function calls. Because the storage of function call will be in stack, but the macro just operates by replacing the texts before the program runs**  
       `#define SQUARE(x) x*x`
   2. Actual Compiler:  
      Transform the preprocess code into the assembly code.  
      Tip:
      - Complier may be confused to output some irrelevant messages
      - Debug line by line
   3. Assembly:  
      The assembler translates the assembly code into an object file which can be executed.  
      The object file contains the machine-executable instructions for the source file but not yet a complete program because it may refer some undefined functions.  
      `gcc -c` can stop after it assemble the source code(It can help to produce several individual files)  
      `gcc -o` can change the default .o file name.
   4. Linking:  
      Linking the program takes one or more object files and combines them with various libraries and produce the actual executable files.  
      Linker errors:  
      First make sure you did not try to name two different functions with the same name. Next, make sure you did not include any files twice on the compilation command line. Finally, make sure you do not `#include` a _.c_ file—only header files—and that you only include function _prototypes_ in the header file, not the function’s definition  
      Apply `-l` to link the outer library

### Basics of compiling gcc

   1. compile with some flags:  
     `gcc -Wall -Werror -pedantic -std=gnu99`
   2. Make: tool for build large programs
      1. Reason: It takes lots of time to recompile large real program -> To reduce the repetitive workload we just need to recompile the changed file and link them together -> tedious manual work -> apply make to manage automatically
      2. Make interface:
         - Input: makefile
         - Components of makefile: Targets, Dependencies, Rules to make the target
	  3. Process:  
	     Start from checking whether a target tree is up-to-date, and do the according necessary rebuilding.
	  4. Example:

	     ```c
	     myProgram: onefile.o anotherfile.o
		     gcc -o myProgram onefile.o anotherfile.o
		 onefile.o: onefile.c oneherader.h
			 gcc -std=gnu99 -pedantic -Wall -c onefile.c
		 anotherfile.o: anotherfile.c anotherHeader.h
			 gcc -std=gnu99 -pedantic -Wall -c anotherfile.c
           ```

           Rule: first specify the target, list prerequisite(用冒号分隔), a new line to rebuild the target(**begin with a TAB**)  
           Specify a particular target to build(if not the first one will be the default)

	  5. Variables:  
	     Simplify the complier options by setting a variable

	     ```c
		 CFLAGS=-std=gnu99 -pedantic -Wall
		 gcc $(CFLAGS) -c onefile.c 
		  ```

		  Apply $() to include the variables

	  6. Clean:  
	     A poney target intended to remove the compiled program, all object files, all editor backups (*.c~ .h~*), and any other files that you might consider to be cluttery  
	     Example:  
	     `.PHONY: clean`  
	     `clean:`  
		     `rm -f myProgram *.o *.c~ *.h~`
	  7.  Generic Rules:  
	     Represent something with %  
	     $<: the name of the first prerequisite

	     ```c
	     CFLAGS=-std=gnu99 -pedantic -Wall
	     myProgram: onefile.o anotherfile.o
		     gcc -o myProgram onefile.o anotherfile.o
		 %.o: %.c
			 gcc $(CFLAGS) -c $<
		 .PHONY: clean
		 clean:
			 rm -f myProgram *.o *.c~ *.h~
		 depend:
			 makedepend anotherfile.c onefile.c
		 /*same as above, depend is also a phony target */
		 onefile.o: oneheader.h
		 anotherfile: anotherheader.h
	     ```

	     make -p: explore the built-in rules  
	     make -j: do parallelizing computation  
	  8.  Built-in functions:  
	     Automatically compute the set of .cfiles in the current directories and generate the list of target object files from that list.  
	     `SRCS=$(wildcard *.c)`  
	     generate the list of .c files in the current directory  
	     `OBJS=$(patsubst %.c,%.o,$(SRCS))`  
	     replace the .c endings with .o endings

	     

## Running

### Running the program

1. ./ to indicate the location of your program:  
   Since the current path is not included in the PATH, we have to add ./ to indicate the location of our program
2. Complier options:
   - .o : specify the output file name  
     Example: `gcc -o myprogram myprogram.c` will produce an executable file named myprogram instead of myprogram.out
   - -std=gnu99:  
     specify the complier should use C99 with GNU extensions
   - -Wall:  
     requests the complier issue warnings for a wide range
   - -Werror:  
     treat warnings as errors

 