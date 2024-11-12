---
title: 2024-05-27-Containers and Iterators
date: 2024-05-27
date modified: 2024-06-06
categories: C_ECE220_Duke
---

## Containers

### Concept

>Container is a **data structure containing other data structures** with **specific access capabilities.**
>
>Example: linked lists, heaps, dynamically-sized array

### Optimization of a list structure

#### Method 1: Create a list element structure with a data pointer(void*)

![](https://s2.loli.net/2024/06/01/9xVWUMPSvKpZJfy.png)  
Pros: Write the list code once  
Cons: Requires more memory access

#### Method2: Struct a data structure with first field serves as a pointer

This method better represents the idea of a container, which considers pack up a pointer structure into the main data structure and link them together.  
Example: create a cyclic doubly-linked list with a sentinel

```c
//Create a double list structure
typedef struct double_list_t{
	double_list_t* prev;
	double_list_t* next;
	}double_list_t;
//List initilalization
void dl_init (double_list_t* head)
{
	head->prev = head->next = head;
}
//List node insertion, we need two pointer pointing to the head and insertion element
//Can be assisted with a picture for understanding
void list_insert (double_list_t* head, double_list_t* el)
{
	elt->next = head->next;
	elt->prev = head;
	head->next->prev = elt;
	head->next = elt;
}
//List node removal, we just need the pointer to the removal element
void list_removal (double_list_t* elt){
	elt->prev->next = elt->next;
	elt->next->prev = elt->prev;
//Find the first list node
void* dl_first (double_list_t* head){
	return (head == head->next ? NULL : head->next);
}
```

> [!Warning]  
> double_list_t must be First in structure Thing  
> Or &my_thing.dl will not pointing to the beginning of the data structure, **we can't convert double_list_t* to struct thing_t*(need to subtract unknow amount from the pointer)**.

## Iterators

### Aim

We want to develop an iterator to tranverse a list of things and implement some operations including **find specific things, remove a set of things, free a set of things".**

### Callback Function

> [!Callback Function]  
> A function is passed as an argument to another function, allowing the called function to call the passed function under certain conditions

Callback function adapts the concept of function pointer, which is usually used to achieve modular and flexible code.It is a higher level of abstraction which can expose less information about details.  
More about function pointer: [[Use of Pointers]]

### Method: Adopt a Callback function

```c
//Design the return value of callback, which should inform what to do next
//Apply enumeration to impart numbers with significant meanings
typedef enum{
	DL_CONTINUE,
	DL_STOP_AND_RETURN, //Return this thing
	DL_REMOVE_AND_CONTINUE, //Remove this thing and continue
	DL_REMOVE_AND_STOP, 
	DL_FREE_AND_CONTINUE
} dl_execute_resopnse_t;

//Definition for callback function. It defines the passing function pointer, the parameters to accept, and the return value type(dl_execute_response_t)
typedef dl_execute_response_t (*dl_execute_func_t) (void* dl, void* arg);

//Iteration function signature, its return value is a pointer to a thing. arg contains all arguments passed to all callback invocations
void* dl_excute_on_all (double_list_t* head, dl_execute_func_t func, void* arg){
	//declare some local variables
	//hold the return result of callback function
	dl_execute_response_t result; 
	double_list_t* dl; //current element
	double_list_t* remove; //element to remove
	
	//Implement iteration
	for (dl = head->next; dl != head; dl = dl->next){
		switch ((result = func (dl, arg))){
		case DL_REMOVE_AND_STOP: dl_remove (dl);
		case DL_STOP_AND_RETURN: return dl;
		case DL_REMOVE_AND_CONTINUE:
		case DL_FREE_AND_CONTINUE:
			remove = dl;
			dl = dl->prev;
			dl_remove (remove);
			if (DL_FREE_AND_CONTINUE == result) free (remove);
			break;
		default: break;
		}
	}
	return NULL; //if loop ends, return NULL	
}
```