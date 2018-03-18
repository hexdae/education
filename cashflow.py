import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# Cashflow diagram plotter, usage:
# t 		: time array			example: [2000, 2001, 2002]
# value 	: value array			example: [20, 24, 23]
# cashflow 	: cashflow array 		example: [2, 2, 2]
# c1		: value color 		 	example: 'r', 'g', 'b', '#FF0099'
# c2		: cashflow color 	 	example: 'r', 'g', 'b', '#FF0099'
# currency	: currency label		example: '$', 'NT$', 'HK$'
# path		: output file			example: '../folder/image.png'	
# aspect 	: aspect ration			example: '[12, 9]'

 
def diagram (t, value, cashflow, c1="k", c2="k", currency="$", path = "test.png", aspect = [12,6], int_x = True, show = False):

	fig, ax1 = plt.subplots(figsize=(aspect))

	# Define x axis as integer (optional)
	if int_x:
		ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

	# Plot value (left axis) with color c1
	ax1.plot(t, value, color = c1)
	ax1.set_xlabel('time (year)')

	# Set value label and currency
	ax1.set_ylabel('Future Value '+ currency, color = c1)
	ax1.tick_params('y', colors = c1)
	
	# Define twin axis for cashflow
	ax2 = ax1.twinx()

	# Find positive and negative values in cashflow
	pos = [i for i in range(len(cashflow)) if cashflow[i] > 0]
	neg = [i for i in range(len(cashflow)) if cashflow[i] < 0]
	
	# Plot cashflow (rught axis) in the correct direction with color c2
	if (len(pos)):
		markerline, stemlines, baseline = ax2.stem(t[pos], cashflow[pos], markerfmt='^', basefmt=" ")
		plt.setp(stemlines, 'color', c2)
		plt.setp(markerline, 'color', c2)
	if (len(neg)):
		markerline, stemlines, baseline = ax2.stem(t[neg], cashflow[neg] ,markerfmt='v', basefmt=" ")
		plt.setp(stemlines, 'color', c2)
		plt.setp(markerline, 'color', c2)

	# Set cashflow label and currency
	ax2.set_ylabel('Cash Flow '+ currency, color=c2)
	ax2.tick_params('y', colors=c2)
	fig.tight_layout()

	# Remove the frame to visualize data more clearly
	ax1.spines['top'].set_visible(False)
	ax1.spines['right'].set_visible(False)
	ax1.spines['bottom'].set_visible(False)
	ax1.spines['left'].set_visible(False)
	ax2.spines['top'].set_visible(False)
	ax2.spines['right'].set_visible(False)
	ax2.spines['bottom'].set_visible(False)
	ax2.spines['left'].set_visible(False)

	# Save the plot to the specified path with 500dpi
	fig.savefig(path, dpi = 500)

	# Show plot (optional)
	plt.show (show)
