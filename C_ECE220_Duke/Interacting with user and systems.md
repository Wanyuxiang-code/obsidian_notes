---
title: Interacting with user and systems
date: 2024-05-27
date modified: 2024-06-06
categories: C_ECE220_Duke
---

## Introduction to operating systems

1. Background  
   Since many operations has to be accomplished with the assistance of hardware, but for most programs they can't directly have access to hardware for safety. In this case, they will take operating system(a lower level software responsible for managing all of the resources on the system) as medium to access the hardware indirecly. The operating systems will check whether the call from the programs is legal.
   
2. Difference between system calls and library calls:  
   System call: transfer control to system  
   Library call: call a function found in library
   
3. Errors from system calls:  
   When a system call fails, it will create a global variable named **errno**(error number) to indicate the reason. We can use **perror** function to print a descriptive message based on the value of erron. Perror can take a string as argument to describe the condition.  
   Example:  
   perror prototype: print message to stderr, it can take an argument as prefix.  
   `void perror (const char* prefix);`

   ```c
   int x = someSystemCall();
   if (x != 0 ){
     perror("The error was: ");
     }
    ```

    ***Notice: When prints out the error messages, take care not to call anything might change erron like some system calls***

## Command Line Arguments

1. Write program to examine command line arguments:  
   Example:  
   `int main(int argc, char ** argv)`  
   **argc**: number of arguments  
   **argv**: argument vector, standing for arguments that were passed in as an array of string. `argv[0]` contains the name of the program  
   Usage: We can examine whether the user has input valid number of arguments and employ these arguments. 
2. The environment pointer:  
   main can also take a third argument: `char ** envp`, which is a pointer to an array of strings containing the values of environment variables.
3. Process creation:  
   <[Process Creation | Coursera](https://www.coursera.org/learn/interacting-system-managing-memory/supplement/ywo87/process-creation)>

## File operation

### Related terminology

1. File descriptor:  
   File descriptors are **small integers which serve as indexes into an array**. The array contains the information about  I/O channel of a given program.
2. I/O channel:  
   It is a channel describing the path of data from input to out. It can be either physical or logical.
3. Streams:
   - An abstraction built on top of file descriptors, which provides **a continuous sequence of bytes including some bufferings**.
   - Usage: **Making a system call is too expensive to just obtain little information, so the stream read more and buffer the rest ultil your program asks for more**.
   - Stream is a pointer to the buffer data structure, with type `FILE*`
4. Default streams:
   - stdin (descriptor0) keyboard
   - stdout (descriptor1) display
   - stderr (descriptor2) display(error)
5. Buffering:  
   Buffering means waiting ultil a certain amount or type of data is available before sending anything or reading extra data in anticipation of future requests for data.(提前读入数据或等待数据积攒到一定量时再传输)

### Opening a file

1. Stream file:  
   Opening a file results in a stream file associated with the file.  
   A stream(noted as FILE * ) is a sequence of data, which can be read and/or written, which can indicate the permission level and path.
2. fopen function:  
   `FILE * fopen(const char * filename, const char * mode);`  
   **filename**: a string that indicates the path name to open. This path can be either absolute path or relative path.  
   **mode**: a string that indicates whether the file should be read/written/creadted...  
   Returns a new stream on success or NULL on failure
3. Typical modes:  
![](https://s2.loli.net/2024/06/01/chtPFJoyNUfIv7r.png)

### Reading a file

1. fgetc:  
   prototype: `int fgetc(FILE * stream);`  
   It is used to read **one character** from the input file once called.  
   It returns an int so that it can return all possible chars, plus a distinct value to indicate that there are no more characters available in the stream—that the end of the file (_EOF_) has been reached.  
   **Notice: we can apply the fact that the assigning operation itself is also an expression that has value of the assigning itself.**  
   Remember **EOF** can serve as a return value to indicate failure!
2. getc:  
   prototype: `int getc(FILE* stream)`  
   It is also used to read a character from the file. But unlike fgetc is a library function, it is preprocessor macro. It takes less time than a function call, but makes the code larger.

   > [!info] Shortcuts with stdin/stdout  
   > reading one character from stdin
> 
   > >int getchar (void);
>
   > write one character to stdout:
>
   > >int putchar (int c);

3. fgets:  
   prototype: `char * fgets(char * str, int size, FILE * stream);`  
   The fgets function is useful when we want to read one line with a maximum length at a time.  
   `char * str`: a pointer to an array in which to store the characters read from the file.  
   `int size`: how much space is available for it to write data into  
   `FILE * stream`: input file  
   The function will return str if it succeeds. It will return NULL either fails or encounters the end of the file.  
   It stops at **the end of the line, or at the end of the input, or exceed the maximum array length**.  
   It is the best way to read inputs by line, better than fscanf which takes the whole string as inputs.
   
4. fread: read **binary** data input from a stream  
   prototype: `size_t fread (void * ptr, size_t size, size_t nitems, FILE *stream);`  
   It is used when we want to read the non-textual data from a file.  
   `void * ptr`: a pointer to data to write. Because it is a void type, it can write any kind of data.  
   `size_t size`: the size of each item  
   `size_t nitems`: how many such items should be read from the stream
5. getchar:  
   It is a shortcut to read one character from stdin.  
   `int getchar (void);`  
   **Don't ever use shortcut for reading a string from stdin. It is a security hazard**

### Writing to Files:

1. fprintf and printf:  
   This function is quite similar to the function `printf` except that it takes an additional argument of type `* FILE` to specify the output location. Return number of characters printed or negative numbers on failure.  
   printf prints the output to **stdout** by default, which is used for output  
   fprintf prints the output to **stderr** by default, which is used for errors
2. fputc, putc and fputs:  
   `int fputc (int c, FILE* stream)`  
   fputc: library function; putc: preprocessor macro  
   Use fputc to write a single character at a time or fputs to write a string without any format conversions.  
   It will return character written(zero-extended from low 8 bits of c) or **EOF** on failure  
   `int fputs (const char*s, FILE* stream);`
3. puts:  
   A short cut to write a string to stdout.  
   `int puts (const char* s);`  
   Notice:**puts adds an end of line sequence(line feed) to the end of the string(fputs does not)**
4. fwrite:  
   It can be used to write **binary output** data.  
   `size_t fwrite(const void * ptr, size_t size, size_t nitems, FILE * stream);`  
   Some errors may be detected later because the C library function will buffer the data to improve the writing and system call efficiency.
5. putchar:  
   `int putchar (int c)`  
   write one character to stdout.

### Use scan/print

1. scanf:  
   `int scanf (const char* format, ...);` reads formatted input from stdin.
2. fscanf: read formatted input from a stream:  
   `int fscanf(FILE *stream, const char* format, ...);`  
   format is the format specifier, remaining argumebnts are as with scanf
3. sscanf: read formatted input from a string  
   `int sscanf (const char* s, const char* format, ...);`
4. printf:  
   `int printf (const char* format, ...);` writes formatted output to stdout
5. fprintf: write formatted output to a stream  
   `int fprintf (FILE* stream, const char* format, ...);`  
   format is the format specifier
6. snprintf: write formatted output to a string:  
   `int snprintf (char* s, size_t size, const char* format, ...);`  
   size is the size of the string

### Closing Files

   fclose:  
   prototype: `int fclose(FILE * stream);`

   - This function can specify which stream to close. Closing the stream sends any buffered write data to the OS and then asks the OS to close the associated file descriptor.
   - The function will return 0 if success or EOF if failure.  
   Failure reason: there are various reasons that the user can't write data like the disk is full. 

### Pipe, Redirect:

prototype: `cmd1 | cmd2`  
We can sue pipe operator to redirect the output of the first file to the input of the second file.  
`<` read stdin from a file  
`>` write stdout to a file  
`>>`append stdout to an existing file  
Use `|&` and `>&` to include stderr

## IO Example

### Writing Variadic Logging Function

```c++
#include<stdarg.h> //include C library function which supports variadic functions
//declare stream variable for the output to store
static FILE* logfile = NULL;
int printlog (const char* fmt, ...)
{
	//our first task is to open the file
	if (NULL == logfile) {
	//open the stream file ,format "a" to indicate append to end of existing file
	logfile = fopen ("the_log", "a");
	if (NULL == logfile){
		return -1;
		}
	}
	//declare a variable argument list using va_list
	va_list args;
	//va_start is a preprocessor macro that starts the variable-length list after the specified argument-in this case, fmt
	va_start (args, fmt);
	//call vfprintf to handle variable arguments
	return vfprintf (logfile, fmt, args);
	//This fucntion will return number of characters printed or a negative value on failure
}
```

### Pyramid Tree I/O Example

Our task:

- write a tree as ASCII
- write a tree as binary
- compare the files
- rebuild a tree from the binary file

```c++
//input: tre structure, the file name to write
//return value: 1 on success, 0 on failure
int32_t write_pyr_tree_ASCII (pyr_tree_t* p, const char* fname)
{
	FILE* out;
	
	if (NULL == (out = fopen(fname, "w"))){
		return 0;
		}
	//start by writing number of nodes to know the size of the array at the beginning
	fprintf (out, "%d\n, p->n_nodes);
	//print each non-leaf node
	int32_t first_leaf = (p->n_nodes + 2) / 4;
	int32_t i;
	for (i = 0; first_leaf > i; i++){
		fprintf(out, "%d %d %d\n", p->node[i].x, p->node[i].y_left), p->node[i].y_right};
	}
	//print leaf node
	for ( ; p->n_nodes >i; i++) {
		fprintf (out, "%d\n", p->node[i].id);
	}
	return (0 == fclose(out));
}
						 
//binary version
int32_t write_pyr_tree_binary (pyr_tree_t* p, const char* fname)
{
	FILE* out;
	
	if (NULL == (out = fopen(fname, "w"))){
		return 0;
		}
	//apply fwrite to write binary data, directly write the node data
	int32_t rval = (1 == fwrite(&p->n_nodes, sizeof(p->n_nodes), 1, out) && p->n_nodes == frite (p->node, sizeof(p->node[0]), p->n_nodes, out));
	fclose (out);
	return rval;
}
```

```c++
//reconstruct a pyramid tree from binary file
pyr_tree_t* read_pyr_tree_binary (const char* fname)
{
	FILE* in; //input stream
	pyr_tree_t* p; //new pyramid tree
	int32_t count; //number of nodes in a file
	if (NULL == (in = fopen(fname, "r")) || 1 != fread (&count, sizeof(count), 1, in)){
		if (NULL != in){
		fclose (in);
		}
	}
	return 0;
	//Allocate space for pyramid tree and node array
	if (NULL == (p = malloc(sizeof(*p))) || NULL == (p->node = malloc(sizeof(p->node[0])*count)))){
		if (NULL != p) free(p);
		fclose(in);
		return NULL;
	}
	//reconstrcuct the tree
	p->n_nodes = count;
	if (p->n_nodes != fread (p->node, sizeof(p->node[0]), p->n_nodes, in)){
		free_pyramid_tree (p);
		fclose (in);
		return NULL;
	}
	fclose (in);
	return p;
}

```

### Counting words in a file