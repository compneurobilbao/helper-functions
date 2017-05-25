#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:51:16 2017

@author: asier
# sligthly modified from:
# https://stackoverflow.com/questions/35206282/assign-specific-colours-to-data-in-matplotlib-pie-chart
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_pie(slices, labels):

    ordered_labels = [label_ for (slice_, label_) in
                      sorted(zip(slices, labels))]
    ordered_slices = [slice_ for (slice_, label_) in
                      sorted(zip(slices, labels))]
    cmap = plt.cm.hot
    ordered_colors = cmap(ordered_slices)

    slices_size = np.ones(len(slices))

    colordict = {}
    for l, c in zip(ordered_labels, ordered_colors):
        print(l, c)
        colordict[l] = c

    fig = plt.figure(figsize=[10, 10])
    ax = fig.add_subplot(111)

    pie_wedge_collection = ax.pie(slices_size,
                                  labels=ordered_labels,
                                  labeldistance=1.05)

    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')
        pie_wedge.set_facecolor(colordict[pie_wedge.get_label()])

    sm = plt.cm.ScalarMappable(cmap=plt.cm.hot, norm=plt.Normalize(vmin=0,
                                                                   vmax=1))
    sm._A = []
    plt.colorbar(sm)

    # titlestring = 'Issues'
    # ax.set_title(titlestring)

    return fig, ax, pie_wedge_collection


slices = [0.5, 0.4, 0.3, 0.25, 0.95, 0.85, 0.80,  0,
          0.01,  0.6,  0.5,  0.5, 0.6, 0.2]
labels = [u'TI', u'Con', u'FR', u'TraI', u'Bug', u'Data', u'Int', u'KB',
          u'Other', u'Dep2', u'PW', u'Uns', u'Perf', u'Dep']

fig, ax, pie_wedge_collection = plot_pie(slices, labels)
plt.show()
