#Bar Chart Example 
# Make your chart here
plt.figure(figsize=(10, 8))
plt.bar(range(len(years)), past_years_averages,	yerr = error, capsize=5)
plt.axis([-.5, 6.5, 70, 95]) 
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.xlabel('Year') 
plt.ylabel('Test average') 
plt.title('Final Exam Averages')
plt.savefig('my_bar_chart.png')
plt.show()

#Side by Side Bar Example
import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]
# Make your chart here
#Create a figure of width 10 and height 8.
plt.figure(figsize=(10, 8))
#Create a set of axes and save them to ax.
ax = plt.subplot()
#sets zoom of graph
plt.axis([0, 10, 70, 90]) 
#Create a new list of x-values called middle_x, which are the values in the middle of school_a_x and school_b_x. This is where we will place the x-ticks. Look at the final graph to see this placement.
#Use list comprehension and zip to create middle_x:
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
#Set the x-tick labels to be the list unit_topics.
ax.set_xticklabels(unit_topics)
# Create a legend, as shown in the final graph, that labels the first set of bars Middle School A and the second set of bars Middle School B.
n = 1 # This is our first dataset (out of 2) 
t = 2 # Number of datasets 
d = 5 # Number of sets of bars 
w = 0.8 # Width of each bar 
x_values1 = [t*element + w*n for element in range(d)]
plt.bar(school_a_x, middle_school_a)
n = 2 # This is our first dataset (out of 2) 
t = 2 # Number of datasets 
d = 5 # Number of sets of bars 
w = 0.8 # Width of each bar 
x_values1 = [t*element + w*n for element in range(d)]
plt.bar(school_b_x, middle_school_b)
plt.legend(['Middle School A', 'Middle School B'])
plt.title('Test Averages on Different Units')
plt.xlabel('Unit') 
plt.ylabel('Test Average') 
plt.savefig('my_side_by_side.png')
plt.show()

#Stacked Bars Example
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)

#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
#Create a figure of width 10 and height 8.
plt.figure(figsize=(10, 8))

#create your plot here
plt.bar(range(len(As)), As)
plt.bar(range(len(Bs)), Bs, bottom=As)
plt.bar(range(len(Cs)), Cs, bottom=c_bottom)
plt.bar(range(len(Ds)), Ds, bottom=d_bottom)
plt.bar(range(len(Fs)), Fs, bottom=f_bottom)
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title('Grade Distrobution')
plt.legend(['A', 'B', 'C', 'D', 'E', 'F'], loc=3)
plt.show()
plt.savefig('my_stacked_bar.png')

#Histogram Example
plt.figure(figsize=(10, 8))
plt.hist(exam_scores1, bins=12, normed=True, histtype = 'step', linewidth=2)
plt.hist(exam_scores2, bins=12, normed=True, histtype = 'step', linewidth=2) 
plt.legend(['1st Yr Teaching', '2nd Yr Teaching'], loc=2)
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.title('Final Exam Score Distribution')
plt.savefig('my_histogram.png')
plt.show()

#Pie Chart Example
plt.figure(figsize=(10, 8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
plt.axis('equal') 
plt.title('Hardest Topics')
plt.savefig('my_pie_chart.png')
plt.show()

#Line with Shaded Error Example
plt.figure(figsize=(10,8))

# Create your hours_lower_bound and hours_upper_bound lists here Create a list hours_lower_bound, which has the elements of hours_reported minus 20%, and a list hours_upper_bound, which has the elements of hours_reported plus 20%.
plt.plot(exam_scores, hours_reported, linewidth=2)
hours_lower_bound = [i - i*.2 for i in hours_reported]
hours_upper_bound = [i + i*.2 for i in hours_reported]
# Make your graph here

plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)
plt.title('Time spent studying vs final exam scores')
plt.xlabel('Score')
plt.ylabel('Hours studying (self-reported)')
plt.savefig('my_line_graph.png')
plt.show()

