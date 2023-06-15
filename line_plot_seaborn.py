from matplotlib import pyplot as plt
import seaborn as sn


fmri = sn.load_dataset("fmri")
print(fmri.head())

sn.lineplot(x="timepoint", y="signal", data=fmri,hue="event", style="event", markers=True)
plt.show()
