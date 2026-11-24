from pathlib import Path
import csv
import statistics as st
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
with (root/'data/oxide_thickness.csv').open() as f:
    oxide = [float(r['thickness_nm']) for r in csv.DictReader(f)]
with (root/'data/photoresist_thickness.csv').open() as f:
    resist = [float(r['thickness_angstrom'])/10 for r in csv.DictReader(f)]
for name, values in [('oxide',oxide),('photoresist',resist)]:
    print(f'{name}: n={len(values)}, mean={st.mean(values):.2f} nm, sample SD={st.stdev(values):.2f} nm, range={max(values)-min(values):.2f} nm')
    fig, ax = plt.subplots(figsize=(7.5,4.2))
    ax.plot(range(1,len(values)+1),values,'o-',label='Reported readings')
    ax.axhline(st.mean(values),ls='--',label=f'Mean: {st.mean(values):.2f} nm')
    ax.set(xlabel='Measurement location (report order)',ylabel='Thickness (nm)',title=f'{name.capitalize()} thickness | Five-point laboratory measurements',xticks=range(1,6))
    ax.legend(); ax.grid(alpha=.2); fig.tight_layout()
    fig.savefig(root/'images'/f'{name}_thickness.png',dpi=180); plt.close(fig)
