# Monte Carlo Simulation

The technique was first developed by Stanislaw Ulam, a mathematician who worked on the Manhattan Project.

A method of estimating the value of an unknown quantity using the principles of inferential statistics.

## Inferential Statistics

- Population : Set of examples
- Sample : proper subset of population
- **Random** sample tends to exhibit the same qualities as the population.

Confidence depends on:

- sample size
- variance. As variance grows, larger samples are required to have the same degree of confidence.

## Roulette Considerations

- Law of large numbers (Bernoulli's law)
    If the probability is p, the difference between the prob obtained by samples to p goes to 0 as number of samples goes to infinity.

- Gambler's Fallacy and Regression to the mean

Gambler's Fallacy: if a particular event occurs more frequently than normal during the past it is less likely to happen in the future (or vice versa), when it has otherwise been established that the probability of such events does not depend on what has happened in the past.

Regression to the mean: Following an extreme random event, it is likely that the next random event will be **less extreme**.

## Quantifying Variation

$$ variance(X) = \frac{\sum_{x\in X}(x - \mu)^2}{|X|} $$

$$\mu$$ is mean

$$\sigma(x) = \sqrt{variance(X)}$$

- outliers have a big effect
- standard deviation always considered relative to mean

## Empirical Rule

- approx. 68% of data within one standard deviation of mean
- approx. 95% of data within 1.96 standard deviation of mean - usually used
- approx. 99.7% of data within 3 standard deviation of mean

### Assumptions

- mean estimation error is zero. Therefore no bias
- The distribution of errors in estimates is normal (mean=zero, sd=1)

## Probability Density Function

- Distributions defined by Probability Density Function, PDF
- Probability of a random value lying between two values
- Defines a curve where the range in the X-axis is between the maximum and minimum values of the variable.
- Area under curve between two points defined the probability of an example falling in that range
