import matplotlib.pyplot as plt

def read_file(filename):
    with open(filename) as f:
        return [float(x) for x in f]

colors = ['blue', 'green', 'purple', 'magenta']

for Kh, color in zip([0.02, 0.03, 0.05, 0.07], colors):

    Kh_file = str(Kh).replace(".", "_")

    altitude = read_file(f"altitude/altitude{Kh_file}.txt")
    actual = read_file(f"actualdescent/actualdescent{Kh_file}.txt")
    target = read_file(f"targetdescent/targetdescent{Kh_file}.txt")

    n = min(len(altitude), len(actual), len(target))

    altitude = altitude[:n]
    actual = actual[:n]
    target = target[:n]

    # Actual = solid
    plt.plot(
        altitude, actual,
        color=color,
        linestyle='-',
        label=f"Actual Kh={Kh}"
    )

    # Target = dashed, same colour
    plt.plot(
        altitude, target,
        color=color,
        linestyle='--',
        label=f"Target Kh={Kh}"
    )

plt.xlabel("Altitude (m)")
plt.ylabel("Descent rate (m/s)")
plt.title("Actual vs Target Descent Rate")
plt.legend()
plt.grid()
plt.gca().invert_xaxis()
plt.show()