import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import scrolledtext
import mpld3
import io

raw_data = '''
-78.14551394,0
-73.54106219,0.461345487
-68.81903288,1.114763502
-64.10727359,2.005786622
-59.41352705,3.203808821
-57.09780101,3.936877971
-56.53206114,4.13238725
-56.49714478,4.144676897
-56.49714478,4.144676897
-56.47750708,4.305511806
-56.47628807,4.362280634
-56.47387129,4.474769222
-56.46892528,4.70502365
-56.45856749,5.187220794
-56.43591559,6.241787185
-56.38230779,8.73766675
-56.23799272,15.4577679
-56.05666328,23.90364962
-55.8943148,31.46751112
-55.75445187,37.98532866
-55.62565646,43.98866376
-55.50189852,49.75835016
-55.38092328,55.39939917
-55.26180464,60.9549311
-55.14406168,66.44733236
-55.02739588,71.89049538
-54.9116029,77.29392823
-54.79653477,82.66451501
-54.68208019,88.00743292
-54.56815302,93.32668845
-54.45468503,98.6254536
-54.34162119,103.9062872
-54.22891639,109.1712863
-54.11653315,114.4221928
-54.00443997,119.6604707
-53.89261009,124.8873628
-53.78102058,130.103934
-53.66965165,135.3111042
-53.55848604,140.5096736
-53.44750868,145.7003427
-53.33670626,150.8837289
-53.22606699,156.0603787
-53.11558039,161.2307787
-53.00523707,166.395364
-52.89502861,171.554525
-52.78494741,176.7086139
-52.6749866,181.8579491
-52.56513992,187.0028197
-52.4554017,192.1434889
-52.34576675,197.2801972
-52.23623029,202.4131645
-52.12678796,207.5425931
-52.01743574,212.6686689
-51.90816992,217.7915634
-51.79898704,222.9114354
-51.68988395,228.0284317
-51.58085766,233.1426888
-51.47190544,238.2543335
-51.36302472,243.3634839
-51.25421311,248.4702504
-51.14546836,253.5747359
-51.03678838,258.677037
-50.9281712,263.777244
-50.81961497,268.8754419
-50.71111796,273.9717104
-50.60267853,279.0661247
-50.49429514,284.1587555
-50.38596632,289.2496695
-50.27769071,294.3389299
-50.16946699,299.4265963
-50.06129393,304.5127251
-49.95317037,309.5973698
-49.84509518,314.6805812
-49.73706732,319.7624073
-49.62908577,324.8428939
-49.52114959,329.9220846
-49.41325786,335.0000206
-49.30540971,340.0767416
-49.19760432,345.1522851
-49.08984089,350.2266869
-48.98211867,355.2999813
-48.87443693,360.3722011
-48.76679498,365.4433775
-48.65919216,370.5135405
-48.55162783,375.5827187
-48.44410139,380.6509396
-48.33661224,385.7182295
-48.22915982,390.7846137
-48.1217436,395.8501163
-48.01436306,400.9147606
-47.9070177,405.978569
-47.79970702,411.041563
-47.69243059,416.1037632
-47.58518793,421.1651895
-47.47797864,426.225861
-47.37080228,431.2857963
-47.26365847,436.3450129
-47.15654681,441.4035282
-47.04946694,446.4613585
-46.94241848,451.5185199
-46.83540109,456.5750277
-46.72841444,461.6308968
-78.14551394,0
-73.61570159,0.452613379
-69.00916358,1.084253294
-64.40198587,1.941757268
-59.79547505,3.092651018
-57.505966,3.799973221
-56.94240523,3.989907385
-56.66311361,4.086493624
-56.52370053,4.135327579
-56.48887877,4.147590162
-56.48887877,4.147590162
-56.45341436,4.156703218
-56.38344876,4.172745542
-56.2440775,4.204812396
-55.96496155,4.269476145
-55.40522913,4.400947795
-54.27972529,4.672657819
-52.00426534,5.252708272
-47.35308915,6.572547568
-42.61661764,8.114081274
-37.88191051,9.868895604
-33.15617062,11.8495579
-28.44239037,14.07089514
-23.74028312,16.54967691
-19.0493846,19.30370868
-14.369241,22.35191799
-9.69941498,25.71451893
-5.039485439,29.4131884
-0.389047038,33.47125271
4.252290188,37.91388573
8.884901152,42.76832063
13.50914594,48.06407709
17.99925331,53.66886997
22.11773166,59.23988649
25.90372196,64.74928668
29.41119835,70.20647452
30.22490432,71.52323365
30.60257666,72.14105423
30.78831838,72.44646419
30.97268717,72.75063768
30.78831838,72.44646419
30.52651326,72.01628291
29.79717014,70.82862961
28.33124531,68.48877274
25.38151866,63.96636757
22.37728584,59.60543782
19.21875922,55.2742704
15.89655611,50.98528488
12.39318064,46.74310519
8.688736608,42.55384355
4.759882647,38.42475868
0.579050473,34.3646013
-3.730335209,30.51737543
-8.029238842,26.99947652
-12.32036468,23.78640776
-16.60346218,20.85795267
-20.87834513,18.1952304
-25.14482647,15.78060626
-29.40272013,13.59755693
-33.65184123,11.630547
-37.89200644,9.864915388
-42.12306177,8.28677132
-46.34672779,6.882908221
-50.56583987,5.641223189
-54.78039731,4.550568614
-55.85171124,4.295882768
-56.40209855,4.168465735
-56.47136302,4.152593765
-56.47136302,4.15483794
-56.47740579,4.310226858
-56.47619162,4.366746615
-56.47377496,4.479253992
-56.46882811,4.709549475
-56.45846928,5.191809988
-56.43581893,6.246419554
-56.38221491,8.741991335
-56.23795597,15.4594794
-56.05672632,23.90071245
-55.89444004,31.46167522
-55.75460152,37.97835405
-55.62581689,43.98118506
-55.50206598,49.75054253
-55.38109648,55.39132196
-55.26198291,60.94661618
-55.14424451,66.43880264
-55.0275829,71.88176912
-54.91179377,77.28502054
-54.79672922,82.65543869
-54.68228232,87.9981991
-54.56835774,93.31730648
-54.45489225,98.61593204
-54.34183083,103.8966335
-54.22912836,109.1615073
-54.11674737,114.4122944
-54.00465636,119.6504584
-53.89282858,124.8772416
-53.7812411,130.0937085
-53.66987412,135.3007785
-53.5587104,140.4992515
-53.44773487,145.6898279
-53.33693422,150.8731246
-53.22629666,156.0496881
-53.11581172,161.2200046
-53.00547002,166.3845091
'''

# Convert the raw CSV data to a Pandas DataFrame
cond_df = pd.read_csv(io.StringIO(raw_data), header=None, names=['Temperature (°C)', 'Pressure (bar)'], index_col=None)

# Function to assign the plot settings to all plots
# Simply typing `rcparams()` in other python scripts will do the job.
def rcparams():
    rcParams['figure.figsize'] = 5, 4
    rcParams['font.family'] = 'sans-serif'

    # Check whether Arial or SF Pro Display are installed in the computer
    try:
        rcParams['font.sans-serif'] = ['SF Pro Display']
    except:
        try:
            rcParams['font.sans-serif'] = ['Arial']
        except:
            print("ERROR Note that Arial and SF Pro are not installed in the computer. The program will use the default font.")
            pass

    # Label should be far away from the axes
    rcParams['axes.labelpad'] = 8
    rcParams['xtick.major.pad'] = 7
    rcParams['ytick.major.pad'] = 7

    # Add minor ticks
    rcParams['xtick.minor.visible'] = True
    rcParams['ytick.minor.visible'] = True

    # Tick width
    rcParams['xtick.major.width'] = 1
    rcParams['ytick.major.width'] = 1
    rcParams['xtick.minor.width'] = 0.5
    rcParams['ytick.minor.width'] = 0.5

    # Tick length
    rcParams['xtick.major.size'] = 5
    rcParams['ytick.major.size'] = 5
    rcParams['xtick.minor.size'] = 3
    rcParams['ytick.minor.size'] = 3

    # Tick color
    rcParams['xtick.color'] = 'black'
    rcParams['ytick.color'] = 'black'

    rcParams['font.size'] = 14
    rcParams['axes.titlepad'] = 10
    rcParams['axes.titleweight'] = 'normal'
    rcParams['axes.titlesize'] = 18

    # Axes settings
    rcParams['axes.labelweight'] = 'normal'
    rcParams['xtick.labelsize'] = 12
    rcParams['ytick.labelsize'] = 12
    rcParams['axes.labelsize'] = 16
    rcParams['xtick.direction'] = 'in'
    rcParams['ytick.direction'] = 'in'

# Updated plotting function for demonstration
def generate_plot(df, t_sensor_col, p_sensor_col, time_unit, plot_type, line_width):
    rcparams()

    fig, ax = plt.subplots()
    time_col = df.iloc[:, 0]
    if time_unit == 'min':
        time_col /= 60
    elif time_unit == 'hrs':
        time_col /= 3600

    # Determine labels based on the plot type
    if plot_type == 'P-t':
        y_label = 'Pressure (bar)'
        x_label = f'Time ({time_unit})'
        ax.plot(time_col, df.iloc[:, p_sensor_col], linewidth=line_width, color='black')

        ## xlim
        x_lim_min = float(x_lim_min_var.get()) if x_lim_min_var.get() != '' else None
        x_lim_max = float(x_lim_max_var.get()) if x_lim_max_var.get() != '' else None
        ax.set_xlim(x_lim_min, x_lim_max)

        ## ylim
        y_lim_min = float(y_lim_min_var.get()) if y_lim_min_var.get() != '' else None
        y_lim_max = float(y_lim_max_var.get()) if y_lim_max_var.get() != '' else None
        ax.set_ylim(y_lim_min, y_lim_max)

    elif plot_type == 'T-t':
        y_label = 'Temperature (°C)'
        x_label = f'Time ({time_unit})'
        ax.plot(time_col, df.iloc[:, t_sensor_col], linewidth=line_width, color='black')

        ## xlim
        x_lim_min = float(x_lim_min_var.get()) if x_lim_min_var.get() != '' else None
        x_lim_max = float(x_lim_max_var.get()) if x_lim_max_var.get() != '' else None
        ax.set_xlim(x_lim_min, x_lim_max)

        ## ylim
        y_lim_min = float(y_lim_min_var.get()) if y_lim_min_var.get() != '' else None
        y_lim_max = float(y_lim_max_var.get()) if y_lim_max_var.get() != '' else None
        ax.set_ylim(y_lim_min, y_lim_max)

    elif plot_type == 'P-T':
        y_label = 'Pressure (bar)'
        x_label = 'Temperature (°C)'
        ax.plot(df.iloc[:, t_sensor_col], df.iloc[:, p_sensor_col], linewidth=line_width, color='black')
        ax.scatter(df.iloc[:, t_sensor_col], df.iloc[:, p_sensor_col], s=line_width*2, 
        color='black')

        ## xlim
        x_lim_min = float(x_lim_min_var.get()) if x_lim_min_var.get() != '' else None
        x_lim_max = float(x_lim_max_var.get()) if x_lim_max_var.get() != '' else None
        ax.set_xlim(x_lim_min, x_lim_max)

        ## ylim
        y_lim_min = float(y_lim_min_var.get()) if y_lim_min_var.get() != '' else None
        y_lim_max = float(y_lim_max_var.get()) if y_lim_max_var.get() != '' else None
        ax.set_ylim(y_lim_min, y_lim_max)

        # Add the condensation line
        ax.scatter(cond_df.iloc[:, 0], cond_df.iloc[:, 1], color='tab:red', s=line_width*2, alpha=0.6)
        ax.plot(cond_df.iloc[:, 0], cond_df.iloc[:, 1], color='tab:red', alpha=0.3)
    else:
        raise Exception("ERROR: Invalid plot type.", fg='red')

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return fig

# Function to generate plot and show preview
def generate():
    try:
        df = pd.read_csv(data_file_path.get(), encoding = "ISO-8859-1")
        df = df.drop(df.columns[0], axis=1)

        ## Drop rows from the `drop_rows` variable
        drop_rows = int(drop_rows_var.get())
        df = df.drop(df.index[drop_rows:])
        
        t_sensor_col = int(t_sensor_var.get()) # `TI001(pv)` ~ `TI005(pv)` are 2nd ~ 6th columns
        p_sensor_col = int(p_sensor_var.get()) + 5 # `PI002(pv)` ~ `PI003(pv)` are 7th ~ 8th columns
        
        # Print the selected columns from the DataFrame
        print(f"Selected temperature column: {df.columns[t_sensor_col]}")
        print(f"Selected pressure column: {df.columns[p_sensor_col]}")
        
        fig = generate_plot(df, t_sensor_col, p_sensor_col, time_unit_var.get(), plot_type_var.get(), line_width_var.get())

        fig.tight_layout()
        
        # Create a new Toplevel window to show the plot and the Close Preview button
        preview_window = tk.Toplevel(root)
        preview_window.title("Preview")
        preview_window.protocol("WM_DELETE_WINDOW", lambda: close_preview(preview_window))
        
        # Embedding the Matplotlib figure in the Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=preview_window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, columnspan=3)
        
        # Add the Close Preview button
        close_button = tk.Button(preview_window, text="Close Preview", command=lambda: close_preview(preview_window))
        close_button.grid(row=1, column=1)
        
        # Add the Export Plot button
        export_button = tk.Button(preview_window, text="Export the HTML plot", command=lambda: export_plot(fig))
        export_button.grid(row=1, column=2)
        
        # Hide the root window while the preview window is open
        root.withdraw()
        
        info_label.config(text="INFO: Plot generated successfully!", fg='green')
    except Exception as e:
        info_label.config(text=f"ERROR: {str(e)}", fg='red')

# Function to close the preview window and show the root window
def close_preview(preview_window):
    preview_window.withdraw()
    root.deiconify()

# Function to export the plot as an HTML file using mpld3
def export_plot(fig):
    file_path = filedialog.asksaveasfilename(defaultextension='.html')
    if file_path:
        mpld3.save_html(fig, file_path)
        messagebox.showinfo("Export Successful", f"HTML plot exported to {file_path} successfully!")
    else:
        messagebox.showerror("Export Failed", "Please enter a valid file name for the HTMLz.")

# Function to exit the application
def exit_app():
    root.quit()
    root.destroy()

# Initialize the Tkinter window
root = tk.Tk()
root.title("LCO2 Autoplotter V1.0.0")

# Add title and author label
title_label = ttk.Label(root, text="EESLab LCO2 Autoplotter", font=("Arial", 25))
title_label.grid(row=0, column=1, columnspan=2, pady=30)

# Add the author label
author_label = ttk.Label(root, text="Author: @wjgoarxiv", font=("Arial", 15))
author_label.grid(row=0, column=3, pady=5)

# Variables to hold user input
t_sensor_var = tk.StringVar(value='1')
p_sensor_var = tk.StringVar(value='2')
time_unit_var = tk.StringVar(value='sec')
plot_type_var = tk.StringVar(value='P-t')
file_name_var = tk.StringVar(value='output.png')
x_lim_min_var = tk.StringVar(value='')
x_lim_max_var = tk.StringVar(value='')
y_lim_min_var = tk.StringVar(value='')
y_lim_max_var = tk.StringVar(value='')
drop_rows_var = tk.StringVar(value='1000')
dpi_var = tk.StringVar(value='350')
transparent_var = tk.BooleanVar(value=True)
line_width_var = tk.IntVar(value=2)
data_file_path = tk.StringVar(value='')
info_label = tk.Label(root, text="INFO: Awaiting user action.", fg='blue')

# Function to open file dialog and set data_file_path
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    data_file_path.set(file_path)
    
    # Alert user if the data file is uploaded. If not, ERROR will be displayed.
    if data_file_path.get() != '':
        info_label.config(text="INFO: Data file uploaded successfully!", fg='green')
        try:
            # Load the first few rows of the data to preview
            df_preview = pd.read_csv(data_file_path.get(), encoding="ISO-8859-1", nrows=10)
            
            # Clear any existing text in the scrolled_text widget
            scrolled_text.delete(1.0, tk.END)
            
            # Insert the new data preview
            scrolled_text.insert(tk.INSERT, df_preview.head().to_string(index=False))
        except Exception as e:
            info_label.config(text=f"ERROR: Unable to preview data - {str(e)}", fg='red')
    else:
        info_label.config(text="ERROR: Please upload a DATA file.", fg='red')

# Initialize ScrolledText widget for data preview
scrolled_text = scrolledtext.ScrolledText(root, width=50, height=10)
scrolled_text.grid(row=13, column=2, rowspan=10, columnspan=2, padx=5, pady=5)
scrolled_text.insert(tk.INSERT, "Exp. data preview will be shown here...")

## Temperature sensors are 1, 2, 3, 4, 5
tk.Label(root, text="T sensor #:").grid(row=1, column=0)
tk.OptionMenu(root, t_sensor_var, '1', '2', '3', '4', '5').grid(row=1, column=1)

## Pressure sensors are 2 and 3
tk.Label(root, text="P sensor #:").grid(row=2, column=0)
tk.OptionMenu(root, p_sensor_var, '2', '3').grid(row=2, column=1)

tk.Label(root, text="Drop Rows From:").grid(row=2, column=2, sticky='e')
tk.Entry(root, textvariable=drop_rows_var).grid(row=2, column=3, sticky='we', pady=5)

tk.Label(root, text="Time Unit:").grid(row=3, column=0)
tk.OptionMenu(root, time_unit_var, 'sec', 'min', 'hrs').grid(row=3, column=1)

tk.Label(root, text="Plot Type:").grid(row=4, column=0)
tk.OptionMenu(root, plot_type_var, 'P-t', 'T-t', 'P-T').grid(row=4, column=1)

tk.Label(root, text="Output File Name:").grid(row=5, column=0)
tk.Entry(root, textvariable=file_name_var).grid(row=5, column=1)

tk.Label(root, text="DPI:").grid(row=6, column=0)
tk.Entry(root, textvariable=dpi_var).grid(row=6, column=1)

tk.Label(root, text="Transparent Plot:").grid(row=7, column=0)
tk.Checkbutton(root, variable=transparent_var).grid(row=7, column=1)

tk.Label(root, text="X Limit Min.:").grid(row=7, column=2, sticky='e')
tk.Entry(root, textvariable=x_lim_min_var).grid(row=7, column=3, sticky='we', pady=5)

tk.Label(root, text="X Limit Max.:").grid(row=8, column=2, sticky='e')
tk.Entry(root, textvariable=x_lim_max_var).grid(row=8, column=3, sticky='we', pady=5)

tk.Label(root, text="Y Limit Min.:").grid(row=9, column=2, sticky='e')
tk.Entry(root, textvariable=y_lim_min_var).grid(row=9, column=3, sticky='we', pady=5)

tk.Label(root, text="Y Limit Max.:").grid(row=10, column=2, sticky='e')
tk.Entry(root, textvariable=y_lim_max_var).grid(row=10, column=3, sticky='we', pady=5)


tk.Label(root, text="Line Width:").grid(row=8, column=0)
tk.Entry(root, textvariable=line_width_var).grid(row=8, column=1)

tk.Button(root, text="Select Experimental Data File", command=open_file_dialog).grid(row=9, column=1, columnspan=1, sticky='we')
tk.Button(root, text="Generate Plot", command=generate).grid(row=10, column=1, columnspan=1, sticky='we')
tk.Button(root, text="Exit", command=exit_app).grid(row=11, column=1, columnspan=1, sticky='we')
info_label.grid(row=12, column=2, columnspan=2, pady=5)

# Run the Tkinter event loop
root.mainloop()