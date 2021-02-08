# Verifying explainability of a deep learning tissue classifier trained on RNA-seq data
Melvyn Yap<sup>1^</sup>, Rebecca L. Johnston<sup>2^</sup>, Helena Foley<sup>1^</sup>, Samual MacDonald<sup>1</sup>, Olga Kondrashova<sup>2</sup>, Khoa Tran<sup>1,2,3</sup>, Katia Nones<sup>2</sup>, Lambros T. Koufariotis<sup>2</sup>, Cameron Bean<sup>1</sup>, John V. Pearson<sup>2</sup>, Maciej Trzaskowski<sup>1*</sup>, Nicola Waddell<sup>2*</sup>

<sup>1</sup> Max Kelsen, Brisbane, QLD, Australia  
<sup>2</sup> QIMR Berghofer Medical Research Institute, Brisbane, QLD, Australia  
<sup>3</sup> Queensland University of Technology, Brisbane, QLD, Australia  
  
<sup>*</sup> Correspondence to nic.waddell@qimrberghofer.edu.au and maciej.trzaskowski@maxkelsen.com, these authors jointly supervised work and 
<sup>^</sup> Authors contributed equally to the work 

Original paper: https://www.nature.com/articles/s41598-021-81773-9


## Abstract
For complex machine learning (ML) algorithms to gain widespread acceptance in decision making, we must be able to identify the features driving the predictions. Explainability models allow transparency of ML algorithms, however their reliability within high-dimensional data is unclear. 

To test the reliability of the explainability model SHapley Additive exPlanations (SHAP), we developed a convolutional neural network to predict tissue classification from Genotype-Tissue Expression (GTEx) RNA-seq data representing 16,651 samples from 47 tissues. 

Our classifier achieved an average F1 score of 96.1% on held-out GTEx samples. Using SHAP values, we identified the 2423 most discriminatory genes, of which 98.6% were also identified by differential expression analysis across all tissues. The SHAP genes reflected expected biological processes involved in tissue differentiation and function. 

Moreover, SHAP genes clustered tissue types with superior performance when compared to all genes, genes detected by differential expression analysis, or random genes. We demonstrate the utility and reliability of SHAP to explain a deep learning model and highlight the strengths of applying ML to transcriptome data.



Directory Structure
-------------------
```
├── README.md               <- Top level README file
│ 
├── data                
│   ├── raw                 
│   ├── interim             
│   ├── processed 
│   ├── gene_lists
│   └── shap
│
├── fig_edit
├── models                  
├── figures                             
├── notebooks                                        
│   ├── 1.0-gtex-preprocessing.ipynb
│   ├── 1.1-smote.ipynb
│   ├── 2.0-cnn.ipynb
│   ├── 3.0-shap.ipynb
│   ├── 4.1-cluster-analysis.ipynb
│   ├── 4.2-cluster-analysis.ipynb
|   └── 5.0-independent-dataset-analysis.ipynb
│
├── src                     
│   ├── helpers             <- Directory containing helper functions/files for project-wide use
│   ├── data                <- Scripts for downloading/generating data
│   ├── preprocessing       <- Scripts for preprocessing
│   ├── feature_engineering <- Scripts for engineering features
│   └── modelling           <- Scripts for training/evaluating models
│   
├── requirements.txt        <- File containing dependencies for pip installation
│
├── setup.py                <- Setup.py file for packaging
│
├── meta.yaml               <- YAML file for building conda package 
│
└── configure.sh            <- Shell script to auto configure both setup.py and meta.yaml
```

Figure Sources
-------------------
| Figure | Source |
| --- | --- |
| 1a | fig_edit/fig1a.pptx |
| 1b | fig_edit/fig1b.pptx |
| 2a | notebooks/2.0-cnn.ipynb, (R code not in this repo) |
| 2b | notebooks/2.0-cnn.ipynb, fig_edit/fig2b.xlsx |
| 3a | notebooks/3.0-shap.ipynb, (R code not in this repo) |
| 3b | notebooks/3.0-shap.ipynb, (R code not in this repo) |
| 3c | (R code not in this repo) |
| 3d | (R code not in this repo) |
| 4a | fig_edit/fig4a.pptx |
| 4b | (R code not in this repo) |
| 4c | (R code not in this repo) |
| 4d | notebooks/4.1-cluster-analysis.ipynb |
| S1a | fig_edit/suppfig1a.pptx |
| S1b | fig_edit/suppfig1b.pptx |
| S2a | fig_edit/suppfig2a.xlsx |
| S2b | (R code not in this repo) |
| S3a | notebooks/4.2-cluster-analysis.ipynb |
| S3b | notebooks/5.0-independent-dataset-analysis.ipynb |
| S4 | (R code not in this repo) |
| S5a | (R code not in this repo) |
| S5b | (R code not in this repo) |
| S6a | (R code not in this repo) |
| S6b | (R code not in this repo) |
| S7 | notebooks/4.2-cluster-analysis.ipynb |
| S8 | notebooks/4.2-cluster-analysis.ipynb |


## Contact
For contact of follow up please enquire at
hello@maxkelsen.com 

## Max Kelsen Research Lab
Max Kelsen is an Australian artificial intelligence and software engineering agency, delivering solutions across a wide range of industries, including medical, government, retail, financial services and insurance.

However, our research laboratory focuses on three areas critical to the advancement of human health, technology and Artificial Intelligence (AI) itself: 
+ algorithmic safety, 
+ genomics, 
+ and quantum computing. 

With long academic traditions, we carry a rigour and a deep understanding of hypothesis testing to deliver research projects with the highest scientific integrity, evident by the growing number of peer-reviewed scientific publications.  

We see scientific rigour and algorithmic safety of paramount importance, because careless deployment of AI in critical sectors, such as healthcare can negatively affect lives.

[Max Kelsen](https://maxkelsen.com)