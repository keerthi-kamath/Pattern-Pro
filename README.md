# Pattern-Pro




  
# How to Contribute?

*Follow the following steps in the same order to contribute to our project.*

<br/>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-description">Project Description</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a>
          <ol>
            <li><a href="#forking">Forking</a></li>
            <li><a href="#cloning">Cloning</a></li>
          </ol>
        </li>
        <li><a href="#development">Development</a>
           <ol>
            <li><a href="#checkout">Checkout</a></li>
            <li><a href="#staging">Staging</a></li>
            <li><a href="#commiting">Commiting</a></li>
            <li><a href="#pushing">Pushing</a></li>
          </ol>
        </li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing / Adding features</a></li>
  </ol>
</details>

<br />

<!-- About Project -->

## ***About the Project***
<br />

#### **Project Description:**
A game built using python that can be played by more than 2 people. The game involves the players to guess the pattern given by the system. In order to defeat the computer, all the players meed to guess the pattern 2 times in a row. 

<br/>
<br/>

<!-- Getting started -->

## ***Getting Started***
<br />

### **Installation** 
<br />

1. ### Forking
  
      Fork the Repository with the help of the <b>FORK</b> button in the top right corner of the repository. 

2. ### Cloning

      1. Once Forked, click on the Green colored <b>CODE</b> button
      2. Make sure you have <b>https</b> selected and copy the url shown.
      3. Open GitBash on your system and use ```cd``` command to navigate to the desktop or whichever folder you want to clone the repository to.



  <br />

  <br />

### **Development**
<br/>

3. ### Checkout

      Branches are unique features of Version Control Systems that allow you to add/remove features and test them individually, without affecting the main code. This also enables multiple contributors to work on a single piece of code together, working on multiple features.

  Initially to create a new branch, you will have to use the ```-b``` flag. 

  ```bash
  git checkout -b your-branch-name
  ```


  Checking out to it the next time.

  ```bash
  git checkout your-branch-name
  ```

4. ### Editing
  
    Work on the features that you believe will make this application better.

5. ### Staging

    There are two main ways of stagin files. 

    1. Staging one file or two files: you can do this by the ```git add``` command followed the names of the files you want to stage separated by a space.

    Example: 

    ```bash
    git add file1.html file2.txt file3.c file4.py
    ```

    As you may have guessed, this is very tedious especially if you have many files that you want to stage together or if you dont exactly remember the number of files you changed. For this, you can use the much easy and reccomended command:

    ```bash
    git add .
    ```
    The period means all. It will stage all files you changed.

6. ### Commiting


```bash
git commit -m "your commit message here"
```

7. ### Pushing


    ```bash
    git push origin your-branch-name
    ``` 



## Contributing 

*Any changes/improvements, bug fixes to this repository are highly encouraged and welcome.*

Improvement pull requests are always welcome. For major changes, please open an issue first to discuss what you would like to change in the project.
