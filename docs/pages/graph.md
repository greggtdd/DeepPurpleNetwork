<div align="center"><a href="https://greggtdd.github.io/DeepPurpleNetwork/"><img src="https://raw.githubusercontent.com/greggtdd/DeepPurpleNetwork/master/docs/site_images/dpnetwork_banner.png"></a></div>

___

<div align="center"><a href="https://greggtdd.github.io/DeepPurpleNetwork/pages/project"><img src="https://raw.githubusercontent.com/greggtdd/DeepPurpleNetwork/master/docs/site_images/button_proj.png"  width="150" height="35"></a> <a href="https://greggtdd.github.io/DeepPurpleNetwork/pages/graph"><img src="https://raw.githubusercontent.com/greggtdd/DeepPurpleNetwork/master/docs/site_images/button_graph.png"  width="150" height="35"></a> <a href="https://greggtdd.github.io/DeepPurpleNetwork/pages/dp_universe"><img src="https://raw.githubusercontent.com/greggtdd/DeepPurpleNetwork/master/docs/site_images/button_univ.png"  width="150" height="35"></a> <a href="https://greggtdd.github.io/DeepPurpleNetwork/pages/bibliography"><img src="https://raw.githubusercontent.com/greggtdd/DeepPurpleNetwork/master/docs/site_images/button_biblio.png"  width="150" height="35"></a> <a href="https://github.com/greggtdd/DeepPurpleNetwork" target="_blank"><img src="https://raw.githubusercontent.com/greggtdd/DeepPurpleNetwork/master/docs/site_images/button_git.png"  width="150" height="35"></a></div>

___

![The Deep Purple Network Project](https://github.com/greggtdd/DeepPurpleNetwork/blob/master/docs/site_images/dpgraph_banner.png?raw=true)

# The Graph
<div style="text-align: justify">The <a href="https://github.com/greggtdd/DeepPurpleNetwork/blob/master/dp_union_edges.csv" target="_blank">dataset</a> used for this project has been made from scratch, by searching all the required information from my collection of Purple-related books, album liner-notes, fanzines and specialized websites. This CSV file includes (to this day) 7915 rows, distributed across 5 columns. Each column indicates the <b>source</b>, the <b>target</b>, the <b>type</b> of a specific associated act (Band, Album, Event, etc.), the <b>universe</b> and the <b>density</b> of each node respectively. The nodes represent the involved artists (written in lowercase characters) and their associated acts (typed in uppercase), while the links show their reciprocal interactions. The size of a single node is based on the number of collaborations of the corresponding musician, while the thickness of its links represent the weight of the potential relationship between the selected artist and a member of Deep Purple. Since the dataset is costanlty updated, the density used for measuring the activity of a node, is computed by calling the <code>weight_sources()</code> method, inside the <b>DataFramer</b> class of the <a href="https://github.com/greggtdd/DeepPurpleNetwork/blob/master/graph_bouncer.py" target="_blank">graph_bouncer.py</a> module. The majority of the bands are distinguished by the different line-ups that occurred over the years (e.g. <code>DEEP PURPLE #1</code>, <code>WHITESNAKE #3</code>, <code>BLACK SABBATH #1</code>, etc.), hence the universe tag denotes the main group to which each formation belongs. Hence, for example, the targets <code>DEEP PURPLE #2</code> and <code>DEEP PURPLE #3</code> have been included under the <code>Deep Purple</code> universe, while <code>WHITESNAKE #3</code> and <code>WHITESNAKE #4</code> have been merged into the <code>Whitesnake</code> universe even if many of their members were in common. This matching pattern is the main idea on which the DataFramer class is based (see the figure below).<br>
<br>
<a href="https://github.com/greggtdd/DeepPurpleNetwork/blob/master/docs/site_images/dp_module_algorithm.jpg?raw=true" target="_blank"><img src="https://github.com/greggtdd/DeepPurpleNetwork/blob/master/docs/site_images/dp_module_algorithm.jpg?raw=true"></a>
<sub>Filtering the original data frame and detecting network communities with <b>DataFramer</b> and <b>Networker</b> custom classes.</sub><br>
<br>
Therefore, each universe acts as a sort of default clustering partition, which lets the user able to explore the graph by looking at a specific archetype of nodes community, detected for the single artist, whose name is entered as a query by the user itself. This kind of data visualization has been developed in order to let the user be able to navigate inside the network without having to iterate through all the edges of the original graph - it would be really hard to load it, given its size - and extracting the relevant parts of the network for each desired artist. When selecting a specific artists from which to generate the related graph, all the neighbors are chosen according to the most appropriate targets and universe that are in common with the selected name. For example, when choosing <code>Ritchie Blackmore</code>, Don Airey will appear as his neighbor since they have been both in Deep Purple (even if in different formations); but, when selecting <code>Glenn Tipton</code>, <code>Don Airey</code> will appear as a member of the Judas Priest universe - given his many collaborations with the band and with Glenn Tipton himself - and not as a Deep Purple member. Moving accross the original network, the most remote nodes represent musicians that can be considered marginal in the context of this analysis. Therefore, when choosing one of them from the dropdown menu, this would be included in a very small universe, which, at first, could seem not so relevant in the Purple family context, but its neighbors surely are. For example, when plotting <code>Alex Machacek</code>'s graph, no members of Deep Purple are shown, but his neighbors <code>Eddie Jobson</code> and <code>Marco Minnemann</code> collaborated with <code>Roger Glover</code> and <code>Joe Satriani</code> amongst others, so their relationship with a Deep Purple member is interpreted as the path that passes through all the involved nodes (see figure below). In order to avoid graph over-fitting, the numerous solo albums line-ups have been taken into account only if they were particularly determinant in finding stable connections between the involved musicians.</div>
<br>
<a href="https://github.com/greggtdd/DeepPurpleNetwork/blob/master/docs/site_images/dpnetowrk_connected.jpg?raw=true" target="_blank"><img src="https://github.com/greggtdd/DeepPurpleNetwork/blob/master/docs/site_images/dpnetowrk_connected.jpg?raw=true"></a>
<sub>Paths between a marginal node and two Deep Purple members. <em>Deep Purple Mk6</em> is a connected component inside the original graph.</sub>


## Start Exploring
Click on a Binder badge below, depending on your device.<br>
After landing on a new page, start exploring the **DP** family graph!

💻 **Desktop Visualization:**

<a href="https://mybinder.org/v2/gh/greggtdd/DeepPurpleNetwork/master?urlpath=%2Fapps%2FDPNetworkDesktopApp.ipynb%3Fappmode_scroll%3D0" target="_blank"><img src="https://mybinder.org/badge_logo.svg"></a>


📱 **Mobile Visualization:**

<a href="https://mybinder.org/v2/gh/greggtdd/DeepPurpleNetwork/master?urlpath=%2Fapps%2FDPNetworkMobileApp.ipynb%3Fappmode_scroll%3D0" target="_blank"><img src="https://mybinder.org/badge_logo.svg"></a>


___
<sub>© 2020 Gregorio Tedde. Made for analysis purpose.</sub><br>
<sub>This project is licensed under the Creative Commons Zero v1.0 Universal License. <a href="https://github.com/greggtdd/DeepPurpleNetwork/blob/master/LICENSE" target="_blank">Click here</a> for more details.</sub>
