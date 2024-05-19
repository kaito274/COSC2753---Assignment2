# COSC2753 - Machine Learning 
# Assessment 2 + 3: Group Machine Learning Project



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
│   └── additional csv files
├── external_resources/
├── feature_extractor_for_all_data/
│   ├── variables/
│   ├── keras_metadata.pb
│   └── saved_model.pb
├── images/
├── query_image/
├── utils/
├── .gitignore
├── Machine Learning-COSC2753_2024A_Assignment 2-1.pdf
├── README.md
├── notebooks for the three tasks
├── scraping.py
└── scraping1.py
```

1. `augmentation/`: The folder contains the data using for augmentation process.
2. `data/`: The folder contains all the splitted data for three tasks and raw Furniture Data.
3. `external_resources/`: The folder contains additional materials using for the assessment.
4. `images/`: The folder contains statistic charts of each training model using for evaluation.
5. `query_image: Saving folder for additional images using for prediction of task 2 and 3.
6. `Machine Learning-COSC2753_2024A_Assignment 2-1.pdf`: PDF file for the detail requirements of the assessment.
7. `utils/`: The folder contains additional figures.
8. `Task 1 CNN`: The notebook of CNN model for task 1.
9. `Task 1 EDA & Preprocess`: The notebook of Exploratory Data Analysis for task 1.
10. `Task 1 ResNet50`: The notebook of ResNet model for task 1.
11. `Task 2 CNN_features`: The notebook of CNN model for task 2.
12. `Task 2 K-means-Clustering`: The notebook of K-means clustering model for task 2.
13. `Task 3 EDA & Preprocess`: The notebook of Exploratory Data Analysis for task 3.
14. `Task 3 CNN`: The notebook of CNN model for task 3.
15. `Task 3 RecommendStyles`: The notebook of recommend style for task 3.

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
    github datasets download -d (https://github.com/DarcieNg/ML-Assignment-2-Dataset) -p ./data/ --unzip
    ```
   
    The folder architecture after download the external dataset should be:
    
    ```
    .
    ├── data/
    │   ├── Furniture_Data (required to run the EDA according to our file path in the code)
    │   └── additional csv files

    ...
    ```
### Using final Trained Models

**Task 1** : 
- CNN model (`model4.h5`)

**Task 2** 
- CNN with similarity calculator

**Task 3**
- VGG16 with Multi Label Binarizer (`model1_Task3.h5`)

            
#### Classify Furniture Images


#### Recommend Furniture Images

