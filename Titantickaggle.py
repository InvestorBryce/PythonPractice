import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
# %matplotlib inline doesn't work, so I'll use plt.show()
import seaborn as sns
sns.set_style("darkgrid")

#import warnings
#arnings.filterwarnings('ignore')

titanic = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# LET THE CODING BEGIN
def main():
	pass

def description():
	print (titanic.describe(include = "all"))
	print (titanic.sample(5))
	print(pd.isnull(titanic).sum())
	
# datatype for each column - PassengerID(int), Survived(bool), Pclass(int), Name(str), Sex(str),
# Age(float), SibSp(int), Parch(int), Ticket(str), Fare(float), Cabin(str), Embarked (str).

# survival by sex in simple bar graph, PercentFormatter sets yaxis to percentages
def survived_sex():
	ax = sns.barplot(x = "Sex", y = "Survived", data = titanic)
	ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
	plt.title("Titanic Survival Rates by Sex")
	plt.ylabel("Survival Rate")
	plt.savefig('Survived_by_Sex')
	plt.show()

# print out the percentages for survival by boarding class
def survived_class():
	print("Percentage of Pclass = 1 who survived:", titanic["Survived"][titanic["Pclass"] == 1].value_counts(normalize=True)[1]*100)
	print("Percentage of Pclass = 2 who survived:", titanic["Survived"][titanic["Pclass"] == 2].value_counts(normalize=True)[1]*100)
	print("Percentage of Pclass = 3 who survived:", titanic["Survived"][titanic["Pclass"] == 3].value_counts(normalize=True)[1]*100)

# factorplot of similar data
def survived_class_sex():
	sns.factorplot("Pclass", "Survived", "Sex", data=titanic, kind="bar", palette="muted", legend=True)
	plt.xlabel('Passenger Class')
	plt.ylabel('Survival Rate')
	plt.title('Survival Rate by Passenger Class & Sex')
	plt.savefig('Survived_by_Class&Sex')
	plt.show()

# Difficult visualization; need to place all passengers into age group bins and re-graph it. Afterwards, auto-save the figure.
def survived_agegroups():
	titanic["Age"] = titanic["Age"].dropna()
	# used dropna() over fillna() as I don't want a column for unknown age passengers
	test["Age"] = test["Age"].dropna()
	bins = [0, 1, 5, 12, 18, 30, 40, 50, np.inf]
	labels = ['Infant', 'Toddler', 'Child', 'Teenager', '20s', '30s', '40s', '50s+']
	titanic['Age Groups'] = pd.cut(titanic["Age"], bins, labels=labels)
	test['Age Groups'] = pd.cut(titanic["Age"], bins, labels=labels)

	ax = sns.barplot(x="Age Groups", y="Survived", data=titanic)
	ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
	plt.savefig('Survived_by_AgeGroups')
	plt.show()

# Graph of the distribution of ages aboard the ship
def age_distribution():
	x = titanic["Age"].dropna()
	ax = sns.kdeplot(data=x, shade=True, color="B")
	ax.yaxis.set_major_formatter(mtick.PercentFormatter(0.1))
	plt.title('Age Distribution Aboard The Titanic')
	plt.xlabel('Age of Passengers')
	plt.ylabel('Percent of Total Occupancy')
	plt.show()

# need to clean up this data








if __name__ == "__main__":
	main()
	description()
	survived_sex()
	survived_class_sex()
	survived_agegroups()
	age_distribution()
