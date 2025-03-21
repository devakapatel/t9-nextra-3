# Unit 2

## <mark> 1) What is statistics? How is it used in Data Science?

### **1. What is Statistics?**

**Statistics** is the branch of mathematics that deals with **collecting, analyzing, interpreting, and presenting** numerical data. It helps in understanding patterns, relationships, and trends in data.

#### **Key Components of Statistics:**

- **Descriptive Statistics** → Summarizes data using measures like mean, median, variance, etc.
- **Inferential Statistics** → Makes predictions or inferences about a population using sample data.

### **2. How is Statistics Used in Data Science?**

Statistics is the backbone of **Data Science**, helping in data analysis, modeling, and decision-making.

#### **A. Data Understanding & Exploration**

- **Descriptive statistics** (mean, median, mode) summarize datasets.
- **Data visualization** (histograms, box plots) reveal patterns and outliers.

#### **B. Data Cleaning & Preprocessing**

- Identifies missing values, outliers, and inconsistent data.
- **Normal distribution & standardization** help scale data for machine learning.

#### **C. Hypothesis Testing & Inferential Analysis**

- Uses **t-tests, chi-square tests, and ANOVA** to validate assumptions.
- Helps determine whether observed patterns are statistically significant.

#### **D. Machine Learning & Predictive Modeling**

- **Regression Analysis** (e.g., Linear Regression) predicts numerical outcomes.
- **Probability & Bayes' Theorem** (e.g., Naïve Bayes Classifier) are used in classification tasks.

#### **E. Performance Evaluation of Models**

- **Error metrics** like Mean Squared Error (MSE), Root Mean Squared Error (RMSE) for regression models.
- **Confusion matrix, Precision, Recall, and F1-score** for classification models.

### **Conclusion**

Statistics is **crucial in Data Science** for understanding data, making predictions, validating models, and ensuring insights are reliable. Mastering statistical concepts helps data scientists build **accurate and efficient** machine learning models.

## <mark> 2) Differentiate between Descriptive and Inferential Statistics with examples. </mark>

### **Descriptive vs. Inferential Statistics**

| Feature        | **Descriptive Statistics**                                                                                                                                         | **Inferential Statistics**                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definition** | Summarizes and describes data.                                                                                                                                     | Makes predictions and generalizations about a population using a sample.                                                                                                                                          |
| **Purpose**    | Organizes, visualizes, and simplifies raw data.                                                                                                                    | Draws conclusions and makes inferences about a larger group.                                                                                                                                                      |
| **Techniques** | Measures of central tendency (mean, median, mode), dispersion (variance, standard deviation), frequency distributions, data visualization (histograms, box plots). | Hypothesis testing (t-test, chi-square test), confidence intervals, regression analysis, probability distributions.                                                                                               |
| **Data Used**  | Works with the **entire dataset** (population or sample).                                                                                                          | Uses a **sample** to infer insights about the **entire population**.                                                                                                                                              |
| **Example**    | - Finding the **average height** of students in a class. <br> - Calculating the **percentage of students** scoring above 80 in an exam.                            | - Predicting the **average height of all students in a city** based on a sample. <br> - Determining if a **new drug is effective** by testing on a small group and generalizing results to the entire population. |

### **Example for Better Understanding**

💡 **Descriptive Statistics Example:**  
A company surveys **100 employees** and finds that the **average salary** is **$50,000**. This is a direct summary of the dataset.

💡 **Inferential Statistics Example:**  
The company wants to **predict the average salary** of **all employees in the industry** using this **sample of 100 employees**. Inferential statistics help estimate this.

### **Conclusion**

- **Descriptive Statistics** helps understand data by summarizing and organizing it.
- **Inferential Statistics** helps make predictions and generalizations from sample data to a larger population.  
  Both are essential in **Data Science** for analyzing trends and making data-driven decisions.

## <mark> 3) Explain the concepts of Population and Sample in statistics. Why is sampling important? </mark>

### **1. Population vs. Sample in Statistics**

| **Concept**         | **Population**                                                                          | **Sample**                                                                      |
| ------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Definition**      | The **entire group** of individuals or data points under study.                         | A **subset** of the population used for analysis.                               |
| **Size**            | **Larger**, often too vast to study completely.                                         | **Smaller**, selected from the population.                                      |
| **Representation**  | Includes **all** possible observations.                                                 | Represents a **portion** of the population.                                     |
| **Example**         | **All students** in a country.                                                          | A **random group of 500 students** selected for a survey.                       |
| **Analysis Method** | Uses **parameters** (e.g., population mean **μ**, population standard deviation **σ**). | Uses **statistics** (e.g., sample mean **x̄**, sample standard deviation **s**). |

### **2. Why is Sampling Important?**

Studying an entire **population** is often **impractical** due to time, cost, and effort. **Sampling** helps by:

✅ **Reducing Cost & Time** → Collecting data from a sample is faster and more affordable.  
✅ **Better Feasibility** → Allows analysis when population size is too large.  
✅ **Statistical Inference** → Enables **generalization** of findings to the entire population.  
✅ **Higher Accuracy** → Proper sampling techniques ensure reliable results with minimal bias.

### **3. Example of Sampling in Data Science**

A company wants to analyze customer satisfaction for **millions of customers**. Instead of surveying all, they collect responses from a **random sample of 1,000 customers** and infer results for the entire customer base.

📌 **Key Sampling Methods:**

- **Random Sampling** → Every individual has an equal chance of selection.
- **Stratified Sampling** → Population is divided into groups, and samples are taken proportionally.
- **Systematic Sampling** → Every **k-th** individual is chosen.

### **Conclusion**

- **Population** is the complete dataset, while **sample** is a smaller subset used for study.
- **Sampling is crucial** for making predictions about a population efficiently, without analyzing every individual.
- In **Data Science**, sampling techniques ensure accurate and scalable models.

## <mark> 4) What are the different types of variables in statistics? Give examples. </mark>

### **Types of Variables in Statistics**

In statistics, variables are characteristics or properties that can take different values. They are classified into **Qualitative (Categorical)** and **Quantitative (Numerical)** variables.

### **1. Qualitative (Categorical) Variables**

These represent **categories** or labels without numerical meaning.

| Type        | Description                                                  | Example                                                                                                  |
| ----------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Nominal** | Categories with no inherent order.                           | - Eye color (**Brown, Blue, Green**) <br> - Blood type (**A, B, AB, O**)                                 |
| **Ordinal** | Categories with a meaningful order, but no fixed difference. | - Education level (**Primary, Secondary, College**) <br> - Customer satisfaction (**Low, Medium, High**) |

### **2. Quantitative (Numerical) Variables**

These represent **measurable** quantities and have numerical values.

| Type           | Description                                            | Example                                                                                                  |
| -------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Discrete**   | Whole numbers, countable values.                       | - Number of students in a class (**30, 35, 40**) <br> - Number of cars in a parking lot (**10, 20, 50**) |
| **Continuous** | Can take any value within a range, including decimals. | - Height of a person (**5.7 feet, 6.2 feet**) <br> - Temperature (**23.5°C, 30.8°C**)                    |

### **Key Differences**

- **Categorical variables** classify data into groups (e.g., gender: Male/Female).
- **Numerical variables** involve measurable quantities (e.g., weight: 70 kg).

📌 **Example:**  
A survey collects the following data:

- **Name:** John (_Nominal_)
- **Age:** 25 years (_Discrete_)
- **Height:** 5.8 feet (_Continuous_)
- **Education Level:** Bachelor’s Degree (_Ordinal_)

### **Conclusion**

Understanding variable types helps in **choosing the right statistical analysis methods** and **building accurate models in Data Science**.

## <mark> 5) Define Measures of Central Tendency. Why is it important in data science? Explain Mean, Median, and Mode with examples. </mark>

### **1. What are Measures of Central Tendency?**

**Measures of Central Tendency** are statistical metrics that describe the center or typical value of a dataset. The three main measures are:

- **Mean** (Average)
- **Median** (Middle Value)
- **Mode** (Most Frequent Value)

### **2. Importance in Data Science**

✅ **Summarizes Data:** Helps in understanding data distribution.  
✅ **Comparison & Decision-Making:** Assists in comparing datasets.  
✅ **Modeling & Predictions:** Used in statistical and machine learning models.  
✅ **Outlier Detection:** Identifies skewness and anomalies in data.

### **3. Explanation of Mean, Median, and Mode with Examples**

#### **A. Mean (Arithmetic Average)**

- The sum of all values divided by the number of values.
- **Formula:**
  $$
  Mean = \frac{\sum X}{N}
  $$
- **Example:**  
  Dataset: **[10, 20, 30, 40, 50]**
  $$
  Mean = \frac{10+20+30+40+50}{5} = 30
  $$
- **Use Case:** Used when data is **normally distributed** (e.g., average income, test scores).

#### **B. Median (Middle Value)**

- The middle value when data is arranged in ascending order.
- **Steps to Calculate:**
  - If **odd** number of elements: Median = Middle value.
  - If **even** number of elements: Median = Average of two middle values.
- **Example:**  
  Dataset: **[5, 10, 15, 20, 25]** (Odd count) → **Median = 15**  
  Dataset: **[5, 10, 15, 20]** (Even count) → **Median = (10+15)/2 = 12.5**
- **Use Case:** Preferred when data has **outliers** (e.g., house prices, salaries).

#### **C. Mode (Most Frequent Value)**

- The most repeated value in a dataset.
- **Example:**  
  Dataset: **[2, 3, 3, 4, 5, 5, 5, 6]**
  - Mode = **5** (since it appears most frequently).
- **Use Case:** Useful in **categorical data analysis** (e.g., most preferred product, most common disease).

### **4. Comparison & When to Use**

| Measure    | Best Used When                               | Affected by Outliers? |
| ---------- | -------------------------------------------- | --------------------- |
| **Mean**   | Data is normally distributed                 | ✅ Yes                |
| **Median** | Data has skewness or extreme values          | ❌ No                 |
| **Mode**   | Categorical or repeated values are important | ❌ No                 |

### **5. Conclusion**

**Mean, Median, and Mode** are essential statistical tools in Data Science. They help **summarize datasets, identify trends, and guide decision-making**, making them crucial in **business analytics, research, and machine learning**.

## <mark> 6) What are Measures of Variability? Discuss Range, Variance, and Standard Deviation. </mark>

### **1. What are Measures of Variability?**

**Measures of Variability** describe how **spread out** or **dispersed** data points are in a dataset. They indicate how much the values differ from the central tendency (mean, median, mode).

### **2. Importance in Data Science**

✅ **Understanding Data Distribution** – Helps in analyzing data spread.  
✅ **Detecting Outliers** – Identifies extreme values affecting predictions.  
✅ **Improving Model Performance** – Variability helps in feature selection and normalization.  
✅ **Risk Assessment** – Higher variability indicates greater uncertainty in data.

### **3. Key Measures of Variability**

#### **A. Range**

- The **simplest measure** of dispersion.
- **Formula:**
  $$
  Range = \text{Maximum Value} - \text{Minimum Value}
  $$
- **Example:**  
  Dataset: **[10, 20, 30, 40, 50]**
  $$
  Range = 50 - 10 = 40
  $$
- **Use Case:** Quick overview of spread, but sensitive to outliers.

#### **B. Variance (σ² or s²)**

- Measures **how far** each data point is from the mean.
- **Formula for Population Variance (σ²):**
  $$
  \sigma^2 = \frac{\sum (X_i - \mu)^2}{N}
  $$
- **Formula for Sample Variance (s²):**
  $$
  s^2 = \frac{\sum (X_i - \bar{X})^2}{n-1}
  $$
- **Example:**  
  Dataset: **[5, 10, 15]** (Mean = 10)
  $$
  \text{Variance} = \frac{(5-10)^2 + (10-10)^2 + (15-10)^2}{3-1} = \frac{25+0+25}{2} = 25
  $$
- **Use Case:** Helps understand variability, but **squared units make interpretation difficult**.

#### **C. Standard Deviation (σ or s)**

- **Square root of variance**, giving spread in the **same unit as data**.
- **Formula:**
  $$
  \sigma = \sqrt{\sigma^2}, \quad s = \sqrt{s^2}
  $$
- **Example (Using Variance from Above):**
  $$
  \sigma = \sqrt{25} = 5
  $$
- **Use Case:**
  - A **low** standard deviation means data points are **close to the mean**.
  - A **high** standard deviation means data is **widely spread**.

### **4. Comparison Table**

| Measure                | Description                                 | Sensitivity to Outliers |
| ---------------------- | ------------------------------------------- | ----------------------- |
| **Range**              | Difference between max & min                | ✅ High                 |
| **Variance**           | Average squared deviations from mean        | ✅ High                 |
| **Standard Deviation** | Square root of variance (same unit as data) | ✅ High                 |

### **5. Conclusion**

Measures of Variability provide insight into **data spread**, essential for **statistical analysis, risk assessment, and machine learning models**. **Standard deviation** is the most commonly used metric due to its interpretability in real-world scenarios.

## <mark> 7) Define Coefficient of Variance (CV) and explain its significance. </mark>

### **1. What is the Coefficient of Variation (CV)?**

The **Coefficient of Variation (CV)** is a **relative measure of dispersion** that compares the standard deviation to the mean. It helps assess the consistency and variability of data across different datasets, even if they have different units or scales.

- **Formula:**

  $$
  CV = \left( \frac{\sigma}{\mu} \right) \times 100
  $$

  Where:

  - $ \sigma $ = Standard Deviation
  - $ \mu $ = Mean

- **Expressed as a Percentage (%)** to make comparisons easier.

### **2. Significance of Coefficient of Variation**

✅ **Comparison Across Different Datasets:** CV allows comparison of variability between datasets with different units or scales.  
✅ **Risk Assessment:** In finance, a lower CV indicates a more stable investment, while a higher CV suggests higher risk.  
✅ **Quality Control:** In manufacturing, a **low CV** means **consistent** product quality, while a **high CV** signals **variability** in production.  
✅ **Machine Learning & Data Science:** Helps normalize features and understand the reliability of data.

### **3. Example of CV Calculation**

#### **Scenario:** Comparing test score consistency in two classes.

| Class | Mean Score ($\mu$) | Standard Deviation ($\sigma$) | CV (%)                                 |
| ----- | ------------------ | ----------------------------- | -------------------------------------- |
| **A** | 80                 | 5                             | $ \frac{5}{80} \times 100 = 6.25\% $   |
| **B** | 75                 | 10                            | $ \frac{10}{75} \times 100 = 13.33\% $ |

💡 **Interpretation:**

- **Class A** has a lower CV (6.25%), meaning scores are more consistent.
- **Class B** has a higher CV (13.33%), indicating more variability in scores.

### **4. When to Use CV?**

- **Best for comparing variability** when datasets have different units or magnitudes.
- **Not suitable** when the mean is **close to zero**, as it leads to high CV values that are misleading.

### **5. Conclusion**

The **Coefficient of Variation (CV)** is a powerful statistical tool for comparing **relative variability** in different datasets. It is widely used in **finance, economics, manufacturing, and machine learning** to assess consistency and stability.

## <mark> 8) What is Skewness? How does it indicate the shape of a distribution? </mark>

### **1. What is Skewness?**

**Skewness** is a statistical measure that describes the **asymmetry** of a dataset's distribution around its mean. It indicates whether the data is **symmetrically distributed** or **skewed** to one side.

- **Positive Skewness (Right-Skewed)** → Tail extends toward higher values.
- **Negative Skewness (Left-Skewed)** → Tail extends toward lower values.
- **Zero Skewness (Symmetric Distribution)** → Data is evenly spread around the mean.

### **2. How Skewness Indicates the Shape of a Distribution**

#### **A. Symmetric Distribution (Skewness ≈ 0)**

- **Mean ≈ Median ≈ Mode**
- **Shape:** Bell-shaped (Normal Distribution).
- **Example:** Heights of people in a population.

#### **B. Positively Skewed (Right-Skewed) (Skewness > 0)**

- **Mean > Median > Mode**
- **Shape:** Long right tail, more low values.
- **Example:** Income distribution (few high earners pull the mean up).

#### **C. Negatively Skewed (Left-Skewed) (Skewness < 0)**

- **Mean < Median < Mode**
- **Shape:** Long left tail, more high values.
- **Example:** Exam scores (most students score high, few score very low).

### **3. Skewness Formula**

$$
Skewness = \frac{n}{(n-1)(n-2)} \sum \left( \frac{X_i - \bar{X}}{\sigma} \right)^3
$$

Where:

- $ X_i $ = Individual data points
- $ \bar{X} $ = Mean
- $ \sigma $ = Standard Deviation
- $ n $ = Number of observations

📌 **Easier Calculation in Python:**

```python
import scipy.stats as stats
skewness = stats.skew(data)
```

### **4. Why is Skewness Important in Data Science?**

✅ **Influences Model Selection** – Many statistical tests assume normality.  
✅ **Affects Mean & Median Relationship** – Helps understand central tendency.  
✅ **Improves Decision-Making** – Essential in finance, risk analysis, and data preprocessing.  
✅ **Detects Data Anomalies** – Helps identify extreme values and distribution shape.

### **5. Conclusion**

Skewness helps in **understanding data distribution**, detecting **biases**, and making **better statistical and machine learning decisions**. **Right-skewed** distributions have long right tails, **left-skewed** have long left tails, and **zero-skewness** indicates symmetry.

## <mark> 9) What is Kurtosis? How does it describe the characteristics of a probability distribution? </mark>

### **1. What is Kurtosis?**

**Kurtosis** is a statistical measure that describes the **"tailedness"** or **peakiness** of a probability distribution. It indicates how heavily the tails of a distribution differ from a **normal distribution**.

### **2. Types of Kurtosis & Their Characteristics**

| **Kurtosis Type**                           | **Value** | **Characteristics**                                                     | **Example**                                     |
| ------------------------------------------- | --------- | ----------------------------------------------------------------------- | ----------------------------------------------- |
| **Mesokurtic (Normal Distribution)**        | ≈ 3       | - Moderate tails and peak. <br> - Similar to a normal distribution.     | Standard normal distribution (e.g., IQ scores). |
| **Leptokurtic (Heavy-Tailed Distribution)** | > 3       | - Higher peak, **fatter tails**. <br> - More extreme values (outliers). | Stock market returns (high volatility).         |
| **Platykurtic (Light-Tailed Distribution)** | < 3       | - Lower peak, **thinner tails**. <br> - Fewer extreme values.           | Uniform distribution (e.g., dice rolls).        |

📌 **Formula for Kurtosis:**

$$
Kurtosis = \frac{\sum (X_i - \bar{X})^4}{n \cdot \sigma^4}
$$

Where:

- $ X_i $ = Data values
- $ \bar{X} $ = Mean
- $ \sigma $ = Standard deviation
- $ n $ = Number of observations

📌 **Python Code to Calculate Kurtosis:**

```python
import scipy.stats as stats
kurtosis_value = stats.kurtosis(data)
print(kurtosis_value)
```

### **3. How Kurtosis Describes a Probability Distribution**

- **Tails** → Higher kurtosis means **more extreme values (outliers)**.
- **Peak** → Leptokurtic distributions have **sharper peaks**, while platykurtic distributions are **flatter**.
- **Risk Analysis** → Used in finance to measure **market crashes and rare events**.

### **4. Importance of Kurtosis in Data Science**

✅ **Outlier Detection** → High kurtosis indicates the presence of extreme values.  
✅ **Risk & Financial Modeling** → Used in stock market analysis to predict crashes.  
✅ **Quality Control & Reliability** → Detects unusual variations in manufacturing.  
✅ **Improving Machine Learning Models** → Helps in preprocessing data to handle outliers.

### **5. Conclusion**

Kurtosis helps in understanding **distribution shape**, **outlier impact**, and **risk assessment** in various fields like **finance, quality control, and machine learning**. **Leptokurtic** distributions have **extreme values**, while **platykurtic** distributions are **more uniform**.

## <mark> 10) What is the Normal Distribution, and why is it important in statistics? </mark>

### **1. What is Normal Distribution?**

The **Normal Distribution**, also called the **Gaussian Distribution**, is a **symmetrical, bell-shaped** probability distribution where most data points cluster around the mean.

#### **Key Characteristics:**

✅ **Symmetrical** → Mean, median, and mode are equal.  
✅ **Bell-Shaped Curve** → Majority of values lie close to the center.  
✅ **Defined by Mean (μ) & Standard Deviation (σ)** →

- **68%** of data falls within **1σ** of the mean.
- **95%** falls within **2σ**.
- **99.7%** falls within **3σ** (**Empirical Rule**).

📌 **Mathematical Formula:**

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

Where:

- $ \mu $ = Mean
- $ \sigma $ = Standard deviation

### **2. Importance of Normal Distribution in Statistics**

✅ **Basis for Statistical Inference**

- Many **hypothesis tests** (e.g., t-test, Z-test) assume normality.
- Used in **confidence intervals** & **probability predictions**.

✅ **Central Limit Theorem (CLT)**

- States that **sample means** follow a normal distribution **even if the population is not normally distributed**, given a large enough sample size.

✅ **Machine Learning & Data Science**

- Many models (e.g., Linear Regression) assume normality for optimal performance.
- Helps in **data preprocessing** (e.g., standardization).

✅ **Real-Life Applications**

- **Finance:** Stock market returns often follow a normal distribution.
- **Medicine:** Human height, blood pressure, IQ scores follow normal distribution.
- **Quality Control:** Manufacturing defects follow a normal pattern.

### **3. Example: Normal Distribution in Python**

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate data
data = np.random.normal(loc=50, scale=10, size=1000)

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')

# Plot normal curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, 50, 10)
plt.plot(x, p, 'k', linewidth=2)

plt.title("Normal Distribution Curve")
plt.show()
```

### **4. Conclusion**

The **Normal Distribution** is fundamental in statistics and data science. Its **symmetry, predictability, and real-world applicability** make it essential for **statistical modeling, hypothesis testing, and decision-making** across various fields.

## <mark> 11) Explain Hypothesis Testing and its importance in statistics. </mark>

### **1. What is Hypothesis Testing?**

**Hypothesis Testing** is a statistical method used to **make decisions or inferences** about a population based on sample data. It helps determine whether an observed effect is **real** or due to **random chance**.

✅ **Compares Two Hypotheses:**

- **Null Hypothesis ($H_0$)** → Assumes no effect or no difference.
- **Alternative Hypothesis ($H_A$)** → Suggests a significant effect or difference.

### **2. Steps in Hypothesis Testing**

1️⃣ **State the Hypotheses**

- **$H_0$** (Null Hypothesis): There is no difference/effect.
- **$H_A$** (Alternative Hypothesis): There is a significant difference/effect.

2️⃣ **Set Significance Level ($\alpha$)**

- Commonly used values: **0.05 (5%)** or **0.01 (1%)**.
- It represents the probability of **rejecting $H_0$ when it is true** (Type I Error).

3️⃣ **Choose a Test Statistic**

- **Z-Test** (for large samples, known variance).
- **T-Test** (for small samples, unknown variance).
- **Chi-Square Test** (for categorical data).

4️⃣ **Calculate the Test Statistic & P-value**

- The **p-value** measures the probability of observing the result if $H_0$ is true.

5️⃣ **Compare P-value with $\alpha$**

- If **p-value ≤ $\alpha$** → Reject $H_0$ (**Significant result**).
- If **p-value > $\alpha$** → Fail to reject $H_0$ (**No significant result**).

### **3. Importance of Hypothesis Testing in Statistics**

✅ **Decision-Making** → Used in research, business, and medicine to make data-driven decisions.  
✅ **Validates Assumptions** → Helps check if a claim about a population is statistically valid.  
✅ **Risk Management** → Reduces uncertainty in financial markets, A/B testing, and clinical trials.  
✅ **Scientific Research** → Used to test theories in psychology, biology, and economics.

### **4. Example of Hypothesis Testing**

💡 **Scenario:** A company claims their new drug increases recovery rates by 10%. We test this by comparing the recovery rates of 100 patients.

- **$H_0$**: The drug has no effect.
- **$H_A$**: The drug improves recovery rates.
- Conduct a **T-test** and obtain a **p-value = 0.03**.
- Since **p-value < 0.05**, we **reject $H_0$** and conclude the drug is effective.

### **5. Conclusion**

Hypothesis Testing is a powerful statistical tool used to **validate assumptions, guide decision-making, and reduce uncertainty** in various fields like **healthcare, finance, and machine learning**.

## <mark> 12) What is the Central Limit Theorem (CLT)? Why is it important in inferential statistics? </mark>

### **1. What is the Central Limit Theorem (CLT)?**

The **Central Limit Theorem (CLT)** states that, **regardless of the population’s original distribution**, the **sampling distribution of the sample mean** will approach a **normal distribution** as the sample size increases (**n ≥ 30**).

✅ **Key Points of CLT:**

- The **mean** of the sample means approximates the **population mean**.
- The **standard deviation** of the sample means is called the **Standard Error (SE)**:
  $$
  SE = \frac{\sigma}{\sqrt{n}}
  $$
- Larger sample sizes ($ n $) result in a **tighter, more normal distribution**.

### **2. Why is CLT Important in Inferential Statistics?**

✅ **Allows Statistical Inference**

- Enables us to **make predictions** about a population using a **sample**.

✅ **Supports Hypothesis Testing**

- Justifies using **t-tests, Z-tests, and confidence intervals**, even if data is not normally distributed.

✅ **Used in Machine Learning**

- Ensures **model assumptions hold**, especially in regression and classification tasks.

✅ **Real-World Applications**

- **Polling & Surveys** → Predict election results from a sample.
- **Quality Control** → Test product quality using small samples.

### **3. Example of CLT in Action**

📌 **Scenario:** A factory produces **metal rods** with an unknown length distribution.

- **Population Mean ($\mu$)** = 50 cm
- **Population Standard Deviation ($\sigma$)** = 10 cm
- If we take **samples of size $ n = 40 $** multiple times:
  - The sample means will form a **normal distribution** centered at **50 cm**.
  - The standard error will be:
    $$
    SE = \frac{10}{\sqrt{40}} = 1.58
    $$

### **4. Conclusion**

The **Central Limit Theorem (CLT)** is a **fundamental concept in inferential statistics** that enables us to **estimate population parameters, perform hypothesis tests, and make predictions** based on sample data. It is widely used in **research, business, and machine learning**.

## <mark> 13) What is a Confidence Interval? How is it calculated? </mark>

### **1. What is a Confidence Interval (CI)?**

A **Confidence Interval (CI)** is a range of values that estimates a population parameter (like the mean) with a certain level of confidence. It provides an **interval estimate** instead of a single point estimate, accounting for variability in data.

✅ **Key Points:**

- Expressed as:
  $$
  (\text{Lower Bound}, \text{Upper Bound})
  $$
- A **95% confidence interval** means that **95 out of 100** times, the true population parameter will fall within this range.
- **Wider CI** → More uncertainty; **Narrower CI** → Higher precision.

### **2. How is a Confidence Interval Calculated?**

#### **Formula for CI (when population standard deviation $\sigma$ is known, large sample $n > 30$)**

$$
CI = \bar{X} \pm Z\_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}
$$

Where:

- $ \bar{X} $ = Sample Mean
- $ Z\_{\alpha/2} $ = Z-score for confidence level (e.g., 1.96 for 95%)
- $ \sigma $ = Population Standard Deviation
- $ n $ = Sample Size

#### **Formula for CI (when population standard deviation is unknown, small sample $ n < 30 $)**

$$
CI = \bar{X} \pm t\_{\alpha/2, df} \times \frac{s}{\sqrt{n}}
$$

Where:

- $ t\_{\alpha/2, df} $ = t-score from **t-distribution** (depends on degrees of freedom $df = n-1$)
- $ s $ = Sample Standard Deviation

### **3. Example Calculation (95% CI, Large Sample, Known $\sigma$)**

📌 **Scenario:** A sample of **n = 100** students has an **average height** of **170 cm** with a **standard deviation** of **15 cm**.  
Find the **95% confidence interval** for the population mean height.

🔹 **Z-score for 95% CI** → $ Z\_{0.025} = 1.96 $

🔹 **CI Calculation:**

$$
CI = 170 \pm (1.96 \times \frac{15}{\sqrt{100}})
$$

$$
CI = 170 \pm (1.96 \times 1.5)
$$

$$
CI = 170 \pm 2.94
$$

$$
CI = (167.06, 172.94)
$$

🔹 **Interpretation:** We are **95% confident** that the true population mean height lies between **167.06 cm and 172.94 cm**.

### **4. Importance of Confidence Intervals in Statistics**

✅ **Estimates Population Parameters** → Provides a range instead of a single point estimate.  
✅ **Helps in Decision-Making** → Used in medicine, business, and research to assess reliability.  
✅ **Supports Hypothesis Testing** → If the CI **excludes** a certain value, it can indicate statistical significance.

### **5. Conclusion**

A **Confidence Interval (CI)** gives a **range of values** where the population parameter is likely to fall, considering sampling variability. It is crucial for **statistical inference, risk assessment, and hypothesis testing** in Data Science.

## <mark> 14) What is a t-test? Explain its applications with examples. </mark>

### **1. What is a t-test?**

A **t-test** is a statistical test used to **compare the means** of one or two groups to determine if they are significantly different from each other. It is used when:  
✅ The **sample size is small** ($ n < 30 $).  
✅ The **population standard deviation ($\sigma$) is unknown**.  
✅ The data follows a **normal distribution\*\* (or approximately normal).

### **2. Types of t-tests & Their Applications**

| **Type**                                      | **Purpose**                                                      | **Example Application**                                                                                                        |
| --------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **1. One-Sample t-test**                      | Compares the mean of a single sample to a known population mean. | A company claims the average battery life of a phone is 10 hours. A sample of 15 phones is tested to see if the claim is true. |
| **2. Two-Sample t-test (Independent t-test)** | Compares the means of two independent groups.                    | Testing if male and female students have different average test scores.                                                        |
| **3. Paired t-test (Dependent t-test)**       | Compares means from the same group before and after a change.    | Measuring the effect of a new diet plan by comparing weights before and after following the diet.                              |

### **3. Formula for t-test**

$$
t = \frac{\bar{X}\_1 - \bar{X}\_2}{\frac{s}{\sqrt{n}}}
$$

Where:

- $ \bar{X} $ = Sample mean
- $ s $ = Sample standard deviation
- $ n $ = Sample size

### **4. Example: Independent t-test in Python**

📌 **Scenario:** A researcher wants to check if **two different teaching methods** lead to different student performance.

```python
import scipy.stats as stats

# Sample data: Test scores of two groups
group1 = [85, 90, 78, 92, 88]
group2 = [80, 83, 77, 85, 82]

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

print(f"T-statistic: {t_stat}, P-value: {p_value}")

# Decision
if p_value < 0.05:
    print("Significant difference in teaching methods.")
else:
    print("No significant difference in teaching methods.")
```

### **5. Importance of t-tests in Data Science**

✅ **A/B Testing** → Comparing website versions to measure effectiveness.  
✅ **Medical Research** → Checking drug effectiveness before & after treatment.  
✅ **Quality Control** → Ensuring product consistency across different batches.  
✅ **Business Analytics** → Evaluating customer satisfaction between different stores.

### **6. Conclusion**

A **t-test** helps determine if **mean differences** between groups are statistically significant. It is widely used in **research, business, and machine learning** for **hypothesis testing and decision-making**.

## <mark> 15) Differentiate between Type I and Type II errors in hypothesis testing. </mark>

### **Type I vs. Type II Errors in Hypothesis Testing**

| **Error Type**                     | **Definition**                                 | **Meaning**                                  | **Example**                                                  | **Probability**                                                     |
| ---------------------------------- | ---------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------- |
| **Type I Error (False Positive)**  | Rejecting a **true** null hypothesis ($H_0$).  | Detecting an effect that **does not** exist. | A medical test wrongly diagnosing a healthy person as sick.  | **Significance level ($\alpha$)**, usually 5% (0.05).               |
| **Type II Error (False Negative)** | Failing to reject a **false** null hypothesis. | Missing an effect that **actually** exists.  | A medical test failing to detect a disease in a sick person. | **Beta ($\beta$)**, related to **statistical power** ($1 - \beta$). |

### **1. Explanation with an Example**

💡 **Scenario:** Testing a new drug’s effectiveness.

- **$H_0$**: The drug has **no effect**.
- **$H_A$**: The drug is **effective**.

✅ **Type I Error (False Positive):**

- We **reject $H_0$** (claim the drug works) **when it actually doesn’t**.
- **Consequence:** Approving an ineffective drug → Waste of resources, health risks.

✅ **Type II Error (False Negative):**

- We **fail to reject $H_0$** (conclude no effect) **when the drug actually works**.
- **Consequence:** A useful drug is not approved → Missed opportunity for treatment.

### **2. How to Reduce These Errors?**

🔹 **Lowering Type I Error ($\alpha$)** → Use a stricter significance level (e.g., 0.01 instead of 0.05).  
🔹 **Reducing Type II Error ($\beta$)** → Increase **sample size** or **statistical power**.

### **3. Conclusion**

- **Type I Error (False Positive):** Detects a false effect (**too cautious**).
- **Type II Error (False Negative):** Misses a real effect (**too lenient**).
- **Trade-off:** Lowering one increases the other, so balance is needed in hypothesis testing.

## <mark> 16) The number of points scored by two teams in a hockey match is given below. With the help of Coefficient of Variation, determine which team is more consistent.

| **No. of Points Scored**    | 0   | 1   | 2   | 3   | 4   | 5   |
| --------------------------- | --- | --- | --- | --- | --- | --- |
| **No. of Matches (Team A)** | 20  | 5   | 4   | 10  | 1   | 2   |
| **No. of Matches (Team B)** | 7   | 15  | 10  | 3   | 2   | 5   |

</mark>

**Step 1: Calculate the Mean**

For each team, the mean is given by:

$$
\mu = \frac{\sum (\text{Points} \times \text{Frequency})}{\sum \text{Frequency}}
$$

- **Team A:**

  $$
  \mu_A = \frac{(0\times20) + (1\times5) + (2\times4) + (3\times10) + (4\times1) + (5\times2)}{20+5+4+10+1+2} = \frac{57}{42} \approx 1.36
  $$

- **Team B:**
  $$
  \mu_B = \frac{(0\times7) + (1\times15) + (2\times10) + (3\times3) + (4\times2) + (5\times5)}{7+15+10+3+2+5} = \frac{77}{42} \approx 1.83
  $$

**Step 2: Calculate the Standard Deviation**

Standard deviation measures how spread out the points are around the mean. It is calculated as:

$$
\sigma = \sqrt{\frac{\sum f (X - \mu)^2}{\sum f}}
$$

- **Team A Calculations:**

  | Points ($X$) | Frequency ($f$) | $X-\mu_A$          | $(X-\mu_A)^2$          | $f \times (X-\mu_A)^2$  |
  | ------------ | --------------- | ------------------ | ---------------------- | ----------------------- |
  | 0            | 20              | $0 - 1.36 = -1.36$ | $1.36^2 \approx 1.85$  | $20 \times 1.85 = 37.0$ |
  | 1            | 5               | $1 - 1.36 = -0.36$ | $0.36^2 \approx 0.13$  | $5 \times 0.13 = 0.65$  |
  | 2            | 4               | $2 - 1.36 = 0.64$  | $0.64^2 \approx 0.41$  | $4 \times 0.41 = 1.64$  |
  | 3            | 10              | $3 - 1.36 = 1.64$  | $1.64^2 \approx 2.69$  | $10 \times 2.69 = 26.9$ |
  | 4            | 1               | $4 - 1.36 = 2.64$  | $2.64^2 \approx 6.97$  | $1 \times 6.97 = 7.0$   |
  | 5            | 2               | $5 - 1.36 = 3.64$  | $3.64^2 \approx 13.25$ | $2 \times 13.25 = 26.5$ |

  Sum of weighted squared deviations ≈ $37.0 + 0.65 + 1.64 + 26.9 + 7.0 + 26.5 \approx 99.69$

  Variance for Team A:

  $$
  \sigma_A^2 = \frac{99.69}{42} \approx 2.37 \quad \Rightarrow \quad \sigma_A \approx \sqrt{2.37} \approx 1.54
  $$

- **Team B Calculations:**

  | Points ($X$) | Frequency ($f$) | $X-\mu_B$          | $(X-\mu_B)^2$          | $f \times (X-\mu_B)^2$   |
  | ------------ | --------------- | ------------------ | ---------------------- | ------------------------ |
  | 0            | 7               | $0 - 1.83 = -1.83$ | $1.83^2 \approx 3.36$  | $7 \times 3.36 = 23.52$  |
  | 1            | 15              | $1 - 1.83 = -0.83$ | $0.83^2 \approx 0.69$  | $15 \times 0.69 = 10.35$ |
  | 2            | 10              | $2 - 1.83 = 0.17$  | $0.17^2 \approx 0.03$  | $10 \times 0.03 = 0.30$  |
  | 3            | 3               | $3 - 1.83 = 1.17$  | $1.17^2 \approx 1.37$  | $3 \times 1.37 = 4.11$   |
  | 4            | 2               | $4 - 1.83 = 2.17$  | $2.17^2 \approx 4.71$  | $2 \times 4.71 = 9.42$   |
  | 5            | 5               | $5 - 1.83 = 3.17$  | $3.17^2 \approx 10.06$ | $5 \times 10.06 = 50.30$ |

  Sum of weighted squared deviations ≈ $23.52 + 10.35 + 0.30 + 4.11 + 9.42 + 50.30 \approx 97.0$ (rounded)

  Variance for Team B:

  $$
  \sigma_B^2 = \frac{97.0}{42} \approx 2.31 \quad \Rightarrow \quad \sigma_B \approx \sqrt{2.31} \approx 1.52
  $$

**Step 3: Calculate the Coefficient of Variation (CV)**

The CV is given by:

$$
CV = \left(\frac{\sigma}{\mu}\right) \times 100\%
$$

- **Team A:**

  $$
  CV_A = \left(\frac{1.54}{1.36}\right) \times 100 \approx 113.5\%
  $$

- **Team B:**
  $$
  CV_B = \left(\frac{1.52}{1.83}\right) \times 100 \approx 83.1\%
  $$

**Step 4: Interpretation**

- A **lower CV** indicates **less relative variability** and hence more consistency.
- **Team B's CV (~83.1%)** is lower than **Team A's CV (~113.5%)**, indicating that **Team B** is more consistent in scoring.

**Final Answer:**  
**Team B is more consistent** than Team A based on the Coefficient of Variation.

## <mark> 17) Coefficients of Variation and Standard Deviation of two series X and Y are 55.43% and 48.86%, and 25.5 and 24.43, respectively. Find the means of series X and Y. </mark>

The coefficient of variation (CV) is defined as:

$$
CV = \frac{\sigma}{\mu} \times 100\%
$$

where:

- $\sigma$ is the standard deviation, and
- $\mu$ is the mean.

We can rearrange the formula to solve for the mean:

$$
\mu = \frac{\sigma}{CV/100}
$$

### **For Series X:**

- Given:
  - $\sigma_X = 25.5$
  - $CV_X = 55.43\%$

$$
\mu_X = \frac{25.5}{55.43/100} = \frac{25.5}{0.5543} \approx 46.0
$$

### **For Series Y:**

- Given:
  - $\sigma_Y = 24.43$
  - $CV_Y = 48.86\%$

$$
\mu_Y = \frac{24.43}{48.86/100} = \frac{24.43}{0.4886} \approx 50.0
$$

### **Final Answer:**

- **Mean of Series X $\approx 46.0$**
- **Mean of Series Y $\approx 50.0$**

## <mark> 18) The standard deviation and mean of the data are 8.5 and 14.5 respectively. Find the coefficient of variation. </mark>

The coefficient of variation (CV) is calculated using the formula:

$$
CV = \left(\frac{\sigma}{\mu}\right) \times 100\%
$$

where:

- $\sigma$ is the standard deviation,
- $\mu$ is the mean.

Given:

- $\sigma = 8.5$,
- $\mu = 14.5$,

Plugging the values into the formula:

$$
CV = \left(\frac{8.5}{14.5}\right) \times 100\% \approx 0.5862 \times 100\% \approx 58.62\%
$$

Thus, the coefficient of variation is approximately **58.62%**.

## <mark> 19) If the mean and coefficient of deviation of data are 13 and 38 respectively, then locate the value of expected variation? </mark>

The coefficient of variation (CV) is given by the formula:

$$
CV = \left(\frac{\sigma}{\mu}\right) \times 100\%
$$

Where:

- $\sigma$ is the standard deviation (expected variation), and
- $\mu$ is the mean.

We are given:

- $\mu = 13$
- $CV = 38\%$

To find the standard deviation $\sigma$, rearrange the formula:

$$
\sigma = \frac{CV \times \mu}{100} = \frac{38 \times 13}{100}
$$

Calculating:

$$
\sigma = \frac{494}{100} = 4.94
$$

Thus, the expected variation (standard deviation) is approximately **4.94**.

## <mark> 20) The mean and standard variation of marks received by 40 students of a class in three subjects Mathematics, English and economics are given below.Which of the three subjects indicates the most elevated deviation and which indicates the most subordinate variation in marks?

| Subject   | Mean | Standard Deviation |
| --------- | ---- | ------------------ |
| Maths     | 65   | 10                 |
| English   | 60   | 12                 |
| Economics | 57   | 14                 |

</mark>

To compare the variability in marks across the three subjects, we use the **Coefficient of Variation (CV)**, which is calculated as:

$$
CV = \left(\frac{\text{Standard Deviation}}{\text{Mean}}\right) \times 100\%
$$

Let's compute the CV for each subject:

- **Maths:**

  $$
  CV\_{Maths} = \left(\frac{10}{65}\right) \times 100 \approx 15.38\%
  $$

- **English:**

  $$
  CV\_{English} = \left(\frac{12}{60}\right) \times 100 = 20\%
  $$

- **Economics:**
  $$
  CV\_{Economics} = \left(\frac{14}{57}\right) \times 100 \approx 24.56\%
  $$

**Interpretation:**

- The **highest CV** is in **Economics (≈24.56%)**, which means Economics has the most elevated deviation in marks.
- The **lowest CV** is in **Maths (≈15.38%)**, indicating that Maths has the most subordinate (least) variation in marks.

**Final Answer:**

- **Economics** indicates the most elevated deviation.
- **Maths** indicates the most subordinate variation in marks.

## <mark> 21) In a small business firm, two typists are employed- typist A and Typist B. Typist A types out, on an average, 30 pages per day with a standard deviation of 6. Typist B, on an average, types out 45 pages with a standard deviation of 10. Which typist shows greater consistency in his output. </mark>

We determine consistency by comparing the **Coefficient of Variation (CV)** for each typist. The CV is calculated as:

$$
CV = \left(\frac{\text{Standard Deviation}}{\text{Mean}}\right) \times 100\%
$$

**For Typist A:**

$$
CV_A = \left(\frac{6}{30}\right) \times 100\% = 20\%
$$

**For Typist B:**

$$
CV_B = \left(\frac{10}{45}\right) \times 100\% \approx 22.22\%
$$

Since a **lower CV indicates more consistency** in performance, Typist A (with a CV of 20%) shows greater consistency than Typist B (with a CV of approximately 22.22%).

## <mark> 22) The male population’s weight data follows a normal distribution. It has a mean of 70 kg and a standard deviation of 15 kg. What would the mean and standard deviation of a sample of 50 guys be if a researcher looked at their records? </mark>

The Central Limit Theorem tells us that the sample mean will have the same mean as the population, and its standard deviation (called the standard error) will be the population standard deviation divided by the square root of the sample size.

Given:

- Population mean, $\mu = 70$ kg
- Population standard deviation, $\sigma = 15$ kg
- Sample size, $n = 50$

**Mean of the sample:**

$$
\mu\_{\text{sample}} = 70 \text{ kg}
$$

**Standard deviation of the sample (Standard Error):**

$$
\sigma\_{\text{sample}} = \frac{15}{\sqrt{50}} \approx \frac{15}{7.07} \approx 2.12 \text{ kg}
$$

Thus, for a sample of 50 guys, the mean weight would be **70 kg** and the standard deviation of the sample would be approximately **2.12 kg**.

## <mark> 23) A distribution has a mean of 69 and a standard deviation of 420. Find the mean and standard deviation if a sample of 80 is drawn from the distribution. </mark>

For a sample drawn from a distribution, the sample mean remains the same as the population mean, and the standard deviation of the sample mean (also called the standard error) is calculated by dividing the population standard deviation by the square root of the sample size.

Given:

- Population mean, $\mu = 69$
- Population standard deviation, $\sigma = 420$
- Sample size, $n = 80$

**Mean of the sample:**

$$
\mu\_{\text{sample}} = \mu = 69
$$

**Standard deviation of the sample (Standard Error):**

$$
\sigma\_{\text{sample}} = \frac{\sigma}{\sqrt{n}} = \frac{420}{\sqrt{80}}
$$

Calculating $\sqrt{80}$:

$$
\sqrt{80} \approx 8.944
$$

Thus,

$$
\sigma\_{\text{sample}} \approx \frac{420}{8.944} \approx 46.97
$$

**Final Answer:**

- Mean of the sample: **69**
- Standard deviation of the sample: **approximately 47**

## <mark> 24) A boy collects some rupees in a week as follows (25,28,26,30,40,50,40) and finds the skewness and Kurtosis of the given Data in question with the help of the skewness formula. </mark>

Let's first list the data:

$$
25,\; 28,\; 26,\; 30,\; 40,\; 50,\; 40
$$

We’ll use the following steps:

1. **Compute the Mean ($\bar{x}$)**
2. **Compute the deviations and then the standard deviation ($s$)**
3. **Compute the third and fourth central moments**
4. **Calculate skewness and kurtosis using the “moment” formulas**

> **Note:** There are several formulas for sample skewness and kurtosis (with bias corrections). Here, we use the “population‐moment” approach as an illustration.

### **Step 1. Mean**

$$
\bar{x} = \frac{25 + 28 + 26 + 30 + 40 + 50 + 40}{7} = \frac{239}{7} \approx 34.14
$$

It is often useful to work exactly in fractions. Notice that:

- $25 = \frac{175}{7}$
- $28 = \frac{196}{7}$
- $26 = \frac{182}{7}$
- $30 = \frac{210}{7}$
- $40 = \frac{280}{7}$
- $50 = \frac{350}{7}$
- Another $40 = \frac{280}{7}$

So, the mean is:

$$
\bar{x} = \frac{175+196+182+210+280+350+280}{7\;} \frac{1}{7} = \frac{239}{7} \approx 34.14
$$

### **Step 2. Deviations and Standard Deviation**

Express each deviation $d_i = x_i - \bar{x}$ in fractional form (using denominator 7):

- For 25: $25 - \frac{239}{7} = \frac{175-239}{7} = -\frac{64}{7}$
- For 28: $28 - \frac{239}{7} = \frac{196-239}{7} = -\frac{43}{7}$
- For 26: $26 - \frac{239}{7} = \frac{182-239}{7} = -\frac{57}{7}$
- For 30: $30 - \frac{239}{7} = \frac{210-239}{7} = -\frac{29}{7}$
- For 40: $40 - \frac{239}{7} = \frac{280-239}{7} = \frac{41}{7}$
- For 50: $50 - \frac{239}{7} = \frac{350-239}{7} = \frac{111}{7}$
- For the other 40: Again, $+\frac{41}{7}$

Now, the squared deviations are:

$$
\begin{array}{lcl}
\left(-\frac{64}{7}\right)^2 &=& \frac{64^2}{7^2} = \frac{4096}{49}\$$1mm]
\left(-\frac{43}{7}\right)^2 &=& \frac{1849}{49}\$$1mm]
\left(-\frac{57}{7}\right)^2 &=& \frac{3249}{49}\$$1mm]
\left(-\frac{29}{7}\right)^2 &=& \frac{841}{49}\$$1mm]
\left(\frac{41}{7}\right)^2 &=& \frac{1681}{49}\$$1mm]
\left(\frac{111}{7}\right)^2 &=& \frac{12321}{49}\$$1mm]
\left(\frac{41}{7}\right)^2 &=& \frac{1681}{49}\$$1mm]
\end{array}
$$

**Sum of squared deviations:**

$$
\text{SS} = \frac{4096+1849+3249+841+1681+12321+1681}{49} = \frac{25718}{49}
$$

The population (or “moment‐based”) variance is then:

$$
\sigma^2 = \frac{25718}{49 \times 7} = \frac{25718}{343} \approx 75
$$

So, the standard deviation is:

$$
s \approx \sqrt{75} \approx 8.66
$$

_(Note: Using the sample formula with $n-1$ would yield a slightly larger value, but here we proceed with the moment method for simplicity.)_

### **Step 3. Third and Fourth Central Moments**

#### **Third Central Moment (for Skewness)**

We need $\frac{1}{n}\sum (x_i-\bar{x})^3$.

Using our deviations in fractional form:

- For 25: $\left(-\frac{64}{7}\right)^3 = -\frac{64^3}{7^3} = -\frac{262144}{343}$
- For 28: $\left(-\frac{43}{7}\right)^3 = -\frac{43^3}{343}$. (Note: $43^3 = 79507$)
- For 26: $-\frac{57^3}{343}$ with $57^3 = 185193$
- For 30: $-\frac{29^3}{343}$ with $29^3 = 24389$
- For 40: $\left(\frac{41}{7}\right)^3 = \frac{41^3}{343}$ with $41^3 = 68921$
- For 50: $\left(\frac{111}{7}\right)^3 = \frac{111^3}{343}$ with $111^3 = 1367631$
- For the other 40: again, $\frac{68921}{343}$

**Sum of cubes:**

$$
\text{SC} = \frac{-262144 - 79507 - 185193 - 24389 + 68921 + 1367631 + 68921}{343}
$$

Let’s add the negatives:

$-262144 - 79507 = -341651$  
$-341651 - 185193 = -526844$  
$-526844 - 24389 = -551233$

Now, the positives:

$68921 + 1367631 = 1436552$  
$1436552 + 68921 = 1505473$

Thus, sum of cubes:

$$
\text{SC} = \frac{1505473 - 551233}{343} = \frac{953240}{343} \approx 2780.2
$$

Now, the **average third moment** is:

$$
\mu_3 = \frac{\text{SC}}{7} \approx \frac{2780.2}{7} \approx 397.17
$$

#### **Skewness Calculation**

Using the formula for skewness based on moments:

$$
\text{Skewness} = \frac{\mu_3}{\sigma^3}
$$

We have $ \sigma \approx 8.66 $ so:

$$
\sigma^3 \approx 8.66^3 \approx 8.66 \times 8.66 \times 8.66 \approx 650 \quad (\text{approximately})
$$

Thus:

$$
\text{Skewness} \approx \frac{397.17}{650} \approx 0.61
$$

This indicates a moderate **positive skew**.

#### **Fourth Central Moment (for Kurtosis)**

We need $\mu_4 = \frac{1}{7}\sum (x_i-\bar{x})^4$.

We calculate the fourth powers (approximately using our decimal deviations):

- For 25: $(-9.14)^4 \approx 9.14^4$. Since $9.14^2 \approx 83.5$, then $83.5^2 \approx 6972$.
- For 28: $(-6.14)^4$ with $6.14^2 \approx 37.7$, then squared gives about $37.7^2 \approx 1420$.
- For 26: $(-8.14)^4$ with $8.14^2 \approx 66.3$, then squared gives about $66.3^2 \approx 4396$.
- For 30: $(-4.14)^4$ with $4.14^2 \approx 17.1$, squared gives about $17.1^2 \approx 292$.
- For 40: $(5.86)^4$ with $5.86^2 \approx 34.3$, squared gives about $34.3^2 \approx 1176$.
- For 50: $(15.86)^4$ with $15.86^2 \approx 251.5$, squared gives about $251.5^2 \approx 63250$.
- For the other 40: again about $1176$.

**Sum of fourth powers (approximate):**

$$
6972 + 1420 + 4396 + 292 + 1176 + 63250 + 1176 \approx 78682
$$

Average fourth moment:

$$
\mu_4 \approx \frac{78682}{7} \approx 11240
$$

Now, the denominator for kurtosis is $\sigma^4$. With $\sigma \approx 8.66$,

$$
\sigma^4 \approx 8.66^4 \approx (8.66^2)^2 \approx 75^2 = 5625 \quad (\text{approximately})
$$

Then, the kurtosis (using the “raw” moment definition) is:

$$
\text{Kurtosis} = \frac{\mu_4}{\sigma^4} \approx \frac{11240}{5625} \approx 2.0
$$

In many texts, a normal distribution has a kurtosis of 3. Thus the **excess kurtosis** here is about $2.0 - 3 = -1.0$, indicating a **platykurtic** (flatter) distribution relative to the normal curve.

### **Final Answers**

- **Skewness:** Approximately **0.61** (indicating a moderate positive skew).
- **Kurtosis:** Approximately **2.0** (or an excess kurtosis of about $-1$), meaning the distribution is flatter than a normal distribution.

> **Summary:**  
> For the data $25,\, 28,\, 26,\, 30,\, 40,\, 50,\, 40$, the skewness is about **0.61** and the kurtosis is about **2.0**.

_Keep in mind that slight differences may arise depending on the specific formula (and bias correction) used for sample skewness and kurtosis._

## <mark> 25) Calculate Population Skewness, Population Kurtosis from the following grouped data and explain the type of kurtosis and skewness of the data.

| Class Interval | Frequency (f) | Midpoint (x) |
| -------------- | ------------- | ------------ |
| 10 - 20        | 2             | 15           |
| 20 - 30        | 3             | 25           |
| 30 - 40        | 5             | 35           |

</mark>

We are given the following grouped data:

| Class Interval | Frequency ($f$) | Midpoint ($x$) |
| -------------- | --------------- | -------------- |
| 10 – 20        | 2               | 15             |
| 20 – 30        | 3               | 25             |
| 30 – 40        | 5               | 35             |

The total frequency is:

$$
N = 2 + 3 + 5 = 10.
$$

We'll calculate the population moments (using the formulas for the entire population) and then obtain the population skewness and kurtosis.

### **Step 1. Calculate the Mean**

The mean is given by:

$$
\bar{x} = \frac{\sum f \cdot x}{N}.
$$

$$
\bar{x} = \frac{2 \times 15 + 3 \times 25 + 5 \times 35}{10} = \frac{30 + 75 + 175}{10} = \frac{280}{10} = 28.
$$

### **Step 2. Calculate the Variance and Standard Deviation**

The variance ($\sigma^2$) is:

$$
\sigma^2 = \frac{\sum f (x - \bar{x})^2}{N}.
$$

First, compute $(x - \bar{x})$ and $(x - \bar{x})^2$ for each class:

- For $x=15$:  
  $15 - 28 = -13,$ and $(-13)^2 = 169.$  
  Contribution: $2 \times 169 = 338.$

- For $x=25$:  
  $25 - 28 = -3,$ and $(-3)^2 = 9.$  
  Contribution: $3 \times 9 = 27.$

- For $x=35$:  
  $35 - 28 = 7,$ and $7^2 = 49.$  
  Contribution: $5 \times 49 = 245.$

Now, sum the contributions:

$$
\sum f (x - \bar{x})^2 = 338 + 27 + 245 = 610.
$$

So,

$$
\sigma^2 = \frac{610}{10} = 61.
$$

The standard deviation is:

$$
\sigma = \sqrt{61} \approx 7.81.
$$

### **Step 3. Calculate the Third Central Moment and Skewness**

The third central moment is:

$$
\mu_3 = \frac{\sum f (x - \bar{x})^3}{N}.
$$

Compute $(x-\bar{x})^3$ for each midpoint:

- For $x=15$:  
  $15 - 28 = -13,$ so $(-13)^3 = -2197.$  
  Contribution: $2 \times (-2197) = -4394.$

- For $x=25$:  
  $25 - 28 = -3,$ so $(-3)^3 = -27.$  
  Contribution: $3 \times (-27) = -81.$

- For $x=35$:  
  $35 - 28 = 7,$ so $7^3 = 343.$  
  Contribution: $5 \times 343 = 1715.$

Sum the contributions:

$$
\sum f (x - \bar{x})^3 = -4394 - 81 + 1715 = -2760.
$$

Then, the third central moment is:

$$
\mu_3 = \frac{-2760}{10} = -276.
$$

Population skewness is given by:

$$
\text{Skewness} = \frac{\mu_3}{\sigma^3}.
$$

We already have $\sigma \approx 7.81$. Note that:

$$
\sigma^3 = (7.81)^3 \approx 7.81 \times 61 \approx 476 \quad (\text{since } 7.81^2 \approx 61).
$$

Thus:

$$
\text{Skewness} \approx \frac{-276}{476} \approx -0.58.
$$

**Interpretation:**  
A skewness of about $-0.58$ indicates a moderate **negative skew** (the left tail is longer or more pronounced than the right).

### **Step 4. Calculate the Fourth Central Moment and Kurtosis**

The fourth central moment is:

$$
\mu_4 = \frac{\sum f (x - \bar{x})^4}{N}.
$$

Compute $(x-\bar{x})^4$ for each midpoint:

- For $x=15$:  
  $15 - 28 = -13,$ so $(-13)^4 = 28561.$  
  Contribution: $2 \times 28561 = 57122.$

- For $x=25$:  
  $25 - 28 = -3,$ so $(-3)^4 = 81.$  
  Contribution: $3 \times 81 = 243.$

- For $x=35$:  
  $35 - 28 = 7,$ so $7^4 = 2401.$  
  Contribution: $5 \times 2401 = 12005.$

Sum the contributions:

$$
\sum f (x - \bar{x})^4 = 57122 + 243 + 12005 = 69370.
$$

Then,

$$
\mu_4 = \frac{69370}{10} = 6937.
$$

Population kurtosis is given by:

$$
\text{Kurtosis} = \frac{\mu_4}{\sigma^4}.
$$

We have:

$$
\sigma^2 = 61 \quad \Longrightarrow \quad \sigma^4 = 61^2 = 3721.
$$

Thus,

$$
\text{Kurtosis} \approx \frac{6937}{3721} \approx 1.86.
$$

**Note on Interpretation:**

- A normal distribution has a kurtosis of 3 (using the “raw” kurtosis definition).
- Here, the calculated kurtosis is about 1.86, which is less than 3.
- The **excess kurtosis** (kurtosis minus 3) is approximately $1.86 - 3 = -1.14$.  
  This indicates a **platykurtic** distribution—one that is flatter than the normal distribution with thinner tails.

### **Final Summary and Interpretation**

- **Mean:** $28$
- **Standard Deviation:** $\approx 7.81$
- **Population Skewness:** $\approx -0.58$  
  This indicates a moderate **negative skew** (the distribution is slightly tilted to the left).
- **Population Kurtosis:** $\approx 1.86$ (or an excess kurtosis of about $-1.14$)  
  This indicates that the distribution is **platykurtic**, meaning it is flatter with lighter tails than a normal distribution.

**Conclusion:**  
The given grouped data shows a distribution with a moderate negative skew and a platykurtic (flatter than normal) shape.

## <mark> 26) A nutritionist claims that the average sugar content in a brand of cereal is less than 10 grams per serving. A random sample of 30 cereal boxes shows an average sugar content of 9.5 grams with a standard deviation of 1.2 grams. At a 5% significance level (α = 0.05), test whether the nutritionist's claim is supported. </mark>

**Step 1: State the Hypotheses**

- **Null Hypothesis ($H_0$)**: The mean sugar content $\mu \geq 10$ grams.
- **Alternative Hypothesis ($H_A$)**: The mean sugar content $\mu < 10$ grams.

This is a one-tailed (left-tailed) test since the claim is that the average is _less than_ 10 grams.

**Step 2: Compute the Test Statistic**

Given:

- Sample size, $n = 30$
- Sample mean, $\bar{x} = 9.5$ grams
- Sample standard deviation, $s = 1.2$ grams
- Significance level, $\alpha = 0.05$

Since the population standard deviation is unknown and $n$ is moderate, we use the t-test. The test statistic is calculated by:

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

where $\mu_0 = 10$ grams (hypothesized mean).

Plugging in the values:

$$
t = \frac{9.5 - 10}{1.2/\sqrt{30}} = \frac{-0.5}{1.2/5.477} \approx \frac{-0.5}{0.2188} \approx -2.285.
$$

**Step 3: Determine the Critical t-value**

For a one-tailed test at $\alpha = 0.05$ with $df = n-1 = 29$, the critical t-value is approximately:

$$
t\_{\text{critical}} \approx -1.699.
$$

**Step 4: Decision**

Since the calculated $t$-value $-2.285$ is less than $-1.699$ (i.e., it falls in the rejection region), we **reject the null hypothesis**.

**Step 5: Conclusion**

At the 5% significance level, the sample provides sufficient evidence to support the nutritionist's claim that the average sugar content in the cereal is less than 10 grams per serving.

## <mark> 27) A manufacturer claims that the average lifespan of its LED bulbs is at least 25,000 hours. A consumer protection agency tests 40 randomly selected bulbs and finds an average lifespan of 24,500 hours with a standard deviation of 1,200 hours. At a 5% significance level (α = 0.05), test whether the agency’s data contradicts the manufacturer’s claim. </mark>

**Step 1: Formulate the Hypotheses**

- **Null Hypothesis ($H_0$)**: $\mu \geq 25000$ hours (the average lifespan is at least 25,000 hours).
- **Alternative Hypothesis ($H_A$)**: $\mu < 25000$ hours (the average lifespan is less than 25,000 hours).

This is a one-tailed (left-tailed) test.

**Step 2: Compute the Test Statistic**

Given:

- Sample size, $ n = 40 $
- Sample mean, $ \bar{x} = 24500 $ hours
- Sample standard deviation, $ s = 1200 $ hours

The t-statistic is computed as:

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

Where $\mu_0 = 25000$ hours.

First, calculate the standard error (SE):

$$
\text{SE} = \frac{1200}{\sqrt{40}} \approx \frac{1200}{6.3249} \approx 189.74.
$$

Then, calculate the t-statistic:

$$
t = \frac{24500 - 25000}{189.74} = \frac{-500}{189.74} \approx -2.635.
$$

**Step 3: Determine the Critical Value**

For a one-tailed test at $\alpha = 0.05$ with $df = 40 - 1 = 39$, the critical t-value is approximately:

$$
t\_{\text{critical}} \approx -1.685.
$$

**Step 4: Decision**

Since the calculated t-value ($-2.635$) is less than the critical t-value ($-1.685$), it falls in the rejection region.

**Step 5: Conclusion**

At the 5% significance level, we **reject the null hypothesis**. The consumer protection agency's data provides sufficient evidence to conclude that the average lifespan of the LED bulbs is **less than 25,000 hours**. Therefore, the agency’s findings contradict the manufacturer’s claim.

## <mark> 28) A soft drink company claims that the average sugar content in its cola is 39 grams per can. A health organization collects a random sample of 50 cans and finds the average sugar content is 40 grams, with a standard deviation of 2 grams. At a 1% significance level (α = 0.01), test if the actual sugar content is different from 39 grams. </mark>

**Step 1: State the Hypotheses**

- **Null Hypothesis ($H_0$)**: The average sugar content is 39 grams per can ($\mu = 39$).
- **Alternative Hypothesis ($H_A$)**: The average sugar content is different from 39 grams ($\mu \neq 39$).

This is a two-tailed test.

**Step 2: Compute the Test Statistic**

Given:

- Sample size, $n = 50$
- Sample mean, $\bar{x} = 40$ grams
- Sample standard deviation, $s = 2$ grams

The test statistic (t) is calculated as:

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} = \frac{40 - 39}{2/\sqrt{50}}
$$

Calculate the standard error:

$$
\text{SE} = \frac{2}{\sqrt{50}} \approx \frac{2}{7.0711} \approx 0.2828
$$

Now, compute t:

$$
t = \frac{1}{0.2828} \approx 3.54
$$

**Step 3: Determine the Critical t-value**

For a two-tailed test at $\alpha = 0.01$ with $df = 50 - 1 = 49$, the critical t-value is approximately $\pm 2.68$ (using standard t-distribution tables).

**Step 4: Decision**

Since the calculated t-value $3.54$ exceeds the critical value $2.68$ (in absolute value), we **reject the null hypothesis**.

**Step 5: Conclusion**

At the 1% significance level, there is sufficient evidence to conclude that the actual sugar content in the cola is **different from 39 grams per can**. Given that the sample mean is 40 grams, it appears that the sugar content is higher than claimed.

## <mark> 29) A company manufacturing automobiles finds that tyre-life is normally distributed with a mean of 40,000 km and standard deviation of 3000 km. It is believed that a change in the production process will result in a better product and the company has developed a new tyre. A sample of 100 new tyres has been selected. The company has found that the mean life of these new tyres is 40,900 Km. Can it be concluded that the new tyre is significantly better than the old one, using the significance level of 0.01. <br> Hint; we are interested in testing whether or not there has been an increase in the mean life of tyres or test whether the mean life of new tyre has increased beyond 40,000 km. </mark>

**Step 1: Define the Hypotheses**

- **Null Hypothesis ($H_0$)**: The new tyre has the same mean life as the old one, $\mu = 40,000$ km.
- **Alternative Hypothesis ($H_A$)**: The new tyre has a higher mean life, $\mu > 40,000$ km.

This is a one-tailed (right-tailed) test.

**Step 2: Calculate the Test Statistic**

Given:

- Population mean (old tyre), $\mu_0 = 40,000$ km
- Population standard deviation, $\sigma = 3,000$ km
- Sample size, $n = 100$
- Sample mean (new tyre), $\bar{x} = 40,900$ km

Since the tyre-life is normally distributed and the standard deviation is known, we use the z-test:

$$
z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} = \frac{40,900 - 40,000}{3000/\sqrt{100}}.
$$

Calculate the standard error:

$$
\text{SE} = \frac{3000}{10} = 300.
$$

Then, the z-value is:

$$
z = \frac{900}{300} = 3.
$$

**Step 3: Determine the Critical Value**

At a significance level of $\alpha = 0.01$ for a one-tailed test, the critical z-value is approximately **2.33**.

**Step 4: Make the Decision**

Since the calculated z-value (3) is greater than the critical value (2.33), we **reject the null hypothesis**.

**Step 5: Conclusion**

At the 0.01 significance level, there is sufficient evidence to conclude that the mean life of the new tyres is significantly greater than 40,000 km. Therefore, the new tyre is significantly better than the old one.

## <mark> 30) <mark> Following are the runs scored by two batsmen in 5 cricket matches, Who is more consistent in scoring runs?

|           | Score 1 | Score 2 | Score 3 | Score 4 | Score 5 |
| --------- | ------- | ------- | ------- | ------- | ------- |
| Batsman A | 38      | 47      | 34      | 18      | 33      |
| Batsman B | 37      | 35      | 41      | 27      | 35      |

</mark>

To assess consistency, we can calculate the mean and the standard deviation, and then use the Coefficient of Variation (CV):

$$
CV = \left(\frac{\text{Standard Deviation}}{\text{Mean}}\right) \times 100\%
$$

### **Batsman A**

**Runs:** 38, 47, 34, 18, 33

1. **Mean ($\bar{x}$):**

   $$
   \bar{x}\_A = \frac{38 + 47 + 34 + 18 + 33}{5} = \frac{170}{5} = 34
   $$

2. **Deviations and Squared Deviations:**

| Score | Deviation ($x - 34$) | Squared Deviation |
| ----- | -------------------- | ----------------- |
| 38    | 38 - 34 = 4          | $4^2 = 16$        |
| 47    | 47 - 34 = 13         | $13^2 = 169$      |
| 34    | 34 - 34 = 0          | $0^2 = 0$         |
| 18    | 18 - 34 = -16        | $(-16)^2 = 256$   |
| 33    | 33 - 34 = -1         | $(-1)^2 = 1$      |

**Sum of Squared Deviations:** $16 + 169 + 0 + 256 + 1 = 442$

3. **Sample Variance and Standard Deviation:**

Using $n - 1$ (for a sample of 5 matches):

$$
s^2_A = \frac{442}{5 - 1} = \frac{442}{4} = 110.5
$$

$$
s_A = \sqrt{110.5} \approx 10.51
$$

4. **Coefficient of Variation (CV):**
   $$
   CV_A = \frac{10.51}{34} \times 100 \approx 30.9\%
   $$

### **Batsman B**

**Runs:** 37, 35, 41, 27, 35

1. **Mean ($\bar{x}$):**

   $$
   \bar{x}\_B = \frac{37 + 35 + 41 + 27 + 35}{5} = \frac{175}{5} = 35
   $$

2. **Deviations and Squared Deviations:**

| Score | Deviation ($x - 35$) | Squared Deviation |
| ----- | -------------------- | ----------------- |
| 37    | 37 - 35 = 2          | $2^2 = 4$         |
| 35    | 35 - 35 = 0          | $0^2 = 0$         |
| 41    | 41 - 35 = 6          | $6^2 = 36$        |
| 27    | 27 - 35 = -8         | $(-8)^2 = 64$     |
| 35    | 35 - 35 = 0          | $0^2 = 0$         |

**Sum of Squared Deviations:** $4 + 0 + 36 + 64 + 0 = 104$

3. **Sample Variance and Standard Deviation:**

$$
s^2_B = \frac{104}{5 - 1} = \frac{104}{4} = 26
$$

$$
s_B = \sqrt{26} \approx 5.10
$$

4. **Coefficient of Variation (CV):**
   $$
   CV_B = \frac{5.10}{35} \times 100 \approx 14.6\%
   $$

### **Conclusion**

- **Batsman A** has a CV of approximately **30.9%**.
- **Batsman B** has a CV of approximately **14.6%**.

A lower coefficient of variation indicates greater consistency. Therefore, **Batsman B** is more consistent in scoring runs than **Batsman A**.

## <mark> 31) Find the skewness for the given Data ( 2,4,6,6) : <br> Skewness = 3(Mean – Median)/S.D. </mark>

**Step 1: Calculate the Mean, Median, and Standard Deviation**

Given Data: 2, 4, 6, 6

1. **Mean ($\bar{x}$)**

   $$
   \bar{x} = \frac{2 + 4 + 6 + 6}{4} = \frac{18}{4} = 4.5
   $$

2. **Median**  
   For the ordered data (2, 4, 6, 6), the median is the average of the two middle values:

   $$
   \text{Median} = \frac{4 + 6}{2} = 5.
   $$

3. **Standard Deviation (Population Standard Deviation)**  
   Calculate each deviation from the mean and then square them:

- $2 - 4.5 = -2.5 \quad \Rightarrow (-2.5)^2 = 6.25$
- $4 - 4.5 = -0.5 \quad \Rightarrow (-0.5)^2 = 0.25$
- $6 - 4.5 = 1.5 \quad \Rightarrow (1.5)^2 = 2.25$
- $6 - 4.5 = 1.5 \quad \Rightarrow (1.5)^2 = 2.25$

Sum of squared deviations:

$$
6.25 + 0.25 + 2.25 + 2.25 = 11.
$$

Population variance:

$$
\sigma^2 = \frac{11}{4} = 2.75.
$$

Standard deviation:

$$
\sigma = \sqrt{2.75} \approx 1.6583.
$$

**Step 2: Calculate Skewness**

Using the formula:

$$
\text{Skewness} = \frac{3(\text{Mean} - \text{Median})}{\sigma}
$$

Plug in the values:

$$
\text{Skewness} = \frac{3(4.5 - 5)}{1.6583} = \frac{3(-0.5)}{1.6583} = \frac{-1.5}{1.6583} \approx -0.9045.
$$

**Final Answer:**

The skewness for the given data is approximately **-0.90**, which indicates a slight negative skew (the distribution is skewed to the left).

## <mark> 32) For the given observations {23, 24, 56, 55, 28, 38, 48}, calculate: <br> - Skewness <br> - Kurtosis <br> - Determine the type of kurtosis </mark>

We'll compute the population skewness and kurtosis for the data

$$
\{23,\;24,\;56,\;55,\;28,\;38,\;48\}
$$

using the following steps:

### **Step 1. Compute the Mean**

$$
\bar{x} = \frac{23 + 24 + 56 + 55 + 28 + 38 + 48}{7} = \frac{272}{7} \approx 38.8571.
$$

### **Step 2. Compute the Median**

First, sort the data:

$$
23,\;24,\;28,\;38,\;48,\;55,\;56.
$$

Since there are 7 values, the median is the 4th value:

$$
\text{Median} = 38.
$$

### **Step 3. Compute the Standard Deviation (Population)**

For each observation $x_i$, compute the deviation $x_i - \bar{x}$ and its square:

| $x_i$ | $x_i - \bar{x}$                 | $(x_i - \bar{x})^2$           |
| ----- | ------------------------------- | ----------------------------- |
| 23    | $23 - 38.8571 \approx -15.8571$ | $(-15.8571)^2 \approx 251.43$ |
| 24    | $24 - 38.8571 \approx -14.8571$ | $(-14.8571)^2 \approx 220.71$ |
| 56    | $56 - 38.8571 \approx 17.1429$  | $17.1429^2 \approx 293.88$    |
| 55    | $55 - 38.8571 \approx 16.1429$  | $16.1429^2 \approx 260.57$    |
| 28    | $28 - 38.8571 \approx -10.8571$ | $(-10.8571)^2 \approx 117.86$ |
| 38    | $38 - 38.8571 \approx -0.8571$  | $(-0.8571)^2 \approx 0.7347$  |
| 48    | $48 - 38.8571 \approx 9.1429$   | $9.1429^2 \approx 83.64$      |

Sum of squared deviations:

$$
\sum (x_i - \bar{x})^2 \approx 251.43 + 220.71 + 293.88 + 260.57 + 117.86 + 0.73 + 83.64 \approx 1228.9.
$$

Since we are treating this as the entire population, the variance is

$$
\sigma^2 = \frac{1228.9}{7} \approx 175.56,
$$

and the population standard deviation is

$$
\sigma \approx \sqrt{175.56} \approx 13.24.
$$

### **Step 4. Compute Population Skewness**

A quick (Pearson’s) measure of skewness is given by

$$
\text{Skewness} = \frac{3(\text{Mean} - \text{Median})}{\sigma}.
$$

Using our values:

$$
\text{Skewness} = \frac{3(38.8571 - 38)}{13.24} = \frac{3(0.8571)}{13.24} \approx \frac{2.5713}{13.24} \approx 0.194.
$$

This indicates a **slight positive skew** (a small positive value).

### **Step 5. Compute Population Kurtosis**

Population kurtosis (using the raw moment definition) is given by

$$
\text{Kurtosis} = \frac{\frac{1}{n}\sum (x_i - \bar{x})^4}{\sigma^4}.
$$

#### **Calculate the Fourth Powers**

For each observation, compute $(x_i - \bar{x})^4$:

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^4$ (approx.)  |
| ----- | --------------- | ------------------------------ |
| 23    | $-15.8571$      | $(15.8571^2)^2 \approx 63,216$ |
| 24    | $-14.8571$      | $(14.8571^2)^2 \approx 48,713$ |
| 56    | $17.1429$       | $(17.1429^2)^2 \approx 86,348$ |
| 55    | $16.1429$       | $(16.1429^2)^2 \approx 67,900$ |
| 28    | $-10.8571$      | $(10.8571^2)^2 \approx 13,894$ |
| 38    | $-0.8571$       | $(0.8571^2)^2 \approx 0.54$    |
| 48    | $9.1429$        | $(9.1429^2)^2 \approx 6,997$   |

Now, sum these values:

$$
\sum (x_i - \bar{x})^4 \approx 63,216 + 48,713 + 86,348 + 67,900 + 13,894 + 0.54 + 6,997 \approx 287,069.
$$

Average fourth moment:

$$
\mu_4 = \frac{287,069}{7} \approx 41,010.
$$

Next, calculate $\sigma^4$:

$$
\sigma^4 = (13.24)^4.
$$

Since $\sigma^2 \approx 175.56$, then

$$
\sigma^4 \approx 175.56^2 \approx 30,778.
$$

Thus, the kurtosis is

$$
\text{Kurtosis} \approx \frac{41,010}{30,778} \approx 1.33.
$$

For many definitions, a normal distribution has a kurtosis of 3. When we subtract 3, we get an **excess kurtosis** of

$$
1.33 - 3 \approx -1.67.
$$

### **Step 6. Interpretation**

- **Skewness:** ~0.194  
  The small positive value indicates a **slightly right-skewed** distribution.
- **Kurtosis:** ~1.33 (or an excess kurtosis of –1.67)  
  Since the kurtosis is less than 3, the distribution is **platykurtic** (flatter than the normal distribution with thinner tails).

### **Final Answers**

- **Population Skewness:** Approximately **0.19** (indicating a slight positive skew).
- **Population Kurtosis:** Approximately **1.33** (excess kurtosis ≈ –1.67), which means the data is **platykurtic** (flatter than a normal distribution).

## <mark> 33) Given the weights of five persons: 120, 140, 150, 160, and 180, find the following: <br> - Mean <br> - Median <br> - Mode <br> - Standard deviation <br> - Variance <br> - Interquartile range <br> - Box plot <br> - Whisker plot </mark>

Below are the steps and results for the given weights:

**Data:** 120, 140, 150, 160, 180

### **1. Mean**

$$
\text{Mean} = \frac{120+140+150+160+180}{5} = \frac{750}{5} = 150
$$

### **2. Median**

When the data are arranged in order (which they already are):

$$
\text{Median} = 150 \quad \text{(middle value)}
$$

### **3. Mode**

Each weight appears only once, so there is **no mode** (or no unique mode).

### **4. Variance and Standard Deviation**

**Step 4a. Compute the squared deviations from the mean:**

- For 120: $ (120 - 150)^2 = (-30)^2 = 900 $
- For 140: $ (140 - 150)^2 = (-10)^2 = 100 $
- For 150: $ (150 - 150)^2 = 0^2 = 0 $
- For 160: $ (160 - 150)^2 = 10^2 = 100 $
- For 180: $ (180 - 150)^2 = 30^2 = 900 $

**Step 4b. Sum of squared deviations:**

$$
900 + 100 + 0 + 100 + 900 = 2000
$$

**Assuming these 5 values represent the entire population:**

$$
\text{Variance} (\sigma^2) = \frac{2000}{5} = 400
$$

$$
\text{Standard Deviation} (\sigma) = \sqrt{400} = 20
$$

_If you were to use the sample formula (n – 1), then:_

$$
s^2 = \frac{2000}{5-1} = \frac{2000}{4} = 500 \quad \text{and} \quad s = \sqrt{500} \approx 22.36.
$$

For this exercise, we assume the given values form the entire population.

### **5. Interquartile Range (IQR)**

**Step 5a. Determine Q1 and Q3:**

For 5 data points, the median (Q2) is 150.

- The lower half (excluding the median) is: 120, 140
  - $ Q1 = \frac{120+140}{2} = \frac{260}{2} = 130 $
- The upper half is: 160, 180
  - $ Q3 = \frac{160+180}{2} = \frac{340}{2} = 170 $

**Step 5b. Compute IQR:**

$$
\text{IQR} = Q3 - Q1 = 170 - 130 = 40
$$

### **6. Box Plot / Whisker Plot**

A box (or whisker) plot for these data is constructed using:

- **Minimum:** 120
- **Q1:** 130
- **Median:** 150
- **Q3:** 170
- **Maximum:** 180

On the plot:

- The box spans from Q1 (130) to Q3 (170).
- A line is drawn at the median (150) inside the box.
- The "whiskers" extend from the box out to the minimum (120) and maximum (180).

### **Summary of Results**

- **Mean:** 150
- **Median:** 150
- **Mode:** None (no repeated value)
- **Variance:** 400
- **Standard Deviation:** 20
- **Interquartile Range (IQR):** 40
- **Box Plot / Whisker Plot:**
  - Minimum = 120
  - Q1 = 130
  - Median = 150
  - Q3 = 170
  - Maximum = 180

These calculations provide a complete picture of the central tendency and dispersion for the given data.

## <mark> 34) A random sample of n = 500 observations from a binomial population produced x = 240 successes. <br> - Find a point estimate for p and place a 95% confidence interval. <br> - Find a 90% confidence interval for p. </mark>

### **Step 1: Point Estimate for $ p $**

The point estimate for the probability of success, $ p $, is given by:

$$
\hat{p} = \frac{x}{n} = \frac{240}{500} = 0.48.
$$

### **Step 2: Standard Error Calculation**

The standard error (SE) for a proportion is:

$$
SE = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0.48 \times 0.52}{500}}.
$$

Calculating:

$$
0.48 \times 0.52 = 0.2496,
$$

$$
\frac{0.2496}{500} = 0.0004992,
$$

$$
SE \approx \sqrt{0.0004992} \approx 0.02235.
$$

### **Step 3: 95% Confidence Interval for $ p $**

For a 95% confidence interval, the critical z-value is approximately $ z\_{0.025} = 1.96 $.

The margin of error (ME) is:

$$
ME\_{95} = z \times SE = 1.96 \times 0.02235 \approx 0.0438.
$$

Thus, the 95% confidence interval is:

$$
\hat{p} \pm ME*{95} \quad \Rightarrow \quad (0.48 - 0.0438,\; 0.48 + 0.0438),
$$

$$
\text{CI}*{95\%} \approx (0.4362,\; 0.5238).
$$

### **Step 4: 90% Confidence Interval for $ p $**

For a 90% confidence interval, the critical z-value is approximately $ z\_{0.05} = 1.645 $.

The margin of error is:

$$
ME\_{90} = 1.645 \times 0.02235 \approx 0.0368.
$$

Thus, the 90% confidence interval is:

$$
\hat{p} \pm ME*{90} \quad \Rightarrow \quad (0.48 - 0.0368,\; 0.48 + 0.0368),
$$

$$
\text{CI}*{90\%} \approx (0.4432,\; 0.5168).
$$

### **Summary of Results**

- **Point Estimate for $ p $:** $ 0.48 $
- **95% Confidence Interval:** Approximately $ (0.436, \; 0.524) $
- **90% Confidence Interval:** Approximately $ (0.443, \; 0.517) $

These intervals indicate that we are 95% confident that the true proportion of successes lies between about 43.6% and 52.4%, and 90% confident it lies between about 44.3% and 51.7%.

## <mark> 35) Given the observations {6, 8, 10, 12, 14, 16, 18, 20, 22, 24}, calculate the following: <br> - Mean <br> - Median <br> - Standard deviation <br> - Variance <br> - Skewness <br> - Kurtosis <br> - Lower quartile <br> - Upper quartile <br> - Middle quartile <br> - Interquartile range <br> - Range </mark>

Let's start by listing the data and then calculate each measure step‐by‐step.

**Data:**  
6, 8, 10, 12, 14, 16, 18, 20, 22, 24

### 1. Mean

$$
\text{Mean} = \frac{6+8+10+12+14+16+18+20+22+24}{10} = \frac{150}{10} = 15.
$$

### 2. Median

Since there are 10 observations (an even number), the median is the average of the 5th and 6th values.  
The ordered data: 6, 8, 10, 12, 14, 16, 18, 20, 22, 24

$$
\text{Median} = \frac{14 + 16}{2} = 15.
$$

### 3. Variance and Standard Deviation

**Step 3a. Compute the deviations from the mean and square them:**

| $x$ | $x - 15$    | $(x-15)^2$ |
| --- | ----------- | ---------- |
| 6   | 6 – 15 = –9 | 81         |
| 8   | –7          | 49         |
| 10  | –5          | 25         |
| 12  | –3          | 9          |
| 14  | –1          | 1          |
| 16  | 1           | 1          |
| 18  | 3           | 9          |
| 20  | 5           | 25         |
| 22  | 7           | 49         |
| 24  | 9           | 81         |

**Sum of squared deviations:**  
$81+49+25+9+1+1+9+25+49+81 = 330$.

For the **population variance** (assuming the data represent the entire population):

$$
\sigma^2 = \frac{330}{10} = 33.
$$

Standard deviation:

$$
\sigma = \sqrt{33} \approx 5.74.
$$

### 4. Skewness

Since the data are perfectly symmetric around the mean (mean = median = 15), the skewness is 0.

Using Pearson’s formula for skewness:

$$
\text{Skewness} = \frac{3(\text{Mean} - \text{Median})}{\sigma} = \frac{3(15-15)}{5.74} = 0.
$$

### 5. Kurtosis

The population kurtosis (using the fourth moment) is computed as:

$$
\text{Kurtosis} = \frac{\mu*4}{\sigma^4},
$$

where

$$
\mu_4 = \frac{1}{n}\sum*{i=1}^{n} (x_i-\bar{x})^4.
$$

**Step 5a. Compute $(x_i - 15)^4$ for each observation:**

| $x$ | $x-15$ | $(x-15)^4$   |
| --- | ------ | ------------ |
| 6   | –9     | $9^4 = 6561$ |
| 8   | –7     | $7^4 = 2401$ |
| 10  | –5     | $5^4 = 625$  |
| 12  | –3     | $3^4 = 81$   |
| 14  | –1     | $1^4 = 1$    |
| 16  | 1      | $1^4 = 1$    |
| 18  | 3      | $3^4 = 81$   |
| 20  | 5      | $5^4 = 625$  |
| 22  | 7      | $7^4 = 2401$ |
| 24  | 9      | $9^4 = 6561$ |

**Sum of fourth powers:**  
$6561 + 2401 + 625 + 81 + 1 + 1 + 81 + 625 + 2401 + 6561 = 19338$.

Now,

$$
\mu_4 = \frac{19338}{10} = 1933.8.
$$

Next, calculate $\sigma^4$. We already found $\sigma^2 = 33$, so

$$
\sigma^4 = 33^2 = 1089.
$$

Thus,

$$
\text{Kurtosis} = \frac{1933.8}{1089} \approx 1.78.
$$

A normal distribution has a kurtosis of 3 (using the “raw” kurtosis measure). The **excess kurtosis** is given by:

$$
\text{Excess Kurtosis} = 1.78 - 3 = -1.22.
$$

This indicates the distribution is **platykurtic** (flatter than a normal distribution with lighter tails).

### 6. Quartiles and Interquartile Range (IQR)

**Ordered Data:** 6, 8, 10, 12, 14, 16, 18, 20, 22, 24

- **Lower Quartile (Q1):** Median of the lower half (first 5 numbers: 6, 8, 10, 12, 14)  
  $Q1 = 10$ (the 3rd value).

- **Upper Quartile (Q3):** Median of the upper half (last 5 numbers: 16, 18, 20, 22, 24)  
  $Q3 = 20$ (the 3rd value).

- **Middle Quartile (Median, Q2):** As computed above, $Q2 = 15$.

- **Interquartile Range (IQR):**
  $$
  IQR = Q3 - Q1 = 20 - 10 = 10.
  $$

### 7. Range

$$
\text{Range} = \text{Maximum} - \text{Minimum} = 24 - 6 = 18.
$$

### 8. Box Plot / Whisker Plot Description

A box plot is drawn using these five summary statistics:

- **Minimum:** 6
- **Q1 (Lower Quartile):** 10
- **Median:** 15
- **Q3 (Upper Quartile):** 20
- **Maximum:** 24

In the box plot:

- The box extends from Q1 to Q3 (10 to 20).
- A line inside the box marks the median (15).
- Whiskers extend from the box to the minimum (6) and maximum (24).

### **Final Answers**

- **Mean:** 15
- **Median:** 15
- **Standard Deviation:** Approximately 5.74
- **Variance:** 33
- **Skewness:** 0 (symmetric distribution)
- **Kurtosis:** Approximately 1.78 (excess kurtosis ≈ –1.22, indicating a platykurtic distribution)
- **Lower Quartile (Q1):** 10
- **Upper Quartile (Q3):** 20
- **Middle Quartile (Median, Q2):** 15
- **Interquartile Range (IQR):** 10
- **Range:** 18

These statistics provide a complete descriptive summary of the given data.

## <mark> 36) The mean of the following frequency distribution was found to be 1.46:

| No. of Accidents | No. of Days (Frequency) |
| ---------------- | ----------------------- |
| 0                | 46                      |
| 1                | ?                       |
| 2                | ?                       |
| 3                | 25                      |
| 4                | 10                      |
| 5                | ?                       |
| **Total**        | **200 days**            |

<mark> Calculate the missing frequencies. </mark>

Let the missing frequencies be:

- $f_1$ for 1 accident,
- $f_2$ for 2 accidents,
- $f_5$ for 5 accidents.

We are given:

- For 0 accidents: $f_0 = 46$
- For 3 accidents: $f_3 = 25$
- For 4 accidents: $f_4 = 10$
- Total days: $200$

Thus, the sum of frequencies is

$$
46 + f_1 + f_2 + 25 + 10 + f_5 = 200.
$$

That is,

$$
f_1 + f_2 + f_5 = 200 - (46+25+10) = 200 - 81 = 119. \tag{1}
$$

Also, we are told that the mean number of accidents is 1.46. (Since “accidents” is our “x‐value”, the mean is given by)

$$
\bar{x} = \frac{\sum x f}{200} = 1.46.
$$

So the total number of accidents in 200 days is

$$
200 \times 1.46 = 292.
$$

Now, the total number of accidents computed from the frequency distribution is

$$
0\cdot46 + 1\cdot f_1 + 2\cdot f_2 + 3\cdot25 + 4\cdot10 + 5\cdot f_5 = 292.
$$

Calculate the contribution from the known parts:

$$
3\cdot25 = 75,\quad 4\cdot10 = 40.
$$

So the known contribution is

$$
75+40=115.
$$

Thus, the unknowns must satisfy

$$
1\cdot f_1 + 2\cdot f_2 + 5\cdot f_5 = 292 - 115 = 177. \tag{2}
$$

Now we have two equations:

1. $ f_1 + f_2 + f_5 = 119 $
2. $ f_1 + 2f_2 + 5f_5 = 177 $

Subtract (1) from (2):

$$
(f_1 + 2f_2 + 5f_5) - (f_1 + f_2 + f_5) = 177 - 119,
$$

$$
(2f_2 - f_2) + (5f_5 - f_5) = 58,
$$

$$
f_2 + 4f_5 = 58. \tag{3}
$$

Now, from (3) we can express

$$
f_2 = 58 - 4f_5.
$$

Substitute this into (1):

$$
f_1 + (58 - 4f_5) + f_5 = 119,
$$

$$
f_1 = 119 - 58 + 3f_5 = 61 + 3f_5.
$$

Thus the missing frequencies are given by:

$$
f_1 = 61 + 3f_5,\quad f_2 = 58 - 4f_5,\quad f_5 = f_5.
$$

Since frequencies must be nonnegative integers, $f_5$ can be any integer such that $f_2 = 58 - 4f_5 \ge 0$. This gives

$$
4f_5 \le 58 \quad \Rightarrow \quad f_5 \le 14.
$$

There is not a unique solution unless we have extra information (for example, if the data suggest that days with 5 accidents are very rare, one might take $f_5 = 0$). A natural (and common) choice is to take $f_5 = 0$ (i.e. no day had 5 accidents), so that the distribution is concentrated in the lower accident numbers.

If we set $f_5 = 0$:

- Then $f_2 = 58 - 4(0) = 58$.
- And $f_1 = 61 + 3(0) = 61$.

Check the totals:

- Total frequency: $46 + 61 + 58 + 25 + 10 + 0 = 200$.
- Total accidents: $0\cdot46 + 1\cdot61 + 2\cdot58 + 3\cdot25 + 4\cdot10 + 5\cdot0 = 61 + 116 + 75 + 40 = 292$.
- Mean $= 292/200 = 1.46$.

Everything checks.

### **Final Answer**

A very acceptable solution is:

- **Frequency for 1 accident:** 61 days
- **Frequency for 2 accidents:** 58 days
- **Frequency for 5 accidents:** 0 days

This gives the correct total frequency (200 days) and the overall mean of 1.46 accidents per day.

## <mark> 37) Calculate Sample mean, sample variance, sample skewness and sample kurtosis from the following grouped data: </mark>

| Class Interval | Frequency |
| -------------- | --------- |
| 2-4            | 3         |
| 4-6            | 4         |
| 6-8            | 2         |
| 8-10           | 1         |

Let's denote the mid‐points (x) for each class interval and use the frequencies (f) to calculate the sample statistics. The data are:

| Class Interval | f   | Midpoint (x) |
| -------------- | --- | ------------ |
| 2–4            | 3   | 3            |
| 4–6            | 4   | 5            |
| 6–8            | 2   | 7            |
| 8–10           | 1   | 9            |

The total number of observations is:

$$
n = 3+4+2+1 = 10.
$$

We'll now compute each required statistic step‐by‐step.

### 1. Sample Mean

The sample mean is given by:

$$
\bar{x} = \frac{\sum f\,x}{n}.
$$

Calculate the sum of $f\,x$:

$$
\sum f\,x = 3(3) + 4(5) + 2(7) + 1(9) = 9 + 20 + 14 + 9 = 52.
$$

Thus,

$$
\bar{x} = \frac{52}{10} = 5.2.
$$

### 2. Sample Variance and Standard Deviation

The sample variance is computed by:

$$
s^2 = \frac{\sum f\,(x-\bar{x})^2}{n-1}.
$$

First, compute the deviations for each midpoint:

| x   | f   | $x-\bar{x}$    | $(x-\bar{x})^2$   | Contribution $f(x-\bar{x})^2$ |
| --- | --- | -------------- | ----------------- | ----------------------------- |
| 3   | 3   | $3-5.2 = -2.2$ | $(-2.2)^2 = 4.84$ | $3 \times 4.84 = 14.52$       |
| 5   | 4   | $5-5.2 = -0.2$ | $(-0.2)^2 = 0.04$ | $4 \times 0.04 = 0.16$        |
| 7   | 2   | $7-5.2 = 1.8$  | $1.8^2 = 3.24$    | $2 \times 3.24 = 6.48$        |
| 9   | 1   | $9-5.2 = 3.8$  | $3.8^2 = 14.44$   | $1 \times 14.44 = 14.44$      |

Now, sum the contributions:

$$
\sum f\,(x-\bar{x})^2 = 14.52 + 0.16 + 6.48 + 14.44 = 35.60.
$$

Then the sample variance is:

$$
s^2 = \frac{35.60}{10-1} = \frac{35.60}{9} \approx 3.956.
$$

And the sample standard deviation is:

$$
s \approx \sqrt{3.956} \approx 1.99.
$$

### 3. Sample Skewness

A common formula for sample skewness (using the adjusted moment estimator) is:

$$
g_1 = \frac{n}{(n-1)(n-2)}\sum f\,\left(\frac{x-\bar{x}}{s}\right)^3.
$$

Let's compute $(x-\bar{x})^3$ for each midpoint:

| x   | f   | $x-\bar{x}$ | $(x-\bar{x})^3$      | Contribution $f(x-\bar{x})^3$  |
| --- | --- | ----------- | -------------------- | ------------------------------ |
| 3   | 3   | $-2.2$      | $(-2.2)^3 = -10.648$ | $3 \times (-10.648) = -31.944$ |
| 5   | 4   | $-0.2$      | $(-0.2)^3 = -0.008$  | $4 \times (-0.008) = -0.032$   |
| 7   | 2   | $1.8$       | $1.8^3 = 5.832$      | $2 \times 5.832 = 11.664$      |
| 9   | 1   | $3.8$       | $3.8^3 = 54.872$     | $1 \times 54.872 = 54.872$     |

Sum of the contributions:

$$
\sum f\,(x-\bar{x})^3 \approx -31.944 - 0.032 + 11.664 + 54.872 = 34.56.
$$

Now, standardize by dividing each deviation by $s$ before cubing would yield the same overall ratio; here we can combine it as:

$$
g_1 = \frac{10}{(9 \times 8)} \times \frac{34.56}{s^3}.
$$

Note: $(n-1)(n-2) = 9 \times 8 = 72$ and $n = 10$, so the multiplier is:

$$
\frac{10}{72} \approx 0.1389.
$$

We already have $s \approx 1.99$, so:

$$
s^3 \approx 1.99^3 \approx 1.99 \times 3.956 \approx 7.88.
$$

Thus:

$$
g_1 \approx 0.1389 \times \frac{34.56}{7.88} \approx 0.1389 \times 4.387 \approx 0.608.
$$

So, the sample skewness is approximately **0.61**, indicating a moderate positive skew.

### 4. Sample Kurtosis

A commonly used formula for sample excess kurtosis (adjusted) is:

$$
g_2 = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum f\left(\frac{x-\bar{x}}{s}\right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}.
$$

Here, $n=10$, so:

- $n(n+1) = 10 \times 11 = 110$,
- $(n-1)(n-2)(n-3) = 9 \times 8 \times 7 = 504$,
- The first multiplier is $110/504 \approx 0.2183$.

Now compute $(x-\bar{x})^4$ for each midpoint:

| x   | f   | $x-\bar{x}$ | $(x-\bar{x})^4$                      | Contribution $f(x-\bar{x})^4$       |
| --- | --- | ----------- | ------------------------------------ | ----------------------------------- |
| 3   | 3   | $-2.2$      | $(-2.2)^4 = (2.2^4) \approx 23.4256$ | $3 \times 23.4256 \approx 70.277$   |
| 5   | 4   | $-0.2$      | $(-0.2)^4 = 0.0016$                  | $4 \times 0.0016 = 0.0064$          |
| 7   | 2   | $1.8$       | $1.8^4 \approx 10.4976$              | $2 \times 10.4976 \approx 20.995$   |
| 9   | 1   | $3.8$       | $3.8^4 \approx 208.5136$             | $1 \times 208.5136 \approx 208.514$ |

Sum of contributions:

$$
\sum f (x-\bar{x})^4 \approx 70.277 + 0.0064 + 20.995 + 208.514 \approx 300.792.
$$

Next, we need $s^4$. We have $s^2 \approx 3.956$, so:

$$
s^4 = (3.956)^2 \approx 15.648.
$$

Now, the standardized fourth moment is:

$$
\frac{\sum f (x-\bar{x})^4}{n\, s^4} \quad \text{(for population, but here we use the adjusted formula below)}.
$$

Using the adjusted formula:

$$
g_2 = 0.2183 \times \left(\frac{300.792}{15.648}\right) - \frac{3(9^2)}{8 \times 7}.
$$

Calculate the ratio:

$$
\frac{300.792}{15.648} \approx 19.22.
$$

Thus, first term:

$$
0.2183 \times 19.22 \approx 4.195.
$$

Now, compute the second term:

$$
\frac{3(n-1)^2}{(n-2)(n-3)} = \frac{3 \times 9^2}{8 \times 7} = \frac{3 \times 81}{56} = \frac{243}{56} \approx 4.339.
$$

Then,

$$
g_2 \approx 4.195 - 4.339 \approx -0.144.
$$

This $g_2$ is the **excess kurtosis**. A normal distribution has excess kurtosis 0 (or a raw kurtosis of 3).  
Thus, the sample kurtosis (excess) is approximately **–0.14**, meaning the distribution is slightly **platykurtic** (flatter than a normal distribution).

### 5. Final Answers

- **Sample Mean:** 5.2
- **Sample Variance:** ≈ 3.96
- **Sample Standard Deviation:** ≈ 1.99
- **Sample Skewness:** ≈ 0.61 (indicating a moderate positive skew)
- **Sample Kurtosis (Excess):** ≈ –0.14 (or a raw kurtosis of about 2.86, indicating a slightly platykurtic distribution)

These values summarize the central tendency, spread, and shape characteristics of the grouped data.
