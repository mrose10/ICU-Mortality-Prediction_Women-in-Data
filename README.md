# WiDS (Women in Data Science) Datathon 2020: ICU Mortality Prediction</h3>

**Can intake data from a patient’s first 24 hours in the Intensive Care Unit (ICU) predict survival?**
<br/>
*The challenge contains data collected from 130,000 hospital ICU across 6 countries and over 200 hospitals by MIT’s GOSSIS (Global Open Source Severity of Illness Score) community initiative. The APACHE model takes vital/physiological data and recodes on a numerical scale and is used to determine patient care. APACHE models were introduced in 1981 (APACHE I)  and have been updated with APACHE II (1985), APACHE III (1991) and APACHE IV (2006) models. These scores can range from 0 - 71 for APACHE II and o to 299 for APACHE III.* 

## 1. Data

[Physionet](https://physionet.org/content/widsdatathon2020/1.0.0/) 


The data consisted of 186 features split across different groupings (shown in the table): demographics (age, ethnicity, hostpital id), vitals (temperature, heart rate), lab tests (lactate, blood gas), apache scores and body systems. Data types included categorical, binary indicators of disease, and lab results (float with  different magnitudes and reanges). 
 
| Descriptors & Test Results    |    APACHE Info        |   
| :----:                        |    :----:            |   
| Identifier            | APACHE covariate     |
| Demographic           | APACHE prediction    |
| vitals                | APACHE comorbidity   |
| labs & labs blood gas | APACHE grouping      |

## 2. Method 

The metric of the competition is the Area Under the Curve/ Receiver Operating Characteristic (AUC ROC) curve. The target variable is mortality, coded in the training data as ‘hospital_death’. As this is a classification task, I will test 3 classifier methods:

* Logistic Regression - the simplest approach to get a feel for the feature importances
* Random Forest - flexible for the different types of data and ensemble voting
* Boosted Trees - boost classification of more difficult samples

The [winning team's](https://www.kaggle.com/c/widsdatathon2020/discussion/133189) AUC score was 91.45, up from an initial commit of 90. 

## 3. EDA

[EDA Notebook](https://github.com/mrose10/WiDs_Datathon_2020/blob/master/notebooks/Load%20Data%20and%20EDA%20.ipynb)

I first looked at the data types and then how much data was available for each patient. Many of the features were empty. This makes sense as data is aggregated across different medical conditions and only some tests are required for some conditions, e.g. not everyone will need invasive gas measurements, and across different times (indicated with 'h1: hour 1' and 'd1: within 24 hours'). 

![percent nan png](https://github.com/mrose10/WiDs_Datathon_2020/blob/master/reports/figures/Screenshot%20Missing%20values.png)

## 4. Feature Engineering and Selection

[Data Cleanup Notebook](https://github.com/mrose10/WiDs_Datathon_2020/blob/master/notebooks/Data_Cleanup.ipynb)

* Demographic, categorical and apache features were kept for initial testing. 

* Many features were highly correlated or even had the same value across different features, like max and min across different times. Features included in the model were collapsed from 'var_h1_min/max' and 'var_d1_min/max' into one variable. 
> * Features were created that indicated whether an invasive test was performed or not, and the labs otherwise collapsed into one variable.
> * A feature was created that indicated whether a patient had any h1 measurement. 

* Not all vitals were included in the intial modeling. Temperature, lactate, bilirubin kept, additional features such as partial oxygen (spo2), systolic and mean blood pressure (sysbp and mbp) should be processed and included to improve fitting. 

* Albumin and creatinine (indicators of kidney function) were transformed in a similar way into the feature ACR and subsequently removed. 

![highly correlated vitals](https://github.com/mrose10/WiDs_Datathon_2020/blob/master/reports/figures/Screenshot%20Vitals%20Correlation.png)




## 5. Model Results

## 6. Model Analysis

## 7. Next Steps

 

## References
<br/>
Lee, M., Raffa, J., Ghassemi, M., Pollard, T., Kalanidhi, S., Badawi, O., Matthys, K., & Celi, L. A. (2020). WiDS (Women in Data Science) Datathon 2020: ICU Mortality Prediction (version 1.0.0). PhysioNet. https://doi.org/10.13026/vc0e-th79.

Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.

Thank you Women in Data for hosting!

## Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
