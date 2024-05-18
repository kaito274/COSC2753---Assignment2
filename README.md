# COSC2753 - Machine Learning 
# Assessment 2 + 3: Group Machine Learning Project

To navigate the project requirements, via [Project Requirement](Machine Learning-COSC2753_2024A_Assignment 2-1.pdf).

---


## Table of Contents


```
.
├── augmentation/
│   ├── beds 
│   ├── dressers
│   └── sofas
├── data/
│   ├── Furniture_Data (*The data of this project available on Canvas/Github to run EDAs)
│   ├── test/bed 
│   ├── train/bed
│   └── val/bed
├── external_resources/
├── images/
├── query_image/
├── .gitignore
├── Machine Learning-COSC2753_2024A_Assignment 2-1.pdf
├── README.md
└── scraping1.py
```

1. `augmentation/`: The folder contains the data using for augmentation process.
2. `data/`: The folder contains all the splitted data for three tasks and raw Furniture Data.
3. `external_resources/`: The folder contains additional materials using for the assessment.
4. `images/`: The folder contains statistic charts of each training model using for evaluation.
5. `query_image: Saving folder for additional images using for prediction of task 2 and 3.
6. `Machine Learning-COSC2753_2024A_Assignment 2-1.pdf`: PDF file for the detail requirements of the assessment.
7. ` `

---


## Using our projects: 
Firstly, clone our repository with the attached link below:

```bash
git clone https://github.com/kaito274/COSC2753---Assignment2.git
```


### Development Environment
Download the packaged using in the project environment with the matched version:
(We suggest that a new python environment in anaconda navigator should be created from 3.6.13 to 3.9 since 3.11 version is not compatible with tensorflow)

```bash
pip install -r requirements.txt
```

### Download raw dataset:
Our additional dataset for this project is available on [Github](https://github.com/DarcieNg/ML-Assignment-2-Dataset). Instruction:
- Direct to project's root directory.
- Remove all existing files in the `data/` folders if anything exists before using the dataset by the command below:

    ```bash
    rm -r ./data/*
    ```
3. Download and **extract contents of** the `.zip` from [Github](https://github.com/DarcieNg/ML-Assignment-2-Dataset) into `data/` folder.

   Moving on, use the [Github](https://github.com/DarcieNg/ML-Assignment-2-Dataset):

    ```bash
    kaggle datasets download -d (path of data) -p ./external_resources/ --unzip
    ```
   
    The folder architecture after download the external dataset should be:
    
    ```
    .
    ├── data/
    │   ├── Furniture_Data (required to run the EDA according to our file path in the code)
    │   ├── test/bed
    │   ├── train/bed
    │   └── val/bed
    │
    ...
    ```
### Using Trained Models


#### Classify Furniture Images


#### Recommend Furniture Images

