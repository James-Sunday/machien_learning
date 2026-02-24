# Iris Classification Project

## Overview

This project implements an end-to-end Machine Learning workflow for classifying iris flower species based on physical measurements.

## Dataset

The Iris dataset contains:

* 150 samples
* 4 numerical features
* 3 flower species

Features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Target:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

## Workflow

1. Data visualization and analysis
2. Train-test split
3. Model comparison using cross-validation
4. Feature scaling using Pipeline
5. Logistic Regression training
6. Model evaluation
7. Model saving using Joblib`



## Model Pipeline

```
StandardScaler → LinearDiscriminantAnalysis
```

---

## Result

Test Accuracy: **100%**

