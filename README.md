# DA-Unit-5
1 Explain 3 principles of data communication
The Main goal is to Clearly and effectively communicate information

Clear - Uncluttered concise, you can see the point that the graph maker is trying to make, and see how independent variables line up with dependent ones, or two graphs move in tandem.

Easy to Understand, at a glance you can tell categories, and see what is what. Good contrasts for different plots on the same graph, good labeling, avoid giving a distorted picture to the viewer.

Tells a Story, your data shows something happening that's important for the viewer to understand, so for instance a line plot of sales per quarter would highlight a sharp dip and include a % change as a sidebar for the viewer. Anything where the presentation of the data makes a point for the person looking at the graph.

Notes
Don't Distort the Data. For instance don't distort axes or scales to make something small seem larger than it is.
Encourage the Eye to compare different Data. If you think there's a relationship between two pieces of data plot the lines together so you their motion in relation to each other is clear.

Notes
Basic Principles
Clear,
Easy to understand,
Has an impact onthe viewer, tells a story
Specific Principles
Show the data,
think about substance not methods,
don't distort,
present many numbers in a small space.
Make Large Datasets coherent,
Encourage the Eye to comprre different pieces of data.
Reveal the data t several levels of detail, from a broad overview to the fine structure,
serve a reasonably clear purposes: description exploration tabulation or decoration.
Be closely integrated with the statistical and verbal descriptions of a data set.
2 Basic Principles of Visual Perception
Order
The order in which items are preceived, in text this follows standard practices, but in viewing graphs it can be random and sporadic, so each element of the graph needs to be comprehensible on its own to help a viewer flow from first viewing to complete understanding. Also in general people don't remember every item they see, only the first 2 or 3 items, so trying to draw the eye to the important information through color choice helps your message last longer in the mind.

Hierarchy
The eye tends to be drawn towards brighter colors, so you can highlight specific items in such a way that every element fits into part of a story, for instance adding a vertical line in a graph draws the attention to each side of the graph, so pay attention to how the line attracts attention, and make sure it fits in with the context of the story you want your data to tell.

Clarity
If there's a part of the data you want to emphasize use design elements to bring attention to it. Like highlighting, or text on the graph.

Relationships
Humans tend to tell stories that relate things which are together on a graph. We like to form patterns and do so naturally. Presenting data together on a graph will naturally lead viewers to connect them in their heads, don't present false relationships.

Convention
We have some expectations on graph layout, and color palette, for instance we'd expect similar items to have similar colors on a legend. This groups things in our mind. Also some graphs are useful for conveying time information, but poor for conveying % information or bin-like informtion. Violating those expectations can lead to mis-understanding, or rejecting the conclusions of the graph.

Understanding these items can be used to highlight the important data you want to convey, and help you avoid conveying things you don't want to convey.

Gestalt Theory principles
1. Similarity
We tend to group similar items in our minds, whether on shape, or color.  Use this to group items in the viewers mind.
2. Continuity
When viewing lines we want to follow the trend that we see in the line.  
3. Closure
Your brain will fill in missing parts, simple form our brains will follow a simple shape to fill in the information.  
4. Proximity
Our brains will lump things that are close together into the same category
5. Figure/Ground
Foreground background, our brain prefers the foreground, 
6. Symmetry & Order
Your brain will take any visual image in the simplest shape possible.  
3. Choose Appropriate Graphs for the Data
Comparison between values
Bar Chart, Our brains are good at quickly estimating comparative heights and what that means about values of longer or shorter bars.

Comparison to the Whole
Stacked Bar Chart this is good when you don't have segments that are too small, and you have a limited number of segments

or a Treemap Column If you have lots of data, or very small segments, the 2-d nature of the tree map keeps the item from being swallowed.

These are both good tools because they show the size of a rectangle as a proportion of a bigger rectangle, letting you form comparisons in your mind more easily. And our visual system is pretty good about making that comparison naturally, so complex relationships can be conveyed sparsely.

But my default is a stacked bar chart, I generally prefer a pie chart to treemap, but familiarity might have convinced everyone to avoid the pie chart. Actually its disliked because it's misleading

Change over time
Line Chart good for sparse plots my preferred plot, the elements of continuity mean that inflection points stand out naturally.

Area. generally less used, but the best example I have is when continuity would lead you to think lines were crossing, so you can use the hashing to clarify this. Again, generally bad because it fills up white space and clutters the graph.

Column not so good for multiple charts, a line chart is generally the best option

Slope: really only good to prevent clutter when there's a lot of data to convey

My view and the view of the videos tends to favor the line chart for things that aren't too cluttered

Ranking data
Bar chart is the best you can use horizontal charts with the independent variable being the ranking, and then it's easy to see how various choices line up.

Slope chart is ok for seeing how things change.

Correlation
Scatter plot almost all of the time, it shows the relationship of 2 variables

The bubble chart is really only used with a 3rd variable, the size of the bubble relates to the size of the 3rd variable

Geographical charts
A generally bad choice, but color pallets like warm_cool can be used to highlight numerical differences across boundaries. For instance setting the data as say unemployment percentage, with low being blue, high being red, you could easily at glance tell which states are the worst performing. The arbitrariness of geographic lines means that other things can be influencing the independent variable that don't show up in the visualization.

Measuring a target
A simple gauge, can look a bit like a thermometer, or a speed gauge, and those are ergonimically optimal measuring devices, so people have plenty of practicec reading them which aids your communication.

Showing Outliers
A table is good for this you can color in certain cells to highlight the big outliers.

Understanding these lets you communicate effectively. If you're analysis is good but your presentation is unclear important points may not be communicated.

It is easy to lie with statistics. It is hard to tell the truth without it.

Theres an old Mark Twain quote, about "Lies, Damn Lies, and Statistics." I think this follows the same logic as the above quote, it's possible to present a truncated view of the data that's still true, but leads to a conclusion that is not true, this is lieing with statistics. However without a reasonable understanding of the statistical underpinnings of our data, it's easy to accidentally present a picture which is not descriptive of reality. Knowing about skew or kurtosis would convince you to either prune outliers, or be wary of the mean value.