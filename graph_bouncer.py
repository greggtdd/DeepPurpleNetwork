######################################################################################################
# Project: The Deep Purple Network.                                                                  #
# (CC) 2020 Made by Gregorio Tedde just for analysis purpose.                                        #
# Work License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License   #
# Libraries licenses in environment.yml                                                              #
# Git Repo: https://github.com/greggtdd/DeepPurpleNetwork                                            #
# PyVis docs used for this module: https://pyvis.readthedocs.io/en/latest/                           #
# Info: greggtedde@gmail.com                                                                         #
######################################################################################################

import pandas as pd
from pyvis.network import Network
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 500)


class DataFramer():
    """
    Python class for filtering the
    original union edges dataframe.

    Parameters
    ----------
    self.dir: string
        Path of the initial dataframe
    """

    def __init__(self, path):
        self.path = path

    def upload_df(self):
        """
        Reads the dataframe located
        at the specified directory.

        Returns
        -------
        self.data_
        """
        self.data_ = pd.read_csv(self.path)

    def density_sources(self):
        """
        Adds a new column based on
        each source density inside
        the network.

        Returns
        -------
        self.data_.Density
        """
        self.data_['Density'] = \
            self.data_.groupby('Source')['Source'].\
                transform('count')

    def artist_research(self):
        """
        Used for artists research.
        It creates a subset based on
        the original dataframe sources.

        Returns
        -------
        self.sour_
        """
        self.sour_ = []
        for source in self.data_['Source']:
            if source not in self.sour_:
                self.sour_.append(source)
    
    def sub_framer(self, keyw):
        """
        Creates the final subset from which
        the graph is built and defines the
        input lists for sources, targets
        and edges weights.

        Parameters
        ----------
        keyw: string
            Name of artist, band or album.

        Returns
        -------
        self
        """
        if keyw in self.sour_:
            sub_df = self.data_[(self.data_['Source'] == keyw)]
            sub_univ = []
            for univ in sub_df['Universe']:
                if univ not in sub_univ:
                    sub_univ.append(univ)
            sub_df = self.data_[self.data_.Universe.isin(sub_univ)]
            self.sources_ = sub_df['Source']
            self.targets_ = sub_df['Target']
            self.weights_ = sub_df['Density']
        return self

    @staticmethod
    def get_edge_data(sources, targets, weights):
        """
        Creates a collection of tuples
        for linking sources and targerts
        inside the graph.

        Parameters
        ----------
        sources: pandas.core.series.Series
            Sources data.
        targets: pandas.core.series.Series
            Targets data.
        weights: pandas.core.series.Series
            Weights data.
        
        Returns
        -------
        zip
        """
        edge_data = zip(sources, targets, weights)
        return edge_data


class Networker:
    """
    Python class for creating
    a network graph from the
    original dataframe.

    Parameters
    ----------
    data: pandas.core.frame.DataFrame
        Original dataframe.
    """

    def __init__(self, data):
        self.edges = data

    def init_graph(self):
        """
        Initializes a new graph and
        sets its basic parameters.

        Returns
        -------
        pyvis.network.Network
        """
        self.nw_ = Network(height="1080px",
                           width="100%",
                           bgcolor="#272651",
                           font_color="white",
                           notebook=True)
        self.nw_.barnes_hut()
        self.nw_.set_edge_smooth(smooth_type="horizontal")
        self.nw_.toggle_hide_edges_on_drag(status=True)
        return self.nw_
    
    def add_elements(self):
        """
        Adds nodes and weighted edges
        to initial object.

        Returns
        -------
        self
        """
        for edge in self.edges:
            source = edge[0]
            dist = edge[1]
            weight= edge[2]
            self.nw_.add_node(source, source, title=source)
            self.nw_.add_node(dist, dist, title=dist)
            self.nw_.add_edge(source, dist, value=weight)
        return self

    def get_neighbors(self):
        """
        Finds neighbors for each node
        in the original graph.

        Returns
        -------
        pyvis.network.Network
        """
        neighbor_map = self.nw_.get_adj_list()
        for node in self.nw_.nodes:
            node['title'] += ":<br>" + "<br>".\
                join(neighbor_map[node['id']])
            node['value'] = len(neighbor_map[node['id']])
        return self

    def get_info(self):
        """
        Prints basic information
        about the original graph.
        """
        print("\n\U0001F310 Total nodes:",
              len(self.nw_.nodes))
        print("\n\U0001F310 Total edges:",
              len(self.nw_.edges))

    def show_graph(self):
        """
        Saves an HTML static webpage
        containing the interactive
        plot of the obtained graph.

        Parameters
        ----------
        name: string
            Name for the output HTML file.

        Returns
        -------
        pyvis.network.Network
        """
        return self.nw_.show("dp_last_graph.html")
