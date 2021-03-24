import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import os

def generate_clist(NUM_COLORS):
    import pylab

    cm = pylab.get_cmap('cool')
    color = [cm(1-1.*i/NUM_COLORS) for i in range(NUM_COLORS)]

    return color

def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    # mask NaNs and calculate average and std ignoring them
    masked_data = np.ma.masked_array(values, np.isnan(values))

    average = np.ma.average(masked_data, weights=weights)
    # Fast and numerically precise:
    variance = np.ma.average((masked_data-average)**2, weights=weights)
    return average, np.sqrt(variance)

def ims_plot(fpath, mass, tolerance, norm_cv, outname, title_label=None,
             charge=None, figsize=None, ylim=None, xlim=None, legend=True):
    """
    Plot IMS unfolding plot by normalising to drift time at certain collision
    voltage

    Parameters
    ----------
    fpath : str or list
        Either glob pattern or list of paths to csv output files form PULSAR.
    mass : int
        Mass to extract from the csv file (in case there are mutliple forms).
    tolerance : int
        Tolerance range for the mass. Allows pooling multiple species.
    norm_cv : int
        Collision voltage to normalise drift times to. Must be present in all datasets.
    outname : str
        Path to save the figure (without extension).
    title_label : str, optional
        Title to plot above the plot. The default is the filepath.
    charge : int, optional
        Only plot drift times from a single charge state. The default is all charge states.

    Raises
    ------
    Exception
        If the glob pattern or list did not match existing files.

    Returns
    -------
    None.

    """
    if figsize != None:
        fig, ax = plt.subplots(1,1, figsize=figsize)
    else:
        fig, ax = plt.subplots(1,1)

    file_dfs = []
    if not isinstance(fpath, list):
        try:
            for file in glob(fpath):
                temp = pd.read_csv(file)
                temp['file'] = file
                file_dfs.append(temp)
        except:
            raise Exception("Could not open glob pattern {}".format(fpath))
    else:
        for file in fpath:
            temp = pd.read_csv(file)
            temp['file'] = file
            file_dfs.append(temp)

    data = pd.concat(file_dfs)

    g = data.groupby('file')
    color = generate_clist(g.ngroups)

    subsets = []
    averages = []

    for ix, filename in enumerate(g.groups.keys()):
        subset = g.get_group(filename)
        # filter by mass (as provided in input)
        subset = subset[(subset['mass'] > mass-tolerance) & (subset['mass'] < mass+tolerance)]
        # filter by charge if requested
        if charge != None:
            print('Filtering by charge {}'.format(charge))
            subset = subset[subset['z'] == charge]
        # warn if the filters remove everything
        if len(subset) == 0:
            raise Exception("Subset after mass filtering is emtpy. Did you use the right mass?")

        # ignore data points with less than 10% basepeak intensity
        subset['basepeak_intensity'] = subset.groupby('collision_voltage')['drift_intensity'].transform('max')
        subset = subset[subset['drift_intensity'] > 0.1 * subset['basepeak_intensity']]
        # sort ascending by collision voltage
        subset.sort_values(by='collision_voltage', inplace=True)

        # normalise by the drift_time of the lowest charge state within charge
        # state groups!
        chargestates = subset['z'].unique()
        for z in chargestates:
            c = subset[subset['z'] == z]
            # use the mean to circumvent the problem, that selection returns a
            # list while we need a single value
            # also allows selecting CV ranges for normalisation
            subset.loc[subset['z'] == z, 'rel_drift_center'] =\
                100*c['drift_center'] / c[c['collision_voltage'] == norm_cv]['drift_center'].mean()


        # init an empty dataframe with only the index
        average = pd.DataFrame(index=subset['collision_voltage'].unique())
        # Normalisation procudes NaN for charge states that did not occur at
        # the desired collision voltage range -> need to ignore in average and
        # std calculations
        average[['Mean', 'Std']] = subset.groupby('collision_voltage').apply(lambda x: weighted_avg_and_std(x['rel_drift_center'], weights=x['drift_intensity'])).tolist()

        # label = str(subset['file_name'].unique()[0])[-30:]
        label = filename[-30:]

        ax.plot(average['Mean'],
                 color=color[ix],
                 label=label)

        ax.fill_between(average.index, average['Mean']-1*average['Std'],
                 average['Mean'] + 1*average['Std'],facecolor=color[ix],
                 alpha=0.1)

        ax.plot(average.index, average['Mean']-1*average['Std'],
                 color=color[ix],
                 linestyle='dotted')

        ax.plot(average.index, average['Mean']+1*average['Std'],
                 color=color[ix],
                 linestyle='dotted')

        subsets.append(subset)
        averages.append(average)

    if legend:
        plt.legend()

    if not title_label:
        title_label = ' '.join(fpath.split(os.path.sep)[-2:])
    ax.set_title(title_label)
    ax.set_xlabel('Collision voltage [V]')
    ax.set_ylabel('Relative Drift Time [%]')
    if ylim:
        ax.set_ylim(ylim)
    if xlim:
        ax.set_xlim(xlim)
    plt.savefig(outname + ".pdf")
    plt.savefig(outname + ".png")
    plt.show()

    return subsets, averages