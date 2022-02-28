# ml_from_scratch

Implementation of ML algorithms from scratch

## Algorithms

- ID3
- SVM
- Fuzzy Inference (Madani)
- Fuzzy Rule Generation (Wang-Mendel)
- k-means
- weiszfeld algorithm
- **Linear Regression**
  - **Gradient Descent Plotting**. Plots cost as a function of two coefficients in univariate gradient descent and the coefficients of the gd algorithm. (**univariate_gd_analysis.py**)
  - **Data Generation**. Generation of:
    - Single feature linear function with error dataset (**dataset_generation_1f.py**)
    - Two feature linear function with error dataset (**dataset_generation_2f.py**)
  - **Univariate Linear Regression** [Notes here](https://carmelgafa.com/tags/linear-regression/) and [here](https://carmelgafa.com/post/ml_linearreg_univariatepython/)
    - Linear Regression solution of single feature dataset (**univariate_lr.py**)
  - **Multivariate Linear Regression**. [Notes here](https://carmelgafa.com/post/ml_linearreg_multivariate/) and [here](https://carmelgafa.com/post/ml_linearreg_multivariatepython/)
    - Linear Regression solution of two feature datatset (**multivariate_lr.py**)
  - **Batch Gradient Descent**. [Notes here](https://carmelgafa.com/post/ml_linearreg_gradientdescent/) and [here](https://carmelgafa.com/post/ml_linearreg_multivariatedescent/)
    - Univariate Batch Gradient Descent , no Vectorization (**uni_batch_gd_nv.py**)
    - Univariate Batch Gradient Descent , with Vectorization (**uni_batch_gd_v.py**)
    - Two Feature Batch Gradient Descent , with Vectorization (**twofeature_batch_gd.py**)
    - N Feature Batch Gradient Descent , with Vectorization (**multifeature_batch_gd.py**). Assuming labels name is 'y'
  - **Stochastic Gradient Descent**. Notes [here](https://carmelgafa.com/post/ml_linearreg_stochasticgd/)
    - Univariate Stochastic Gradient Descent, exits on maximum epochs reached(**stochastic_gd_1f_1**)
    - Univariate Stochastic Gradient Descent, exits on minimum error reached or convergence of training set cost. Plots cost. (**stochastic_gd_1f_2**)
    - N Feature Stochastic Gradient Descent, exits on maximum epochs reached(**stochastic_gd_nf_1**)
    - N Feature Stochastic Gradient Descent, exits on minimum error reached or convergence of training set cost.(**stochastic_gd_nf_2**)
  - **Mini Batch Gradient Descent**. Notes [here](https://carmelgafa.com/post/ml_linearreg_minibatchgd/)
    - Multivariate Mini Batch Gradient Descent, exit when cost converges on max epochs reached(**minibatch_gd_1**)
    - Multivariate Mini Batch Gradient Descent,  exit when cost converges on max epochs reached. Uses validation set(**minibatch_gd_2**)
    - Multivariate Mini Batch Gradient Descent,  exit when cost converges on max epochs reached. Uses validation set and momentum(**minibatch_gd_3**)
    - Example of Mini Batch Gradient Descent, plots the gradient descent(**minibatch_gd_2_v.py**)
- logistic regression

### John Guttag MIT worked examples

- Brute force resolution
- Graph Theory (BFS, DFS)
- Greedy algorithms
- Stochastic Techniques
- Monte Carlo Simulation
- Random Walk

### Utilities

- Tree structure

## Change log

- **24022022** : Mini Batch and Stochastic Gradient Descent.
- **18012022** : Gradient Descent Generic multivariate.
- **13012022** : Linear Regression.
- **13012022** : Reorganization of the code.
- **08092020** : Added id3_v2 class to compute ID3.
- **28122020** : Added Greedy algorithm.
- **08012021** : Added Graphs, Monte Carlo, Stochastic, Random walk.
- **14122021** : Added k-means in Excel.
