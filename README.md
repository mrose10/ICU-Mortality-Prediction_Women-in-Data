<span style="color: green"> 
**Problem Statement**
 </span>
Can intake data from a patient’s first 24 hours  in the Intensive Care Unit (ICU) predict survival? 
How do ethnicity and gender factor into survival? 

Context
Data was collected from 130,000 hospital ICU across 6 countries and over 200 hospitals by MIT’s GOSSIS (Global Open Source Severity of Illness Score) community initiative. Data includes vitals, demographic information, hospital code and the APACHE score. 

The APACHE model takes vital/physiological data and recodes on a numerical scale and is used to determine patient care. APACHE models were introduced in 1981 (APACHE I)  and have been updated with APACHE II (1985), APACHE III (1991) and APACHE IV (2006) models. These scores can range from 0 - 71 for APACHE II and o to 299 for APACHE III. 

Criteria for Success
I will use the same metrics as the Datathon competition and evaluate based on the Area Under the Curve/ Receiver Operating Characteristic (AUC ROC) curve. The target variable is mortality, coded in the training data as ‘hospital_death’. 

Scope of solution space
My approach is to start with 1 - 3 main features and build a logistic regression model. I will add features as needed to improve the fit.  Other solutions would be to examine  the use of decision trees. My constraints are working with data that is reported from certain hospitals, and missing demographic and funding data of the hospitals themselves. Some factors could be standardized according to ICU equipment and staff availability and percentage of population served. 

Stakeholders
In keeping with Springboard’s metrics, the stakeholders could be two groups. First, the hospital staff in deciding who to treat. The second, policy makers. If the data show strong correlation with certain demographic factors, such as ethnicity, this could lead to further studies into why this is the case.  

 References 
Lee, M., Raffa, J., Ghassemi, M., Pollard, T., Kalanidhi, S., Badawi, O., Matthys, K., & Celi, L. A. (2020). WiDS (Women in Data Science) Datathon 2020: ICU Mortality Prediction (version 1.0.0). PhysioNet. https://doi.org/10.13026/vc0e-th79.

Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
