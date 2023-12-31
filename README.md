# MONU-VIRT-DATA-PT-02-2023-U-LOLC

## Introduction

This is the Monash Data Bootcamp Class Repository

```mermaid
flowchart TD
Welcome([Welcome])
```

## Repository structure 

Please read this section to understand how to navigate the repository. 

The contents of the repository is broken down as follows: 

```
root 
|__ 01-Lesson
    |__ <week_num>-<topic_title>
        |__ <lesson_num>
            |__<slide.pdf>
            |__ Activities
                |__<activity_num>-<activity_type>_<activity_title>
                    |__ README.md
                    |__ solved/*
                    |__ unsolved/*
```

- `week_num`: refers to the week number e.g. 01, 02, 03. 
- `topic_title`: refers to the week's topic e.g. Excel, VBA-Scripting, Python, etc...
- `lesson_num`: refers to the lesson number i.e. 1 or 2 or 3. This also corresponds to the day of the week i.e. 1 = Monday, 2 = Tuesday, 3 = Thursday
- `activity_num` : refers to the activity number e.g. 01, 02, 03 and so on.
- `activity_type`: refers to the activity type i.e. [`ins`] instructor, [`stu`] student, [`evr`] everyone, [`par`] partner
- `activity_title`: refers to the activity title e.g. ExcelPlayground, PivotTables, etc...
- `*`: denotes all files in the folder

Example: 
```
root 
|__ 01-Lesson
    |__ 01-Excel
        |__ 3
            |__ aus_1.3 Excel Plotting.pdf
            |__ Activities
                |__ 02-Ins_BasicCharting
                    |__ README.md
                    |__ solved/*
                    |__ unsolved/*
                |__ 03-Stu_LineAndBar
                    |__ README.md
                    |__ solved/*
                    |__ unsolved/*
                |__ 04-Ins_ScatterPlot
                    |__ solved
    |__ 02-VBA-Scripting
        |__ 1
            |__ aus_2.1 Fundamentals of Programming with VBA.pdf
            |__ Images
            |__ Activities
                |__ 01-Ins_HelloWorld
                    |__ README.md
                    |__ unsolved/*
```

**Each activity contains the following folders: **
- `README.md`: contains instruction or denoting which actvitiy the instructor does demo.
- `solved`: contains the solved solutions for the activity. [`stu`] solved solutions will be uploaded at the end of each class. 
- `unsolved`: contains the unsolved starting code for the activity. This folder may be empty at times if the code is to be created from scratch. 

**Please Note:** 
- Some activity might not have unsolved or solved folder depending on what we will be doing. Some acivity might have additional folder such as `Resources` or `Images`. 
- Your weekly homework can be found in https://courses.bootcampspot.com/
