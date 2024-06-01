---
title: MIT missing semester
date created: 星期一, 五月 27日 2024, 11:46:53 中午
date modified: 星期六, 六月 1日 2024, 2:08:35 下午
---


## Lecture1 Shell

1.common command:
   - date
   - echo:
     1.usage: prints out the argument you given and space can separate different arguments
	 2.echo $PATH：present all paths executable
	 which echo: find out which file is executed
   - path related
	 cd: change to another path
	 pwd: see the current path
	 ".." refers to parent directory
	 "." refers to current directory
	 ls: see what is stored in a given directory
   - 
	 cp: copy a file (when copy a folder use -r)
	 mv: move a file
	 mkdir: create a directory
	 touch: create a file
	 cat: display the content of the file
	 rm: delete the file (when delete a folder apply "-r", can apply \*)
	 vim: open a text editor
   - redirect your input and output:
     \< file : rewire you input (**将输入重定向**)
     \> file : rewire your output(**将输出结果重定向**)
     \>> append a file
     \| : take the output of the former as the input of the later( chain programs together)
   - root
     sudo: (super user do)
     permission class:
     owner文件所有者, group用户组, other user其他用户
     chmod: rwx(八进制数字模式)
   - 
2.Basic knowledge
   - path:
     The location of your targeted file, separated by "/" for linux and "\\"for windows 
     / represents root (For windows it might be like C:\\ )
	     1.absolute path and relative path
	     absolute path: begin with root
   - flag and options:
	 flag: begin with "-" can modify the behaviour of the command
     options: flags with values
    >
    >r w x: (read write and execute)different permissions:
    > Above, only the owner is allowed to modify (`w`) the `missing` directory (i.e., add/remove files in it). To enter a directory, a user must have “search” (represented by “execute”: `x`) permissions on that directory (and its parents). To list its contents, a user must have read (`r`) permissions on that directory.





## Lecture2 Version control
1.Data model -> recursive structure
- folders -> trees, files -> blogs
- A direction graph without loops 
- Metadata: every snapshot has metadata including the submission date and the user who submitted it

2.Principle:
Take a snapshot at a certain time, recording all the information

3.Lower level->actual data structure
Notice: The trees, snapshots and blob are just pointers, and hash values are also pointers
- blob : file an array of bytes
- tree: mapping from the filename or the directoryname to the actual content( tree or file)
- snapshots: commits, including parents( an array of previous commits), author and a message
    The actual content of a snapshot is a tree
- objects:
	 The actual content of your repository
- references: map from<strings,strings>
	 With references, you can easily name a certain snapshot.(Without considering the long hash values)
	 The mapping relationship can be changed.
- branch
	 - master: default branch when you initialized a git repository, often refer to the most up-to-date version of your project. Usually it is a pointer to the latest commit.
	 - head: where you currently looking right now


4.git command
- git init
  It can initialize the reposiotry for git.
  And apply "ls .git" you could see the disk area containing objects and references...
- git help
  list the helpful command line
- git status
  check the current status
- git cat-file -p \<hash value\>
	look the what contains in the location that this hash value points
- git add
  Track the file in the next snapshot, if you don't apply "add", the changes will be untracked
  It can employ the staging area and has more flexibility to add commit history
  git add -p \<file\> : track the file by pieces

- git commit -m "information"
  Take a snapshot of the tracked changes, information can inform the readers
  git commit -a: commit all tracked files

- git log
  Visualize  the commit graph
  Powerful arguments: git log --all --graph --decorate

- git checkout
  Help you move around in your version history, moves the head pointer (different bracnches)
  This can help you change your working projects flow

- git diff
  Compare the difference from last commit of a certain file(you can also specify the version by adding arguments)

- git branch:
  - Without an argument: list the current branches
  - Followed by a file name: create a new branch 
  - git branch -vv: detailed information


- git merge:
  A powerful command that can help you merge different versions of snapshots together. Usually, it will merge the branch to your main branch.
   **Notice: If there are versions conflicts between the branches, the programmers should solve this issue**
   
- git remote
  list all the remote repositories that git knows for our local repository
  - git remote add \<name\> \<url\> (If there is only one remote, it is called origin by convention)
  - git push(help your repository interact worth the remote repository)
	 git push \<remote\> \<local branch\>:\<remote branch\>
  -  git branch --set-upstream-to=\<remote\>/\<branch\>
    Create a mapping between your local checking branch to the remote set branch
  - git fetch: retrieving changes to a repository that are present on a remote and getting the changes on your local machine
  - git pull
    Similar to "git fetch" + "git merge"

- git clone
  Clone a copy of repository to your local folder
  git clone \<url\> \<local folder\>
  git clone --shallow : much more faster but no versions history