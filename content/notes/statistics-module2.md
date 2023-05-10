# Statistics - Module 2

# Probability Theory

Probability theory is a fundamental branch of mathematics that deals with the study of random events. It is an important tool used in various fields such as finance, science, engineering, and social sciences.

### Introduction to Probability

Probability is the measure of the likelihood of an event occurring. It is expressed as a number between 0 and 1, with 0 indicating that the event is impossible and 1 indicating that the event is certain to occur.

### Probability Rules and Laws

There are various rules and laws that govern probability theory, such as the addition rule, multiplication rule, and Bayes' theorem. These rules and laws help to calculate the probability of complex events.

### Probability Distributions

Probability distributions are mathematical functions that describe the likelihood of different outcomes in a random event. Common probability distributions include the normal distribution, binomial distribution, and Poisson distribution.

### Examples

Some examples of probability theory in action include predicting the outcome of a coin toss, estimating the probability of a stock market crash, and calculating the likelihood of a disease outbreak.

### Elementary Outcome and Sample Space

An **elementary outcome** is a single possible outcome of a random event. It is not necessarily a single number, but it simply corresponds to a single observed result. For example, in a game where 3 coin tosses are taken as a single result, the whole of the 3 tosses will be the elementary outcome. 

The **sample space** is the set of all possible elementary outcomes of a random event. For example, when flipping a coin, the sample space is {heads, tails}, and each of these outcomes is an elementary outcome. The sample space can be finite, countably infinite, or uncountably infinite, depending on the event being studied.

A **finite sample space** is a sample space with a finite number of possible outcomes. An example of a finite sample space is rolling a six-sided die, with a sample space of {1, 2, 3, 4, 5, 6}.

A **countably infinite sample space** is a sample space with a countably infinite number of possible outcomes. An example of a countably infinite sample space is rolling a pair of six-sided dice, with a sample space of {(1,1), (1,2), (1,3), ..., (6,5), (6,6)}.

An **uncountably infinite sample space** is a sample space with an uncountably infinite number of possible outcomes. An example of an uncountably infinite sample space is choosing a real number at random from the interval [0,1]. The sample space in this case is the entire interval [0,1], which has an uncountably infinite number of possible outcomes.

### Cardinality of the Sample Space

The cardinality of a sample space is the number of possible outcomes in the sample space. For example, the sample space of flipping a coin has a cardinality of 2, as there are two possible outcomes: heads and tails. 

### Simple and Compound Events

A **simple event** is an event that consists of a single elementary outcome. For example, if we roll a six-sided die, the event "rolling a 2" is a simple event.

A **compound event** is an event that consists of two or more elementary outcomes. For example, if we roll a six-sided die twice and record the numbers, the event "rolling a 2 on the first roll and a 3 on the second roll" is a compound event.

Compound events can be classified as either independent or dependent. Two events are **independent** if the occurrence of one event does not affect the probability of the other event occurring. For example, flipping a coin twice and getting heads on the first flip does not affect the probability of getting heads on the second flip.

Two events are **dependent** if the occurrence of one event affects the probability of the other event occurring. For example, drawing a card from a deck and then drawing another card without replacing the first card affects the probability of the second card being a certain value, as it depends on the value of the first card drawn.

Let A and B be two arbitrary events defined on a same sample space Omega.

- The **union of A and B** is the event that either A or B or both occur, denoted A ∪ B. For more than 2 events, the union is the set of elementary outcomes that satisfy **all** of the event conditions.
- The **intersection of A and B** is the event that both A and B occur, denoted A ∩ B. For more than 2 events, the union is the set of elementary outcomes that satisfy **at least one** event condition.
- The **complementary of A** is the event that A does not occur, denoted A<sup>C</sup> or A<sup>'</sup>.

### Events can be considered as sets of Points

Each event can be considered as a set of points in the sample space. The union of events A and B is the set of points that belong to either A or B or both. The intersection of events A and B is the set of points that belong to both A and B. The complementary of event A is the set of points that do not belong to A. These concepts can be used to calculate probabilities of events and to solve probability problems.

When we consider events as sets of points in the sample space, we can use set operations to combine or compare events. For example, let's say we have two events A and B, defined on the same sample space. We can define the union of A and B, denoted as A ∪ B, as the set of all points that belong to A or B or both. The intersection of A and B, denoted as A ∩ B, is the set of all points that belong to both A and B. Finally, the complementary of A, denoted as A', is the set of all points that do not belong to A.

These set operations can be used to calculate probabilities of events. For example, if we know the probabilities of events A and B, we can use the formula P(A ∪ B) = P(A) + P(B) - P(A ∩ B) to calculate the probability of the union of A and B. Similarly, we can use the formula P(A ∩ B) = P(A) * P(B|A) to calculate the probability of the intersection of A and B, where P(B|A) is the conditional probability of event B given that event A has occurred.

Understanding events as sets of points also allows us to classify events as simple or compound, and as independent or dependent. A simple event is an event that consists of a single elementary outcome, while a compound event consists of two or more elementary outcomes. Two events are independent if the occurrence of one event does not affect the probability of the other event occurring, while two events are dependent if the occurrence of one event affects the probability of the other event occurring.

**Partition of the Sample Space**

A partition of the sample space is a collection of events that are mutually exclusive and collectively exhaustive. This means that each event in the partition cannot occur at the same time as any other event in the partition, and that the events in the partition cover all possible outcomes in the sample space.

For example, if we roll a six-sided die, a partition of the sample space would be {1, 2, 3} and {4, 5, 6}. These two events are mutually exclusive because a roll of the die cannot result in both an outcome in the first set and an outcome in the second set. They are also collectively exhaustive because every possible outcome of the roll is included in one of the two sets.

Partitions of the sample space are useful in probability theory because they allow us to break a complex event down into simpler, mutually exclusive events. This can make it easier to calculate probabilities and to solve probability problems.

For a collection of events to be considered a partition of the sample space, the events must satisfy two conditions:

1. The events must be **mutually exclusive**, meaning that no two events can occur at the same time.
2. The events must be **collectively exhaustive**, meaning that at least one of the events must occur. 

These two conditions ensure that every possible outcome in the sample space is included in one and only one of the events in the partition. Obviously each partition has to have a positive chance of occurring.

### Kolmogorov Axioms

Kolmogorov's three axioms of probability are as follows:

1. The probability of any event is a non-negative real number.
2. The probability of the entire sample space is 1.
3. If A1, A2, ..., are mutually exclusive events (i.e. they cannot occur simultaneously), then the probability of the union of these events is equal to the sum of their individual probabilities: P(A1 ∪ A2 ∪ ...) = P(A1) + P(A2) + ...

These axioms are the foundation of probability theory, and they allow us to define a probability measure for any sample space. The probability measure assigns probabilities to events in the sample space, and is used to calculate the likelihood of different outcomes and to solve probability problems.

Kolmogorov's axioms can be extended to more complex events using the rules of probability theory, such as the addition rule and the multiplication rule. These rules allow us to calculate the probability of compound events, such as the probability of rolling a 3 on a six-sided die twice in a row.

In summary, Kolmogorov's axioms provide a rigorous framework for defining and calculating probabilities, and are the foundation of probability theory.

### Random Variables

A random variable is a variable whose value is determined by the outcome of a random process or experiment. In other words, it is a variable that takes on different values with different probabilities based on some underlying probability distribution.

For example, consider rolling a fair six-sided die. The outcome of the roll is a random variable, since we cannot predict with certainty which face of the die will land face up. The possible values of this random variable are the integers 1 through 6, each with a probability of 1/6.

Random variables are important in probability theory and statistics because they allow us to study the behavior of complex systems in a probabilistic manner. They can be discrete or continuous, depending on whether they take on a finite or infinite number of values. Additionally, they can be described by various statistical measures such as the mean, variance, and probability distribution function.

## Discrete vs Continuous random variables

In probability theory, random variables are used to represent the outcomes of random events in mathematical terms. Random variables can be classified into two main categories: discrete and continuous.

A discrete random variable is one that can only take on a countable number of possible values. For example, the number of heads in three coin flips is a discrete random variable that can only take on the values 0, 1, 2, or 3.

On the other hand, a continuous random variable can take on an infinite number of possible values within a certain range. For example, the weight of a randomly selected apple from a basket is a continuous random variable that can take on any value between 0 and the weight of the heaviest apple in the basket.

One key difference between the two types of random variables is that a probability distribution for a discrete random variable can be represented using a probability mass function (PMF), while a probability distribution for a continuous random variable can be represented using a probability density function (PDF). The PMF gives the probability that the random variable takes on a particular value, while the PDF gives the probability density at each point in the range of the random variable.

Another important difference is that the probabilities associated with a discrete random variable are discrete probabilities, meaning that they are represented by individual points on a probability distribution. In contrast, the probabilities associated with a continuous random variable are continuous probabilities, meaning that they are represented by the area under a curve on a probability distribution.

In summary, the key differences between discrete and continuous random variables lie in the possible values they can take, the type of probability distribution used to represent them, and the nature of the probabilities associated with them.
