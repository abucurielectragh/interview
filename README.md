# Retviews final interview
Hello, and congratulations for reaching this far.

For this stage of the process, you will have to build a functional spider (a script that will take the data from a certain website)

**Requirements:**
- conda (https://conda.io/projects/conda/en/latest/user-guide/install/index.html) - used to install scrapy
- git (https://git-scm.com/downloads) - used to clone the project
- pycharm (https://www.jetbrains.com/pycharm/) - the IDE you will write code (you can use any other editor you want, but we recommand pycharm)

Be aware to include git/conda to ENV PATH

After all requirements are done, you will have to install scrapy:

Write this command into shell (cmd/git/powershell etc) `conda install scrapy`

Clone the project into your desired directory:

Write this command into shell (cmd/git/powershell etc) 

`git clone https://github.com/retviewsinterviu/final_interviu.git`

## All set! Lets go!

Open the project on pycharm and start coding.

## Helpfull tools

Run the script:  `scrapy crawl myspider`

Additional settings:

- `-s CLOSESPIDER_ITEMCOUNT=x` will stop when x requests are made
- `-o output_file` will print the data scraped to output_file (extension must be `json`)
- in `spiders/` you will find an example already made, called `marisfrolg.py`. this can be used as example



### GOOD LUCK!
