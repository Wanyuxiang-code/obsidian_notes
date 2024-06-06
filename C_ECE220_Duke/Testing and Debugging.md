---
title: Testing and Debugging
date: 2024-05-27
date modified: 2024-06-06
categories: C_ECE220_Duke
---

## Test

### Idea:

   Testing is to find bugs in the code -> The corner cases should be good testing examples

### Black Box Testing:

   - The tester considers only the expected behavior of the function—not any implementation details—to devise test cases
   - Advantages:
     1. One advantage is that if you have a comprehensive test-suite written before you start, you are unlikely to skimp on testing after you implement your code
     2. By thinking about your corner cases in advance, you are less likely to make mistakes in developing and implementing your algorithm

### Tips:

   1. Test every corner cases
   2. Test every error condition
   3. Test more or less cases
   4. Examine the datatype
   5. Test boundary cases

### White box tests:

   1. Statement coverage:  
      Test whether each statement is executed
   2. Decision coverage:  
      All possible outcomes are execrised. Cover every edge in the control flow graph.
   3. Path coverage:  
      Span all possible valid paths through the control flow graph

### Generating test case:

   1. Based on the algorithms to generate large amount of test cases randomly
   2. Verify: You can improve the confidence by testing the property of your program instead of directly proving your programs.

### Assert:

   There are some invariants during execution. So we can use some assert statement to check whether they can pertain their property or boolean true value. If they dieobey their property, the program will crash down and print the error message.

## Debugging

### Scientific method:

   - Observe a phenomenon -> 
   - Raise a quetion -> 
   - Recursively gather information(assisted by debugger) -> 
   - Form a  hypothesis(testable and actionable) -> 
   - Verify the hypothesis(Construct testcases; Inspect the internal state; Add asserts; Code inspection)

### Intro to GDB 

1. Process:
      1. compile codes with debugging symbols: `gcc -ggdb3`
      2. run gdb inside emacs (ESC x or ALT x)
2. Basic commands in GDB:
      1. start:  
         runs the program and stops when execution enters main
      2. run:  
         runs the program
      3. step:  
         move forward by a line(**go into the function called current line**)
      4. next:  
         advance the program one line of code, but will execute the entire function call
      5. print:  
         evaluates the expression and prints the results  
         print multiple elements from an array: eg. `p arr[0]@length`  
         print will assign the value you want to print to the internal variables named $-  
         **Notice: up and down can switch between different stack frames to see different variables**
      6. display:  
         display the expression's value every time gdb stops and display a prompt
      7. backtrace: lists all of the stack frames
      8. up and down:  
         switch between different stack frames.  
         Especiallly useful when the program stops in a failed assert, you can use up to return to the previous stack frames
      9. info:  
         get information about various aspects of the program.
     10. break:
         - set a breakpoint  
         eg. `break function: line`
         - **Conditional break points**:  
           `break 7 if i==25000` or you also use `cond` to add conditions  
           `cond <break point number> <condition>`
         - info breakpoints(i b): check the current states of break points 
         - `clear <name>` can clear the break points
     11. until and finish:
         - until: causes a loop to execute until it finishes
         - finish: causes execution until the current function returns
     12. watch:  
         set watch points that can have gdb stop when the value of a particular expression changes  
         **Particular useful when examining coping pointer-related problems, if you worry the pointer is a local variable, you can watch the internal variables in gdb**
3. Signals:
   1. SIGSEGV:  
      Indicates a segmentation fault and gdb will stop on the line that this fault happens
   2. SIGABRT:  
      Happens when the program calls abort() or fails an assert
   3. SIGINT:  
      Happens when the program is interrupted.(eg. the user presses Control-c)
